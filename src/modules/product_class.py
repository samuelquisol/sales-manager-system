# Product class representing a product with basic attributes
class Product:
    def __init__(self, id, name, price, stock):
        # Variables (Video 4)
        # Constructor to initialize the product's attributes
        self.id = id  # Attributes (Video 11)
        self.name = name  # Attributes (Video 11)
        self.price = price  # Attributes (Video 11)
        self.stock = stock  # Attributes (Video 11)

    def __str__(self):
        # Method to represent the product as a string
        return f"ID: {self.id}, Name: {self.name}, Price: \n${self.price:.2f}, Stock: {self.stock}"
    
    def create_product_dto():
        id = int(input("\n🆔 Product ID: "))
        name = input("📛 Product Name: ")
        price = float(input("💲 Product Price: "))
        stock = int(input("📦 Product Stock: "))
        product = Product(id, name, price, stock)
        return product
    