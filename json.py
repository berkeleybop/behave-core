####
#### Basic functions for checking JSON data.
#### Heavily uses JSONPath.
####

from behave import *

import json
import jsonpath_rw

## Adds:
##  context.content_json
@when('the content is converted to JSON')
def step_impl(context):
    if not context.content :
        ## Apparently no text at all...
        assert True is False
    else:
        context.content_json = json.loads(context.content)

@then('the JSON should have the top-level property "{prop}"')
def step_impl(context, prop):
    if not context.content_json :
        ## Apparently no JSON at all...
        assert True is False
    else:
        assert context.content_json.get(prop)

@then('the JSON should have the JSONPath "{jsonpath}"')
def step_impl(context, jsonpath):
    if not context.content_json :
        ## Apparently no JSON at all...
        assert True is False
    else:
        jsonpath_expr = jsonpath_rw.parse(jsonpath)
        res = jsonpath_expr.find(context.content_json)
        #assert len(res) > 0
        #print(res)
        assert res

@then('the JSON should have JSONPath "{jsonpath}" equal to "{thing}" "{value}"')
def step_impl(context, jsonpath, thing, value):
    if not context.content_json :
        ## Apparently no JSON at all...
        assert True is False
    else:
        jsonpath_expr = jsonpath_rw.parse(jsonpath)
        res = jsonpath_expr.find(context.content_json)
        if not res[0] :
            assert True is False
        else:
            if thing == "string":
                assert res[0].value == value
            elif thing == "integer":
                assert res[0].value == int(value)
            elif thing == "float":
                assert res[0].value == float(value)
            else:
                ## Not a thing we know how to deal with yet.
                assert True is False
