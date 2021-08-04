# -*- coding: utf-8 -*-
from selenium import webdriver
import time                                                                                                                                                                    
import os
import urllib.request
import requests
from bs4 import BeautifulSoup 


driver=webdriver.Chrome()


def download_images():


    # url="https://www.pinterest.com/lxt800/psychedelic-spiritual-art/"
    # url="https://www.pinterest.com/mari_saywho/psy-art/"
    # url="https://www.pinterest.dk/vnitya3112/psy-images/?amp_client_id=CLIENT_ID(_)&mweb_unauth_id=%7B%7Bdefault.session%7D%7D&amp_url=https%3A%2F%2Fwww.pinterest.dk%2Famp%2Fvnitya3112%2Fpsy-images%2F&open_share=t"
    # url="https://www.pinterest.co.uk/search/pins/?q=Psychedelic%20art&rs=srs&b_id=BLLPdh1CfKbGAAAAAAAAAABSkE9WYciLRLYMwLxn3XzJuQv_huvDowH6B2SuIgeUbm5PigBwxUBw5HLuEziiFRQ&source_id=gh3BkCv2"
    # url='https://www.pinterest.com/kathleen0765/awesome-nature-paintings/'
    # url="https://www.pinterest.co.uk/amnesia92/spiritual-art-design-of-inspiration/"
    # url="https://www.pinterest.com/catherinemcewenwhalen/object-photography/"
    # url="https://www.pinterest.com/cherryannsavich/background/"
    # url="https://www.pinterest.es/minabarrio/object-photography/"
    # url = "https://www.pinterest.com/morkile9/frames-background/"
    # url ="https://www.pinterest.com/stevem50/tactical-gear/"
    # url="https://www.google.com"
    # url = "https://www.pinterest.com/gmoseshvili/tanks/"
    # url = 'https://www.pinterest.com/mjoksiglandi/artillery/'
    # url = "https://www.pinterest.com/pin/843791680181928083/"
    # url = "https://www.pinterest.co.uk/davidcoates1426/ancient-british-irish-artifacts-and-sites/"
    # url = "https://www.pinterest.com/rabianaz786/frame/"
    # url = "https://in.pinterest.com/shivachinmaya/frame/"
    # url = "https://www.pinterest.com/generalfinishes/uniquely-from-wood/"
    # url = "https://www.pinterest.ie/pin/150166968798770063/"

    # url ="https://www.pinterest.com/pin/363806476132862238/" # ye krna scrap content

    url = "https://www.pinterest.com/Papazrul/psychedelic-neon-trippy-shit/"




    driver.get(url)
    time.sleep(5)


    # For infite scrolling

    SCROLL_PAUSE_TIME = 3
    
    last_height = driver.execute_script("return document.body.scrollHeight")  # Get scroll height
    print (last_height)
    while True:
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Scroll down to bottom
        
        time.sleep(SCROLL_PAUSE_TIME)  # Wait to load page
        
        new_height = driver.execute_script("return document.body.scrollHeight") # Calculate new scroll height and compare with last scroll height
        print (new_height)
        if new_height == last_height:
            break
        last_height = new_height


    img_name=308
    images=driver.find_elements_by_tag_name('img')
    for im in images:
        try:
            # f_image_0=im.get_attribute('srcset')
            f_image_0=im.get_attribute('src')  # for inner pintrest
            f_image=f_image_0                  # for inner pintrest
            # f_image_1=f_image_0.split(',')[-1]
            # print (f_image_1)
            # f_image=f_image_1.split(' ')[1]

            print ('.....')
            f_image = f_image.replace("236x", "736x")
            f_image = f_image.replace("474x", "736x")
            print (f_image)
            content = requests.get(f_image).content
            with open(path+'/'+str(img_name)+'.jpg', 'wb') as handle: handle.write(content)
            # urllib.request.urlretrieve(f_image,path+'/'+str(img_name)+'.jpg')
            img_name=img_name+1
            print ('.Image..'+str(img_name)+' is downloading....')
        except Exception as e:
            print (e)
            pass

     


    print ('''
        ----------
        Downloaded
        ----------''')

         

if __name__ == '__main__':

    

            
    

    path="E:\\NFT-(Daily-Scarping)\\Content-images\\27-july-style-images(pintrest)/"            # Enter folder name
    try:
        os.mkdir("E:\\NFT-(Daily-Scarping)\\Content-images\\27-july-style-images(pintrest)")   # Enter folder name
    except Exception as e:
        print (e)
    try:
        download_images()
    except Exception as e:
        print (e)
        pass
    driver.close()
    driver.quit()



# img=driver.find_elements_by_xpath('/html/body/div[2]/div[2]/div[3]/div[4]/a/img')
# for i in img:
#     d=i.get_attribute('src')



# s=driver.find_elements_by_tag_name('img')
# for i in s:
#     d=i.get_attribute('src')

