####
#### Setup gross testing environment.
####

#import time
from behave_core.environment import start_browser, define_target, quit_browser
from behave import *

## Run this before anything else.
def before_all(context):
    #pass
    start_browser(context)
    define_target(context)
    #time.sleep(10)
    
## Do this after completing everything.
def after_all(context):
    #pass
    quit_browser(context)
