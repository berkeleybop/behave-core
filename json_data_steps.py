####
#### Basic functions for checking JSON data.
#### Heavily uses JSONPath.
####

import json
import jsonpath_rw

# from behave_core.json import *
from behave import step

## Adds:
##  context.content_json
@step('the content is converted to JSON')
def step_convert_to_json(context):
    if not context.content :
        ## Apparently no text at all...
        assert True is False
    else:
        print('json: ', json)
        context.content_json = json.loads(context.content)

## Uses:
##  context.content_json
@step('the JSON should have the top-level property "{prop}"')
def step_json_top_should(context, prop):
    if not context.content_json :
        ## Apparently no JSON at all...
        assert True is False
    else:
        assert context.content_json.get(prop)

## Uses:
##  context.content_json
@step('the JSON should have the JSONPath "{jsonpath}"')
def step_jsonpath_should(context, jsonpath):
    if not context.content_json :
        ## Apparently no JSON at all...
        assert True is False
    else:
        jsonpath_expr = jsonpath_rw.parse(jsonpath)
        res = jsonpath_expr.find(context.content_json)
        #assert len(res) > 0
        #print(res)
        assert res

## Uses:
##  context.content_json
@step('the JSON should have JSONPath "{jsonpath}" equal to "{thing}" "{value}"')
def step_jsonpath_value_should(context, jsonpath, thing, value):
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
