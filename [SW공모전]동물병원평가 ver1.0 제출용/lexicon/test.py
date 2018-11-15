file_names = ['expressive-type.csv', 'intensity.csv', 'nested-order.csv', 'polarity.csv'
             , 'subjectivity-polarity.csv', 'subjectivity-type.csv']

for file_name in file_names:
    f = open(file_name, 'r', encoding = 'utf-8')
    lines = f.readlines()
    count=0
    for line in lines:
        print(line)
        count +=1
        if count > 20:
            break
    print()
