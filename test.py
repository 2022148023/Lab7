from lab7_p3_2022148023 import list_D2

list1 = list_D2([[1, 2], [2, 3], [1, 2]])
list1_ = list_D2([[1, 2], [2, 3], [1, 2]])
list2 = list_D2([[1, 2, 3], [1, 2, 3]])
print(list1.transpose())
try:
    list3 = list1 @ list1_
except Exception as e:
    print(e)
list3 = list1 @ list2
print(list3)
print(list(list3))
print(list1.avg())
