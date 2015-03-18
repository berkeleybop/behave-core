
Feature: Library JSON handling is sane
 Library handling of JSON blobs behaves as expected for various inputs.
 
 ## No Background necessary.

 @json
 Scenario: User attempts to use consume the JSON
    Given I collect data at URL "http://amigo.geneontology.org/amigo/term/GO:0022008/json"
    when the content is converted to JSON
     then the JSON should have the top-level property "results"
      and the JSON should have the top-level property "type"
      and the JSON should have the JSONPath "results.term_dbxref_links[*].dbname"
      and the JSON should have JSONPath "results.name" equal to "string" "neurogenesis"
