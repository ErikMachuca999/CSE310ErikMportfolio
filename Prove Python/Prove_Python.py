import sys 
# library to use exit function! used to quit a program.

# a function can be used for creating many lines of code and commands
# all in one block for more easier functionality instead of haiving
# evey line of code do something. GReat for organized and specifically
# assigned commands. 

def amazonMenu():
    # the helloUser give a personlized greeting for the people 
    # using the Program.
    helloUser = input("Welcome, User! Please Enter your name: ")
    # print "f" strings allow prins statments to include variables to be read
    # which especially help in saying User input in a hard coded line
    print(f"Hello, {helloUser}! Welcome to The Amazon Shop program! :)")
    # a neat thing for this while loop is for the menu to cycle and loop over
    # and over instead of leaving the program constantly after each choice
    while True: 
        print()
        print(f"{helloUser}, ")    
        print('''
        PLEASE SELECT A NUMBER FOR THE ACTION DESIRED TO COMMEMNCE:

        1. View Cart
        2. Add an Item to Cart
        3. Remove Item
        4. Check if Item is in cart
        5. Cart quantity
        6. Empty Shopping cart
        7. Calculate Total Spending
        8. Exit
        ''')

        selection = input("Select an option: ")
    # if, elif, and else statments are used to give pending
    # choices! they can be used to create specific outcomes 
    # for each programed purpose
        if selection == "1":
            showCart() # functions must be defined and called to have them run
    # Functions are also used in the statements

    # this function will allow Users to write in their Shopping cart any items
    # they wish to buy, just like the website!    
        elif selection == "2":
            addItem()
    # this function will allow Users 
        elif selection == "3":
            returnItem()
        
        elif selection == "4":
            reviewInventory()

        elif selection == "5":
            cartQuantity()
        
        elif selection == "6":
            emptyCart()
        
        elif selection == "7":
            calculateTotal()
        
        elif selection == "8":
            sys.exit()
        else:
            print("ERROR: Invalid Choice. [:(] Please try again.")

amazon_cart = ["item 1", "item 2", "item 3", "item 4"]
#==============================================================================================
# for the showCart fuction, the for loop assings a variable within
# and sets the first item in the amazon_cart list to be set as.
# and cycles through the list
def showCart():  
    # placeholder borders to establish organization
    print("===========================================") 
    print("ꟼ|_Your_Amazon_Cart_/")
    for item in amazon_cart: 
        print("* " + item) 
    print("===========================================")
    # print statements can write out anything harcoded in
    # or even white space to help in readability of outputs 
#==============================================================================================
def addItem():
    # input commands allow the USER input to write in the program 
    # for it to be used! works similar to a print statement.
    product = input("Enter The Awesome Stuff you wish to buy! : ") 
    amazon_cart.append(product)
    print(product + " has been added to your Cart!")
#==============================================================================================
# The returnItem function does is job as a remove item command.
# works similarly as the append fucntion. that one adds, this one 
# subtracts the item

def returnItem():
    product = input("Enter the Item you wish to return to the store: ") 
    amazon_cart.remove(product)
    print(product + " has been removed from your Cart!")
#==============================================================================================
# the reviewInventory function is recognized as a shopping list cart. 
# It checks the amazon_cart list and sees if the item is in the cart
# or not, and even reminds about it.
def reviewInventory():
    inventoryObject = input("What product do want to check in your Shopping Cart? ")
    if inventoryObject in amazon_cart:
        print(f"{inventoryObject} is in the cart")
    else:
        print(f"{inventoryObject} is Not in the cart. Remember to get it!")
#==============================================================================================
# the cartQuantity function will count and show how many items are in your
# shopping cart. Utilizes the len fuction to see the amazon_cart list's Lenght.
def cartQuantity():
    print("Your Shopping Cart currently has", len(amazon_cart), "products to buy." )
#==============================================================================================
# the most simple function: To clear the shopping cart
# using the clear fucntion attached to the shopping cart list
def emptyCart():
    amazon_cart.clear()
    print("Shopping is now empty. Endless Possibilities! :)")
#==============================================================================================
# This Function layout out the computing of the cost of the user's shopping items
# Sadly for now, the quickest one to do was having the items have an equal price
# as a group, but in the end, uses the normal price, and shows the tax amount
# added and the final price right on the dot, and can be allowed to put ANY
# tax rate. 

def calculateTotal():
    num_of_items = int(input("Enter The number of Items in your Shopping Cart: "))
    price_of_item = float(input("How much does each item cost: "))
    
    # this utilzes ints and floats commands to house Number and 
    # decimal Variables. ints are for only whole numbers, 
    # floats can also house decimal numbers, NOT whole

    sales_tax_value = float(input('What is the sales tax rate? '))
    sales_tax_formula = float(sales_tax_value / 100)
    # the math formulas to calulate tax
    # and added sales price total.
    subtotal = (price_of_item * num_of_items)
    sales_tax_adder = float(subtotal * sales_tax_formula)
    complete_total = subtotal + sales_tax_adder
    
    # f strings can also utilze specific decimal positioning with
    # this method of rounding to the nearest decimal without the 
    # round function, It needs assigned float variables though.
    print(f'Subtotal: ${subtotal:.2f}')
    print(f'Sales Tax: ${sales_tax_adder:.2f}')
    print(f'Total: ${complete_total:.2f}')
#==============================================================================================

# the call of the Whole program on one line.
amazonMenu()