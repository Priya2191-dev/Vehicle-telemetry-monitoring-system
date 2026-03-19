Feature: Telemetry Visualization

  Scenario: Generate telemetry plot
    Given speed values 10,20,30
    And pressure values 5,10,15
    When I generate telemetry plot
    Then plot file should exist
