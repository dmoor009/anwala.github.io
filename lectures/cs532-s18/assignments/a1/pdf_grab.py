#!/usr/bin/python

import sys
import urllib3 as UL
from bs4 import BeautifulSoup
import json
import urllib

class PdfGrab:

    http = UL.PoolManager()
    url = None
    response = None
    html = None
    #stat = response.status
    f = None
    links = None
    li = []
    le = None
    
    def __init__(self,url):
        self.url = url   
        self.response = self.http.request('GET', url)
        self.html = self.response.data
        self.f = open("links.txt","a")
        self.links = BeautifulSoup(self.html,'html.parser')
        #grab all link tags and append to list
        self.le = self.links.find_all('a')
    
            
    def handle3Hund(self,url,response):
        location = response.get_redirect_location()
        #print(location)
        if location != False:
            return "{}".format(location)
        else: 
            return "{}".format(u)
    def handle2Hund(self,response):   
        return response.headers['Content-Length']
            
if __name__ == "__main__":
    grab = PdfGrab(sys.argv[1])
    for link in grab.le:
        #url of extrcted link
        u = "{}".format(link.get('href'))
        r = grab.http.request('GET', u,redirect=False)
        #print(r.get_redirect_location())
        while r.status in range (300,399):
            u = "{}".format(grab.handle3Hund(u,r))
            #print (u)
            r = grab.http.request('GET', u,redirect=False)
        #if r.status == 200:
            #print(r.headers)
        if r.headers['Content-Type'] == 'application/pdf':
            size = grab.handle2Hund(r)
            grab.f.write("{}    {}\n".format(u,size))        
        else:
            pass