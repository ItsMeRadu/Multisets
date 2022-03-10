class Multiset:
    def CreateSet(self):
        sett = []                                                   #create an empty set
        inputNo = int(input("Write the length of the multiset: "))  #input the length of the set
        for i in range(inputNo):        
            while True:
                try:
                    number = int(input())           #input the number to add to the set
                except ValueError:                  #if mistakenly presses enter, the program will ask for a valid number, instead of closing
                    number = None
                if number == None:
                    print("Insert a valid number.")
                    continue
                else:
                    sett.append(number)             #add the number to the set
                    break
        sett.sort()
        print("Your chosen multiset is: ", sett, "\n")  #print the updated set
        return sett

    def SetNoElements(self, sett):
        print("The number of elements in the set is: ", len(sett), "\n")    #printing the number of elements
        return len(sett)

    def PrintSet(self, element):
        print("The elements of the multiset: ", element, "\n")      #printing the full set

    def IsSetEmpty(self, sett):
        if len(sett) == 0:                          #check if the length of the set is 0
            print("The set is empty.\n")            #if so, print it is empty
        else:
            print("The set is not empty.\n")        #else print it`s not empty

    def IsElement(self, sett):
        print("The element to search for: ")            #choose the element to search for
        element = int(input())                          #input the element
        if element in sett:                             #search for the element in the set
            print("The element is in the set.\n")       #if found, print it is in the set
        else:
            print("The element is not in the set.\n")   #if not, print it`s not in the set

    def SetSupp(self, sett):
        helpingSet = []                         #create a new empty set for the support of the initial set
        for i in sett:                          #iterate through the set with i
            if i not in helpingSet:             #check if i is already in the helping set
                helpingSet.append(i)            #if it`s not, add it
        return helpingSet                       #return the updated set

    def NumberOfApparitions(self, sett):
        count = 0                                           #initialize a new variable count to 0 (the number of initial apparitions)
        print("The element to count: ")            
        element = int(input())                              #input the element to count
        for i in sett:                                      #iterate through the set with i
            if i == element:                                #if we find an element equal to i
                count += 1                                  #increment the number of it`s apparitions
        print("The number of apparitions: ", count, "\n")   #print the number of apparitions

    def SetInclusion(self, set1, set2):
        setHelp1 = ""                                           #create two new empty helping strings
        setHelp2 = ""
        for i in self.SetSupp(set1):                            #iterate with i through the support of the set 1
            setHelp1 += str(i)                                  #add i to the new helping set 1
        for j in self.SetSupp(set2):                            #iterate with i through the support of the set 2
            setHelp2 += str(j)                                  #add i to the new helping set 2
        if setHelp2 in setHelp1:                                #if the helping set 2 is included in helping set 2
            print("Multiset2 is included in multiset1.\n")      #print it is included
            return True
        else:
            print("Multiset2 is not included in multiset1.\n")  #else print it`s not included
            return False

    def SetReunion(self, set1, set2):
        reunion = set1 + set2                   #compute the reunion of the two sets
        print("Reunion :", reunion, "\n")       #print the reunion

    def SetDifference(self, set1, set2):
        if self.SetInclusion(set1, set2):                        #check if the second set can be included in the first one
            difference = set(set1) - set(set2)                   #compute the difference between the two sets
            diff = list(difference)                              #convert the difference from set to list
            print("Difference: ", diff, "\n")
        else:
            print("Multiset2 is not included in multiset1.\n")   #or else the difference can`t be computed, and print so

    def SetIntersection(self, set1, set2):              #compute the intersection of the two sets
        intersection = set(set1) & set(set2)            #convert the intersection from set to list
        inter = list(intersection)                      #print the intersection of the two sets
        print("Intersection: ", inter, "\n") 

    def SetComparison(self, set1, set2):                     #check if the second set can be included in the first one
        if self.SetInclusion(set1, set2):                    #check if the two sets are equal
            if set1 == set2:                                 
                print("The multisets are equal.\n")          #print that they are
            else:
                print("The multisets are not equal.\n")      #or else, print they`re not
 