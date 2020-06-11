class Category:
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
    
    def __str__(self):
        # product_list = 
        return f"{self.name}: {self.description}"