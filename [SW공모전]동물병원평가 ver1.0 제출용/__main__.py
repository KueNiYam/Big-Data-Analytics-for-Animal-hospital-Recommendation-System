#스크립트들을 순서대로 실행해주는 메인 함수
import time
import subprocess
import sys

if __name__ == "__main__":
    subprocess.check_call([sys.executable,'data_download.py'])
    subprocess.check_call([sys.executable,'parse_animal_hospital_db.py'])
    subprocess.check_call([sys.executable,'google_crawl.py'])
    subprocess.check_call([sys.executable,'trim_crawled_files.py'])
    subprocess.check_call([sys.executable,'morph_analyser.py'])
    subprocess.check_call([sys.executable,'parse_lexicon.py'])
    subprocess.check_call([sys.executable,'score_emotion.py'])
    subprocess.check_call([sys.executable,'final_analysis.py'])