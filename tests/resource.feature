
Feature: Library external resource handling is sane
 Library handling resources behaves as expected.
 
 ## No Background necessary.

 @resource
 Scenario: User attempts to use consume the JSON
    Given I collect data at URL "http://amigo.geneontology.org/amigo/term/GO:0022008/json"
     then the content type should be "application/json"
      and the content should contain "results"
