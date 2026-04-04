import re
import numpy
from pathlib import Path

runfile = Path(__file__).parent

line_number2 = 0
a = False
labels = numpy.zeros(60)
pattern_a_multi = r'r(\d+)'
port_pattern = r'P(\d+)'
freenumpatr = r"'([0-9-._]+)'"
symbols_to_remove = "[],"
modepattrn = r'"([a-z._]+)"'
heshpattrn = r'#([a-zA-Z0-9_]+)'
plusminpattern = r"[\,+\,-,\*/]"
ram_pattern = r'&(\d+)'


inputfile = runfile / 'execute.lbc.txt'
outputfile = runfile / 'dopfile.txt'

with open (outputfile, 'w+', encoding='utf-8') as outfile2:
        pass

def outstr(main_str):
    with open (outputfile, 'a', encoding='utf-8') as outfile2:
            print(main_str, file=outfile2)
def closestr():
         with open (outputfile, 'a', encoding='utf-8') as outfile2:
            print("hlt (0)(0)(0)(0)", file=outfile2)
            print("[STP]", file=outfile2)
            pass

         
with open (outputfile, 'a', encoding='utf-8') as outfile:
            print("sht (0)(0)(0)(0){SHIFT}", file=outfile, end= '\n')
            #print("crg (0)(0)(0)(0)", file=outfile) бывшая команда для отчищения регистров,  перекачивала ещё со времён эмулятора logisim
            m_str = "".join(map(str,["sht"," ","(",0,")","(",0,")","(",0,")","(",0,")","{","SHIFT","}"]))
            print(m_str)

with open(inputfile, 'r', encoding='utf-8') as file3:
        lines = file3.readlines()
        while a == False:
            encstr2 = (lines[line_number2].strip())
            func_meta = re.search(r'(\w+)(?=.)', encstr2)
            func_meta = {func_meta.group(1)}
            func_meta = str(func_meta)
            func_meta = func_meta.replace('{', "")
            func_meta = func_meta.replace('}', "")
            func_meta = func_meta.replace("'", "")
            #print("func:", func_meta)
            if func_meta == "halt":
                print("hlt (0)(0)(0)(0)")
                print("[STP]")
                closestr()
                break

            if func_meta != "halt" and func_meta != "go" and func_meta != "label" and func_meta != "assig":
                        regmeta = re.findall (pattern_a_multi, encstr2)
                        "".join(regmeta)
                        
            if func_meta != "halt" and func_meta != "math" and func_meta != "go" and func_meta != "label":
                        num_meta = re.findall(freenumpatr, encstr2)
                        "".join(num_meta)
                        num_meta = str(num_meta)
                        num_meta = num_meta.replace('[', "")
                        num_meta = num_meta.replace(']', "")
                        num_meta = num_meta.replace("'", "")
                    
            if func_meta == "math":
                    mode_meta = re.findall(modepattrn, encstr2)
                    "".join(mode_meta)
                    mode_meta = str(mode_meta)
                    mode_meta = mode_meta.replace('[', "")
                    mode_meta = mode_meta.replace(']', "")
                    mode_meta = mode_meta.replace("'", "")
            if func_meta == "go":
                        label_meta = re.search(heshpattrn, encstr2)
                        label_meta = {label_meta.group(1)}
                        label_meta = str(label_meta)
                        label_meta = label_meta.replace('{', "")
                        label_meta = label_meta.replace('}', "")
                        label_meta = label_meta.replace("'", "")
            if func_meta == "label":
                        label_meta = re.search(heshpattrn, encstr2)
                        label_meta = {label_meta.group(1)}
                        label_meta = str(label_meta)
                        label_meta = label_meta.replace('{', "")
                        label_meta = label_meta.replace('}', "")
                        label_meta = label_meta.replace("'", "")
            if func_meta == "if":
                        brh_meta = re.search(r"([$=<>])", encstr2)
                        brh_meta = {brh_meta.group(1)}
                        brh_meta = str(brh_meta)
                        brh_meta = brh_meta.replace('{', "")
                        brh_meta = brh_meta.replace('}', "")
                        brh_meta = brh_meta.replace("'", "")
                        label_meta = re.search(heshpattrn, encstr2)
                        label_meta = {label_meta.group(1)}
                        label_meta = str(label_meta)
                        label_meta = label_meta.replace('{', "")
                        label_meta = label_meta.replace('}', "")
                        label_meta = label_meta.replace("'", "")
            if func_meta == "raml":
                        mode_meta = re.search(modepattrn, encstr2)
                        mode_meta = {mode_meta.group(1)}
                        mode_meta = str(mode_meta)
                        mode_meta = mode_meta.replace('{', "")
                        mode_meta = mode_meta.replace('}', "")
                        mode_meta = mode_meta.replace("'", "")
                        if mode_meta != "m":
                                    ram_meta = re.search(ram_pattern, encstr2)
                                    ram_meta = {ram_meta.group(1)}
                                    ram_meta = str(ram_meta)
                                    ram_meta = ram_meta.replace('{', "")
                                    ram_meta = ram_meta.replace('}', "")
                                    ram_meta = ram_meta.replace("'", "")
            if func_meta == "ramw":
                        mode_meta = re.search(modepattrn, encstr2)
                        mode_meta = {mode_meta.group(1)}
                        mode_meta = str(mode_meta)
                        mode_meta = mode_meta.replace('{', "")
                        mode_meta = mode_meta.replace('}', "")
                        mode_meta = mode_meta.replace("'", "")

                        if mode_meta != "m":
                                    ram_meta = re.search(ram_pattern, encstr2)
                                    ram_meta = {ram_meta.group(1)}
                                    ram_meta = str(ram_meta)
                                    ram_meta = ram_meta.replace('{', "")
                                    ram_meta = ram_meta.replace('}', "")
                                    ram_meta = ram_meta.replace("'", "")
            if func_meta == "out":
                         port_meta = re.search(port_pattern, encstr2)
                         port_meta = {port_meta.group(1)}
                         port_meta = str(port_meta)
                         port_meta =  port_meta.replace('{', "")
                         port_meta =  port_meta.replace('}', "")
                         port_meta =  port_meta.replace("'", "")
                         mode_meta = re.search(modepattrn, encstr2)
                         mode_meta = {mode_meta.group(1)}
                         mode_meta = str(mode_meta)
                         mode_meta = mode_meta.replace('{', "")
                         mode_meta = mode_meta.replace('}', "")
                         mode_meta = mode_meta.replace("'", "")
            if func_meta == "input":
                         port_meta = re.search(port_pattern, encstr2)
                         port_meta = {port_meta.group(1)}
                         port_meta = str(port_meta)
                         port_meta =  port_meta.replace('{', "")
                         port_meta =  port_meta.replace('}', "")
                         port_meta =  port_meta.replace("'", "")
                         mode_meta = re.search(modepattrn, encstr2)
                         mode_meta = {mode_meta.group(1)}
                         mode_meta = str(mode_meta)
                         mode_meta = mode_meta.replace('{', "")
                         mode_meta = mode_meta.replace('}', "")
                         mode_meta = mode_meta.replace("'", "")
                        
            # начало компиляции строки
            opcode = "non"
            main_str = "non (0)(0)(0)(0)"
            reg0 = 0
            reg1 = 0
            reg2 = 0
            reg3 = 0
            if func_meta == "assig":
                    ldi_meta = re.search(pattern_a_multi, encstr2)
                    ldi_meta = {ldi_meta.group(1)}
                    ldi_meta = str(ldi_meta)
                    ldi_meta = ldi_meta.replace('{', "")
                    ldi_meta = ldi_meta.replace('}', "")
                    ldi_meta = ldi_meta.replace("'", "")
                    opcode = "ldi"
                    main_str = "".join(map(str,[opcode," ","(",reg0,")","(",ldi_meta,")","(",num_meta,")","(",ldi_meta,")"]))
            if func_meta == "math":
                if mode_meta is not "":
                    reg1 = regmeta
                    reg1 = str(reg1)
                    reg1 = reg1.replace('[', "")
                    reg1 = reg1.replace(']', "")
                    reg1 = reg1.replace("'", "")
                    num_meta = re.search(freenumpatr, encstr2)
                    num_meta = num_meta.group(1)
                    num_meta = str(num_meta)
                    num_meta = num_meta.replace('[', "")
                    num_meta = num_meta.replace(']', "")
                    num_meta = num_meta.replace("'", "")
                    if mode_meta == "i":
                            opcode = "adi"
                            main_str = "".join(map(str,[opcode," ","(",reg0,")","(",reg1,")","(",num_meta,")","(",reg1,")"]))
                    if mode_meta == "d":
                            opcode = "sbi"
                            main_str = "".join(map(str,[opcode," ","(",reg0,")","(",reg1,")","(",num_meta,")","(",reg1,")"]))
                else:
                        operator_meta = re.search(r'[-+*/]', encstr2)
                        if operator_meta:
                              operator_meta = operator_meta.group() 
                        operator_meta = str(operator_meta)
                        operator_meta = operator_meta.replace('{', "")
                        operator_meta = operator_meta.replace('}', "")
                        operator_meta = operator_meta.replace("'", "")
                        reg1, reg2, reg3 = regmeta
                        if operator_meta == "+":
                            opcode = "add"
                            main_str = "".join(map(str,[opcode," ","(",reg0,")","(",reg3,")","(",reg2,")","(",reg1,")"]))
                        if operator_meta == "*":
                            opcode = "mul"
                            main_str = "".join(map(str,[opcode," ","(",reg0,")","(",reg3,")","(",reg2,")","(",reg1,")"]))
                        if operator_meta == "-":
                            opcode = "sub"
                            main_str = "".join(map(str,[opcode," ","(",reg0,")","(",reg3,")","(",reg2,")","(",reg1,")"]))
                        if operator_meta == "/":
                            opcode = "div"
                            main_str = "".join(map(str,[opcode," ","(",reg0,")","(",reg3,")","(",reg2,")","(",reg1,")"]))

            if func_meta == "go":
                    opcode = "jmp"
                    main_str = "".join(map(str,[opcode," ","(",reg0,")","(",reg0,")","(",reg0,")","(",reg0,")","{",label_meta,"}"]))

            if func_meta == "global":
                    reg1 = regmeta
                    reg1 = str(reg1)
                    if reg1 != "[]":
                            reg1 = reg1
                            reg1 = str(reg1)
                            reg1 = reg1.replace('[', "")
                            reg1 = reg1.replace(']', "")
                            reg1 = reg1.replace("'", "")

                    else:
                        reg1 = 0
                    opcode = "gmp"
                    mode_meta = re.findall(modepattrn, encstr2)
                    "".join(mode_meta)
                    mode_meta = str(mode_meta)
                    mode_meta = mode_meta.replace('[', "")
                    mode_meta = mode_meta.replace(']', "")
                    mode_meta = mode_meta.replace("'", "")
                    main_str = "".join(map(str,[opcode," ","(",reg0,")","(",reg0,")","(",reg0,")","(",reg1,")","{",mode_meta,"}"]))
            if func_meta == "transf":
                    reg1, reg2 = regmeta
                    opcode = "mov"
                    main_str = "".join(map(str,[opcode," ","(",reg0,")","(",reg2,")","(",reg0,")","(",reg1,")"]))


            if func_meta == "label":
                    opcode = "non"
                    main_str = "".join(map(str,[opcode," ","(",reg0,")","(",reg0,")","(",reg0,")","(",reg0,")","[",label_meta,"]"]))
            if func_meta == "if":
                    if brh_meta == "=":
                            opcode = "brh"
                            reg1,reg2 = regmeta
                            main_str = "".join(map(str,[opcode," ","(",reg0,")","(",reg0,")","(",reg2,")","(",reg1,")","{",label_meta,"}"]))
                    if brh_meta == "<":
                            opcode = "brm"
                            reg1,reg2 = regmeta
                            main_str = "".join(map(str,[opcode," ","(",reg0,")","(",reg0,")","(",reg2,")","(",reg1,")","{",label_meta,"}"]))
                    if brh_meta == ">":
                            opcode = "brp"
                            reg1,reg2 = regmeta
                            main_str = "".join(map(str,[opcode," ","(",reg0,")","(",reg0,")","(",reg2,")","(",reg1,")","{",label_meta,"}"]))
                    if brh_meta == "$":
                            opcode = "brn"
                            reg1 = regmeta
                            reg1 = str(reg1)
                            reg1 = reg1.replace('[', "")
                            reg1 = reg1.replace(']', "")
                            reg1 = reg1.replace("'", "")
                            main_str = "".join(map(str,[opcode," ","(",reg0,")","(",reg0,")","(",num_meta,")","(",reg1,")","{",label_meta,"}"]))
            if func_meta == "raml":
                    if mode_meta == "r":
                            opcode = "lrm"
                            reg1 = regmeta
                            reg1 = str(reg1)
                            reg1 = reg1.replace('[', "")
                            reg1 = reg1.replace(']', "")
                            reg1 = reg1.replace("'", "")
                            main_str = "".join(map(str,[opcode," ","(",reg0,")","(",reg1,")","(",ram_meta,")","(",reg0,")"]))
                    if mode_meta == "m":
                            opcode = "rlm"
                            reg1, reg2 = regmeta
                            main_str = "".join(map(str,[opcode," ","(",reg0,")","(",reg2,")","(",reg1,")","(",reg0,")"]))
            # я даун, и по эмому я перепутал загрузку/запись в память lrm - запись числа из памяти в регистр, а вот wrm это запись из регистра в память!             
            if func_meta == "ramw":  
                    if mode_meta == "r":
                            opcode = "wrm"
                            reg1 = regmeta
                            reg1 = str(reg1)
                            reg1 = reg1.replace('[', "")
                            reg1 = reg1.replace(']', "")
                            reg1 = reg1.replace("'", "")
                            main_str = "".join(map(str,[opcode," ","(",reg0,")","(",reg0,")","(",ram_meta,")","(",reg1,")"]))
                    if mode_meta == "n":
                            opcode = "wnm"
                            main_str = "".join(map(str,[opcode," ","(",reg0,")","(",reg0,")","(",ram_meta,")","(",num_meta,")"]))
                    if mode_meta == "m":
                            opcode = "rwm"
                            reg1, reg2 = regmeta
                            main_str = "".join(map(str,[opcode," ","(",reg0,")","(",reg0,")","(",reg2,")","(",reg1,")"]))
                    if mode_meta == "c":
                            opcode = "wam"
                            arr_symb = re.findall(r'\[(.*?)\]', encstr2)
                            arr_symb = str(arr_symb)
                            arr_symb = arr_symb.replace("'", '')
                            main_str = "".join(map(str,[opcode," ","(",reg0,")","(",reg0,")","(",ram_meta,")","(0)",arr_symb]))
            if func_meta == "out":
                    if mode_meta == "r":
                            opcode = "orp"
                            reg1 = regmeta
                            reg1 = str(reg1)
                            reg1 = reg1.replace('[', "")
                            reg1 = reg1.replace(']', "")
                            reg1 = reg1.replace("'", "")
                            main_str = "".join(map(str,[opcode," ","(",reg0,")","(",reg0,")","(",reg1,")","(",port_meta,")"]))
                    if mode_meta == "n":
                            opcode = "onp"
                            main_str = "".join(map(str,[opcode," ","(",reg0,")","(",reg0,")","(",num_meta,")","(",port_meta,")"]))
                    if mode_meta == "m":
                            opcode = "omp"
                            main_str = "".join(map(str,[opcode," ","(",reg0,")","(",reg0,")","(",ram_meta,")","(",port_meta,")"]))
                            
            if func_meta == "input":
                    if mode_meta == "r":
                            opcode = "irp"
                            reg1 = regmeta
                            reg1 = str(reg1)
                            reg1 = reg1.replace('[', "")
                            reg1 = reg1.replace(']', "")
                            reg1 = reg1.replace("'", "")
                            main_str = "".join(map(str,[opcode," ","(",reg0,")","(",reg1,")","(",reg0,")","(",port_meta,")"]))
                            pass
            if func_meta == "section":
                    None
            print(main_str)
            outstr(main_str)
            line_number2 += 1