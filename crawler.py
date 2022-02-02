#!/usr/bin/env python3

import requests
import re

#Allows you to specify a URL every iteration
url=input("Enter a URL: ")
#Scraping function
def scrape(url):
    r = requests.get(url)
    #REGEX to find all url types
    matches = re.findall(r'href=[\'|\"](\S*)[\'|\"]', r.text)
    fixed = []
    for x in matches:
        try:
            #Differentiates reletive and absolute paths
            if x[0] == '/':
                fixed.append(f'{url}{x}')
                
            elif x[0:4] == 'http':
                fixed.append(x)
            
            else:
                pass
        except IndexError:
            pass

    # print(matches)
    return fixed

#calls function
res = scrape(url)
#print(res)

fin = set()
#goes through the first layer results of the scrape
for x in res:
    fin.add(x)

#gets the results of the scrape and prints it
for x in fin:
    out = print(scrape(x))
#outputs to output.txt
f = open('output.txt', 'a')
f.write(str(out))
f.close()
#goes through the second layer results of the scrape
for y in res:
    fin.add(y)
#gets the results of the scrape and prints it
for y in fin:
    out = print(scrape(y))
    
#outputs to output.txt
f = open('output.txt', 'a')
f.write(str(out))
f.close()