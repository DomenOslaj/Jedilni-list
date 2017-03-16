print "Hi and wellcome to the our menu program"

menu = {}

while True:
    add_dish = raw_input( "Please enter the name of the dish " )
    add_price = raw_input( "Please enter the price for " + add_dish )

    menu[add_dish] = add_price #add key add_dish and value add_price to the menu dictionary

    new_dish = raw_input ("Would you like to add another dish? ( yes, no ) ")

    if new_dish.lower() == "no": #because they can write Yes instead of yes
        break

print "Menu: %s" % menu

with open("menu.txt", "w+") as menu_file:
    for dish in menu:
        menu_file.write("%s: %s EUR\n" % (dish, menu[dish]))

print "Thank you and goodbye."