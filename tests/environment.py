####
#### Setup gross testing environment.
####

from behave_core.environment import start_browser, define_target, quit_browser
from behave import *

## Run this before anything else.
def before_all(context):
    start_browser(context)
    define_target(context)
    #pass
    
## Do this after completing everything.
def after_all(context):
    quit_browser(context)
    #pass
