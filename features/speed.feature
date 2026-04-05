Feature: Speed Monitoring

  As a vehicle system
  I want to monitor speed
  So that I can analyze driving behavior

  Scenario Outline: Calculate average and max speed
    Given speed data "<values>"
    When I monitor speed
    Then average speed should be "<avg>"
    And max speed should be "<max>"

    Examples:
      | values        | avg  | max |
      | 40,50,60     | 50   | 60  |
      | 10,20,30,40  | 25   | 40  |
      | 0,100        | 50   | 100 |

 Scenario: Invalid input - negative speed
    Given speed data "40,-10,60"
    When I monitor speed
    Then an error should occur

 Scenario: Invalid input - non-numeric
    Given speed data "40,fast,60"
    When I monitor speed
    Then an error should occur
