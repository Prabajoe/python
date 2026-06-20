from abc import ABC ,abstractmethod

class parent(ABC):

    def growth(self,name):
        print(name)
        print("good person")
        print("respect everyone")
        print("be health")

    @abstractmethod
    def study(self):
      pass  
    
    @abstractmethod
    def marriage(self):
        pass
        
        
    


class child(parent):

     def study(self):
         print("MCA")
     
     @abstractmethod
     def marriage(self):
        pass

class child2(parent):

    def study(self):
        print("BCA")

    def marriage(self):
        print("Priya")
        
c2=child2()
c2.growth("JOE")
c2.study()
c2.marriage()

      
        


