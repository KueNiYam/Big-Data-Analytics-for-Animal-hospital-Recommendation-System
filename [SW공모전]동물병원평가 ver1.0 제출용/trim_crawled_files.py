#크롤링된 파일들 사이 사이의 '\n'와 split_char_of_morph_analyser로 선언된 특수문자를 모두 제거한다.
#crawled -> trimmed
import os

split_char_of_morph_analyser = ':'

def remove_splitchar_of_morph_analyser(text : str, splitchar):
    new_text = text
    index = new_text.find(splitchar)
    while index != -1:
        new_text = new_text.replace(splitchar, ' ')
        index = new_text.find(splitchar)
    return new_text

crawled_dir = 'crawled'
if os.path.isdir(crawled_dir) == False:
    raise FileNotFoundError(crawled_dir + ' 디렉터리가 존재하지 않습니다.')

trimmed_dir = 'trimmed'
if os.path.isdir(trimmed_dir) == False:
    os.mkdir(trimmed_dir)

file_list = os.listdir(crawled_dir)

for item in file_list:
    if item.find('txt') == -1:
        continue
    new_file = ''
    with open(crawled_dir + '\\' + item, 'r', encoding='utf-8') as read_file:
        for line in read_file:
            text = line.strip()
            text = remove_splitchar_of_morph_analyser(text, split_char_of_morph_analyser)
            new_file += text
    with open(trimmed_dir + '\\' + item, 'w', encoding='utf-8') as write_file:
        write_file.write(new_file)