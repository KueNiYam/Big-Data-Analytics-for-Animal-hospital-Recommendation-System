#구글에서 크롤링하는 스크립트
#processed.dat -> crawled
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
import time

#for driver get
driver_name = 'chromedriver'
google = 'https://www.google.co.kr/'
google_map = 'https://www.google.com/maps'
#for data
processed_file = 'processed.dat'
url_dir = 'reference_url'
data = [] ##for processed_file
name_index = 2 ##동물병원 이름이 있는 인덱스

#get data
with open(processed_file, 'r', encoding='utf-8') as file:
    for line in file:
        data.append(line.strip().split(':'))
data.pop(0) ## delete category of data

driver = webdriver.Chrome(driver_name)
driver.get(google)

#check dir
if os.path.isdir('crawled') == False:
    os.mkdir('crawled')

#crawl
sites = ['blog.', 'cafe.', 'tistory.', 'twitter.', 'instagram.'] ##types of site which will be crawled
blacks = ['리스트', '모음', '일반정보', '전국', '취업', '연락망', '약도', '구직', '부동산', '전화번호부', '데이터셋', '초등학교',
          '프로그램', '자전거', '맛집'] ##black because of meanless searching

if os.path.isdir(url_dir) == False:
    os.mkdir(url_dir)
for one_tuple in data:
    file_name = 'crawled\\' + one_tuple[name_index] + '.txt'
    url_file = url_dir + '\\' + one_tuple[name_index] + '.txt'
    if os.path.isfile(file_name):
        os.remove(file_name)
    if os.path.isfile(url_file):
        os.remove(url_file)
    with open(url_file, 'a', encoding='utf-8') as url_write:
        with open(file_name, 'a', encoding='utf-8') as forWrite:
            q = driver.find_element_by_name('q')
            q.clear()
            search = '노원구 ' + one_tuple[name_index]
            for black in blacks:
                search += ' -' + black
            q.send_keys(search, Keys.ENTER)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            texts = soup.find_all('cite', {'class':'iUh30'})
            if texts != None:
                for index, text in enumerate(texts):
                    address = text.get_text()
                    for site in sites:
                        if address.find(site) >= 0:
                            driver.find_elements_by_class_name('LC20lb')[index].click()
                            url = driver.current_url
                            html = driver.page_source
                            soup = BeautifulSoup(html, 'html.parser')
                            contents = soup.find_all('p')
                            if contents != None:
                                for content in contents:
                                    forWrite.write(content.get_text() + '\n')
                                url_write.write(url + '\n')
                            driver.back()

driver.close()

