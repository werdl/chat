"""
Old lib, not needed
"""
import requests
import urllib
from requests_html import HTML
from requests_html import HTMLSession
def source(url):
    try:
        session = HTMLSession()
        response = session.get(url)
        return response
    except requests.exceptions.RequestException as e:
        print(e)
def get_results(query):
    query = urllib.parse.quote_plus(query)
    response = source("https://www.google.co.uk/search?q=" + query)
    return response
attemps=0
def parse_results(response):
    global attemps
    if attemps>100:
        return ["An error occured"]
    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = ".VwiC3b"
    results = response.html.find(css_identifier_result)
    output = []  
    for result in results:
        try:
            item = result.find(css_identifier_text, first=True).text
        except:
            attemps+=1
            item=""
            parse_results(response) # try again
        output.append(item)    
    return output
def google_search(query):
    response = get_results(query)
    return parse_results(response)