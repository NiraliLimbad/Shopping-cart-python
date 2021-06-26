import sys

def Mainfunction():
    while True:
        print()
        print('''### SHOPPING LIST

        Select a Number for the action you would like to do:

        1. View Shopping list
        2.Add items to shopping list
        3.Remove item from shopping list
        3.check if item is on shopping list
        5.How many items on shopping list
        6.Clear shopping list
        7.Exit
        ''')

        selection = input("Make your selection")

        if selection =="1":
            displaylist()
        elif selection =="2":
            additem()
        elif selection =="3":
            removeitem()
        elif selection =="4":
            checkitem()
        elif selection =="5":
            listlen()
        elif selection =="6":
            clearlist()
        elif selection =="7":
            sys.exit()
        else:
            print("please select valid selection : ")

shopping_list = ["t-shirt","jeans","watch","tie","shoes"]

def displaylist():
    print("-----------------Your shopping list------------")
    print()
    for i in shopping_list:
        print("* "+ i)
    print()

def additem():
    item= input("Enter the item you want to add to the shopping list")
    shopping_list.append(item)
    print()
    print(item + "has been added to the shopping list")
    print()


def removeitem():
    item= input("Enter the item you want to remove from the shopping list")
    shopping_list.remove(item)
    print()
    print(item + "has been removed from the shopping list")
    print()

def checkitem():
    item = input("Enter an item to check if it is in the shopping list or not :  ")
    if item in shopping_list:
        print("yes, ",item," is in your shopping list :)")
    else:
        print("Sorry..... the item is not in the shopping list")

def listlen():
    print("there are ", len(shopping_list) , " items in shopping list" )

def clearlist():
    shopping_list.clear()
    print("Shopping list is now empty...")

Mainfunction()