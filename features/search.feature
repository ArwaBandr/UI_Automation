Feature: search functionality
  Scenario: The user can search and see the correct result
    Given The user open the page and clicks on the search icon
    When The user enter a valid search query
    Then The search result should be displayed

  Scenario: The user can see a text to indicate that there is no result
    Given The user open the page and clicks on the search icon
    When The user enter an invalid search query
    Then The user should see a message indicates that there is no search result

    Scenario: The user enters suspicious search input
      Given The user open the page and clicks on the search icon
      When The user enter a suspicious search query
      Then The system should reject the users request

    Scenario: The user input only spaces in the search field
      Given The user open the page and clicks on the search icon
      When The user input a spaces in the search field
      Then The search result should be displayed

   Scenario: The user input one character in the search field
     Given The user open the page and clicks on the search icon
     When The user enter only one character in the search field
     Then The search result should be displayed

   Scenario: The user input a huge number of characters in the search field
     Given The user open the page and clicks on the search icon
     When The user enter a huge number characters in the search field
     Then The system should reject the users request
