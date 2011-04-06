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

    transitions = schema.Text(title=_(u"Transitions enabled"),
        description=_(u"If comment popup is not enabled for all transitions, "
                       "it will be enabled for this specific transitions."),
        required=False,
        )
