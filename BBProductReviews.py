import csv
import pandas as pd
import requests
import math
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
url = 'https://www.bigbasket.com/product-reviews/126906/aashirvaad-atta-whole-wheat-10-kg-pouch/?page=1'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content,'html.parser')

data1 = soup.find('div', class_ ='_3E_3Z _3DhQU')
Rating = data1.find('div', class_='_1hJeb').get_text()
r = int(Rating[0:4])
x = math.ceil(r/10)


def printinfo(y):
    res = []
    for i in range(0,len(data)):
        try:
            star_rating = data[i].find('div', class_='_2Ze34').get_text()
        except:
            star_rating ='None'
        try:
            heading = data[i].find('div', class_='GM5RN').get_text()
        except:
            heading ='None'
        try:
            review_text = data[i].find('div', class_='zF-ya').get_text()
        except:
            review_text ='None'
        try:
            reviewer_name = data[i].find('div', class_='_2oF3-').get_text()
            reviewer_name = reviewer_name.split(",")[0]
        except:
            reviewer_name ='None'
        try:
            review_date= data[i].find('div', class_='_2oF3-').get_text()
            review_date = review_date.split("(")[0]
            review_date = review_date[:len(review_date) - 1]
        except:
            review_date ='None'
        try:
            upvote= data[i].find('div', class_='_2R0cI').get_text()
        except:
            upvote ='None'
        try:
            reviewer_location = data[i].find('div', class_='_2oF3-').get_text()
            reviewer_location = reviewer_location.split(",")[1]
            reviewer_location  = reviewer_location .split("(")[0]
        except:
            reviewer_location ='None'

        res.append({'star_rating': star_rating, 'heading ': heading,
                    'review_text': review_text, 'reviewer_name': reviewer_name,'review_date':review_date,'upvote':upvote,'reviewer_location':reviewer_location })
    return res

l = []

for page_no in range(1,(x+1)):
    new_url = 'https://www.bigbasket.com/product-reviews/126906/aashirvaad-atta-whole-wheat-10-kg-pouch/?page='+str(page_no)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content,'html.parser')
    data = soup.find_all('div', class_="_2K9Rb")
    list2 = printinfo(data)
    l= l+list2

print(l)
df = pd.DataFrame(l)
df.to_csv('reviews_result.csv')
