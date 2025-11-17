*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  aapo
    Set Password  aapo1234  aapo1234
    Click Button  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  aapo1234  aapo1234
    Click Button  Register
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  aapo
    Set Password  aapo1  aapo1
    Click Button  Register
    Register Should Fail With Message  Password is too short

Register With Valid Username And Invalid Password
    Set Username  aapo
    Set Password  aapoaapo  aapoaapo
    Click Button  Register
    Register Should Fail With Message  Password can't be only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  aapo
    Set Password  aapo1235  aapo1234
    Click Button  Register
    Register Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123  kalle123
    Click Button  Register
    Register Should Fail With Message  User with username kalle already exists

*** Keywords ***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]    ${password}    ${password_confirmation}
    Input Password    password                 ${password}
    Input Password    password_confirmation    ${password_confirmation}

Register Should Succeed
    Title Should Be  Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page