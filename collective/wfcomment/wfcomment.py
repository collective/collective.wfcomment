from five import grok

from zope import schema
from zope.component import getUtility
from zope.interface import Interface
from z3c.form import form, button
from z3c.form.field import Fields
from z3c.form.interfaces import HIDDEN_MODE

from plone.z3cform.layout import FormWrapper
from plone.registry.interfaces import IRegistry
from plone.app.layout.viewlets.interfaces import IHtmlHeadLinks

from Products.ATContentTypes.interfaces import IATContentType
from collective.wfcomment.interfaces import IWorkflowCommentSettings
from collective.wfcomment import _


# change in a transition url:
# %(content_url)s/content_status_history?workflow_action=reject
class WfCommentViewlet(grok.Viewlet):
    grok.context(IATContentType)
    grok.viewletmanager(IHtmlHeadLinks)

    def render(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IWorkflowCommentSettings)
        enable_for_all_transitions = settings.enable_for_all_transitions
        if not enable_for_all_transitions:
            if settings.transitions:
                transitions = frozenset(settings.transitions.split('\n'))
            else:
                transitions = ()
            transitions_expr = u", ".join(['#workflow-transition-%s' % t for t in transitions])
        else:
            transitions_expr = u'#plone-contentmenu-workflow dd.actionMenuContent a[href*=content_status_modify]'
        return u"""
<script type="text/javascript">
jQuery(function($){

$('%(transitions_expr)s').each(function() {
    var href = $(this).attr('href');
    var newhref = href.substring(0, href.indexOf('content_status_modify')) + 'content_status_comment' + href.substring(href.indexOf('?'));
    $(this).attr('href', newhref);
    $(this).attr('class', "kssIgnore"); // TODO: this is not enough, we need to unbind the kss event
}
);

$('#plone-contentmenu-workflow dd.actionMenuContent a[href*=content_status_comment]').prepOverlay(
        {
            subtype: 'ajax',
            filter: common_content_filter,
            formselector: 'form',
            noform: 'reload',
            closeselector: '[name=form.buttons.cancel]'
        }
    );

});
</script>
""" % {'transitions_expr': transitions_expr}


class IComment(Interface):

    workflow_action = schema.Text(
        title=_(u"Workflow action"),
        required=True)

    comment = schema.Text(
        title=_(u"Comment"),
        description=_(u"Please enter a comment for this state change."),
        required=False)


class WfCommentForm(form.AddForm):
    fields = Fields(IComment)
    fields['workflow_action'].mode = HIDDEN_MODE
    next_url = None

    def updateActions(self):
        super(WfCommentForm, self).updateActions()
        self.actions["save"].addClass("context")
        self.actions["cancel"].addClass("standalone")

    def updateWidgets(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IWorkflowCommentSettings)
        comment_required = settings.comment_required
        IComment['comment'].required = comment_required
        super(WfCommentForm, self).updateWidgets()
        if 'workflow_action' in self.request:
            self.widgets['workflow_action'].value = (
                self.request['workflow_action'])

    @button.buttonAndHandler(_(u'Save'), name='save')
    def handleAdd(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        self._finishedAdd = True
        self.next_url = (
            u"%s/content_status_modify?workflow_action=%s&comment=%s" % (
                self.context.absolute_url(),
                data['workflow_action'],
                data['comment'].strip()))
    
    @button.buttonAndHandler(_(u'Cancel'), name='cancel')
    def handleCancel(self, action):
        self._finishedAdd = True
        self.next_url = self.context.absolute_url()

    def nextURL(self):
        return self.next_url


class WfCommentView(FormWrapper, grok.View):
    grok.name("content_status_comment")
    grok.context(IATContentType)
    grok.require('cmf.RequestReview')
    form = WfCommentForm

    def __init__(self, context, request):
        grok.View.__init__(self, context, request)
        FormWrapper.__init__(self, context, request)
