Feature: Brake Pressure Analysis

  Scenario: Analyze brake pressure
    Given brake pressure data 10,20
    When I analyze brake pressure
    Then brake output should be 2.0,4.0
