import re
import config as conf
symbols_to_remove = "[],"
line_number = 0
line_number2 = 0
addsymbol = "1"
zerosymbol = "0"
fivesymbol = "5"
justzero = "0"
tabstr = 0
folder_path = conf.path_folderway
with open (folder_path, 'r', encoding='utf-8') as paths:
         pathfold = paths.readlines()
         inputfile = (pathfold[1].strip())
         inputfile = inputfile.replace('\\', '/')
         inputfile = inputfile.replace('"', '')
         outputfile = (pathfold[2].strip())
         outputfile = outputfile.replace('\\', '/')
         outputfile = outputfile.replace('"', '')
         print(inputfile)
 
def tabinput(compiledopcode):
   with open (outputfile, 'a', encoding='utf-8') as outfile3:
            print(compiledopcode, file=outfile3, end=' ')
    

   pass
def enterinput(compiledopcode):
   with open (outputfile, 'a', encoding='utf-8') as outfile3:
            print(compiledopcode, file=outfile3, end='\n')
   

   pass
lb1  = 0
lb2  = 0
lb3  = 0
lb4  = 0
lb5  = 0
lb6  = 0
lb7  = 0
lb8  = 0
lb9  = 0
lb10 = 0
lb11 = 0
lb12 = 0
lb13 = 0
lb14 = 0
lb15 = 0
lb16 = 0
lb17 = 0
lb18 = 0
lb19 = 0
lb20 = 0
lb21 = 0
lb22 = 0
lb23 = 0
lb24 = 0
lb25 = 0
lb26 = 0
lb27 = 0
lb28 = 0
lb29 = 0
lb30 = 0
lb31 = 0   
lb32 = 0
lb33 = 0
lb34 = 0
lb35 = 0
lb36 = 0
lb37 = 0
lb38 = 0
lb39= 0 
lb40= 0
lb41= 0
lb42= 0
lb43= 0
lb44= 0 
lb45= 0
lb46= 0
lb47= 0
lb48= 0
lb49= 0
lb50 = 0
lb51 = 0
lb52 = 0
lb53 = 0
lb54 = 0
lb55 = 0
lb56 = 0
lb57 = 0
lb58 = 0
lb59 = 0
lb60 = 0
a=0




with open(inputfile, 'r', encoding='utf-8') as file:
   lines2 = file.readlines()

   
while a==0:
   encstr2 = (lines2[line_number2].strip())
   label2 = re.findall(r"\[([A-Z0-9_]+)\]", encstr2)
   label2 = ''.join(label2)
   label2 = label2.replace("'", "")
   label2 = label2.replace('[', "")
   label2 = label2.replace(']', "")
   label2 = str(label2)
   match label2:
      case "LB1": lb1 = line_number2
      case "LB2": lb2 = line_number2
      case "LB3": lb3 = line_number2
      case "LB4": lb4 = line_number2
      case "LB5": lb5 = line_number2
      case "LB6": lb6 = line_number2
      case "LB7": lb7 = line_number2
      case "LB8": lb8 = line_number2
      case "LB9": lb9 = line_number2
      case "LB10":lb10 = line_number2
      case "LB11":lb11 = line_number2
      case "LB12":lb12 = line_number2
      case "LB13":lb13 = line_number2
      case "LB14":lb14 = line_number2
      case "LB15":lb15 = line_number2
      case "LB16":lb16 = line_number2
      case "LB17":lb17 = line_number2
      case "LB18":lb18 = line_number2
      case "LB19":lb19 = line_number2
      case "LB20":lb20 = line_number2
      case "LB21":lb21 = line_number2
      case "LB22":lb22 = line_number2
      case "LB23":lb23 = line_number2
      case "LB24":lb24 = line_number2
      case "LB25":lb25 = line_number2
      case "LB26":lb26 = line_number2
      case "LB27":lb27 = line_number2
      case "LB28":lb28 = line_number2
      case "LB29":lb29 = line_number2
      case "LB30":lb30 = line_number2
      case "LB31":lb31 = line_number2
      case "LB32":lb32 = line_number2
      case "LB33":lb33 = line_number2
      case "LB34":lb34 = line_number2
      case "LB35":lb35 = line_number2
      case "LB36":lb36 = line_number2
      case "LB37":lb37 = line_number2
      case "LB38":lb38 = line_number2
      case "LB39":lb39 = line_number2
      case "LB40":lb40 = line_number2
      case "LB41":lb41 = line_number2
      case "LB42":lb42 = line_number2
      case "LB43":lb43 = line_number2
      case "LB44":lb44 = line_number2
      case "LB45":lb45 = line_number2
      case "LB46":lb46 = line_number2
      case "LB47":lb47 = line_number2
      case "LB48":lb48 = line_number2
      case "LB49":lb49 = line_number2
      case "LB50":lb50 = line_number2
      case "LB51":lb51 = line_number2
      case "LB52":lb52 = line_number2
      case "LB53":lb53 = line_number2
      case "LB54":lb54 = line_number2
      case "LB55":lb55 = line_number2
      case "LB56":lb56 = line_number2
      case "LB57":lb57 = line_number2
      case "LB58":lb58 = line_number2
      case "LB59":lb59 = line_number2
      case "LB60":lb60 = line_number2
      case "STP":a=1
   line_number2= line_number2 + 1
   
while True:
   encstr = (lines2[line_number].strip())
   stropcodes = re.findall(r"\(([0-9_]+)\)", encstr)
   prt3, prt5, prt6, prt7 = stropcodes
   opcodedata = re.findall(r"([a-z_]+)", encstr)
   curropcode = ''.join(opcodedata)
   jmplabel = re.findall(r"\{([A-Z0-9_]+)\}", encstr)
   jmplabel = ''.join(jmplabel)
   jmplabel = str(jmplabel)
   jmplabel = jmplabel.replace("'", "")
   match jmplabel:
      case "SHIFT":
         shifter = int(prt5)
         currjmpnon = 1
         currjmp = 0
      case "GLB":
         currjmp = int(prt5)
         currjmpnon = 0
         
   match jmplabel:
      case "LB1": currjmp =  lb1
      case "LB2": currjmp =  lb2
      case "LB3": currjmp =  lb3
      case "LB4": currjmp =  lb4
      case "LB5": currjmp =  lb5
      case "LB6": currjmp =  lb6
      case "LB7": currjmp =  lb7
      case "LB8": currjmp =  lb8
      case "LB9": currjmp =  lb9
      case "LB10": currjmp = lb10
      case "LB11": currjmp = lb11
      case "LB12": currjmp = lb12
      case "LB13": currjmp = lb13
      case "LB14": currjmp = lb14
      case "LB15": currjmp = lb15
      case "LB16": currjmp = lb16
      case "LB17": currjmp = lb17
      case "LB18": currjmp = lb18
      case "LB19": currjmp = lb19
      case "LB20": currjmp = lb20
      case "LB21": currjmp = lb21
      case "LB22": currjmp = lb22
      case "LB23": currjmp = lb23
      case "LB24": currjmp = lb24
      case "LB25": currjmp = lb25
      case "LB26": currjmp = lb26
      case "LB27": currjmp = lb27
      case "LB28": currjmp = lb28
      case "LB29": currjmp = lb29
      case "LB30": currjmp = lb30
      case "LB31": currjmp = lb31
      case "LB32": currjmp = lb32
      case "LB33": currjmp = lb33
      case "LB34": currjmp = lb34
      case "LB35": currjmp = lb35
      case "LB36": currjmp = lb36
      case "LB37": currjmp = lb37
      case "LB38": currjmp = lb38
      case "LB39": currjmp = lb39
      case "LB40": currjmp = lb40
      case "LB41": currjmp = lb41
      case "LB42": currjmp = lb42
      case "LB43": currjmp = lb43
      case "LB44": currjmp = lb44
      case "LB45": currjmp = lb45
      case "LB46": currjmp = lb46
      case "LB47": currjmp = lb47
      case "LB48": currjmp = lb48
      case "LB49": currjmp = lb49
      case "LB50": currjmp = lb50
      case "LB51": currjmp = lb51
      case "LB52": currjmp = lb52
      case "LB53": currjmp = lb53
      case "LB54": currjmp = lb54
      case "LB55": currjmp = lb55
      case "LB56": currjmp = lb56
      case "LB57": currjmp = lb57
      case "LB58": currjmp = lb58
      case "LB59": currjmp = lb59
      case "LB60": currjmp = lb60
      case "":currjmp = 0
   
   
   currjmp = int(currjmp)
   intprt3 = int(prt3)
   intprt5 = int(prt5)
   intprt6 = int(prt6)
   intprt7 = int(prt7)
   currjmp = int(currjmp)
   if currjmpnon == 1:
      currjmp = currjmp + shifter
   else:
      curjmp = currjmp
      currjmpnon = 1
   intprt3 = hex(intprt3).split('x')[-1]
   intprt5 = hex(intprt5).split('x')[-1]
   intprt6 = hex(intprt6).split('x')[-1]
   intprt7 = hex(intprt7).split('x')[-1]
   currjmp = hex(currjmp).split('x')[-1]
   intprt3 = str(intprt3)
   intprt5 = str(intprt5)
   intprt6 = str(intprt6)
   intprt = str(intprt7)
   currjmp = str(currjmp)
   
   intprt3 = intprt3.zfill(2)
   intprt5 = intprt5.zfill(4)
   intprt6 = intprt6.zfill(4)
   intprt7 = intprt7.zfill(4)
   currjmp = currjmp.zfill(4)
 
   if curropcode == "add":
      compiledopcode = ''.join(map(str,[zerosymbol,intprt3,"1",intprt5,intprt6,intprt7]))
   if curropcode == "sub":
      compiledopcode = ''.join(map(str,[zerosymbol,intprt3,"2",intprt5,intprt6,intprt7]))
   if curropcode == "ldi":
      compiledopcode = ''.join(map(str,[zerosymbol,intprt3,"3",intprt5,intprt6,intprt7]))
   if curropcode == "ldi":
      compiledopcode = ''.join(map(str,[addsymbol,intprt3,"3",intprt5,intprt6,intprt7]))
   if curropcode == "adi":
      compiledopcode = ''.join(map(str,[zerosymbol,intprt3,"4",intprt5,intprt6,intprt7]))
   if curropcode == "sbi":
      compiledopcode = ''.join(map(str,[addsymbol,intprt3,"2",intprt5,intprt6,intprt7]))
   if curropcode == "jmp":
      compiledopcode = ''.join(map(str,[zerosymbol,intprt3,"5",currjmp,intprt6,intprt7]))
   if curropcode == "brh":
      compiledopcode = ''.join(map(str,[zerosymbol,intprt3,"6",currjmp,intprt6,intprt7]))
   if curropcode == "lrm":
      compiledopcode = ''.join(map(str,[zerosymbol,intprt3,"7",intprt5,intprt6,intprt7]))
   if curropcode == "wnm":
      compiledopcode = ''.join(map(str,["6",intprt3,"8",intprt5,intprt6,intprt7]))
   if curropcode == "wrm":
      compiledopcode = ''.join(map(str,[zerosymbol,intprt3,"8",intprt5,intprt6,intprt7]))
   if curropcode == "rwm":
      compiledopcode = ''.join(map(str,[fivesymbol,intprt3,"8",intprt5,intprt6,intprt7]))
   if curropcode == "rlm":
      compiledopcode = ''.join(map(str,[fivesymbol,intprt3,"7",intprt5,intprt6,intprt7]))
   if curropcode == "orp":
      compiledopcode = ''.join(map(str,[zerosymbol,intprt3,"9",intprt5,intprt6,intprt7]))
   if curropcode == "omp":
      compiledopcode = ''.join(map(str,[zerosymbol,intprt3,"a",intprt5,intprt6,intprt7]))
   if curropcode == "onp":
      compiledopcode = ''.join(map(str,[zerosymbol,intprt3,"b",intprt5,intprt6,intprt7]))
   if curropcode == "irp":
      compiledopcode = ''.join(map(str,[zerosymbol,intprt3,"c",intprt5,intprt6,intprt7]))
   if curropcode == "inp":
      compiledopcode = ''.join(map(str,[addsymbol,intprt3,"c",intprt5,intprt6,intprt7]))
   if curropcode == "brp":
      compiledopcode = ''.join(map(str,["2",intprt3,"6",currjmp,intprt6,intprt7]))
   if curropcode == "brm":
      compiledopcode = ''.join(map(str,["3",intprt3,"6",currjmp,intprt6,intprt7]))
   if curropcode == "brn":
      compiledopcode = ''.join(map(str,[addsymbol,intprt3,"6",currjmp,intprt6,intprt7]))
   if curropcode == "non":
      compiledopcode = ''.join(map(str,["0000000000000000"]))
   if curropcode == "hlt":
      compiledopcode = ''.join(map(str,["000d000000000001"]))
   if curropcode == "crg":
      compiledopcode = ''.join(map(str,["000e000000000001"]))
   if curropcode == "sht":
      compiledopcode = ''.join(map(str,["0000000000000000"]))

   if curropcode == "end":
      break
   if tabstr == 7:
            print ((compiledopcode), end="\n")
            enterinput(compiledopcode)
            tabstr = 0
   else:
      print ((compiledopcode), end=" ")
      tabinput(compiledopcode)

      tabstr = tabstr + 1
   line_number = line_number + 1

   continue
# он делает currjmp на все 



      

         
         




   
   
   

   
   
   

   





  
      

    