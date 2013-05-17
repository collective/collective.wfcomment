*** Settings ***
Resource        plone/app/robotframework/selenium.robot
Resource        plone/app/robotframework/keywords.robot
Resource        collective/wfcomment/tests/robot/keywords.robot

Library         Remote  ${PLONE_URL}/RobotRemote

Test Setup      Open test browser
Test Teardown   Close All Browsers


*** Test cases ***
Scenario: User cancels the workflow comment dialog
    Given i am logged in as  Contributor
      And i add a new folder
      And i want to publish the folder
      And the workflow comment dialog should open
     When i hit the cancel button
     Then the workflow comment dialog should close
      And workflow transition should not be triggered

Scenario: User enters a workflow comment
    Given i am logged in as  Contributor
      And i add a new folder
      And i want to publish the folder
      And the workflow comment dialog should open
     When i enter a workflow comment
      And i hit the save button
     Then the workflow comment dialog should close
      And workflow transition should be triggered
