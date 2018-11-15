#lexicon 파싱
#lexicon data -> emotion_lexicon.dat
import csv
import os
import sys

def create_temp_item(morph : str, morph_type: str, attribute: str, value: str, split_char):
    temp_item = morph + split_char + morph_type + split_char + attribute + split_char + value
    return temp_item

csvfile = '.\\lexicon\\polarity.csv'
result = 'emotion_lexicon.dat'
data = []
split_char = ':'

if os.path.isfile(result):
    print('기존 ' + result +'파일을 제거하고 새로 만듭니다.')
    #print('기존 ' + result + '파일이 있습니다.' + sys.argv[0] + '을 종료합니다.')
    #exit()
else:
    print('기존 ' + result + '파일이 없어 새로 만듭니다.')

with open(csvfile, 'r', encoding='utf-8') as raw:
    cooked = csv.reader(raw)
    for line in cooked:
        semicolon_index = line[0].find(';')
        if semicolon_index != -1:
            continue
        slash_index = line[0].find('/')
        morph_type = line[0][slash_index+1:]
        morph = line[0][0:slash_index]
        attribute = line[7] ## pos or neg or else
        value = line[8]
        temp_item = create_temp_item(morph, morph_type, attribute, value, split_char)
        data.append(temp_item)

with open(result, 'w', encoding='utf-8') as write_file:
    for line in data:
        write_file.write(line + '\n')