

import subprocess
import os
import config as conf


ver= "2.0"


def debug_procedure2(path_first, path_second):
    print("CPM: debug process run")
    
    # Проверяем существование первого файла
    if not os.path.exists(path_first):
        print(f"Ошибка: файл 1 {path_first} не найден")
        return
    
    try:
        subprocess.run(['python', path_first, path_way], check=True)
        print("CPM: loGbasic -> assembly completed!")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка выполнения первого файла: {e}")
        return
    except Exception as e:
        print(f"Неожиданная ошибка при запуске первого файла: {e}")
        return
    
    # Проверяем существование второго файла
    if not os.path.exists(path_second):
        print(f"Ошибка: файл 2 {path_second} не найден")
        return
        
    try:
        subprocess.run(['python', path_second, path_way], check=True)
        print("CPM: assembly -> mashine_code completed!")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка выполнения второго файла: {e}")
        return
    except Exception as e:
        print(f"Неожиданная ошибка при запуске второго файла: {e}")
        return
    
    print(f"CPM: sucsessfuly debug! v/{ver}")
def clearfiles():
    print("clear loGlang file:")
    with open (path_way, 'r', encoding='utf-8') as paths:
         pathfold = paths.readlines()
         inputfile = (pathfold[1].strip())
         inputfile = inputfile.replace('\\', '/')
         inputfile = inputfile.replace('"', '')
         outputfile = (pathfold[2].strip())
         outputfile = outputfile.replace('\\', '/')
         outputfile = outputfile.replace('"', '')
    with open (inputfile, "w", encoding = 'utf-8') as clearfile1:
        pass
    print("clear!")
    print("clear assembly file:")
    with open (outputfile, "w", encoding = 'utf-8') as clearfile2:
        pass
    print ("sucess!")
    pass

print (f"logsdk v {ver}")
print ("loading compiller paths:")
code_path = conf.path_progway
code_path = code_path.replace('\\', '/')
code_path= code_path.replace('"', "")
print (code_path)
with open (code_path, 'r', encoding='utf-8') as paths:
        pathfold = paths.readlines()
        inputfile = (pathfold[0].strip())
        outputfile = (pathfold[1].strip())
path_first = inputfile
path_first = path_first.replace('\\', '/')
path_first = path_first.replace('"', '')
print("\n Loglang compiller:",path_first)
path_second = outputfile
path_second = path_second.replace('\\', '/')
path_second = path_second.replace('"', '')
print("\n assembly compiller:",path_second)
path_way = conf.path_folderway
path_way = path_way.replace('\\', '/')

print("\n folder file path:", path_way)
print ("loading completed, press Y to start, r to crear code files(промежуточные)")
start_button = input()

if start_button == "y":
    print("clear cash files:\n")
    clearfiles()
    debug_procedure2(path_first, path_second)
if start_button == "r":
    print("вы точно хотите отчистить все промежуточные файлы? y/n")
    input1 = input()
    if input1 == "y":
        clearfiles()
    if input1 == "n":
        pass
     


