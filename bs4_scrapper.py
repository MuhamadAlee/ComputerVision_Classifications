# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import csv
import unicodecsv                                                                                                                                                                      
# import json
# import requests
import os
import urllib
import urllib.request
from bs4 import BeautifulSoup 
import requests 
import pandas as pd

def quran():
    for i in range(1,115):
        ar=[]
        ur=[]
        qs_arabi="https://www.searchtruth.com/chapter_display.php?chapter="+str(i)+"&translator=17&show_arabic=1"
        arabic = requests.get(qs_arabi)
        arabic_soup = BeautifulSoup(arabic.content, 'html.parser')
        arbi=arabic_soup.find_all(class_="QuranDataArabic word-spacing-arabic w3-right-align")
        qs_trans="https://www.urdupoint.com/islam/quran-urdu/surah-al-baqara/"+str(i)+".html"
        urdu = requests.get(qs_trans)
        urdu_soup = BeautifulSoup(urdu.content, 'html.parser')
        trans=urdu_soup.find_all(class_="fs18 full urdu bsbb pt10 pb10 fr ar rtl lh30")
        
        for j in range(0,len(trans)):
            if i==1:
                arabic=arbi[j+1].text[:-1]
                translation=trans[j].text[3:]
            else:
                arabic=arbi[j].text[:-1]
                translation=trans[j].text[3:]
            ar.append(arabic)
            ur.append(translation)
        surah={'Arabic' : ar,
                'Urdu' : ur}
        
        df = pd.DataFrame(surah, columns = ['Arabic', 'Urdu'])
        df.to_csv("Surah/"+str(i)+".csv",index = False)   







                                                                                                                                                                                                                                                                                                                                                                        #sr_no,productID,a,b,name,c,d,e,short_description,description,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,price,all_category,v,w,image_url,a1,a2,a3,a4,a5,a6,a7,a8,brand,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26

        

def get_url_list(file_name):
    url_list=[]
    f=open(file_name ,'r')
    for i in f:
        i=i.replace('\n','')
        url_list.append(i)
    return url_list


def get_detail():

    # driver.get(li_url)
    li_url='https://pixabay.com/videos/search/nature/'
    page=requests.get(li_url)
    print (page.status_code)
    # time.sleep(1)
    soup=BeautifulSoup(page.text,'lxml')
    

    # try:
    img_no=0
    int_no=0
    images=soup.find_all('div',class_="media")
    for im in images:
        print (int_no)
        f_img='https://makito.es/'+im.find['data-mp4']
        print (f_img)


    print ('-----Downloaded-----')



        

if __name__ == '__main__':
    path="textile_Category"
    try:
        os.mkdir("textile_Category")
    except Exception as e:
        print (e)
    try:
        get_detail()
    except Exception as e:
        print (e)
    

    # driver.close()
    # driver.quit()




