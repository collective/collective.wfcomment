from zope.interface import Interface
from zope import schema

from collective.wfcomment import _


class IWorkflowCommentSettings(Interface):

    comment_required = schema.Bool(
        title=_(u"Comment required"),
        default=False,
        )

    enable_for_all_transitions = schema.Bool(
        title=_(u"Enable comment for all transitions"),
        default=True,
        )

    transitions = schema.Set(title=_(u"Transitions enabled"),
        description=_(u"If comment popup is not enabled for all transitions, "
                       "it will be enabled for this specific transitions."),
        required=False,
        value_type=schema.Choice(vocabulary="plone.app.vocabularies.WorkflowTransitions"),
        )


class IWfCommentControlPanel(Interface):
    """Control panel view
    """


class IComment(Interface):

    workflow_action = schema.Text(
        title=_(u"Workflow action"),
        required=True)

    comment = schema.Text(
        title=_(u"Comment"),
        description=_(u"Please enter a comment for this state change."),
        required=False)


class IWorkflowCommentBrowserLayer(Interface):
    """Browser layer for installed collective.wfcomment
    """