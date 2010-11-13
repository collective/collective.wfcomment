# -*- coding: utf-8 -*-
from five import grok

from plone.app.registry.browser import controlpanel
from Products.CMFPlone.interfaces import IPloneSiteRoot

from collective.wfcomment.interfaces import IWorkflowCommentSettings
from collective.wfcomment import _


class ControlPanelEditForm(controlpanel.RegistryEditForm):

    schema = IWorkflowCommentSettings
    label = _(u"Workflow comment settings")
    description = _(u"help_wfcomment_settings_editform",
                    default=u"You can set here some options related to the "
                             "workflow comment feature.")


class WfCommentControlPanel(controlpanel.ControlPanelFormWrapper, grok.View):
    grok.name('wfcomment-controlpanel')
    grok.context(IPloneSiteRoot)
    grok.require('cmf.ManagePortal')
    form = ControlPanelEditForm

    def __init__(self, context, request):
        grok.View.__init__(self, context, request)
        controlpanel.ControlPanelFormWrapper.__init__(self, context, request)
