#Name and menu question Riley Sullivan. 3/05/22. Version 2. The purpose of this is to get the users name and output it while asking if they would like to see the menu.
print("Hello what is your name?")
name = input()


def response():

    show_menu = input(
        f'Kia Ora {name} Would you like you see the menu? ').lower()

#Menu options and pricing, Riley Sullivan. 
  

    if show_menu == "yes" or show_menu == "y":
        print(
            "You can buy a pie for $4.50 or a burger for $7.89, What would you like to buy? ")
  
    elif show_menu == "n" or show_menu == "no":
        exit("Goodbye")

    else:
        print("Please answer Yes or No")
        response()


response()

#Menu options, Riley Sullivan. 6/05/22. Version 4. The purpose of this is to show the user the menu options

order = input().lower()

if order == "burger":
    print("Thank you for ordering the burger! That will be $7.89")

elif order == "pie":
    print("Thank you for ordering the pie! That will be $4.50")

else:
    print("Thank you visiting us at Fraser High School Canteen.")
