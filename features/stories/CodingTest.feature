Feature: The solution program
    This is simple cli utility
    For New Voice Media
    In order to demonstrate development in Python

    Scenario: It parses incorrect initial input
        Given an instance of the cli
        When I give it an invalid_input in
            | A | $ | a | _ | ~ | ' | 1a3 |
        Then an appropriate error is raised

    Scenario Outline: It allows you to subtract an arbitary number from all inputs
        Given an instance of the cli
        When I give it a set of <input_numbers>
        And I subtract a <difference>
        Then I expect the cli to return <correct_output>

        Examples: Valid subtractions
        | input_numbers |
