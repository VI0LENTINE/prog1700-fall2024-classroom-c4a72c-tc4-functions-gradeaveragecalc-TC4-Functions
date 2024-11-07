############################################
# Tech Check 4 - Provided Starter File
# Take this provided single-grade entry program and re-work it to use a function, to allow the customized entry of 6 different course grades, and
# to calculate a final grade point average for all six courses.
############################################

# Student Name: Valentine
# Student ID: W0516070

############################################

numericGrade = 0.0

# main() FUNCTION
def main():
    print("Grade Point Calculator\n")
    print("Valid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0.\n")

def userInput():   
    counter = 0
    classes = ["PROG1700", "NETW1700", "OSYS1200", "WEBD1000", "COMM1700", "DBAS1007"]
#Gather user inputs
#letterGrade = input("Please enter a letter grade : ").upper()
#modifier = input("Please enter a modifier (+, - or nothing) : ")  
    if counter == 0:
        prog = input("Please enter a letter grade for : {0}".format(classes))
        progM = input("Please enter a modifier (+, - or nothing) : ")
        counter = counter + 1
    elif counter == 1:
        netw = input("Please enter a letter grade for {1}: ".format(classes))
        netwM = input("Please enter a modifier (+, - or nothing) : ")
        counter = counter + 1
    elif counter == 2:
        osys = input("Please enter a letter grade for {2}: ".format(classes))
        osysM = input("Please enter a modifier (+, - or nothing) : ")
        counter = counter + 1
    elif counter == 3:
        webd = input("Please enter a letter grade for {3}: ".format(classes))
        webdM = input("Please enter a modifier (+, - or nothing) : ")
        counter = counter + 1
    elif counter == 4:
        comm = input("Please enter a letter grade for {4}: ".format(classes))
        commM = input("Please enter a modifier (+, - or nothing) : ")
        counter = counter + 1
    elif counter == 5:
        dbas = input("Please enter a letter grade for {5}: ".format(classes))
        dbasM = input("Please enter a modifier (+, - or nothing) : ")
        
    courses = [prog, netw, osys, webd, comm, dbas]
    mods = [progM, netwM, osysM, webdM, commM, dbasM]

    return courses, mods

    def gradeCalc(courses):
        global numericGrade
        userInput()
    # Determine base numeric value of the grade
        if courses.upper() == "A":
            numericGrade = 4.0
        elif courses.upper() == "B":
            numericGrade = 3.0
        elif courses.upper() == "C":
            numericGrade = 2.0
        elif courses.upper() == "D":
            numericGrade = 1.0
        elif courses.upper() == "F":
            numericGrade = 0.0
        else:
            #If an invalid entry is made
            print("You entered an invalid letter grade.")

        return numericGrade
        
        # Determine whether to apply a modifier
    def modifier(mods, courses, numericGrade):
        userInput()
        gradeCalc()
        if mods == "+":
            if courses != "A" and courses != "F": # Plus is not valid on A or F
                numericGrade += 0.3
        elif mods == "-":
            if courses != "F":     # Minus is not valid on F
                numericGrade -= 0.3

        # Output final message and result, with formatting
        print("The numeric value is: {0:.1f}".format(numericGrade))
#PROGRAM EXECUTION STARTS HERE
main()