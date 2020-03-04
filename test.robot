*** Settings ***

Documentation    Example RobotFramework test using the space separated plain text format.
Library          OperatingSystem
Library          Collections
Library         SeleniumLibrary
Library         ./hello_world.py

*** Variables ***

${MESSAGE}       Hello, world!

*** Test Cases ***

My Test
    [Documentation]                       Hello World Test
    Log to console                        ${MESSAGE}
    Browser Test Using Robot Framework
    Browser Test Using Python

*** Keywords ***

Do A For Loop

Browser Test Using Robot Framework
    Robot Browser                         https://the-internet.herokuapp.com/login    ${BROWSER}

Browser Test Using Python
    Python Selenium Test                  ${BROWSER}

*** Keywords ***

Robot Browser
    [Arguments]                           ${url}                                      ${BROWSER}
    Open Browser                          url=${url}                                  browser=${BROWSER}
    Wait Until Element Is Visible         css:#username
    Click Element                         css:#username
    Press Keys                            css:#username                               tomsmith
    Wait Until Element Is Visible         css:#password
    Click Element                         css:#password
    Press Keys                            css:#password                               SuperSecretPassword!
    Click Element                         css:button[type=submit]
    Wait Until Element Is Visible         css:.button > i.icon-signout                # This is an id, so you can use just the id name as an argument here
    Close Browser
