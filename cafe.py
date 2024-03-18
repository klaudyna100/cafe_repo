# Create list with items from the menu.

menu = ["tea", "apple pie", "coffee", "hot chocolate"]

# Create a dictionary to assign a stock value to every item from the menu.

stock = {"tea": 5 , "apple pie": 7 , "coffee": 2 , "hot chocolate": 3}

# Create a dictionary to assign a price to every item from the menu.

price = {"tea": 2 , "apple pie": 4.50 , "coffee": 2.50 , "hot chocolate": 2}

# Create a variable to store the total price value of all available stock at the cafe.

total_stock_value = 0

# Create a for loop using a key from dictionaries.
# To calculate the total price value of all available stock at the cafe.

for key in price:
  total_stock_value += price[key]*stock[key]

# Display the outcome to the user.

print(f"The total price value of a stock in a cafe is: £{total_stock_value} ")
