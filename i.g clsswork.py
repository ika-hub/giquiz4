import requests
from bs4 import BeautifulSoup
from time import    sleep
from random import randint

file = open('mobiles.csv', 'w', encoding='utf-8_sig')
headings = 'მობილურის სახელი,ფასი,მონაცემები\n'
file.write(headings)

index = 20
while index < 41:
    url = 'https://zoommer.ge/mobilurebi-2?pagesize=0'+str(index)
    language = {'Accept-Language': 'en-US'}
    r = requests.get(url, headers=language)
    content = (r.text)
    soup = BeautifulSoup(content, 'html.parser')
    smarts = soup.find('div', {'class':'popular_products_inside'})
    # print(smarts)
    all_smarts = smarts.find_all('div', {'class':'lg_3 lp_3 md_4 sm_6 xs_6 product_item'})
    # print(all_smarts)


    for mobiles in all_smarts:
        name = mobiles.find('h4').text
        # url = mobiles.a['href']
        price = mobiles.find('div', class_='product_new_price').text
        info = mobiles.find('div', class_='product_description_hover only_for_desktop_laptop').text
        print(name, price, info)
        # info = each.h4.span.text
        # print(info)
        file.write(name+','+price+','+info+'\n')


    index +=20
    sleep(randint(13,20))

#Pagging სხვანაირად არ გამომივიდა გვერდები არაქვს საიტს და მერე ვნახე "მეტი" აქვს და მაგით იშლება შემდეგი 20.
#Pagging სხვანაირად არ გამომივიდა გვერდები არაქვს საიტს და მერე ვნახე "მეტი" აქვს და მაგით იშლება შემდეგი 20.
