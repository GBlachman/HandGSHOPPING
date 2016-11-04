
Shopping_list = {"Target":['socks', 'soap', 'detergent', 'sponges'], 
    "Safeway": ['butter', 'cake', 'cookies', 'bread'], 
    "PeterGrocery":['apples', 'oranges', 'bananas', 'milk'], 
    "JaneGrocery":['oreos', 'brownies', 'soda']}


#0
def main_menu():
    print """Here's the Main Menu:
        
        1 Show all lists
        2 Show a specific list
        3 Add a new shopping list
        4 Add an item to the shopping list
        5 Remove an item from a shopping list
        6 Remove a list by nickname
        7 Exit """

    menu_response =raw_input("Please choose a menu option 0-7: ")
    
    if int(menu_response) == 7:
        return exit()
#main_menu()

# #7
def exit():
    print "Thank you, come again! :)"
    return main_menu()

main_menu()

# #1
# def show_all_lists(""):
#     return 

# #2
# def show_specific_list():
#     return

# #3
# def add_new_shooping_list():
#     return

# #4
# def add_item_to_list():
#     return

# #5
# def remove_item():
#     return

# #6
# def delete_list():
#     return


# if raw_input