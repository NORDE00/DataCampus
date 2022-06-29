def fileopen(f):
    file = open(f,'r')
    data = file.read()
    data_list = data.replace("=","").split()
    file.close
    return(data_list)

def word_duration (file_list, sen):
    count = 1
    for filename in file_list:
        data_list = fileopen(filename)
        total = 0
        print('#', count)
        
        for word in sen.split():
            for d in data_list:
                if d == '"'+word+'"':
                    i = data_list.index(d)
                    dur = float(data_list[i-2])-float(data_list[i-4])
                    total = total + dur
                    print("duration of words", d, round(dur,3))
        
        print("total = " , round(total,3))
        count = count + 1

import os
path = "./"
file_list = os.listdir(path) #현재 경로에서의 file list를 file_list에 저장
file_list_textgrid = [file for file in file_list if file.endswith(".TextGrid")]
file_list = file_list_textgrid

sen = "push the button"
word_duration(file_list, sen)