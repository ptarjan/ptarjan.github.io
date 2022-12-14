#!/usr/bin/env python
import os
import urllib.request, urllib.error, urllib.parse
from BeautifulSoup import BeautifulSoup
root = 'http://paultarjan.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}

req = urllib.request.Request(root, headers=headers)
page = urllib.request.urlopen(req)
soup = BeautifulSoup(page)
for a in soup('a', rel='me'):
    for img in a('img'):
        src = img['src']
        if 'http://' in src:
            fname = a.text + '.ico'
            fname = fname.replace(' ', '_')

            if os.path.isfile(fname):
                print('Skipping %s' % fname)
                continue
            try:
                req = urllib.request.Request(src, headers=headers)
                data = urllib.request.urlopen(req).read()
                f = open(fname, 'w')
                f.write(data)
                f.close()
            except Exception as e:
                print(src, fname, e)
