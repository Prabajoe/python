class car:
    
    def cardetails(self):
        
        print("carname",self.name)
        print("carcolor",self.color)
        print("speed",self.speed)
    

c=car() 
c1=car()
c.name="bmw"
c.color="Red"
c.speed="200km/per hr"
c.cardetails()  
c1.name="audi" 
c1.color="blue"
c1.speed="230km/per hr"
c1.cardetails()
    
    

