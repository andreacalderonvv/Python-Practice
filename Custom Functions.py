### Assignment Four - feet and meters converter
### Author: Andrea Calderon
#!/usr/bin/env python3

# function for feet to meters
def fttome():
  feet=float(input("Enter feet: "))
  meter=feet*0.3048
  meter= round(meter,2)
  print("This is your conversion: "+ str(meter)+ " m.")

# function for meters to feet
def metoft():
  meter=float(input("Enter meters: "))
  feet=meter/0.3048
  feet=round(feet,2)
  print("This is your conversion: "+ str(feet)+ " ft.")

answer="y"

# while loop to continue the program for as long as the user wants
while answer.lower()=="y":

  print("Feet and Meters Converter\n")

  print("Conversion Menu:\n \n a. Feet to Meters\n b. Meters to Feet")

  # receives the users input for choice of conversion
  menuchoice=input("\nSelect a conversion.(a/b): ")

  # calls the appropriate function for the response 
  if menuchoice.lower()=="a":
    fttome()
  else:
    metoft()
# input from the user to continue or not
  answer=input("Would you like to continue?(y/n) ")
else:
  print("Thank you for using.")
  
