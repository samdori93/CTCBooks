#Filename : MyModule.py

print(__name__)

def min(l):
    temp = 9999
    for i in l:
        if temp > i:
            temp = i
    return temp

def max(l):
    temp = 0
    for i in l:
        if temp < i:
            temp = i
    return temp

def avg(l):
    temp = 0
    num = len(l)
    for i in l:
        temp = temp + i
    temp = temp / num
    return temp

class Myclass:
    def __init__(self, l):
        self.result = 0
        self.l = l
    def min(self):
        temp = 9999
        for i in self.l:
            if temp > i:
                temp = i
        self.result = temp
        return self.result
    def max(self):
        temp = 0
        for i in self.l:
            if temp < i:
                temp = i
        self.result = temp
        return self.result
    def avg(self):
        temp = 0
        num = len(self.l)
        for i in self.l:
            temp = temp + i
        self.result = temp / num        
        return self.result




if __name__ == "__main__":
    a = [10, 50, 22, 47, 69, 99, 5]
    b = Myclass(a)
    
    print('min ->', min(a))
    print('max ->', max(a))
    print('avg ->', avg(a))
    print('b.min ->', b.min())
    print('b.max ->', b.max())
    print('b.avg ->', b.avg())
