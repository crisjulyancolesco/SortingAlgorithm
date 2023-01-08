# SORTING ALGORITHM
# Insertion Sorting
# Merge Sorting

import sys

# Shows the choices the user can choose
def MainMenu():
    global UserInput
    print("-------------------------------------")
    print("**** SORTING ALGORITHM APPLICATION ****")
    print("Programmed by: <Cris Julyan C. Olesco>")
    print("      <BSCOE> <Second Year> <1>")
    print("\n     <-<-< M A I N  M E N U >->->")
    print("""
        (1) SELECTION SORTING
        (2) BUBBLE SORTING
        (3) INSERTION SORTING
        (4) MERGE SORTING""")        
    UserInput = int(input("\n      Select an option: "))
    print("-------------------------------------")

    # Selection Sorting
    def SelectionSorting(Items):
        Len = len(Items)
        for x in range(Len - 1): 
            MinVal = x

            # Ascending / Alphabetical
            if Order == 1:
                for y in range(x, Len):
                    if Items[y] < Items[MinVal] :
                        MinVal = y
                
            # Descending
            elif Order == 0:
                for y in range(x, Len):
                    if Items[y] > Items[MinVal] :
                        MinVal = y

            if MinVal != x :
                New = Items[x]
                Items[x] = Items[MinVal]
                Items[MinVal] = New
                print(f"PASS {x+1}: {Elements}")
        
        return Items

    # Part of the menu after you choose a sort algorithm
    # Creating List and the user input
    Elements = []
    Size = int(input("How many elements are there on your list? "))
    Mode = int(input("[1]ASCENDING [2]DESCENDING [3]ALPHABETICALLY => "))
    Type = int(input("[1]INTEGERS [2]LETTERS (Upper-case only) => "))

    # If statements for the variable "Type"
    if Type == 1:
        Type = str("INTEGERS")
    elif Type == 2:
        Type = str("LETTERS")
    else:
        print("Invalid Input")

    # If statements for the variable "Mode"
    if Mode == 3:
        for n in range(Size):
            Elements.append(str(input(f"Enter your {Size} {Type} now (END EACH BY ENTER KEY) => ")))
            Order = 1
    if Mode == 1:
        for n in range(Size):
            Elements.append(int(input(f"Enter your {Size} {Type} now (END EACH BY ENTER KEY) => ")))
            Order = 1
    if Mode == 2:
        for n in range(Size):
            Elements.append(int(input(f"Enter your {Size} {Type} now (END EACH BY ENTER KEY) => ")))
            Order = 0

    # The final sorted output
    print(f"FINAL SELECTION SORTED ELEMENTS => {SelectionSorting(Elements)}")

    # Options to exit or continue
    Exit = input("Do you want to try again? [y/n]")
    if Exit == 'y':
        MainMenu()
    elif Exit == 'n':
        print("Thank you for use the SORTING ALGORITHM APPLICATION")
        exit()

    # Bubble Sorting
    def BubbleSorting(Items):

        # If statements for the variable "Mode"
        if Mode == 3:
            for n in range(Size):
                Elements.append(str(input(f"Enter your {Size} {Type} now (END EACH BY ENTER KEY) => ")))
                Len = len(Items)

            for x in range(Len - 1) :

                for y in range(Len - 1) :
                    # Alphabetical
                    if Items[y] > Items[y + 1]:
                        New = Items[y]
                        Items[y] = Items[y + 1]
                        Items[y + 1] = New
                        print(f"PASS {x+1}: {Elements}")        

            return Items

        if Mode == 1:
            for n in range(Size):
                Elements.append(int(input(f"Enter your {Size} {Type} now (END EACH BY ENTER KEY) => ")))
                Len = len(Items)

            for x in range(Len - 1) :

                for y in range(Len - 1) :
                    # Ascending
                    if Items[y] > Items[y + 1]:
                        New = Items[y]
                        Items[y] = Items[y + 1]
                        Items[y + 1] = New
                        print(f"PASS {x+1}: {Elements}")        

            return Items

        if Mode == 2:
            for n in range(Size):
                Elements.append(int(input(f"Enter your {Size} {Type} now (END EACH BY ENTER KEY) => ")))
                Len = len(Items)

            for x in range(Len - 1) :

                for y in range(Len - 1) :
                    # Descending
                    if Items[y] < Items[y + 1]:
                        New = Items[y]
                        Items[y] = Items[y + 1]
                        Items[y + 1] = New
                        print(f"PASS {x+1}: {Elements}")        

            return Items

    # Part of the menu after you choose a sort algorithm
    # Creating List and the user input
    Elements = []
    Size = int(input("How many elements are there on your list? "))
    Mode = int(input("[1]ASCENDING [2]DESCENDING [3]ALPHABETICALLY => "))
    Type = int(input("[1]INTEGERS [2]LETTERS (Upper-case only) => "))

    # If statements for the variable "Type"
    if Type == 1:
        Type = str("INTEGERS")
    elif Type == 2:
        Type = str("LETTERS")
    else:
        print("Invalid Input")

        # The final sorted output
    print(f"FINAL BUBBLE SORTED ELEMENTS => {BubbleSorting(Elements)}")

    # Options to exit or continue
    Exit = input("Do you want to try again? [y/n]")
    if Exit == 'y':
        MainMenu()
    elif Exit == 'n':
        print("Thank you for using the SORTING ALGORITHM APPLICATION")
        exit()
            
# To call the options the user chooses
Option = 0
while True:
    MainMenu()
    if Option == 1:
        UserInput = SelectionSorting()
    if Option == 2:
        UserInput = BubbleSorting()
    if Option == 3:
        UserInput = InsertionSorting()
    if Option == 4:
        UserInput = MergeSorting()