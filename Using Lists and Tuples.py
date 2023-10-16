### Assignment - wizard inventory
### Author: Andrea Calderon

# prints title of program
def title():
  print("The Wizard Inventory Program")

# prints menu of commands
def commandmenu():
  print("\nCommand Menu\n")
  print("show- shows all items\n \ngrab- grab an item\n \ndrop- drop an item\n \nexit- exit program")

# shows all the items in the wizard's inventory
def show(inventory):
  for i, item in enumerate (inventory, start = 1):
    print (f"{i}.{item}")
  print()

# allows user to input the items they want in inventory
def grab_item(inventory):
  item=input("Enter an item: ")
  # if the number is bigger or equal to 4 doesn't allow user to input more to the list
  if len(inventory)>=4:
    print("You can't hold any more items. If you would like to, you can \ndrop one.")
  else:
    inventory.append(item)
    print("Item added.")

    # user can remove items from inventory
def drop_item(inventory):
  number=int(input("Pick a number. "))
  if  number < 1 or number > len(inventory):
    print("Invalid item number.")
  else:
    object=inventory.pop(number-1)
    print(f"{object} was dropped.")

  # main function
def main():
  # main list used as wizard's inventory
  inventory = ["wand", "wizard hat", "potion"]

  title()
  commandmenu()
  command=""
  #keeps the ability to choose a command until user chooses exit
  while not command=="exit":
    command=input("What is your command? ")
  
    if command=="show":
      show(inventory)
    elif command=="grab":
      grab_item(inventory)
    elif command=="drop":
      drop_item(inventory)
  else:
    print("Goodbye.")
#calling main function
if __name__=="__main__":
  main()
