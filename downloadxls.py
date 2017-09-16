###################################################################################################################
# This program fetchs url of xls file from the pages and downloads it
#
###################################################################################################################

import requests
from bs4 import BeautifulSoup
# Python 3.x
# from urllib.request import urlopen, urlretrieve, quote
# from urllib.parse import urljoin

from urllib import urlopen, urlretrieve, quote

# Remove the trailing / you had, as that gives a 404 page
url = 'https://www.rbi.org.in/Scripts/bs_viewcontent.aspx?Id=2009'
u = urlopen(url)
try:
    html = u.read().decode('utf-8')
finally:
    u.close()

# using beautifulsoup to parse the html page
soup = BeautifulSoup(html, "html.parser")

# Select all  <a> elements with href attributes containing URLs starting with http://
for link in soup.select('a[href^="http://"]'):
    href = link.get('href')

    # Make sure it has one of the correct extensions
    if not any(href.endswith(x) for x in ['.csv','.xls','.xlsx']):
        continue
    href = href.replace('http://','https://')
    filename = href.rsplit('/', 1)[-1]
    print("Downloading %s to %s" % (href, filename) )
    urlretrieve(href, filename)
    print("Done.")
    with open("filename.txt", "a") as text_file:
    	text_file.write("\n%s : %s" % (href, filename))