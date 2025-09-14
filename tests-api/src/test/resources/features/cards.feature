Feature: cards api
  Background:
    * url 'http://app:8080'

  Scenario: list cards
    Given path '/cards'
    When method get
    Then status 200
    And match response == []

  Scenario: create and update limit
    Given path '/cards'
    And request { holder: 'Alice', limit: 1000 }
    When method post
    Then status 200
    And match response.holder == 'Alice'
    * def id = response.id

    Given path '/cards', id, 'limit'
    And request { limit: 1500 }
    When method patch
    Then status 200
    And match response.limit == 1500