# -*- coding: utf-8 -*-
from zope.interface import implements

from plone.app.registry.browser import controlpanel
from Products.Five.browser import BrowserView
from plone.app.layout.viewlets.common import ViewletBase

from collective.wfcomment.interfaces import (
    IWorkflowCommentSettings, IWfCommentControlPanel)
from collective.wfcomment import _


class ControlPanelEditForm(controlpanel.RegistryEditForm):

    schema = IWorkflowCommentSettings
    label = _(u"Workflow comment settings")
    description = _(u"help_wfcomment_settings_editform",
                    default=u"You can set here some options related to the "
                             "workflow comment feature.")


class WfCommentControlPanel(controlpanel.ControlPanelFormWrapper, BrowserView):
    form = ControlPanelEditForm

    implements(IWfCommentControlPanel)

    def __init__(self, context, request):
        BrowserView.__init__(self, context, request)
        controlpanel.ControlPanelFormWrapper.__init__(self, context, request)


class WfCommentControlPanelJS(ViewletBase):

    def render(self):
        return """
<script id="wfcomment-controlpanel-js" type="text/javascript">
    var update_collective_wfcomment_controlpanel = function(){
        var checkbox = jQuery('#form-widgets-enable_for_all_transitions-0');
        if(checkbox.attr('checked')){
            jQuery('#formfield-form-widgets-transitions').hide('fast');
        }
        else{
            jQuery('#formfield-form-widgets-transitions').show('fast');
        }
    }

    jQuery(function(){
        update_collective_wfcomment_controlpanel();
        jQuery('#form-widgets-enable_for_all_transitions-0').change(update_collective_wfcomment_controlpanel);
    });
</script>
    """