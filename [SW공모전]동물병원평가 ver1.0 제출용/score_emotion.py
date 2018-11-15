#감성 점수를 내주는 스크립트
#morph -> emotion_score
import os

emotion_lexicon_file_name = 'emotion_lexicon.dat'
split_char = ':'
db_dir = 'morph'
result_dir = 'emotion_score'

emotion_dic = {} ##this is class 'dict'
read_data = []

with open(emotion_lexicon_file_name, 'r', encoding='utf-8') as file:
    for line in file:
        division = line.strip().split(split_char)
        read_data.append(division)

if os.path.isdir(db_dir) == False:
    os.mkdir(db_dir)
if os.path.isdir(result_dir) == False:
    os.mkdir(result_dir)

file_list = os.listdir(db_dir)

#딕셔너리 생성
for item in read_data[1:]:
    emotion_dic[(item[0], item[1])] = (item[2], item[3])

for file_name in file_list:
    sum = 0
    number = 0
    keys = []
    average = 0
    if file_name.find('txt') == -1:
        continue
    with open(db_dir + '\\' + file_name, 'r', encoding='utf-8') as read_file:
        for line in read_file:
            key_list = line.strip().split(split_char)
            keys.append((key_list[0], key_list[1]))
    if len(keys) == 0:
        print('점수를 저장합니다.')
        with open(result_dir + '\\' + file_name, 'w', encoding='utf-8') as write_file:
            write_file.write('No data')
        continue

    for key in keys:
        value_tuple = emotion_dic.get(key,(None,None))
        if value_tuple[0] == 'POS':
            sum += float(value_tuple[1])
            number += 1
        elif value_tuple[0] == 'NEG':
            sum -= float(value_tuple[1])
            number += 1
    if number != 0:
        average = sum / number

    print('점수를 저장합니다.')
    with open(result_dir + '\\' + file_name, 'w', encoding='utf-8') as write_file:
        write_file.write(str(average))




