from Multisets import Multiset
from Test import Test

Obj = Multiset()
testObj = Test()

multiset1 = Obj.CreateSet()
multiset2 = Obj.CreateSet()

change = True
while change:
    option = int(testObj.GetOption())
    if option == 0:
        change = False
        break
    else:
        testObj.Switch(option, multiset1, multiset2)