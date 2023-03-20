
import re
import time
import os
import threading
from os import replace
from bs4 import BeautifulSoup
from bs import Bs
from web_client import WebClient as wc

# ('变脸','ebe7b9f6-3485-4b35-8100-ce0ace95b606',12)
# ('jhyx','ebe7b9f6-3485-4b35-8100-ce0ace95b606',59)
# ('xrsc','0ab68d0f-6b09-4d79-8a81-76afe907416a',15)
# ('wtxlnjl','d86df9ba-288a-426b-8ec5-70b5eaebd8d4',12)
# ('yyrq','895fea5c-a099-42e1-a964-79d37b669bda',50)
# ('fctt','dbe1def2-c913-427b-b407-84c6d6d1a707',11)
# ('lafzq','acd59a3a-9a06-4bb5-a03e-5912eb6585f9',15)
# ('jlggdrqtj','7093d995-565e-4562-bcd4-06667f727c9f',13)
# ('rqzjqbdsdxx','616d362f-2275-4cc2-a436-27db3147c644',10)

# ('gcbddrqch','8b71a5f4-f4f3-4e78-9a3e-8584f667fc03',16)
# ('ymdyh','4b7828ce-f2f0-48d0-af46-c08f676bfcde',30)
# ('yqw','6cd2fe73-3646-4967-9184-f338d6818f7c',134)

code=('gcbddrqch','8b71a5f4-f4f3-4e78-9a3e-8584f667fc03',16)

#下载单页
def downpage(in_url,in_num):
    # 取列表
    html=wc.get_string(in_url)
    numA=0
    imgs_url=get_img_url(html,in_num)
    for img_url in imgs_url:
        numA+=1
        file_name=code[0]+'/'+str(in_num)+'_'+str(numA)+'.jpg'
        print(img_url,file_name)
        threading.Thread(target=save_img,args=(img_url,file_name)).start()
        pass    

def save_img(in_url,file_name):
    wc.save_bytes(in_url,file_name)
    pass

def get_img_url(html,in_num):
    i_list=str(Bs.select(html,'script#__NEXT_DATA__'))
    p1='http.*?jpg'
    imgs_url=re.findall(p1,i_list)
    if len(imgs_url)!=0:
        return imgs_url

    html_url2='https://rouman5.xyz/api/books/'+code[1]+'/' +str(in_num)
    html2=wc.get_string(html_url2)
    p1='http.*?jpg'
    imgs_url=re.findall(p1,html2)
    if(len(imgs_url)!=0):
        return imgs_url

    i_list=str(Bs.select(html,'div>img'))
    p1='http.*?jpg'
    imgs_url=re.findall(p1,i_list)
    if len(imgs_url)!=0:
        return imgs_url
    

def main():
    if not os.path.exists(code[0]):
        os.mkdir(code[0])
    else:
        print('is here')
        exit()

    url0='https://rouman5.xyz/books/'+code[1]+'/%s';
    for i in range(0,code[2]):
        url1=url0 %(i)
        downpage(url1,i)
    print('ok')
    pass

main()