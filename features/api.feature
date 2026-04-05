Feature: API Testing

  Scenario: Get speed data
    When I call speed API
    Then response should contain average

  Scenario: Health check
    When I call health API
    Then status should be running

  Scenario: Invalid speed input
    When I call speed API with invalid data
    Then an error should occur
