####
#### A set of basic steps for use with HTML/webapp pages.
#### These are mostly going to be Selenium.
####
#### Often assumes that the following variables exist:
####  context.browser (as webdiver)
####  context.target (occasional default when getting page)
####

import time
from behave_core.page import *
from behave import step

## The basic and critical "go to page".
@step('I go to page "{page}"')
def step_go_to_page(context, page):
    #print(context.browser.title)
    context.browser.get(context.target + page)

## The basic and critical "go to page".
@step('I go to URL "{page_url}"')
def step_go_to_url(context, page_url):
    #print(page_url)
    context.browser.get(page_url)
    
## Title check.
@step('the title should be "{title}"')
def step_title_should(context, title):
    #print(context.browser.title)
    #print(title)
    assert context.browser.title == title

## The empty title check, a bit of a special case for known "bad" page
## titles.
@step('the title should be ""')
def step_title_empty_should(context):
    assert( context.browser.title == "" or context.browser.title == None )

## The document body should contain a certain piece of text.
@step('the document should contain "{text}"')
def step_doc_contain_should(context, text):
    #print(context.browser.title)
    #print(title)
    webelt = context.browser.find_element_by_tag_name('html')
    assert webelt.text.rfind(text) != -1

## A given element id should contain a given piece of text/content.
@step('the id "{id}" should contain "{text}"')
def step_id_contain_should(context, id, text):
    #print(context.browser.title)
    #print(title)
    webelt = context.browser.find_element_by_id(id)
    assert webelt.text.rfind(text) != -1

## A given class should contain a given piece of text/content. Not
## generably usable by non-dev test writers.
@step('the class "{clss}" should contain "{text}"')
def step_class_contain_should(context, clss, text):
    #print(context.browser.title)
    #print(title)
    webelt = context.browser.find_element_by_class_name(clss)
    assert webelt.text.rfind(text) != -1
