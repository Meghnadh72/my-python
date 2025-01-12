class MyClass:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __mydunder__(self):
        return self.first_name + " " + self.last_name

    def get_full_name(self):
        return self.first_name + " " + self.last_name


my_object = MyClass("Ram", "Meghnadh")
special_function = my_object.__mydunder__
print(special_function())
sp_fucntion = my_object.get_full_name
print(sp_fucntion())
