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
    Click Button  name=form.buttons.cancel

i hit the save button
    Click Button  name=form.buttons.save

the workflow comment dialog should close
    Wait until keyword succeeds  5  0.5  Element Should Not Be Visible  css=div.overlay #form

workflow transition should not be triggered
    Element Should Be Visible  css=span.state-private

workflow transition should be triggered
    Element Should Be Visible  css=span.state-pending

i enter a workflow comment
    Input Workflow Comment  luke, i'm your father.

Input Workflow Comment
    [Arguments]  ${comment}
    Input text  name=form.widgets.comment  ${comment}
