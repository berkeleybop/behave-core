####
#### Setup gross testing environment.
####

from behave_core.environment import *
from behave import *

## Run this before anything else.
def before_all(context):
    start_browser(context)
    define_target(context)

## Do this after completing everything.
def after_all(context):
    quit_browser(context)
