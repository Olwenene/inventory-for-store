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

highest_qty()
        
        
                #max_quantity = quantity
                #max_line = line

    #if max_line is not None:
        #stripped = max_line.strip().split(',')
        #shoe_sale = stripped[2]
        #return f"The {shoe_sale} is for sale and has a quantity of {max_quantity} pairs in stock"
    #else:
        #return "No products found in the inventory."

# Call the function with the file path
#result = highest_qty('inventory.txt')
#print(result)