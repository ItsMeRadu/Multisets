from Multisets import Multiset

class Test:
    def GetOption(self):                                #function to give the user an interface and him to be able to choose
        print("1. Print.")                              #what operations he wants to use on the two sets
        print("2. Show the number of elements.")
        print("3. Check if the multiset is empty.")
        print("4. Search for an element.")
        print("5. Compute the support.")
        print("6. Check the number of apparitions of an element.")
        print("7. Check if the second multiset is included in the first one.")
        print("8. Compute the reunion of the two multisets.")
        print("9. Compute the difference of the two multisets.")
        print("10. Compute the intersection of the two multisets.")
        print("11. Compare the two multisets.")
        print("0. Exit.\n")
        i = input()                                     #input the choice
        print()                                         #empty print for an empty line between the option and the solution
        return i

    def SetOption(self, set1, set2):        #function to choose between the two sets
        print("  Choose the set: ")
        print("    a. ", set1)
        print("    b. ", set2)
        opt = input()
        if opt == 'a':
            return set1
        elif opt == 'b':
            return set2
        else:
            return []                       #in case the user inputs something different than the two available choices return an empty list

    def Switch(self, element, set1, set2):  #function to use the specific operations called in the GetOption function
        Object = Multiset()
        if element == 1:
            Object.PrintSet(self.SetOption(set1, set2))
        elif element == 2:
            Object.SetNoElements(self.SetOption(set1, set2))
        elif element == 3:
            Object.IsSetEmpty(self.SetOption(set1, set2))
        elif element == 4:
            Object.IsElement(self.SetOption(set1, set2))
        elif element == 5:
            support = Object.SetSupp(self.SetOption(set1, set2))
            print("The support of the multiset is: ", support, "\n")
        elif element == 6:
            Object.NumberOfApparitions(self.SetOption(set1, set2))
        elif element == 7:
            Object.SetInclusion(set1, set2)
        elif element == 8:
            Object.SetReunion(set1, set2)
        elif element == 9:
            Object.SetDifference(set1, set2)
        elif element == 10:
            Object.SetIntersection(set1, set2)
        elif element == 11:
            Object.SetComparison(set1, set2)
        else:
            return