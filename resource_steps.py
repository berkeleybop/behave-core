###
### Step definitions.
###

from behave_core.resource import *
from behave import step

## Collector for internal path.
@step('I collect data at path "{path}"')
def step_get_data_path(context, path):
    full_url = context.target + path
    get_and_process(context, full_url, {})

## Collector for remote resource.
@step('I collect data at URL "{url}"')
def step_get_data_url(context, url):
    get_and_process(context, url, {})

@step('the content type should be "{ctype}"')
def step_content_type_should(context, ctype):
    if not context.content_type :
        ## Apparently no content type at all...
        assert True is False
    else:
        assert context.content_type == ctype

@step('the content should contain "{text}"')
def step_content_contain_should(context, text):
    if not context.content :
        ## Apparently no text at all...
        assert True is False
    else:
        assert context.content.rfind(text) != -1
