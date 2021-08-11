# This project is my first use of classes in python
import sys

class testing:
    global treeList
    global preference
    treeList = ["Birch Tree", "Oak Tree", "Cherry Tree", "Pine Tree", "Fir Tree", "Binary Tree"]
    preference = 0

    def setPreference(stringPref): # change current preference
        global treeList
        global preference
        found = False
        count = 0
        for i in treeList:
            if i == stringPref:
                preference = count
                found = True
            else:
                count += 1    
        if found == False:
            addType(stringPref)
            preference = len(treeList)-1
        print("Preference now {0}\n\n".format(treeList[preference]))

    def addType(stringType): # add new tree type
        global treeList
        global preference
        treeList.append(stringType)
        print("Type Added")
        print("\n\n")

    def getTrees(): # list all tree types
        global treeList
        print("All tree types:")
        for i in treeList:
            print(i)
        print("\n\n")

    def getPref(): # print current preference
        global treeList
        global preference
        print("Current Preference is: {0}\n\n".format(treeList[preference]))

    def removeType(stringType): # remove a tree type
        global treeList
        found = False
        for i in treeList:
            if i == stringType:
                found = True
            else:
                count += 1  
        if found == False:
            print("Type not found")
        else:
            treeList.remove(stringType)
            print("Type removed")
        print("\n\n")


def main():
    treeTest = testing
    while True:
        print("Options:\n" + # options menu
              "1: Get current preference\n" +
              "2: List all tree types\n" +
              "3: Change current preference\n" +
              "4: Add tree type\n"+
              "5: Remove tree type\n"+
              "6: Quit")
        choice = int(input("Type the number of your choice: "))
        if choice == 1:
            treeTest.getPref()
        elif choice == 2:
            treeTest.getTrees()
        elif choice == 3:
            inpString = input("Enter your new preference: ")
            treeTest.setPreference(inpString)
        elif choice == 4:
            inpString = input("Enter new tree type")
            treeTest.addType(inpString)
        elif choice == 5:
            inpString = input("Enter tree type to be removed")
            treeTest.removeType(inpString)
        elif choice == 6:
            sys.exit(0)

main()