*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Registration Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  jalle
    Set Password  jalle123
    Set Password Confirmation  jalle123
    Submit Credentials
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ja
    Set Password  jalle123
    Set Password Confirmation  jalle123
    Submit Credentials
    Registration Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  jalle
    Set Password  jalle1
    Set Password Confirmation  jalle1
    Submit Credentials
    Registration Should Fail With Message  Password must be at least 8 characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  jalle
    Set Password  jalle123
    Set Password Confirmation  jalle1
    Submit Credentials
    Registration Should Fail With Message  Password and password confirmation do not match

Login After Successful Registration
    Set Username  jalle
    Set Password  jalle123
    Set Password Confirmation  jalle123
    Submit Credentials
    Registration Should Succeed
    Go To Login Page
    login_resource.Set Username  jalle
    login_resource.Set Password  jalle123
    login_resource.Submit Credentials
    login_resource.Login Should Succeed

Login After Failed Registration
    Set Username  ja
    Set Password  jalle123
    Set Password Confirmation  jalle123
    Submit Credentials
    Registration Should Fail With Message  Username must be at least 3 characters long
    Go To Login Page
    login_resource.Set Username  ja
    login_resource.Set Password  jalle123
    login_resource.Submit Credentials
    login_resource.Login Should Fail With Message  Invalid username or password

*** Keywords ***
Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Registration Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Create User And Go To Registration Page
    Create User  kalle  kalle123
    Go To Registration Page
    Registration Page Should Be Open
