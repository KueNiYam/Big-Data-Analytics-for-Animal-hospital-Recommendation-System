#이 프로그램은 다른 컴퓨터와의 호환성을 생각하지 않고, 특정 컴퓨터에서만 구동되도록 설계되었습니다.
하지만 굳이 실행시키고 싶다면, 아래를 따라주세요.


1.실행환경이 바뀌었을때 바꾸어야할 설정
data_download.py 파일의

download_file_expected = 'C:\\Users\\사용자\\Downloads\\서울시 노원구 동물병원 현황.csv'

를 data_download.py 파일을 실행했을때 파일이 저장되는 절대경로로 바꾼다.
마찬가지로

csvfile = 'C:\\Users\\사용자\\Downloads\\서울시 노원구 동물병원 현황.csv'

도 바꾸어준다.


2.
각 모듈이 있는지 확인하고 다운로드 받는다.


#결과는 result 폴더에 저장됩니다.