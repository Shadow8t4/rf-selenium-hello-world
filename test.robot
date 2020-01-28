*** Settings ***

Documentation    Example RobotFramework test using the space separated plain text format.
Library          OperatingSystem
Library          SeleniumLibrary
Library          ./hello_world.py

*** Variables ***

${MESSAGE}       Hello, world!

*** Test Cases ***

My Test
    [Documentation]                  Hello World Test
    Log to console                   ${MESSAGE}

Browser Test Using Robot Framework
    Robot Browser                    https://www.phptravels.net/admin                ${BROWSER}

Browser Test Using Python
    Python Selenium Test             ${BROWSER}

*** Keywords ***

Robot Browser
    [Arguments]                      ${url}                                          ${BROWSER}
    Open Browser                     url=${url}                                      browser=${BROWSER}
    Wait Until Element Is Visible    css:.input-outlined > input[name='email']
    Click Element                    css:label.input-outlined:nth-child(2) > span
    Press Keys                       css:.input-outlined > input[name='email']       admin@phptravels.com
    Wait Until Element Is Visible    css:.input-outlined > input[name='password']
    Click Element                    css:label.input-outlined:nth-child(3) > span
    Press Keys                       css:.input-outlined > input[name='password']    demoadmin
    Click Element                    css:button[type=submit]
    Wait Until Element Is Visible    logout                                          # This is an id, so you can use just the id name as an argument here
    Close Browser
