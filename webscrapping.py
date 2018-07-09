# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 01:21:29 2018

@author: Ajay
"""

import os
from bs4 import BeautifulSoup

import urllib.request

resp = urllib.request.urlopen('https://www.isbe.net/pages/illinois-state-report-card-data.aspx')
soup = BeautifulSoup(resp.read(), "html.parser")
links = soup.find_all('a')

if not os.path.exists(os.path.dirname('docs/')):
    os.makedirs(os.path.dirname('docs/'))

for link in links:
    if link.get('href'): # and 'docx' in link.get('href'):
        href = link.get('href')
        #print(href.split('/')[-1])
        name = href.split('/')[-1]
        if name == 'rc17_assessment.zip' or name == 'RC17_layout.xlsx': # we could edit the year extension in futre using the date functions
            res = urllib.request.urlopen('https://www.isbe.net' +href)  # or we could just use any suitable regex. or we could pass the file name we want to download
            print(href)
            docx = open('docs/' + name, 'wb')
            docx.write(res.read())
            docx.close()
