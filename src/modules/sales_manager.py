import pickle

# SalesManager class that manages a list of products and the sales made
class SalesManager:
    def __init__(self):
        # Variables (Video 4)
        # Constructor that initializes a list of products and the total sales
        self.products = []  # Attributes (Video 11)
        self.total_sales = 0  # Attributes (Video 11)

    def add_product(self, productDto):
        # Method to add a productDto to the list of products (Methods and Attributes - Video 11)
        self.products.append(productDto)
        print("\n--------------------------------")
        print("\n🎉 Product added successfully! 🎉")
        print("\n--------------------------------")

    def show_products(self):
        # Method to display all products in the list (Methods and Attributes - Video 11)
        print("\n📦 Products list:")
        for product in self.products:
            print("\n--------------------------------\n")
            print(product)
        print("\n--------------------------------")

    def perform_sale(self, product_id, quantity):
        # Method to make a sale of a product given its ID and the quantity to sell (Methods and Attributes - Video 11)
        for product in self.products:
            if product.id == product_id:
                # Check if there is enough stock to make the sale (Control Flow - Video 6)
                if quantity <= product.stock:
                    product.stock -= quantity  # Modify the stock (Variables - Video 4)
                    total_sale = quantity * product.price  # Calculate the total sale (Operators - Video 5)
                    self.total_sales += total_sale  # Increase the total sales (Operators - Video 5)
                    print(f"\n✅ Sale completed. Total sale: \n${total_sale:.2f} ✅\n")
                else:
                    print("\n--------------------------------")
                    print("\n❌ Insufficient stock for this sale. ❌\n")
                print("\n--------------------------------")
                return
        print("\n--------------------------------")
        print("\n❌ Product not found. ❌")
        print("\n--------------------------------")

    def calculate_total_sales(self):
        # Method to calculate the total sales made (Methods and Attributes - Video 11)
        return self.total_sales

    def save_products(self, file_name):
        # File Handling (Video 18)
        # Method to save the list of products to a file using pickle (Object Serialization - Video 19)
        with open(file_name, 'wb') as file:
            pickle.dump(self.products, file)
            print("\n--------------------------------")
        print("\n💾 Data saved successfully! 💾")
        print("\n--------------------------------")

    def load_products(self, file_name):
        # File Handling (Video 18)
        # Method to load the list of products from a file using pickle (Object Serialization - Video 19)
        try:
            with open(file_name, 'rb') as file:
                self.products = pickle.load(file)
            print("\n📂 Data loaded successfully! 📂\n")
        except FileNotFoundError:
            print("\n--------------------------------")
            print("\n❌ The file does not exist. ❌")
        print("\n--------------------------------")
