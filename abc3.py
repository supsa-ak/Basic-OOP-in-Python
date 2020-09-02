class Computer:

    def __init__(self,cpu,ram):
        self.processor = cpu
        self.memory = ram

    def config(self):
        print('config is ',self.processor, self.memory)

com1 = Computer('i5',16)
com2 = Computer('i7',32)

print(com1.processor)
print(com2.processor)
print(com1.memory)
print(com2.memory)

com1.config()
com2.config()
