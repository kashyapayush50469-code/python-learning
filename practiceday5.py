class parent: 
    def __init__(self, fname, lname): 
        self.fname = fname 
        self.lanme = lname 
    def fun_parent(self): 
        print(self.fname, self.lanme)

class child(parent): 
    def __init__(self, fname, lname): 
        parent.__init__(self, fname, lname)  

x = child("arman", "ayush") 
(x.fun_parent()) 

class parent: 
    def __init__(self, fname, lname): 
        self.fname = fname 
        self.lname = lname 
    def fun_parent(self): 
        print(self.fname, self.lname) 

class child(parent): 
    def __init__(self, fname, lname): 
        super().__init__(fname, lname) 

x = child("Ayush", "Arman") 
x.fun_parent() 

class parent: 
    def __init__(self, property, falt): 
        self.property = property 
        self.flat = falt 
    def my_parent(self): 
        print(f"My property will gives my son name is {self.property}") 
        print(f"And theses falt is his {self.flat}") 

class child(parent): 
    def __init__(self, property, flat, property1): 
        super().__init__(property, flat)
        self.property1 = property1

    def welcome(self): 
        print(f"I bought my new property like these {self.property1}") 

y = parent(15, 5) 
y.my_parent()
x = child(15, 5, 10) 
x.welcome() 

class parent: 
    def __init__(self, field, home, pustaniehome): 
        self.field = field 
        self.home = home 
        self.pustaniehome = pustaniehome 

class child(parent): 
    def __init__(self, field, home, pustaniehome, myhome): 
        super().__init__(field, home , pustaniehome)
        self.myhome = myhome 
    def welcome_to(self): 
        print(f"This is my {self.field} and these are my {self.home}") 
        print(f"and those are my {self.pustaniehome} and that is my  {self.myhome}") 

x = child("field", "home", "pust home", "personal home") 
x.welcome_to() 

class car: 
    def __init__(self, car, model): 
        self.car = car 
        self.model = model 
    def move(self): 
        print("drive!") 

class Boat: 
    def __init__(self, boat, model): 
        self.boat = boat 
        self.model = model 
    def move(self): 
        print("sail!") 

class plane: 
    def __init__(self, plane, model): 
        self.plane = plane
        self.model = model 
    def move(self): 
        print("Fly!") 

class taxi: 
    def __init__(self, taxi, model): 
        self.taxi = taxi
        self.model = model 
    def move(self): 
        print("Drive!") 

car1 = car("Bmw", 6.5) 
boat1 = Boat("arua", 5.5)  
plane1 = plane("indigo", 7.5)
taxi1 = taxi("supernova", 6.4) 

for x in (car1, boat1, plane1, taxi1): 
    x.move() 


class machine:
    def __init__(self, brand, model): 
        self.brand = brand 
        self.model = model 
    def move(self): 
        print("drive!") 

class car(machine): 
    pass 

class plane(machine): 
    def move(self): 
        print("Fly!") 

class Boat(machine): 
    def move(self): 
        print("sail!") 

class texi(machine): 
    def move(self):
        print("drive!")

car1 = car("Bmw", "Mustring") 
plane1 = plane("boieng", 787) 
boat = Boat("super", 78) 
texi1 = texi("drive", 456) 

for x in (car1, plane1, boat, texi1): 
    print(x.brand) 
    print(x.model) 
    x.move() 

class protectaion: 
    def __init__(self, name, username, password): 
        self.name = name 
        self.__username = username 
        self.__password = password 

x = protectaion("ayush", "ayush@2010", "53456352347") 
print(x.name) 
'''print(x.__username) 
print(x.__password)''' 

class protection: 
    def __init__(self, name , username, password): 
        self.name = name 
        self.__username = username 
        self.__password = password 
    def get_username(self): 
         return self.__username, self.__password, self.name
x = protection("Ayush", "Ayush@783gmail.com", "Ayush#$$@$$#$#$@$")
print(x.get_username()) 

class Student:
  def __init__(self, name):
    self.name = name
    self.__grade = 0

  def set_grade(self, grade):
    if 0 <= grade <= 100:
      self.__grade = grade
    else:
      print("Grade must be between 0 and 100")

  def get_grade(self):
    return self.__grade

  def get_status(self):
    if self.__grade >= 60:
      return "Passed"
    else:
      return "Failed"

student = Student("Ayush")
student.set_grade(85)
print(student.get_grade())
print(student.get_status())

class computer: 
    def __init__(self): 
        self.cpu = self.cpu() 
        self.ram = self.ram() 

    class cpu: 
        def process(self): 
            print(f"processong data...")

    class ram: 
        def store(self): 
            print(f"storing data....") 

comp = computer() 
comp.cpu.process() 
comp.ram.store() 


class animal: 
    def __init__(self, name, species): 
        self.name = name 
        self.species = species 
    def show_details(self): 
        print(f"name:{self.species}") 
        print(f"species:{self.species}") 

class Dog(animal): 
    def __init__(self, name, breed): 
        animal.__init__(self, name, species= "dog") 
        self.breed = breed 
    def show_details(self):
        animal.show_details(self) 
        print(f"breed: {self.breed}") 

class Goldenretriever(Dog): 
    def __init__(self, name, color): 
        Dog.__init__(self, name, breed = "Goldenretriever") 
        self.color = color 
    def show_details(self):
        Dog.show_details(self) 
        print(f"color:{self.color}") 

x = Goldenretriever("Tomy", "Black")
x.show_details() 


class solution: 
    def __init__(self, r, h): 
        self.r = r 
        self.h = h 
    def volume(self): 
        return 3.14 * self.r * self.r * self.h / 3 

class cyclinder: 
    def __init__(self, r, h): 
        self.r = r 
        self.h = h 
    def volume(self): 
        return 3.14 * self.r * self.r * self.h 

class circle: 
    def __init__(self, r, h): 
        self.r = r 
        self.h = h 
    def volume(self): 
        return 3.14 * self.r * self.r 

a = solution( 7, 5)
b = cyclinder( 5, 2) 
c = circle(7, 1) 
for i in (a, b, c): 
    print(i.volume()) 

class vector:
    def __init__(self, i, j, k):
        self.i = i 
        self.j = j 
        self.k = k

    def __str__(self):
        return f"{self.i}i +{self.j}j +{self.k}k"
    def __add__(self, x):
        # return f"{self.i +x.i}i + {self.j+x.j}j + {self.k + x.k}k" 
        return vector(self.i+ x.i, self.j+x.j, self.k+x.k) 
v1 = vector(3, 5, 6) 
print(v1) 
v2 = vector(1, 2, 9) 
print(v2) 
print(v1 + v2) 
print(type(v1 + v2)) 




class text: 
    def __init___(self, i, j, k): 
        self.i = i 
        self.j = j 
        self.k = k 

    def __str__(self): 
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self, x): 
        return text(self.i + x.i,  self.j + x.j, self.k + x.k)

v1 = text() 
print(v1) 
v2 = text() 
print(v2) 
print(v1 + v2) 
print(type(v1 + v2))












