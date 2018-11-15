#형태소 분해 스크립트, (형태소, split_char)\n 형식으로 파일 저장
#timmed -> morph
from konlpy.tag import Kkma
import konlpy
import os
import sys

split_char = ':'

kkma = Kkma()
trimmed_dir = 'trimmed'
if os.path.isdir(trimmed_dir) == False:
    raise FileNotFoundError(trimmed_dir + ' 디렉터리가 존재하지 않습니다.')

morph_dir = 'morph'
if os.path.isdir(morph_dir) == False:
    os.mkdir(morph_dir)

file_list = os.listdir(trimmed_dir)

for item in file_list:
    if item.find('txt') is -1:
        continue
    with open(trimmed_dir + '\\' + item, 'r', encoding='utf-8') as read_file:
        raw_text = read_file.readline()
        print(item + '파일의 형태소 분석 중 입니다.')
        morphs = kkma.pos(raw_text)
        print('형태소 분석이 끝났습니다.')
    with open(morph_dir + '\\' + item, 'w', encoding='utf-8') as write_file:
        for morph in morphs:
            write_file.write(morph[0] + split_char)
            write_file.write(morph[1] + '\n')