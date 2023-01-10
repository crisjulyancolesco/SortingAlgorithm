# Selection Sorting --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def SelectionSorting():
    print("SELECTION SORTING")
    # If statements for the variable "Mode"
    # Ascending/Alphabetical
    if Mode == 3 or Mode == 1:
        Len = len(Elements)    
        for x in range(Len - 1): 
            MinVal = x
            for y in range(x, Len):
                if Elements[y] < Elements[MinVal] :
                    MinVal = y
            if MinVal != x :
                New = Elements[x]
                Elements[x] = Elements[MinVal]
                Elements[MinVal] = New
            print(f"PASS {x+1}: {Elements}")
        
    # Descending
    if Mode == 2:
        Len = len(Elements)    
        for x in range(Len - 1): 
            MinVal = x
            for y in range(x, Len):
                if Elements[y] > Elements[MinVal] :
                    MinVal = y
            if MinVal != x :
                New = Elements[x]
                Elements[x] = Elements[MinVal]
                Elements[MinVal] = New
            print(f"PASS {x+1}: {Elements}")

# Bubble Sorting ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def BubbleSorting():
    print("BUBBLE SORTING")
    # If statements for the variable "Mode"
    # Alphabetical
    if Mode == 3 or Mode == 1:
        Len = len(Elements)
        for x in range(Len):
            Sorted = True
            
            for y in range(Len - x - 1):
                if Elements[y] > Elements[y + 1]:

                    Elements[y], Elements[y + 1] = Elements[y + 1], Elements[y]

                    Sorted = False
                    print(f"{x + 1}, {Elements}")    

            if Sorted:
                break

        return Elements

    # Descending
    if Mode == 2:
        Len = len(Elements)
        for x in range(Len):
            Sorted = True
            
            for y in range(Len - x - 1):
                if Elements[y] < Elements[y + 1]:

                    Elements[y], Elements[y + 1] = Elements[y + 1], Elements[y]

                    Sorted = False
                    print(f"PASS {x + 1}: {Elements}")    

            if Sorted:
                break

        return Elements

# Insertion Sorting -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def InsertionSorting():
    print("INSERTION SORTING")
    # If statements for the variable "Mode"
    # Aplabetical
    if Mode == 3 or Mode == 1:
        Len = len(Elements)
        for x in range(1, Len):
            
            New = Elements[x]
            
            y = x - 1
            while y >= 0 and New < Elements[y] :
                    Elements[y+1] = Elements[y]
                    y -= 1
            
            Elements[y+1] = New
            print(f"PASS {x}: {Elements}")
        return Elements  

    # Descending
    if Mode == 2:
        Len = len(Elements)
        for x in range(1, Len):
            
            New = Elements[x]
            
            y = x - 1
            while y >= 0 and New > Elements[y] :
                    Elements[y+1] = Elements[y]
                    y -= 1
            
            Elements[y+1] = New
            print(f"PASS {x}: {Elements}")
        return Elements                 

# Merge Sorting -----------------------------------------------------------------------------------------------------------------------------------------------------  
def MergeSorting(Elements, Order):
    # Merge Sorting operator/ or Merge sorting program
    Len = len(Elements)
    if Len > 1:
        Midpoint = Len // 2
        Left = Elements[:Midpoint]
        Right = Elements[Midpoint:]

        MergeSorting(Left, Order)
        MergeSorting(Right, Order)
        
        # Iterators
        x = 0
        y = 0
        z = 0

        LeftLen = len(Left)
        RightLen = len(Right)
        while x < LeftLen and y < RightLen:
            # Ascending/Alphabetical
            if Mode == 3 or Mode == 1:   
                if Left[x] < Right[y]:
                    Elements[z] = Left[x]
                    x += 1
                else:
                    Elements[z] = Right[y]
                    y += 1
                z += 1
            
            # Descending
            else:
                if Left[x] > Right[y]:
                    Elements[z] = Left[x]
                    x += 1
                else:
                    Elements[z] = Right[y]
                    y += 1
                z += 1
        
        while x < LeftLen:
            Elements[z] = Left[x]
            x += 1
            z += 1
        while y < RightLen:
            Elements[z]=Right[y]
            y += 1
            z += 1
        
        print(f"Right: {Right} - Left: {Left} => Merge Sorting: {Elements}")

def MainMenu():
    global UserInput, Elements, Mode
    while True:
        print("")
        print(
"""******* SORTING ALGORITHM APPLICATION ********
*   Programmed by: Cris Julyan C. Olesco     *
*                 BSCOE 2-1                  *
*                                            *
*    <-<-< M  A  I  N   M  E  N  U >->->     *
*                                            *
*          (1) SELECTION SORTING             *
*          (2) BUBBLE SORTING                *
*          (3) INSERTION SORTING             *
*          (4) MERGE SORTING                 *
*                                            *
**********************************************""")
        UserInput = int(input("      Select an option: "))

        # Part of the menu after you choose a sort algorithm
        # Creating List and the user input
        Elements = []
        print("")
        Size = int(input("How many elements are there on your list? "))
        Mode = int(input("[1]ASCENDING [2]DESCENDING [3]ALPHABETICALLY => "))
        Type = int(input("[1]INTEGERS [2]LETTERS (UPPER-CASE ONLY) => "))

        # If statements for the variable "Type"
        if Type == 1:
            Type = str("INTEGERS")
            for n in range(Size):
                Elements.append(int(input(f"Enter your {Size} {Type} now (END EACH BY ENTER KEY) => ")))
        elif Type == 2:
            Type = str("LETTERS")
            for n in range(Size):
                Elements.append(input(f"Enter your {Size} {Type} now (END EACH BY ENTER KEY) => "))
                
        else:
            print("**Invalid Input Please Try Again**")
            return MainMenu()

        # To call the options the user chooses
        if UserInput == 1:
            SelectionSorting()
        if UserInput == 2:
            BubbleSorting()
        if UserInput == 3:
            InsertionSorting()
        if UserInput == 4:
            MergeSorting(Elements, Mode)

        # The final sorted output
        print(f"FINAL SELECTION SORTED ELEMENTS => {Elements}\n")

        # Options to exit or continue
        Exit = input("Do you want to try again? [y/n] ")
        if Exit == 'y':
            MainMenu()
        elif Exit == 'n':
            print("Thank you for using the SORTING ALGORITHM APPLICATION")
            exit()

# Start the Program
MainMenu()