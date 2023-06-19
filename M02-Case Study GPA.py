""" M02 Lab-Case Study
 GPA Award Application
 Created by: Tanner Cole
Descrpition: Ask for a students last name and for the student's GPA then
the program will determine whether or not the student will receive
an award.
"""
# Establish last name variable
last_name = input("Enter students last name: ")
#Checking last name to see if quit function has been entered
while last_name != "ZZZ":
    #asking for students first name and gpa
    first_name = input("Enter students first name: ")
    gpa = float(input("Enter students GPA: "))
   #determining whether student has made deans list or honor roll
    if gpa >= 3.5:
        print("{} {} has made the deans list!".format(first_name, last_name))
    else:
        if gpa >= 3.25:
            print("{} {} has made the honor roll!".format(first_name, last_name))
    last_name = input("\nEnter students last name: ")
    #loop repeats until ZZZ is entered