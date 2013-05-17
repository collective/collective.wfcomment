*** Settings ***
Resource        plone/app/robotframework/selenium.robot
Resource        plone/app/robotframework/keywords.robot

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


*** Keywords ***
i am logged in as
    [Arguments]  ${role}
    Enable autologin as  ${role}

i add a new folder
    Go To  ${PLONE_URL}
    Add folder  A sample Folder

i want to publish the folder
    Workflow Submit

the workflow comment dialog should open
    Wait until keyword succeeds  5  0.5  Element Should Be Visible  css=div.overlay #form

i hit the cancel button
    Click Button  Cancel

i hit the save button
    Click Button  Save

the workflow comment dialog should close
    Wait until keyword succeeds  5  0.5  Element Should Not Be Visible  css=div.overlay #form

workflow transition should not be triggered
    Element Should Be Visible  css=span.state-private

workflow transition should be triggered
    Page should contain    Item state changed
    Element Should Be Visible  css=span.state-pending

i enter a workflow comment
    Input Workflow Comment  luke, i'm your father.

Input Workflow Comment
    [Arguments]  ${comment}
    Input text  name=form.widgets.comment  ${comment}
