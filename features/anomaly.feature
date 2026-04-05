Feature: Anomaly Detection

  Scenario: Detect anomaly in data
    Given anomaly data "50,55,120"
    When I check anomaly
    Then anomaly should be "True"

  Scenario: No anomaly case
    Given anomaly data "50,52,55"
    When I check anomaly
    Then anomaly should be "False"

  Scenario: Invalid input
    Given anomaly data "50,high,60"
    When I check anomaly
    Then an error should occur
