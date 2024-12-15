#make robots
class Robots:
    def __init__(self,name,type,year,color): #this is a method that allows us to assign attributes
        self.name = name  #thses are attributes
        self.type = type
        self.year = year
        self.color = color
   
#make a class and make the robots introduce themselves
    def intro(self):
        print("Hi, my name is "+ self.name +". I am a "+self.type+" type of robot")

    def when(self):
        print(f"I was made in the year {self.year} by Tesla. \n I am {self.color} in color") 

robot_1 = Robots("Tom", "cat", 2002, "blue and white") 
robot_2 =  Robots("Jerry", "mouse", 2003,"brown")

print(robot_1.name)
print(robot_1.type)
print(robot_1.year)
print(robot_1.color)

robot_1.intro()
robot_2.intro()
robot_2.when()