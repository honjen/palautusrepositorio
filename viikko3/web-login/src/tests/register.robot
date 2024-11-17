*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  ellak
    Set Password  ellak456
    Set Password Confirmation  ellak456
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  el
    Set Password  ellak456
    Set Password Confirmation  ellak456
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters long and contain only letters a-z

Register With Valid Username And Too Short Password
    Set Username  ellak
    Set Password  el456
    Set Password Confirmation  el456
    Submit Credentials
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  ellak
    Set Password  ellakkkkk
    Set Password Confirmation  ellakkkkk
    Submit Credentials
    Register Should Fail With Message  Password cannot consist solely of letters

Register With Nonmatching Password And Password Confirmation
    Set Username  ellak
    Set Password  ellak456
    Set Password Confirmation  ellak654
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  ellak456
    Set Password Confirmation  ellak456
    Submit Credentials
    Register Should Fail With Message  Username is already taken

Login After Successful Registration
    Set Username  ellak
    Set Password  ellak456
    Set Password Confirmation  ellak456
    Submit Credentials
    Register Should Succeed
    Continue to Main
    Set Username  ellak
    Set Password  ellak456
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  kalle
    Set Password  ellak456
    Set Password Confirmation  ellak456
    Submit Credentials
    Register Should Fail With Message  Username is already taken
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Submit Login Credentials
    Login Should Succeed


*** Keywords ***
Continue To Main
    Click Link  Continue to main page
    Click Button  Logout
    Login Page Should Be Open

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page