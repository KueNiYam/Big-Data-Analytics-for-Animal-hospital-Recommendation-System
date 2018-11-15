#노원구 동물병원 db를 받아서 폐업을 제거하고 열은 ':' 행은 '\n'으로 분리한 .dat파일로 저장
#Web->processed.dat
import csv
import os
csvfile = 'C:\\Users\\사용자\\Downloads\\서울시 노원구 동물병원 현황.csv'
result = 'processed.dat'
data = []
willBeDeleted = []
with open(csvfile, 'r', encoding='utf-8') as raw:
    cooked = csv.reader(raw)
    for line in cooked:
        data.append(line)

for line in data:
    for item in line:
        if item == '폐업':
            willBeDeleted.append(data.index(line))
            break

willBeDeleted.reverse()

for item in willBeDeleted:
    data.pop(item)

if os.path.isfile(result):
    os.remove(result)
    print('기존 ' + result + '파일을 제거하고 새로 만듭니다.')
else:
    print('기존 ' + result + '파일이 없어 새로 만듭니다.')
with open(result, 'w', encoding='utf-8') as processed:
    for line in data:
        processed.write(':'.join(line))
        processed.write('\n')
















