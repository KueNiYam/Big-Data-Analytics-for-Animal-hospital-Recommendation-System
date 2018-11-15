#데이터를 노원구 홈페이지에서 다운받는 스크립트
from selenium import webdriver
import os
import time
import error

download_file_expected = 'C:\\Users\\사용자\\Downloads\\서울시 노원구 동물병원 현황.csv'
if os.path.isfile(download_file_expected):
    os.remove(download_file_expected)
    print('원본' + download_file_expected + '을 제거하고 새로 다운받습니다.')
else:
    print(download_file_expected + '를 다운받습니다.')

driver_name = 'chromedriver'
driver = webdriver.Chrome(driver_name)
homepage = 'http://data.seoul.go.kr/dataList/datasetView.do?infId=OA-11010&srvType=S&serviceKind=1&currentPageNo=1'
driver.get(homepage)
driver.find_elements_by_class_name('Tab_Inbtn')[1].click()

time.sleep(10)
if os.path.isfile(download_file_expected) == False:
    raise error.DownloadFailedError(download_file_expected)
driver.close()




