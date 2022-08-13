import sys

class machine:
    def __init__(self):
        self.PC = 0 
        self.A = 0 
        self.V = 0
        self.program_memory = []*65535
        self.data_memory = {}
        self.command_register_parameter = [0]
        self.command_register = {
            "ADDi": self.ADDi,
            "ADDm": self.ADDm,
            "ADDpc": self.ADDpc,
            "BVS": self.BVS,
            "LDAi": self.LDAi,
            "LDAm": self.LDAm,
            "LDApc": self.LDApc,
            "STAm": self.STAm,
            "STApc": self.STApc,
            "HLT": self.HLT
        }

    def execute(self):
        command, parameter = self.program_memory[self.PC]
        self.command_register_parameter = parameter
        return self.command_register[command]()

    def ADDi(self):
        if((self.A + self.command_register_parameter[0]) > 65535):
            self.V = 1
        else:
            self.V = 0
        self.A += self.command_register_parameter[0]
        self.PC+=1
    
    def ADDm(self):
        if((self.A + self.data_memory[self.command_register_parameter[0]]) > 65535):
            self.V = 1
        else:
            self.V = 0
        self.A += self.data_memory[self.command_register_parameter[0]]
        self.PC+=1
    
    def ADDpc(self):
        if((self.A + self.PC) > 65535):
            self.V = 1
        else:
            self.V = 0
        self.A+=self.PC 
        self.PC+=1
    
    def BVS(self):
        if (self.V == 1):
            self.PC = self.command_register_parameter[0]
        else:
            self.PC+=1
    
    def LDAi(self):
        self.A = self.command_register_parameter[0]
        self.PC+=1

    def LDAm(self):
        self.A = self.data_memory[self.command_register_parameter[0]]
        self.PC+=1
    
    def LDApc(self):
        self.A = self.PC
        self.PC+=1

    def STAm(self):
        self.data_memory[self.command_register_parameter[0]] = self.A
        self.PC+=1

    def STApc(self):
        self.PC = self.A

    def HLT(self):
        return 0

rm = machine()
rm.program_memory.append(["LDAi", [2]])
rm.program_memory.append(["ADDi",[2]])
rm.program_memory.append(["STAm",[1]])
rm.program_memory.append(["ADDm",[1]])
rm.program_memory.append(["ADDpc",None])
rm.program_memory.append(["ADDi",[70000]])
rm.program_memory.append(["STAm",[100]])
rm.program_memory.append(["BVS", [9]])
rm.program_memory.append([None, None])
rm.program_memory.append(["HLT", None])

while True:
    code = rm.execute()
    if code is None:
        pass
    elif code == 0:
        break
    print("data memory:", rm.data_memory)
    print(" ")
    print("accumulator:",rm.A)
    print(" ")
    print("program memory:",rm.program_memory)
    print(" ")
    print("program counter:",rm.PC)
    print("-------------")