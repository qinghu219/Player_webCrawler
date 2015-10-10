import scrapy
import json
import re
import requests
import urlparse
import string

class UslsoccerSpider(scrapy.Spider):
    name = "uslsoccer"
    allowed_domain = ["uslpro.uslsoccer.com"]
    start_urls = ["http://uslpro.uslsoccer.com/teams/2014/22310.html#ROSTER"]

    def parse(self, response):
        pattern = re.escape("$j('div#indicator').fadeIn();") + '\s*url\s*=\s*(.*);'
        urlStr = response.selector.re(pattern)[0]
        urlStr = urlparse.urljoin(response.url, string.replace(urlStr, "'", ""))
        html_source = requests.get(urlStr)
        plain_text = html_source.text
        players = json.loads(plain_text)
        i = 1
        for id, player in players["players"].items():
            print "Player", i
            for key, value in player.items():
                print key, ":", value
            i = i + 1