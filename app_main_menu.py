from src.modules.sales_manager import SalesManager
from src.modules.product_class import Product

# Classes and Objects (Video 10)
sales_manager = SalesManager()

while True:
    # Control Flow (Video 6)
    # Menu of options to interact with the sales management system
    print("\n--------------------------------\n")
    print("             📋 Main Menu")
    print("1. Add Product")
    print("2. Show Products List")
    print("3. Perform Sale")
    print("4. Calculate Total Sales")
    print("5. Save Recent Products Data")
    print("6. Load Products Data from a File")
    print("7. Exit")
    print("\n--------------------------------")
    
    option = input("Select an Option: ")

    if option == "1":
        # Option to add a new product
        product = Product.create_product_dto()
        sales_manager.add_product(product)

    elif option == "2":
        # Option to display the list of products
        sales_manager.show_products()

    elif option == "3":
        # Option to perform a sale of a product
        product_id = int(input("\n🆔 Product ID to sell: "))
        quantity = int(input("🔢 Quantity to sell: "))
        sales_manager.perform_sale(product_id, quantity)

    elif option == "4":
        # Option to calculate the total sales made
        total_sales = sales_manager.calculate_total_sales()
        print("\n--------------------------------")
        print(f"\n💰 Total sales made: \n${total_sales:.2f}")
        print("\n--------------------------------")

    elif option == "5":
        # Option to save the list of products to a file
        file_name = input("\n📁 Name of the file to save the data: ")
        sales_manager.save_products(file_name)

    elif option == "6":
        # Option to load the list of products from a file
        file_name = input("\n📁 Name of the file to load the data from: ")
        sales_manager.load_products(file_name)

    elif option == "7":
        # Option to exit the program
        print("\n--------------------------------")
        print("\n👋 Exiting the program.")
        print("\n--------------------------------")
        break

    else:
        # Message for invalid option
        print("\n--------------------------------")
        print("\n❌ Invalid option. Please select a valid option. ❌")
        print("\n--------------------------------")
