###
### Step definitions.
###

import behave_core
from behave import step

## Collector for internal path.
@given('I collect data at path "{path}"')
def step_impl(context, path):
    full_url = context.target + path
    get_and_process(context, full_url, {})

## Collector for remote resource.
@given('I collect data at URL "{url}"')
def step_impl(context, url):
    get_and_process(context, url, {})

@then('the content type should be "{ctype}"')
def step_impl(context, ctype):
    if not context.content_type :
        ## Apparently no content type at all...
        assert True is False
    else:
        assert context.content_type == ctype

@then('the content should contain "{text}"')
def step_impl(context, text):
    if not context.content :
        ## Apparently no text at all...
        assert True is False
    else:
        assert context.content.rfind(text) != -1
