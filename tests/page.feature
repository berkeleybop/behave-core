Feature: All of the basic page functionality works as expected
 The library's page handling and query functions should all
 behave as expected.

 ## No Background necessary.

 @page
 Scenario Outline: the core url getter is okay
   Given I go to url "http://google.com"
    then the title should be "Google"
