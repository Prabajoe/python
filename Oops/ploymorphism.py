class animal:

    # overriding -runtime ploymorphism

    def sound(self):
        print("animal sound")

class dog(animal):

    def sound(self):
        print("bark")

class cat(animal):

    def sound(self):
        print("meow")

c=cat()
c.sound()

class calculator:

    def sum(self ,operator,*args):

        if operator=="add":
            print(args[0]+args[1])
        elif operator=="sub":
            print(args[0]-args[1])
        elif operator=="mul":
            print(args[0]*args[1])
        elif operator=="div":
            print(args[0]/args[1])
        

     def sum(self ,*args):
          
          if len(args)==2:           
           print(args[0]+args[1])
          elif len(args)==3:
           print(args[0]+args[1]+args[2])
          elif len(args)==4:
            print(args[0]+args[1]+args[2]+args[3])
         
         

        
           
       
      



ca=calculator()
ca.sum(1,2,3,4)
