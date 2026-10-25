class Employee:
    #magic method/dunder method/constructor
    def __init__(self , name ,id , dep , ):
        self.name = name 
        self.id = id
        self.dep = dep
        print("This constructor will be called automatically")

    #methods
    def travel(self, destination):
        print("This wont be executed when the object is made but rather when called")
        print(f"Employee is now travelling to {destination}")


#creating the object
sam = Employee("Sam" , 34 , "Data Science")

#printing attribute
print(sam.dep)

#calling method
sam.travel("Mumbai")
