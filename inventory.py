#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)
       
    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity
        
    def __str__(self):
       return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"

#List of all the shoes in the file inventory.txt
shoe_list = []

def read_shoes_data():
    shoe_list = []
    try:
        with open("inventory.txt", "r") as file:
            next(file)
            for line in file:
                values = map(str.strip, line.split(','))
                try:
                    shoe_list.append(Shoe(*values))
                except ValueError as ve:
                    print(f"Error creating Shoe object: {ve}")
        print("Data read successfully")
                    
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return shoe_list

def capture_shoes():
    try:
        country = input("Enter the country: ")
        code = input("Enter the code: ")
        product = input("Enter the product: ")
        cost = float(input("Enter the cost: "))
        quantity = int(input("Enter the quantity: "))

        # Create a new Shoe object and append it to the list
        shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoe)

        print("Shoe captured successfully.")
    except ValueError:
        print("Invalid input. Please enter valid numeric values for cost and quantity.")
    except Exception as e:
        print(f"An error occurred: {e}")

def re_stock():
    try:
        min_line = None
        min_value = float('inf')

        with open("inventory.txt", "r") as file:
            lines = file.readlines()

            for line_number, line in enumerate(lines, start=1):
                numeric_values = [float(value) for value in line.strip().split(',') if value.replace('.', '', 1).isdigit()]
                if numeric_values:
                    current_min_value = min(numeric_values)
                    if current_min_value < min_value:
                        min_line = line.strip()
                        min_value = current_min_value

        if min_line:
            print(f"Current line: {min_line}")
            new_value = float(input("Enter the value for restocking: "))
            updated_value = min_value + new_value

            # Update the line with the new value
            index = lines.index(min_line + '\n')
            lines[index] = lines[index].replace(str(min_value), str(updated_value))

            # Write the updated lines back to the file
            with open("inventory.txt", "w") as file:
                file.writelines(lines)

            print(f"Updated Value after Restocking: {updated_value}")
        else:
            print("No quantity found in the file.")
        print("Thank you for restocking!!")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def search_shoe():
    try:
        code_to_search = input("Enter the code of the shoe: ").upper()
        found_shoe = next((shoe for shoe in shoe_list if shoe.code == code_to_search), None)
        
        # Print the found shoe or a message if not found
        print(found_shoe) if found_shoe else print("Shoe not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def value_per_item():
    for shoe in shoe_list:
        total_cost_per_item = shoe.cost * shoe.quantity
        print(f"Total cost for {shoe.product} ({shoe.quantity} items on stock): R{total_cost_per_item} with each shoe costing R{shoe.cost}")

def highest_qty():
    max_quantity = float('-inf')
    max_line = None

    with open("inventory.txt", 'r') as file:
        for line_number, line in enumerate(file):
            try:
                _, _, product, _, quantity_str = line.strip().split(',')
                quantity = int(quantity_str)
            except ValueError:
                print(f"Error converting quantity to integer in line {line_number + 1}: {line}")
                continue

            if quantity >= max_quantity:
                max_quantity = quantity
                max_line = line

    if max_line is not None:
        stripped = max_line.strip().split(',')
        shoe_sale = stripped[2]
        print(f"The {shoe_sale} is for sale and has a quantity of {max_quantity} pairs in stock")
    else:
        print("No products found in the inventory.")

def write_shoes_data(shoe_list):
    with open("inventory.txt", "w") as file:
        file.write("Country, Code, Product, Cost, Quantity\n")
        for shoe in shoe_list:
            file.write(f"{shoe.country}, {shoe.code}, {shoe.product}, {shoe.cost}, {shoe.quantity}\n")
       
#function for the main menu
def main_menu():
    print("\n=== Shoe Management System ===")
    print("1. Read Shoes data")
    print("2. Capture New Shoes")
    print("3. View All Shoes")
    print("4. Restock Lowest Quantity Shoe")
    print("5. Search Shoe by Code")
    print("6. Calculate and Print Total Value")
    print("7. Determine Product for Sale")
    print("8. Exit")
  
while True:
    main_menu()

    try:
        choice = int(input("Enter your choice (1-8): "))

        if choice == 1:
            shoe_list = read_shoes_data() 
        elif choice == 2:
            capture_shoes()
            write_shoes_data(shoe_list)                   
        elif choice == 3:
            [print(shoe) for shoe in shoe_list]
        elif choice == 4:
            re_stock()
            write_shoes_data(shoe_list)   
        elif choice == 5:
            search_shoe()
        elif choice == 6:
           value_per_item()
        elif choice == 7:
             highest_qty()
        elif choice == 8:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

