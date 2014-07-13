from BeautifulSoup import BeautifulSoup, SoupStrainer
from bs4 import BeautifulSoup
import urllib
import requests
import re
import csv

#1. Use the "generate_search_url" function to create different Urls
#2. Use the "get_listing_urls" to return the listings
#3. use the functions to extract various information from the listing page.

#get_raw_html
#function that when given a raw URL link
#queries and returns the raw html file as String

def get_raw_html(r_link):
    r = requests.get(r_link)
    return r.text


#get_listing_urls
#given a raw html of a single search result page
#extract the list of URL links to actual listings.


def get_listing_urls(rawHtml):
    soup = BeautifulSoup(str(rawHtml))
    for a in soup.findAll('a',href=True):
        if re.findall('/listing/', a['href']):
            print "http://www.boattrader.com" + a['href']

#Generate the search result links

def generate_search_url(pages):
    pagenum = 1
    while pagenum <= pages:
        stem_url = "http://www.boattrader.com/search-results/NewOrUsed-any/Type-any/Category-all/State-all/Year-1920,2015/Sort-Length:DESC/Page-" + str(pagenum) + ",25"
        print str(stem_url)
        pagenum += 1

#Extracting the Listing Details

#The unique identifer of the listing
def get_UID(listing):
    soup = BeautifulSoup(get_raw_html(listing))
    focus = soup.find(attrs={'id':'ad_id'})
    return focus["value"]

#Title of a listing page

def get_title(listing):
    soup = BeautifulSoup(get_raw_html(listing))
    focus =  soup.find("title").text
    return focus.split('-')[0]

#Price
def get_price(listing):
    soup = BeautifulSoup(get_raw_html(listing))
    return soup.find('h2').text

#Decription of a listing
#has to be a better way
def get_description(listing):
    soup = BeautifulSoup(get_raw_html(listing))
    return soup.find('div', {"id":"main-content"}).find('a',{"id":"Contact-Seller-btn"}).next.next.next.next

#List of image URLS
def get_img_URL(listing):
    soup = BeautifulSoup(get_raw_html(listing))
    img_list = []
    for img in soup.findAll('img'):
        search_obj = re.search('http(.*jpg)', str(img))
        try:
            img_list.append(search_obj.group())
        except:
            pass
    return img_list

#Phone Number of a Listing
def get_phone_num(listing):
    soup = BeautifulSoup(get_raw_html(listing))
    return soup.find('div', {"class":"phone"}).text

#Details Section
def get_details(listing):
    soup = BeautifulSoup(get_raw_html(listing))
    return soup.find('div', {"id":"ad_detail"}).text

