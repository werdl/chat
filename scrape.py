"""
I found this code at the following location
https://stackoverflow.com/questions/74869449/how-to-scrape-the-url-title-and-description-of-google-search-results

Whereas it uses some of the parsing code, I have also added error checking and some pre-processing for later on
"""
from bs4 import BeautifulSoup
import requests, lxml  # lxml for parsing bs4 arg


class Search():

  def __init__(self, query):
    self.query = query
    self.code = 200
    self.text = ""
    self.first = ""
    self.params=""
    self.headers=""
    self.firstlink=""
  def search(self):
    self.params = {
      "q": self.query,
      "hl": "en",
      "gl": "uk",
      "start": 0,
    }
    self.headers = {
      "User-Agent":
      "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"  # set http headers
    }
    data = []
    html = requests.get("https://www.google.com/search",
                        params=self.params,
                        headers=self.headers,
                        timeout=30)  # grab data
    soup = BeautifulSoup(html.text, 'lxml')  # parse data
    for result in soup.select(".tF2Cxc"):  # search through for useful info
      title = result.select_one(".DKV0Md").text
      try:
        snippet = result.select_one(".VwiC3b").text
        add = True
      except:
        add = False
      links = result.select_one(".qLRx3b")
      if add != False:
        data.append({
          "title": title,
          "snippet": snippet,
          "links": links
        })  # search through for useful info
    if data == "":
      self.code = 500  # internal error
    else:
      self.code = 200  # response ok
    self.text = data 
    try:self.first = self.text[0]['snippet']
    except:self.first=self.text