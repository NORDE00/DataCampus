import os

def fileopen(f):
    file = open(f,'r')
    global data
    data = file.read()

def word_duration (file_list, sen):
    count = 1
    for filename in file_list:
        
        fileopen(filename)
        data_list = data.split()
        total = 0
        print('#', count) 
        
        for word in sen.split():
            for d in data_list:
                if d == '"'+word+'"':
                    i = data_list.index(d)
                    dur = float(data_list[i-3])-float(data_list[i-5])
                    total = total + dur
                    print("duration of words", d, round(dur,3))
        
        print("total = " , round(total,3))
        count = count + 1

def file_lister(p):
    file_list = os.listdir(p) #현재 경로에서의 file list를 file_list에 저장
    file_list_textgrid = [file for file in file_list if file.endswith(".TextGrid")]
    file_list = file_list_textgrid
    return file_list

sen = "push the button"
file_list = file_lister("C:/Users/sangw/Desktop/DataCampus/Introduction_to_Language_Technology")
word_duration(file_list, sen)