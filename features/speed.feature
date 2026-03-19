Feature: Speed Monitoring

  Scenario: Calculate average and max speed
    Given speed data 40,50,60
    When I monitor speed
    Then average speed should be 50
    And max speed should be 60
