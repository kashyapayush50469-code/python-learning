class car: 
    str1 = "tiear" 
    str2 = "staring" 
    # str3 = "motorguard" 
    # str4 = "seatbelt" 
    # str5 = "driving seat" 

car_obj = car() 
car_obj1 = car() 
car_obj1.str1 = "seatbelt" 
print(car_obj.str1)
print(car_obj1.str1) 

# # keyword- class class_name

# class Home:
#     st1 = "Belan"   # properties 
#     st2 = "Gas"   # properties 
#     st3 = "Bed"   # properties 
#     st4 = 10
#     st5 = 50.0
    


# obj = Home()
# obj1 = Home()
# obj2 = Home()

# del obj1
# print(st1)
# print(st2)

# class Persion:
#     age = 16
#     Village = "Kahua"

# p_obj = Persion()
# # age = p_obj.age
# # village = p_obj.Village
# # # p_obj.age = 25
# # # p_obj.Village = "Neuri"
# # age = 25
# # village = "Neuri"

# print(age, village)

# We are going to see Construture 
class Persion:
    # age = 16
    # Village = "Kahua"

    # def __init__(self):
    #     self.age = 20
    #     self.Village = "Neuri"

    def __init__(self, age , village, Name, Father):
        self.age1 = age
        self.village1 = village
        self.name = Name
        self.Father = Father

p_obj = Persion(20,"Kahua", "Ayus", "Pawan jha")

p_obj.age1 = 25
p_obj.village1 ="neuri"
p_obj.name = "Gaurav"
p_obj.Father ="Khesari Mishra"

print(p_obj.age1)
print(p_obj.village1)
print(p_obj.name)
print(p_obj.Father)



class Table:

    def __init__(self, num, strs , fllot):
        self.nums = num
        self.str = strs
        self.fllot = fllot

    def Table_f(self):
        print("Output 1")
        for i in range(1, 11):

            print(i*self.nums)
    
    def Even_f(self):
        print("Output 2")
        if self.nums % 2 == 0:
            print("Even")
        else:
            print("ODD")
    
    def Upper_f(self):

        print(self.str.upper())
    
    def float_F(self):
        print(self.fllot)



# 1. Print Table    
# 2. Even or ODD   
# 3. upper case 
# 3. upper case 

p_obj = Table(7, "Ayush", 25.5)
p_obj1 = Table(8, "Gaurav", 20.5)


p_obj.Table_f()
p_obj.Even_f()

print("other objet or objet1")
p_obj1.Upper_f()
p_obj1.float_F()


# def __init__(self, Khet_area, Ghar_area):

    #     self.Khet_area = Khet_area
    #     self.Ghar_area = Ghar_area
    
    # def print_all(self):
    #     print(f"khet ka area {self.Khet_area} and ghar ka area{ self.Ghar_area }")

class Bacha_ka_Bacha(Child): #parent vo dadaji honge
    pass


# papa = Parent(250, 10)

# childs = Child(250, 10)

baacha = Child(30, 60, 56)

baacha.print_all()
baacha.print_child()

