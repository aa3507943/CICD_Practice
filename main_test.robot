*** Settings ***
Library          Calculator.py

*** Variables ***   


*** Test Cases ***
Test Add
    ${result}   Add    ${2}    ${3}
    Should Be Equal    ${result}    ${5}

Test Subtract
    ${result}   Subtract    ${5}    ${3}
    Should Be Equal    ${result}    ${2}

Test Multiply
    ${result}   Multiply    ${2}    ${3}
    Should Be Equal    ${result}    ${6}

Test Divide
    ${result}   Divide    ${6}    ${3}
    Should Be Equal    ${result}    ${2.0}
