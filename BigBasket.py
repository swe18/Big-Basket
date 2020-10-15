import csv
import pandas as pd
import requests
import json
import numpy as np

#read the JSON response
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3', 'cookie': '_bb_vid="MzgwODQxNTcyOA=="; _bb_tc=0; _bb_rdt="MzE0MDAzNzQxOA==.0"; _bb_rd=6; sessionid=n4esgpg7d93hn53ys2n5wj1c95qvqypv; _ga=GA1.2.2081055311.1601019070; adb=0; _gcl_au=1.1.1918595813.1601019076; _fbp=fb.1.1601019076340.1449883926; _gid=GA1.2.731303090.1601822689; _bb_source=pwa; _gac_UA-27455376-1=1.1602053939.CjwKCAjwq_D7BRADEiwAVMDdHtA17mIBjb8tZDWxK6m9hahxBw9Y4lodxkdN5V0JRv0FzhnPBSjUohoCctQQAvD_BwE; _gcl_aw=GCL.1602053946.CjwKCAjwq_D7BRADEiwAVMDdHtA17mIBjb8tZDWxK6m9hahxBw9Y4lodxkdN5V0JRv0FzhnPBSjUohoCctQQAvD_BwE; _client_version=2326; _bb_hid=382; _bb_cid=24; _bb_aid="MzE5NTMyMDQ5OA=="; csrftoken=DTK1gysc7hXXGy9h9eUT0tilRHKcSnIAux5e4yzRCd8rSqLnKaGNR1IBcmApkXLh; _gat_gtag_UA_27455376_1=1; bigbasket.com=71b919af-2f74-4641-8b09-86461d896895; ts="2020-10-08 11:33:24.484"'}
#url ='https://www.bigbasket.com/product/get-products/?slug=atta&type=deck'
#url = 'https://www.bigbasket.com/product/get-products/?slug=atta&page=2&tab_type=[%22all%22]&sorted_on=relevance&listtype=ps'
url = 'https://www.bigbasket.com/custompage/getsearchdata/?slug=atta&type=deck'
response = requests.get(url, headers=headers)
BigbasketProducts = json.loads(response.text)

total_pages = BigbasketProducts["json_data"]["tab_info"][0]["product_info"]["tot_pages"]

compare = BigbasketProducts["json_data"]["tab_info"][0]["product_info"]["products"]


def printinfo(x):
    res = []
    for i in range(0,len(x)):
        y = x[i]["all_prods"]
        try:
            source_product_url = (x[i]["absolute_url"])
        except:
            source_product_url = None
        try:
            source_product_mrp = (x[i]["mrp"])
        except:
            source_product_mrp = None
        try:
            source_product_id = (x[i]["sku"])
        except:
            source_product_id = None
        try:
            source_product_ratingCount = (x[i]["rating_info"]["rating_count"])
        except:
            source_product_ratingCount  = None
        try:
            source_product_reviewCount = (x[i]["rating_info"]["review_count"])
        except:
            source_product_reviewCount  = None
        try:
            source_product_brand = (x[i]["p_brand"])
        except:
            source_product_brand = None
        try:
            source_product_sellingPrice = (x[i]["sp"])
        except:
            source_product_sellingPrice = None
        try:
            source_product_name = (x[i]["llc_n"])
        except:
            source_product_name = None
        try:
            source_product_weight = (x[i]["w"])
        except:
            source_product_weight = None

        for j in range(0,len(y)):
            try:
                source_product_url_ap = (y[j]["absolute_url"])
            except:
                source_product_url_ap = None
            # if source_product_url == source_product_url_ap:
            #     continue
            try:
                source_product_mrp_ap = (y[j]["mrp"])
            except:
                source_product_mrp_ap = None
            try:
                source_product_id_ap = (y[j]["sku"])
            except:
                source_product_id_ap = None
            try:
                source_product_ratingCount_ap = (y[j]["rating_info"]["rating_count"])
            except:
                source_product_ratingCount_ap = None
            try:
                source_product_reviewCount_ap = (y[j]["rating_info"]["review_count"])
            except:
                source_product_reviewCount_ap = None
            try:
                source_product_brand_ap = (y[j]["p_brand"])
            except:
                source_product_brand_ap = None
            try:
                source_product_sellingPrice_ap = (y[j]["sp"])
            except:
                source_product_sellingPrice_ap = None
            try:
                source_product_name_ap = (y[j]["llc_n"])
            except:
                source_product_name_ap = None
            try:
                source_product_weight_ap = (y[j]["w"])
            except:
                source_product_weight_ap = None

            res.append({'source_product_url': source_product_url_ap, 'source_product_brand ': source_product_brand_ap,
                        'source_product_name': source_product_name_ap, 'source_product_weight': source_product_weight_ap,
                        'source_product_mrp': source_product_mrp_ap,
                        'source_product_sellingPrice': source_product_sellingPrice_ap,
                        'source_product_id': source_product_id_ap,
                        'source_product_ratingCount': source_product_ratingCount_ap,
                        'source_product_reviewCount': source_product_reviewCount_ap})

        res.append({'source_product_url': source_product_url,'source_product_brand ':source_product_brand ,'source_product_name':source_product_name ,'source_product_weight':source_product_weight,'source_product_mrp': source_product_mrp,'source_product_sellingPrice':source_product_sellingPrice,'source_product_id':source_product_id,'source_product_ratingCount':source_product_ratingCount,'source_product_reviewCount':source_product_reviewCount})
    return res

list1 = printinfo(compare)

l = []

for page_no in range(2,(total_pages+1)):
    new_url = 'https://www.bigbasket.com/product/get-products/?slug=atta&page='+str(page_no)+'&tab_type=[%22all%22]&sorted_on=relevance&listtype=ps'
    response = requests.get(new_url, headers=headers)
    BigbasketProducts = json.loads(response.text)
    compare1 = BigbasketProducts["tab_info"]["product_map"]["all"]["prods"]
    list2 = printinfo(compare1)
    l= l+list2

all_list = list1 + l
list_of_unique_dicts=list({v['source_product_url']:v for v in all_list}.values())

print(list_of_unique_dicts)
print(len(list_of_unique_dicts))


#
# df = pd.DataFrame(list_of_unique_dicts)
# df.to_csv('result_trial4.csv')



