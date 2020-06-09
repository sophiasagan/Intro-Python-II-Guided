
from category import Category

class Store:
    #attributes
    #name
    #categories(departments)
    
    #constructor - the function that runs every time you create a new instance
    def __init__(self, name, categories): #self refers to the current instance of the class(in JS == "this")
        self.name = name
        self.categories = categories
        self.employees = []

    def __str__(self):
        #transfers obect into string in printing
        #return a string representing the store
        output = f"Welcome to {self.name}!"
        i = 1
        for category in self.categories:
            output += f'\n {i}. {category.name}'
            i += 1
        return output

        # return f"Welcome to {self.name}, have a wonderful day! Here are the categories: {self.categories}"

    def __repr__(self):
        #also returns a string
        return f"self.name = {self.name} ; self.categories = {self.categories}"


running_category = Category("Running", "All your running needs", [])
baseball_category = Category("Baseball", "Tigers Fans Only", [])
basketball_category = Category("Basketball", "Indoor and outdoor products", [])


sports_store = Store("Gander Mountain", [running_category, baseball_category, baseball_category])
produce_store = Store("Trader Joe's", ["Dairy", "Meat", "Bread", "Produce"])

# print(sports_store)
# print(produce_store)
# print(sports_store.name)
#str(sports_store)
# print(repr(sports_store))




#REPL <- Read Evaluate Print Loop
choice = -1
print(sports_store)
print("Type q to quit")
while True:
    # Read
    choice = input("Please choose a category (#):")
    # Evaluate and Print
    try:
        if (choice == 'q'):
            break
        choice = int(choice) - 1
        if choice >= 0 <= len(sports_store.categories):
            print(sports_store.categories[choice])
        else:
            print("The number is out of range")
    except ValueError:
        print("Please entere a valid number")
    

