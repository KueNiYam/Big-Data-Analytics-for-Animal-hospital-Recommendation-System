#결과 분석
import matplotlib.pyplot as plt
import os
import operator

db_dir = 'emotion_score'
result_dir = 'result'
result_graph = result_dir + '\\' + 'result_graph.pdf'
page_name = result_dir + '\\' + 'emotion_score.txt'
statics_file = result_dir + '\\' + 'statics.txt'
file_list = os.listdir(db_dir)
key_list = []
score_list = []
index_alphabet = [] ##아무 값(실행결과 참고)

if os.path.isdir(result_dir) == False:
    os.mkdir(result_dir)

#감정 점수 읽기
for file in file_list:
    if file.find('txt') == -1:
        continue
    with open(db_dir + '\\' + file, 'r', encoding='utf-8') as forRead:
        receive = forRead.readline()
        if receive == 'No data':
            score_list.append(receive)
        else:
            score_list.append(float(receive))
    key_list.append(file)

#병원과 점수목록 출력
with open(page_name, 'w', encoding='utf-8') as page:
    for i in range(len(key_list)):
        page.write(str(key_list[i]) + ': ' + str(score_list[i]) + '\n')
print('병원의 감정 지수가 저장되었습니다.')

#그래프 출력
no_zero_index = []
for i in range(len(key_list)):
    if score_list[i] != 'No data':
        no_zero_index.append(int(i))

no_zero_keys = []
no_zero_alphabets = []
no_zero_scores = []
no_zero_tuples = []
for index in no_zero_index:
    no_zero_scores.append(score_list[index])
    no_zero_keys.append(key_list[index])
    no_zero_tuples.append((key_list[index],score_list[index]))

alphabet = 'a'
for i in range(len(no_zero_index)):
    no_zero_alphabets.append(alphabet)
    if alphabet == 'z':
        alphabet = 'A'
    else:
        alphabet = chr(ord(alphabet) + 1)

plt.title('emotion score distribution')
plt.scatter(no_zero_alphabets, no_zero_scores)
plt.xlabel('hospital')
plt.ylabel('emotion_score')
fig = plt.gcf()
fig.savefig(result_graph)
print('그래프가 저장되었습니다.')

#통계값 - 최댓값, 최솟값, 중간값, 평균값, 분산
sortedTuples = sorted(no_zero_tuples, key=operator.itemgetter(1))
min_value = sortedTuples[0][1]
max_value = sortedTuples[-1][1]
if len(sortedTuples) % 2 == 0:
    mid_value = (sortedTuples[len(sortedTuples) // 2][1]
                + sortedTuples[(len(sortedTuples) // 2) + 1][1]) / 2
else:
    mid_value = sortedTuples[(len(sortedTuples) // 2) + 1][1]

sum_value = 0
for item in sortedTuples:
    sum_value += item[1]

average_value = sum_value / len(sortedTuples)

square_sum = 0
for item in sortedTuples:
    square_sum += item[1] * item[1]

square_sum_average = square_sum / len(sortedTuples)

variance = square_sum_average - (average_value * average_value)

with open(statics_file, 'w', encoding='utf-8') as st_file:
    st_file.write('Max value: ' + str(max_value) + '\n')
    st_file.write('Min value: ' + str(min_value) + '\n')
    st_file.write('Mid value: ' + str(mid_value) + '\n')
    st_file.write('Average value: ' + str(average_value) + '\n')
    st_file.write('Variance: ' + str(variance) + '\n')
print('통계값이 저장되었습니다.')












