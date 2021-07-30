class Zoo:
    def __init__(self):
        self.animal_list = []
        self.animal_name = "name"
        self.food = ""
    
    def add_animal(self,obj):
        self.animal_list.append(obj)


class Animal(Zoo): 
    def __init__(self,name):
        super().__init__()
        self.animal_name = name

    def add_food(self,food):
        self.food = food

    def add_names(self,names):
        self.names = names

    def add_catagory(self,catagory):
        self.catagory = catagory

    def add_noise(self,noise):
        self.noise = noise

    def show_animals(self):
        print(self.animals_list)

obj = Zoo()



n=int(input("Enter the count of lion in numbers: "))
for i in range(0,n):
    ani = Animal(f"lion{i+1}")
    names = input(f"Enter the name for Lion {i+1}: ")
    catagory = input(f"Enter the catagory for Lion {i+1}: ")
    noise = input(f"Enter Noise made by lion {i+1}: ")
    food = input(f"Enter Food Loved by lion {i+1}: ") 

    ani.add_noise(noise)
    ani.add_food(names)
    ani.add_catagory(catagory)
    ani.add_names(names)
    obj.add_animal(ani)



n=int(input("Enter the count of giraffe in numbers: "))
for i in range(0,n):
    ani = Animal(f"giraffe{i+1}")
    name = input(f"Enter the name for giraffe {i+1}: ")
    catagory = input(f"Enter the catagory for giraffe {i+1}: ")
    noise = input(f"Enter Noise made by giraffe {i+1}: ")
    food = input(f"Enter Food Loved by giraffe {i+1}: ") 

    ani.add_noise(noise)
    ani.add_food(name)
    ani.add_names(names)
    ani.add_catagory(catagory)
    obj.add_animal(ani)


n=int(input("Enter the count of tiger in numbers: "))
for i in range(0,n):
    ani = Animal(f"tiger{i+1}")
    name = input(f"Enter the name for tiger {i+1}: ")
    catagory = input(f"Enter the catagory for tiger {i+1}: ")
    noise = input(f"Enter Noise made by tiger {i+1}: ")
    food = input(f"Enter Food Loved by tiger {i+1}:") 

    ani.add_noise(noise)
    ani.add_food(name)
    ani.add_names(names)
    ani.add_catagory(catagory)
    obj.add_animal(ani)



n=int(input("Enter the count of elephant in numbers: "))
for i in range(0,n):
    ani = Animal(f"elephant{i+1}")
    name = input(f"Enter the name for elephant {i+1}: ")
    catagory = input(f"Enter the catagory for elephant {i+1}: ")
    noise = input(f"Enter Noise made by elephant {i+1}: ")
    food = input(f"Enter Food Loved by elephant {i+1}: ") 

    ani.add_noise(noise)
    ani.add_food(name)
    ani.add_names(names)
    ani.add_catagory(catagory)
    obj.add_animal(ani)


n=int(input("Enter the count of deer in numbers: "))
for i in range(0,n):
    ani = Animal(f"deer{i+1}")
    name = input(f"Enter the name for deer {i+1}")
    catagory = input(f"Enter the catagory for deer {i+1}")
    noise = input(f"Enter Noise made by deer {i+1}")
    food = input(f"Enter Food Loved by deer {i+1}") 

    ani.add_noise(noise)
    ani.add_food(name)
    ani.add_names(names)
    ani.add_catagory(catagory)
    obj.add_animal(ani)


for i in obj.animal_list:
    print(i.animal_name)
    print("name",i.names)
    print("catagoty",i.catagory)
    print("noise",i.noise)
    print("food",i.food)


