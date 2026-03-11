class car: 
    def __init__(self, num, tum, hum, drame): 
        self.nums = num 
        self.tums = tum 
        self.sums = hum 
        self.drames = drame 

    def branded_car(self): 
        print(self.nums.upper()) 

    def most_dimindngcar(self): 
        print(self.tums.upper()) 

    def most_favouritecar(self): 
        print(self.sums.upper()) 

    def chinese_bestcars(self): 
        print(self.drames.upper()) 
    
obj_num = car("rolse roise", "bmw", "tesla", "byd") 
obj_num1 = car("tata", "mihindrea", "scarpyue", "byd")
obj_num1.branded_car() 
obj_num1.most_dimindngcar() 
obj_num1.most_favouritecar() 
obj_num1.chinese_bestcars() 

class Employee(): 
    def __init__(self, name): 
        self.name = name 
    def show(self): 
        print(f"The employee name is {self.name}") 

class collegues: 
    def __init__(self, hiswork): 
        self.hiswork = hiswork 
    def show(self): 
        print(f"His work is {self.hiswork}") 

class restorenent(Employee, collegues): 
    def __init__(self, hiswork, name): 
        self.hiswork = hiswork 
        self.name = name 

x =restorenent("computer based", "Ankush") 
print(x) 
print(x.name) 
print(x.hiswork) 
x.show() 
print(restorenent.mro()) 
              

class Employee: 
    def __init__(self, name): 
        self.name = name 
    def show_name(self):
        print(f"My name is {self.name}") 

class occupation: 
    def __init__(self, occupation): 
        self.occupation = occupation 
    def show_details(self):
        print(f"My occupation is {self.occupation}")
    
class Home: 
    def __init__(self, myhome): 
        self.myhome = myhome 
    def my_home(self):
        print(f"My home is in {self.myhome}") 

class threeclass(Employee, occupation, Home): 
    def __init__(self, name, occupation, myhome): 
        self.name = name 
        self.occupation = occupation
        self.myhome = myhome 

x = threeclass("Ayush", "programmer", "Darbhanga") 

x.show_name() 
x.show_details() 
x.my_home()


class three(): 
    def __init__(self, name, occupation, myhome): 
        self.name = name 
        self.occupation = occupation
        self.myhome = myhome 

    def show_details_yourself(self): 
        print(f"My name is {self.name}") 
        print(f"My occupation is {self.occupation}") 
        print(f"My home is in {self.myhome} ") 

x = three("Ayush", "python programmer", "Darbhanga") 
x.show_details_yourself() 

class routine: 
    def __init__(self, hobby, play): 
        self.hobby = hobby 
        self.play = play 
    def tell_me_about_your_hobby(self): 
        print(f"My hobby is {self.hobby}") 
        print(f"Do you like a play {self.play}") 

x = routine("play chase", "cricket. no i watch cricket") 
x.tell_me_about_your_hobby() 
print("world       trade    organization")
class bigcompany: 
    def __init__(self, name, networth): 
        self.name = name 
        self.networth = networth 
    def company_details(self): 
        print(f"The biggest company name is {self.name}") 
        print(f"The companies networth is {self.networth}")  
class secondbigcomany: 
    def __init__(self, nme, natworth): 
        self.name = nme 
        self.networth = natworth  
    def show_company_details(self): 
        print(f"The second biggest company name is {self.name}") 
        print(f"companies networth is {self.networth}") 
        print(f"we are called search engine") 
class thirdlargestcompany: 
    def __init__(self, nam, nitworth): 
        self.name = nam 
        self.networth = nitworth 
    def show_details(self): 
        print(f"The third largest company is {self.name}") 
        print(f"The companies networth is {self.networth}") 
class combine(bigcompany, secondbigcomany, thirdlargestcompany): 
    def __init__(self, name, networth): 
        self.name = name 
        self.networth = networth 
    def __init__(self, nme, natworth): 
        self.name = nme 
        self.networth = natworth
    def __init__(self, nam, nitworth): 
        self.name = nam 
        self.networth = nitworth

x = combine("NVDIA", 4.5)
x.company_details() 
y = combine("Google", 3.9)
y.show_company_details()
z = combine("microsoft", 3.4) 
z.show_details()
print("hello       universe")
class company: 
    def __init__(self, name, networth): 
        self.name = name 
        self.networth = networth
    def company_detail(self): 
        print(f"The largest company name is {self.name}")
        print(f"The company networth is {self.networth}") 
    
    def __init__(self, name, networth): 
        self.name = name 
        self.networth = networth  
    def show_detail(self): 
        print(f"The second largest name is {self.name}") 
        print(f"The compines networth is {self.networth}") 

    def __init__(self, name, networth): 
        self.name = name 
        self.networth = networth 
    def show(self): 
        print(f"The third largest company name is {self.name}") 
        print(f"The companies networth is {self.networth}")

a = company("NVDIA", 4.5) 
a.company_detail() 
b = company("Google", 3.9) 
b.show_detail() 
c = company("microsoft", 3.4) 
c.show()

class myclass: 
    def __init__(self, num, cum): 
        self.num = num 
        self.cum = cum 

    def even_number(self): 
        for i in range(1, 20): 
            if i % 2 == 0: 
                print(i)  

    def odd_number(self): 
        for i in range(1, 30): 
            if i % 2 != 0: 
                print(i) 

z = myclass(20, 30)
z.even_number() 
z.odd_number() 

class table: 
    def __init__(self, num, kum): 
        self.num = num 
        self.kum = kum 
    def prime_num(self): 
        for i in range(2, self.num + 1): 
            count = 0 
            for x in range(1, i + 1): 
                if i % x ==0: 
                    count += 1 
            if count == 2: 
              print(i) 

    def check_num(self): 
        count = 0 
        for i in range(1, self.kum + 1): 
            if self.kum % i ==0: 
                count += 1 
        if count == 2: 
            print("prime numbers:")
        else: 
            print("not a prime numbers:") 
e = table(19, 7) 
e.prime_num() 
e.check_num() 

class multitable: 
    def __init__(self, rum , sam): 
        self.rum = rum 
        self.sam = sam 
    def multiplication_table(self): 
        for i in range(1, 16): 
            print(self.rum, "*", i, "=", i * self.rum) 

    def multi_table(self): 
        for i in range(1, 16): 
            print(self.sam, "*", i, "=", i * self.sam)
            if i == 15: 
                break 
y = multitable(16, 16) 
y1 = multitable(16, 15)
y1.multiplication_table() 
y1.multi_table() 

class calculator: 
    def add_num(self, a, b): 
        return a + b 
    def  sub_num(self, a, b): 
        return a - b 
    def multiply_num(self, a, b): 
        return a * b 
    def divided_num(self, a, b): 
        return a / b 
x = calculator() 
print(x.add_num(1200, 1000)) 
print(x.sub_num(1200, 1000))  
print(x.multiply_num(1200, 1000)) 
print(x.divided_num(1200, 1000))

class Employee: 
    def __init__(self, name, id , address): 
        self.name = name 
        self.id = id 
        self.address = address
    def __str__(self): 
        return f"The Employee name is {self.name} and his id no = {self.id} or his address is {self.address}" 

e = Employee("Abhishek", 1240, "patana") 
print(e)

class company: 
    def __init__(self, name, networth): 
        self.name = name 
        self.networth = networth
    def __str__(self): 
         return (f"the company name is {self.name} and his networht is {self.networth}") 
x = company("css", 2) 
print(x) 

class school: 
    def __init__(self, schoolname, propertyname): 
        self.schoolname = schoolname 
        self.propertyname = propertyname 
    def __str__(self): 
        return f"who is owener of the property {self.propertyname} and what is the school name {self.schoolname}" 
x = school("mrm. college", "ram kishor")
print(x) 

class intro: 
    def __init__(self, name, age, quallification): 
        self.name = name 
        self.age = age 
        self.quallification = quallification 
    def __str__(self):
        return f"My name is {self.name} and my age is {self.age} and i am studing in diploma {self.quallification}" 
i = intro("Aysuh", 16, "in computer science") 
print(i) 

class sentence: 
    def __init__(self, profession, quallification): 
        self.pro = profession 
        self.qua = quallification 
    def __str__(self): 
        return f"what is your profession {self.pro} and waht is  {self.qua}"

ayush = sentence("promagging", "diploma") 
print(ayush) 

class parent: 
    def __init__(self, name, work): 
        self.name = name 
        self.work = work 
    def praent_method(self): 
        print(f"this is also called {self.name}") 
        print(f"this is also called {self.work}")  
    
class child(parent): 
    pass 

obj = child("base clss", "derived class") 
obj.praent_method() 

class parent: 
    def __init__(self, property, farmhouse): 
        self.property = property 
        self.farmhouse = farmhouse 
    def parent_property(self): 
        print(f"that all property is for my {self.property}") 
        print(f"And farmhouse is also have my {self.farmhouse}") 

class child(parent): 
    def __init__(self, property, farmhouse, salary): 
        parent.__init__(self, property, farmhouse) 
        self.salary = salary 

x = child("child", "ankush", 50)   

class parentclass: 
    def parent_method(self): 
        print("This is the parent method.") 

class childclass(parentclass): 
    def parent_method(self):
        print("Ayush")  
        super().parent_method()
    def child_method(self): 
        print("This is the child method.") 
        super().parent_method() 

child_object = childclass() 
child_object.child_method() 
child_object.parent_method()

