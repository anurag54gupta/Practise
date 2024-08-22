class Person:
    name="anonymous"
    def __hello(self):
        print("hello "+"name")
    def welcome(self):
        self.__hello()
p1=Person()
p1.welcome()

