####
#### Basic functions for checking external data resources.
####

from behave import *

import urllib2
import urllib
import httplib

###
### Helpers.
###

## The basic and critical remote collector.
## It defines:
##  context.code
##  context.content_type
##  context.content
##  context.content_length
def get_and_process(context, url, data):

    ## Build request. 
    if data:
        req_data = urllib.urlencode(data)
        req = urllib2.Request(url, req_data)
    else:
        req = urllib2.Request(url)

    ## Make the attempt, or chatty fail.
    #httplib.HTTPConnection.debuglevel = 1    
    response = None
    try:
        response = urllib2.urlopen(req)
    except urllib2.URLError as e:
        print('Tried: ', url)
        if hasattr(e, 'reason'):
            print('Failed to reach server: ', e.reason)
        if hasattr(e, 'code'):
            print('Server error, code: ', e.code)
        if response and response.read():
            print('Response: ', response.read())
        assert True is False
    else:
        ## Final
        pass
    
    ## Parcel out what we have for downstream checking.    
    context.code = response.code
    ## https://docs.python.org/2/library/mimetools.html#mimetools.Message
    context.content_type = response.info().gettype()
    context.content = response.read()
    context.content_length = 0
    if context.content :
        context.content_length = len(context.content)
