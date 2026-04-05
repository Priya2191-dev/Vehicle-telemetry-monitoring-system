Feature: Engine Temperature Monitoring

  As a vehicle system
  I want to monitor engine temperature
  So that overheating can be detected

  Scenario Outline: Check temperature status
    Given temperature data "<values>"
    When I evaluate temperature
    Then status should be "<expected>"

    Examples:
      | values     | expected        |
      | 80,105     | Normal,High     |
      | 100,99     | Normal,Normal   |
      | 150,120    | High,High       |

  Scenario: Invalid input
    Given temperature data "80,hot"
    When I evaluate temperature
    Then an error should occur
