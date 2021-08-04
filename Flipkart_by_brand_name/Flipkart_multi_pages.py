from requests import get
from  bs4 import BeautifulSoup as beauty
import json

inp=int(input('Enter how many pages you want to scrape:'))
a=input('Enter brand name that you want to scrape:')
def page_info(inp,a):
    d={}
    list1=[]
    for i in range(1,inp+1):
        print(i,'page is scaping')
        page=get('https://www.flipkart.com/search?q='+a+'&page='+str(i))
        soup=beauty(page.text,'html.parser')
        brand=soup.findAll("div",class_="_4rR01T")
        page_link=soup.findAll('div',class_='_13oc-S')
        full_details=soup.findAll('ul',class_='_1xgFaf')
        price=soup.findAll("div",class_="_30jeq3 _1_WHN1")
        for  i,j,k,l in zip(brand,page_link,full_details,price):
            d['Name']=i.text
            d['main_link']='https://www.flipkart.com'+j.find('a').get('href')
            d['full_info']=k.text
            d['price']=l.text
            list1.append(d.copy())
    return list1

def link_of_img(a):
    list2=[]
    print('second function')
    for i in a:
        lin=i['main_link']
        page=get(lin)
        soup=beauty(page.text,'html.parser')
        link=soup.find('div',class_='_2c7YLP UtUXW0 _6t1WkM _3HqJxg')
        img=link.find('img').get('src')
        list2.append(img)
        print('Run.....')
    return list2

def merge(list2,d):
    print('third function')
    for i,j in zip(d,list2):
        for k in d:
            k['img_link']=j
    with open('Final_data.json','w') as f:
        f.write(json.dumps(d,indent=4))
        f.close()
    print('Run....')
merge(link_of_img(page_info(inp,a)),page_info(inp,a))