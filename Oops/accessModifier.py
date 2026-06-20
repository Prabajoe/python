class parent:

    def __init__(self,name,age,accountno):
        
        self.name=name
        self._age=age
        self.__accountno=accountno

    def display(self):
        print(self.name)
        print(self._age)
        print(self.__accountno)



class child(parent):


    def __init__(self, name, age, accountno):
        super().__init__(name, age, accountno)

    


c=child("praba",33,123345)
print(c.name)
print(c._age)

c.display()