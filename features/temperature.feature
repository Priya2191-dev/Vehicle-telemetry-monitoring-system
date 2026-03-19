Feature: Engine Temperature Monitoring

  Scenario: Check temperature status
    Given temperature data 80,105
    When I evaluate temperature
    Then status should be Normal,High
