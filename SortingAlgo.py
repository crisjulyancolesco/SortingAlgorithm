# SORTING ALGORITHM

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



# Selection Sorting --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def SelectionSorting(Items):

# If statements for the variable "Mode"
# Alphabetical
    if Mode == 3:
        for n in range(Size):
            Elements.append(str(input(f"Enter your {Size} {Type} now (END EACH BY ENTER KEY) => ")))
        Len = len(Items)    
        for x in range(Len - 1): 
            MinVal = x
            for y in range(x, Len):
                if Items[y] < Items[MinVal] :
                    MinVal = y
            if MinVal != x :
                New = Items[x]
                Items[x] = Items[MinVal]
                Items[MinVal] = New
            print(f"PASS {x+1}: {Elements}")
        return Items

    # Ascending
    if Mode == 1:
        for n in range(Size):
            Elements.append(int(input(f"Enter your {Size} {Type} now (END EACH BY ENTER KEY) => ")))
        Len = len(Items)    
        for x in range(Len - 1): 
            MinVal = x
            for y in range(x, Len):
                if Items[y] < Items[MinVal] :
                    MinVal = y
            if MinVal != x :
                New = Items[x]
                Items[x] = Items[MinVal]
                Items[MinVal] = New
            print(f"PASS {x+1}: {Elements}")
        return Items

    # Descending
    if Mode == 2:
        for n in range(Size):
            Elements.append(int(input(f"Enter your {Size} {Type} now (END EACH BY ENTER KEY) => ")))
        Len = len(Items)    
        for x in range(Len - 1): 
            MinVal = x
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
    print("SELECTION SORTING")
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
    print(f"FINAL SELECTION SORTED ELEMENTS => {SelectionSorting(Elements)}")

    # Options to exit or continue
    Exit = input("Do you want to try again? [y/n]")
    if Exit == 'y':
        MainMenu()
    elif Exit == 'n':
        print("Thank you for use the SORTING ALGORITHM APPLICATION")
        exit()

# Bubble Sorting ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def BubbleSorting(Items):

    # If statements for the variable "Mode"
    # Alphabetical
    if Mode == 3:
        for n in range(Size):
            Elements.append(str(input(f"Enter your {Size} {Type} now (END EACH BY ENTER KEY) => ")))
        Len = len(Items)

        for x in range(Len):
            Sorted = True
            
            for y in range(Len - x - 1):
                if Items[y] > Items[y + 1]:

                    Items[y], Items[y + 1] = Items[y + 1], Items[y]

                    Sorted = False
                    print(f"{x + 1}, {Items}")    

            if Sorted:
                break

        return Items

    # Ascending
    if Mode == 1:
        for n in range(Size):
            Elements.append(int(input(f"Enter your {Size} {Type} now (END EACH BY ENTER KEY) => ")))
        Len = len(Items)

        for x in range(Len):
            Sorted = True
            
            for y in range(Len - x - 1):
                if Items[y] > Items[y + 1]:

                    Items[y], Items[y + 1] = Items[y + 1], Items[y]

                    Sorted = False
                    print(f"{x + 1}, {Items}")    

            if Sorted:
                break

        return Items

    # Descending
    if Mode == 2:
        for n in range(Size):
            Elements.append(int(input(f"Enter your {Size} {Type} now (END EACH BY ENTER KEY) => ")))
        Len = len(Items)

        for x in range(Len):
            Sorted = True
            
            for y in range(Len - x - 1):
                if Items[y] < Items[y + 1]:

                    Items[y], Items[y + 1] = Items[y + 1], Items[y]

                    Sorted = False
                    print(f"{x + 1}, {Items}")    

            if Sorted:
                break

        return Items

    # Part of the menu after you choose a sort algorithm
    # Creating List and the user input
    Elements = []
    print("BUBBLE SORTING")
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
            
# Insertion Sorting -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def InsertionSorting(Items):
    
    # If statements for the variable "Mode"
    # Aplabetical
    if Mode == 3:
            for n in range(Size):
                Elements.append(str(input(f"Enter your {Size} {Type} now (END EACH BY ENTER KEY) => ")))

                Len = len(Items)
            for x in range(1, Len):
                
                New = Items[x]
                
                y = x - 1
                while y >= 0 and New < Items[y] :
                        Items[y+1] = Items[y]
                        y -= 1
                
                Items[y+1] = New
                print(f"PASS {x}: {Items}")
            return Items  

    # Ascending
    if Mode == 1:
            for n in range(Size):
                Elements.append(int(input(f"Enter your {Size} {Type} now (END EACH BY ENTER KEY) => ")))

                Len = len(Items)
            for x in range(1, Len):
                
                New = Items[x]
                
                y = x - 1
                while y >= 0 and New < Items[y] :
                        Items[y+1] = Items[y]
                        y -= 1
                
                Items[y+1] = New
                print(f"PASS {x}: {Items}")
            return Items

    # Descending
    if Mode == 2:
            for n in range(Size):
                Elements.append(int(input(f"Enter your {Size} {Type} now (END EACH BY ENTER KEY) => ")))

                Len = len(Items)
            for x in range(1, Len):
                
                New = Items[x]
                
                y = x - 1
                while y >= 0 and New > Items[y] :
                        Items[y+1] = Items[y]
                        y -= 1
                
                Items[y+1] = New
                print(f"PASS {x}: {Items}")
            return Items                 
    
    # Part of the menu after you choose a sort algorithm
    # Creating List and the user input
    Elements = []
    print("INSERTION SORTING")
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
    print(f"FINAL INSERTION SORTED ELEMENTS => {InsertionSorting(Elements)}")

    # Options to exit or continue
    Exit = input("Do you want to try again? [y/n]")
    if Exit == 'y':
        MainMenu()
    elif Exit == 'n':
        print("Thank you for using the SORTING ALGORITHM APPLICATION")
        exit()

    # Merge Sorting -----------------------------------------------------------------------------------------------------------------------------------------------------
def MergeSorting(Items):
    Len = len(Items)
    if Len > 1:
        Midpoint = Len // 2
        Left = Items[:Midpoint]
        Right = Items[Midpoint:]

        MergeSorting(Left)
        MergeSorting(Right)
        
        # Iterators
        x = 0
        y = 0
        z = 0

        LeftLen = len(Left)
        RightLen = len(Right)
        while x < LeftLen and y < RightLen:
            if Left[x] < Right[y]:
                Items[z] = Left[x]
                x += 1
            else:
                Items[z] = Right[y]
                y += 1
            
            z += 1
        
        while x < LeftLen:
            Items[z] = Left[x]
            x += 1
            z += 1
        while y < RightLen:
            Items[z]=Right[y]
            y += 1
            z += 1
        
        print(f"Right: {Right} - Left: {Left} => Merge Sorting: {Items}")

    # Part of the menu after you choose a sort algorithm
    # Creating List and the user input
    Elements = []
    print("MERGE SORTING")
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
    # Alphabetical
    if Mode == 3:
        for n in range(Size):
            Elements.append(str(input(f"Enter your {Size} {Type} now (END EACH BY ENTER KEY) => ")))
            Order = 1 

    # Ascending
    if Mode == 1:
        for n in range(Size):
            Elements.append(int(input(f"Enter your {Size} {Type} now (END EACH BY ENTER KEY) => ")))
            Order = 1 

    # Descending
    if Mode == 2:
        for n in range(Size):
            Elements.append(int(input(f"Enter your {Size} {Type} now (END EACH BY ENTER KEY) => ")))
            Order = 2 

    # Call the function
    MergeSorting(Elements)

    # The final sorted output if ascending/alphabetical or descending order
    if Order == 1:
        Elements.sort()
        print(f"FINAL MERGE SORTED ELEMENTS => {Elements}")

    if Order == 2:
        Elements.sort(reverse = True)
        print(f"FINAL MERGE SORTED ELEMENTS => {Elements}")

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