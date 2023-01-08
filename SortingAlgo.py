# SORTING ALGORITHM
# Selection Sorting
# Bubble Sorting
# Insertion Sorting
# Merge Sorting

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

# To call the options the user chooses
Option = 0
while True:
    MainMenu()
