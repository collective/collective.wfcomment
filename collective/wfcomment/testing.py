# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName

from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.testing import z2
from zope.configuration import xmlconfig


class WFCommentLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.wfcomment
        xmlconfig.file(
            'configure.zcml',
            collective.wfcomment,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        workflowTool = getToolByName(portal, 'portal_workflow')
        workflowTool.setDefaultChain('simple_publication_workflow')

        applyProfile(portal, 'collective.wfcomment:default')

WFCOMMENT_FIXTURE = WFCommentLayer()
WFCOMMENT_ROBOT_TESTING = FunctionalTesting(
    bases=(AUTOLOGIN_LIBRARY_FIXTURE, WFCOMMENT_FIXTURE, z2.ZSERVER),
    name="collective.wfcomment:Robot")
