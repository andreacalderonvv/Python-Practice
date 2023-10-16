### Assignment - reading and writing files
### Author: Andrea Calderon
import csv

filename= "contacts.csv"

# this makes the csv into a list
def read_contact():
  contacts=[]
  with open(filename, newline="") as file:
    reader= csv.reader(file)
    for row in reader:
      contacts.append(row)
  return contacts

# allows for the file to written in
def write_contacts(contacts):
  with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(contacts)

# prints the title of the program
def title():
  print("Contact Manager")

# prints the command menu
def menu():
  print("Command Menu\n\nlist - Display all contacts\nview - View a contact\nadd - Add a contact\nexit - Exit program ")

# Lists the contacts in the list
def list(contacts):
  for i, contact in enumerate(contacts, start=1):
    print(f"{i}. {contact[0]}")
  print()

# allows user to add contacts
def add(contacts):
  name= input("Name: ")
  email= input("Email: ")
  phone= input("Phone: ")
  contact= [name, email, phone]
  contacts.append(contact)
  write_contacts(contacts)
  print(f"{name} was added.\n")

# allows user to view a specific contact
def view(contacts):
  index=int(input("Which number contact would you like to view? "))
  if index < 1 or index > len(contacts):
    print("Invalid valid contact number.")
  else:
    contact = contacts[index-1]
    print ("Name: " + contact[0])
    print ("Email:" + contact[1])
    print ("Phone:" + contact[2])
  
# the main function
def main():
  menu()
  contacts= read_contact()

  # loop that controls the command
  while True:
    answer= input("What is your command? ")
    if answer.lower()== "list":
      list(contacts)
    elif answer.lower()== "view":
      view(contacts)
    elif answer.lower()== "add":
      add(contacts)
    elif answer.lower()== "exit":
      print("Thank you for using, bye!")
      break
    else:
      print("Invalid.")

# calling main file
if __name__ == "__main__":
  main()
