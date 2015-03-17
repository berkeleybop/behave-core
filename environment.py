####
#### Setup gross testing environment.
####
#### This currently includes the UI instance target and browser type
#### (FF vs PhantomJS).
####

import os
from selenium import webdriver

## Choose a browser based on environment; add the appropriate
## webdriver to the context.
## Reads from environment "BROWSER".
## It defines:
##  context.browser
def start_browser(context):
    ## Default to Firefox for now.
    if 'BROWSER' in os.environ and os.environ['BROWSER'] == 'phantomjs':
        context.browser = webdriver.PhantomJS()
    else:
        context.browser = webdriver.Firefox()

## Do this after completing everything.
def quit_browser(context):
    context.browser.quit()

## Choose a default host to interrogate.
## Reads from environment "TARGET".
## It defines:
##  context.target
def define_target(context, default_target = None):
    ## Determine the server target. Default to localhost if no defined
    ## default
    if not default_target:
        context.target = 'http://localhost'
    ## Pull from environment if possible.
    if 'TARGET' in os.environ:
        context.target = os.environ['TARGET']
