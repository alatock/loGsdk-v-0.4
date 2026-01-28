

import subprocess
import os
from pathlib import Path


ver= "4.0"


def debug_procedure2(path_first, path_second):
    print("CPM: debug process run")
    
    # Проверяем существование первого файла
    if not os.path.exists(path_first):
        print(f"Ошибка: файл 1 {path_first} не найден")
        return
    
    try:
        subprocess.run(['python', path_first], check=True)
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
        subprocess.run(['python', path_second], check=True)
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
    inputfile = runfile / 'dopfile.txt'
    with open (inputfile, "w", encoding = 'utf-8') as clearfile1:
        pass
    outputfile = runfile / 'execute.asm.txt'
    print("clear!")
    print("clear assembly file:")
    with open (outputfile, "w", encoding = 'utf-8') as clearfile2:
        pass
    print ("sucess!")
    pass

runfile = Path(__file__).parent
print (runfile)
print (f"logsdk v {ver}")
print ("loading compiller paths:")
path_first = runfile / 'logbscd.py'
print("\n Loglang compiller:",path_first)
path_second = runfile / 'assembly_compiller.py'
print("\n assembly compiller:",path_second)

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
     


