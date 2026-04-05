Feature: Telemetry Visualization

  As a vehicle system
  I want to visualize telemetry data
  So that trends can be analyzed

  Scenario: Generate telemetry plot
    Given speed values "10,20,30"
    And pressure values "5,10,15"
    When I generate telemetry plot
    Then plot file should exist

  Scenario: Invalid input
    Given speed values ""
    And pressure values ""
    When I generate telemetry plot
    Then an error should occur
