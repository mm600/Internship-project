# Created by maria at 12/21/2023
Feature: Test Scenario for filter by sale status High Demand

  Scenario: User can filter by sale status High Demand
    Given Open reelly page
    When Log in to the page
    And Click on “off plan” at the left side menu
    And Filter by sale status of “High Demand”
    Then Verify each product contains the High Demand tag
