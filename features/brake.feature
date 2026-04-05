Feature: Brake Pressure Analysis

  As an ADAS system
  I want to analyze brake pressure
  So that braking decisions can be validated

  Scenario Outline: Analyze valid brake pressure data
    Given brake pressure data "<values>"
    When I analyze brake pressure
    Then brake output should be "<expected>"

    Examples:
      | values     | expected   |
      | 10,20      | 2.0,4.0    |
      | 5,15       | 1.0,3.0    |
      | 0,50       | 0.0,10.0   |

  Scenario: Invalid input - negative values
    Given brake pressure data "10,-5"
    When I analyze brake pressure
    Then an error should be raised

  Scenario: Invalid input - non-numeric
    Given brake pressure data "10,abc"
    When I analyze brake pressure
    Then an error should be raised
