class Student:
    def __init__(self,name):
        self.name=name
s1=Student("arjun")
print(s1.name)
print(s1)
del s1
try:
    print(s1)
except Exception as err:
    print(f"{err=},{type(err)=}")

