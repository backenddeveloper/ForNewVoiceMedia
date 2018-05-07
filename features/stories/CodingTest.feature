Feature: The solution program
    This is simple cli utility
    For New Voice Media
    In order to demonstrate development in Python

    Scenario Outline: It errors on invalid charactors in initial input or input of wrong length
        Given I have an input such as <invalid_input>
        When I validate it
        Then the input validation fails
        And a validation_error error is returned to the user

        Examples: invalid charactors
            | invalid_input |
            | 1 2 3 4 5 A   |
            | 1 2 3 4 5 $   |
            | 1 2 3 4 5 a   |
            | 1 2 3 4 5 _   |
            | 1 2 3 4 5 ~   |
            | 1 2 3 4 5 '   |
            | 1 2 3 4 5 1a3 |
            | 1 2 3 4 5 -1  |
            | 1 2 3 4 5 A   |

        Examples: invalid input length
            | invalid_input     |
            | 1                 |
            | 1 2               |
            | 1 2 3             |
            | 1 2 3 4           |
            | 1 2 3 4 5         |
            | 1 2 3 4 5 6 7     |
            | 1 2 3 4 5 6 7 8   |
            | 1 2 3 4 5 6 7 8 9 |

    Scenario: It prints a selection menu
        Given I have an input such as 1 2 3 4 5 6
        When I start a new cli
        Then a menu output is returned to the user

    Scenario Outline: It allows you to subtract an arbitary number from all inputs
        Given I have an input such as <input_numbers>
        When I start a new cli
        And I subtract a <difference>
        Then I expect the cli to return <correct_output>

        Examples: Valid subtractions
        | input_numbers | difference | correct_output    |
        | 1 2 3 4 5 6   | 1          | 0, 1, 2, 3, 4, 5  |
        | 8 7 6 5 4 3   | 3          | 5, 4, 3, 2, 1, 0  |
        | 7 7 7 7 7 7   | 7          | 0, 0, 0, 0, 0, 0  |

    Scenario Outline: It calculates the product
        Given I have an input such as <input_numbers>
        When I start a new cli
        And I calculate a the product
        Then I expect the returned object to be valid JSON
        And that object should contain a key of 'Multiplication' and a value of <product>
        And that object should contain 6 keys containing 'InputNumber'

        Examples: Valid products
        | input_numbers | product |
        | 1 2 3 4 5 6   | 720     |
        | 2 3 4 5 6 7   | 5040    |
        | 3 4 5 6 7 8   | 20160   |
