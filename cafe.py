# Create list with items from the menu.

menu = ["tea", "apple pie", "coffee", "hot chocolate", "brownie", "tart", "iced-tea"]

# Create a dictionary to assign a stock value to every item from the menu.

stock = {"tea": 5 ,
         "apple pie": 7,
         "coffee": 2,
         "hot chocolate": 3,
         "brownie": 2,
         "tart": 3,
         "iced-tea": 4}

# Create a dictionary to assign a price to every item from the menu.

price = {"tea": 3,
         "apple pie": 5.50,
         "coffee": 3.50, 
         "hot chocolate": 3,
         "brownie": 3.75,
         "tart": 4.50,
         "iced-tea": 3.50}

# Create a variable to store the total price value of all available stock at the cafe.

total_stock_value = 0

# Create a for loop using a key from dictionaries.
# To calculate the total price value of all available stock at the cafe.

for key in price:
  total_stock_value += price[key]*stock[key]

# Display the outcome to the user.

print(f"The total price value of a stock in a cafe is: £{total_stock_value} ")
