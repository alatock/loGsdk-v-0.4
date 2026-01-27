class AssemblerEmulator:
    def __init__(self):
        # Память 32 КБ (32768 байт)
        self.memory = [0] * 32768
        # Регистры 32 штуки
        self.registers = [0] * 32
        # Флаги
        self.flag_eq = False  # равенство
        self.flag_gt = False  # больше
        self.flag_lt = False  # меньше
        # Программный счётчик
        self.pc = 0
        # Лейблы
        self.labels = {}
        # Порты ввода/вывода
        self.ports = {}
        # Статус выполнения
        self.running = True
        
    def parse_instruction(self, instruction):
        """Разбор строки инструкции"""
        # Убираем пробелы и разбиваем по скобкам
        instruction = instruction.strip()
        
        if not instruction:
            return None
            
        # Ищем лейбл если есть
        label = None
        if '[' in instruction and ']' in instruction:
            label_start = instruction.find('[')
            label_end = instruction.find(']')
            label = instruction[label_start+1:label_end]
            instruction = instruction[:label_start]
            
        # Разбиваем по скобкам
        parts = []
        current_part = ""
        bracket_count = 0
        
        for char in instruction:
            if char == '(':
                bracket_count += 1
            elif char == ')':
                bracket_count -= 1
            if char == '(' or char == ')' or (char == ' ' and bracket_count == 0):
                if current_part.strip():
                    parts.append(current_part.strip())
                current_part = ""
            else:
                current_part += char
                
        if current_part.strip():
            parts.append(current_part.strip())
            
        # Парсим тип инструкции
        inst_type = parts[0] if parts else ""
        
        # Парсим параметры
        params = []
        for i in range(1, len(parts)):
            try:
                params.append(int(parts[i]))
            except ValueError:
                params.append(0)
                
        return inst_type, params, label
        
    def execute_instruction(self, instruction):
        """Выполнение одной инструкции"""
        if not instruction:
            return
            
        inst_type, params, label = self.parse_instruction(instruction)
        
        # Если есть лейбл, сохраняем его позицию
        if label:
            self.labels[label] = self.pc
            
        # Проверяем тип инструкции
        if inst_type == "add":
            r1 = params[3] if len(params) > 3 else 0
            r2 = params[2] if len(params) > 2 else 0
            r3 = params[1] if len(params) > 1 else 0
            
            self.registers[r3] = self.registers[r1] + self.registers[r2]
            
        elif inst_type == "sub":
            r1 = params[3] if len(params) > 3 else 0
            r2 = params[2] if len(params) > 2 else 0
            r3 = params[1] if len(params) > 1 else 0
            
            self.registers[r3] = self.registers[r1] - self.registers[r2]
            
        elif inst_type == "ldi":
            r1 = params[1] if len(params) > 1 else 0
            num = params[2] if len(params) > 2 else 0
            
            self.registers[r1] = num
            
        elif inst_type == "adi":
            r1 = params[3] if len(params) > 3 else 0
            num = params[2] if len(params) > 2 else 0
            r3 = params[1] if len(params) > 1 else 0
            
            self.registers[r3] = self.registers[r1] + num
            
        elif inst_type == "sbi":
            r1 = params[3] if len(params) > 3 else 0
            num = params[2] if len(params) > 2 else 0
            r3 = params[1] if len(params) > 1 else 0
            
            self.registers[r3] = self.registers[r1] - num
            
        elif inst_type == "jmp":
            addr = params[1] if len(params) > 1 else 0
            
            # Если адрес в скобках, это лейбл
            if '{' in instruction:
                label_start = instruction.find('{')
                label_end = instruction.find('}')
                label = instruction[label_start+1:label_end]
                if label in self.labels:
                    self.pc = self.labels[label] - 1  # -1 потому что потом будет инкремент
                    return
                    
            self.pc = addr - 1  # -1 потому что потом будет инкремент
            
        elif inst_type == "brh":
            rA = params[3] if len(params) > 3 else 0
            rB = params[2] if len(params) > 2 else 0
            addr = params[1] if len(params) > 1 else 0
            
            if self.registers[rA] == self.registers[rB]:
                # Если есть лейбл
                if '{' in instruction:
                    label_start = instruction.find('{')
                    label_end = instruction.find('}')
                    label = instruction[label_start+1:label_end]
                    if label in self.labels:
                        self.pc = self.labels[label] - 1  # -1 потому что потом будет инкремент
                        return
                else:
                    self.pc = addr - 1  # -1 потому что потом будет инкремент
                    
        elif inst_type == "brn":
            rA = params[3] if len(params) > 3 else 0
            rB = params[2] if len(params) > 2 else 0
            addr = params[1] if len(params) > 1 else 0
            
            # Неравенство
            if self.registers[rA] != self.registers[rB]:
                # Если есть лейбл
                if '{' in instruction:
                    label_start = instruction.find('{')
                    label_end = instruction.find('}')
                    label = instruction[label_start+1:label_end]
                    if label in self.labels:
                        self.pc = self.labels[label] - 1  # -1 потому что потом будет инкремент
                        return
                else:
                    self.pc = addr - 1  # -1 потому что потом будет инкремент
                    
        elif inst_type == "brp":
            rA = params[3] if len(params) > 3 else 0
            rB = params[2] if len(params) > 2 else 0
            addr = params[1] if len(params) > 1 else 0
            
            # Больше нуля
            if self.registers[rA] > 0:
                # Если есть лейбл
                if '{' in instruction:
                    label_start = instruction.find('{')
                    label_end = instruction.find('}')
                    label = instruction[label_start+1:label_end]
                    if label in self.labels:
                        self.pc = self.labels[label] - 1  # -1 потому что потом будет инкремент
                        return
                else:
                    self.pc = addr - 1  # -1 потому что потом будет инкремент
                    
        elif inst_type == "brm":
            rA = params[3] if len(params) > 3 else 0
            rB = params[2] if len(params) > 2 else 0
            addr = params[1] if len(params) > 1 else 0
            
            # Меньше нуля
            if self.registers[rA] < 0:
                # Если есть лейбл
                if '{' in instruction:
                    label_start = instruction.find('{')
                    label_end = instruction.find('}')
                    label = instruction[label_start+1:label_end]
                    if label in self.labels:
                        self.pc = self.labels[label] - 1  # -1 потому что потом будет инкремент
                        return
                else:
                    self.pc = addr - 1  # -1 потому что потом будет инкремент
                    
        elif inst_type == "lrm":
            r1 = params[3] if len(params) > 3 else 0
            ram_addr = params[2] if len(params) > 2 else 0
            
            self.registers[r1] = self.memory[ram_addr]
            
        elif inst_type == "wrm":
            r1 = params[3] if len(params) > 3 else 0
            ram_addr = params[2] if len(params) > 2 else 0
            
            self.memory[ram_addr] = self.registers[r1]
            
        elif inst_type == "lnm":
            num = params[2] if len(params) > 2 else 0
            addr = params[1] if len(params) > 1 else 0
            
            self.memory[addr] = num
            
        elif inst_type == "orp":
            r1 = params[3] if len(params) > 3 else 0
            port_num = params[2] if len(params) > 2 else 0
            
            # Вывод значения регистра в порт
            self.ports[port_num] = self.registers[r1]
            
        elif inst_type == "omp":
            ram_addr = params[2] if len(params) > 2 else 0
            port_num = params[1] if len(params) > 1 else 0
            
            # Запись из памяти в порт
            self.ports[port_num] = self.memory[ram_addr]
            
        elif inst_type == "onp":
            num = params[2] if len(params) > 2 else 0
            port_num = params[1] if len(params) > 1 else 0
            
            # Запись числа в порт
            self.ports[port_num] = num
            
        elif inst_type == "irp":
            r1 = params[3] if len(params) > 3 else 0
            port_num = params[2] if len(params) > 2 else 0
            
            # Считываем значение из порта в регистр
            self.registers[r1] = self.ports.get(port_num, 0)
            
        elif inst_type == "non":
            pass  # Пустая ячейка
            
        elif inst_type == "inp":
            r1 = params[3] if len(params) > 3 else 0
            port_num = params[2] if len(params) > 2 else 0
            
            # Считываем значение из порта в регистр (аналог irp)
            self.registers[r1] = self.ports.get(port_num, 0)
            
        elif inst_type == "hlt":
            self.running = False
            
        elif inst_type == "crg":
            # Обнуляем все регистры
            for i in range(32):
                self.registers[i] = 0
                
        elif inst_type == "add":
            r1 = params[3] if len(params) > 3 else 0
            r2 = params[2] if len(params) > 2 else 0
            r3 = params[1] if len(params) > 1 else 0
            
            self.registers[r3] = self.registers[r1] + self.registers[r2]
            
        elif inst_type == "sub":
            r1 = params[3] if len(params) > 3 else 0
            r2 = params[2] if len(params) > 2 else 0
            r3 = params[1] if len(params) > 1 else 0
            
            self.registers[r3] = self.registers[r1] - self.registers[r2]
            
        elif inst_type == "ldi":
            r1 = params[3] if len(params) > 3 else 0
            num = params[2] if len(params) > 2 else 0
            
            self.registers[r1] = num
            
        elif inst_type == "adi":
            r1 = params[3] if len(params) > 3 else 0
            num = params[2] if len(params) > 2 else 0
            r2 = params[1] if len(params) > 1 else 0
            
            self.registers[r1] = self.registers[r2] + num
            
        elif inst_type == "sbi":
            r1 = params[3] if len(params) > 3 else 0
            num = params[2] if len(params) > 2 else 0
            r2 = params[1] if len(params) > 1 else 0
            
            self.registers[r1] = self.registers[r2] - num
            
        elif inst_type == "jmp":
            addr = params[2] if len(params) > 2 else 0
            
            # Если есть лейбл
            if '{' in instruction:
                label_start = instruction.find('{')
                label_end = instruction.find('}')
                label = instruction[label_start+1:label_end]
                if label in self.labels:
                    self.pc = self.labels[label] - 1  # -1 потому что потом будет инкремент
                    return
                    
            self.pc = addr - 1  # -1 потому что потом будет инкремент
            
        else:
            print(f"Неизвестная инструкция: {inst}")
            
    def run(self, instructions):
        # Сначала пройдем по всем инструкциям и найдем лейблы
        self.labels = {}
        for i, instruction in enumerate(instructions):
            if '[' in instruction:
                label_start = instruction.find('[')
                label_end = instruction.find(']')
                label = instruction[label_start+1:label_end]
                self.labels[label] = i
                
        # Затем выполним программу
        while self.running and self.pc < len(instructions):
            instruction = instructions[self.pc]
            self.execute_instruction(instruction)
            self.pc += 1
            
    def print_memory(self, start=0, end=10):
        for i in range(start, min(end, len(self.memory))):
            print(f"Memory[{i}]: {self.memory[i]}")
            
    def print_registers(self):
        print("Registers:")
        for i in range(32):
            print(f"R{i}: {self.registers[i]}")

# Пример использования:
if __name__ == "__main__":
    # Создаем эмулятор
    emulator = Emulator()
    
    # Пример программы (вам нужно будет заменить на вашу программу)
    program = [
        "ldi (0)(3)(16)(0)",  # Загружаем число 16 в регистр R3
        "ldi (0)(4)(16)(0)",  # Загружаем число 16 в регистр R4
        "add (0)(5)(3)(4)",   # Складываем R3 и R4, результат в R5
        "hlt (0)(0)(0)(0)"    # Останавливаем программу
    ]
    
    # Запускаем программу
    emulator.run(program)
    
    # Печатаем результаты
    print("Результаты:")
    emulator.print_registers()
    emulator.print_memory(0, 20)