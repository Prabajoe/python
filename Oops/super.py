# # super()
# # super() parent class function call
# # super() parent class __init__() constructor call

# class chola:

#     def __init__(self):
#          print("hi i am chola")


# class chera(chola):
     
     
#      def __init__(self):
#           super().__init__()
#           print("hi i am chera")


#      def chumma(self):
#           print("chumma tha")
          


# class pandiya(chera):
     
#      def __init__(self):
#           super().__init__()
#           super().chumma()
#           print("hi i am pandiya")

# p=pandiya()


class employee:
  
    def __init__(self,emp_id,name,dept):
        print("Employee Info")
        self.emp_id=emp_id
        self.name=name
        self.dept=dept

class manager(employee):

    def __init__(self,emp_id,name,dept,salary):
        print("Manager Info")
        super().__init__(emp_id,name,dept)
        self.salary=salary

    def display(self):
       
        print("EMP ID : ",self.emp_id)
        print("NAME : ",self.name)
        print("DEPARTMENT : ",self.dept)
        print("SALARY : ",self.salary)

m=manager(101,"JOE","IT",20000)
m1=manager(102,"Kumar","BPU",19000)
m.display()
m1.display()