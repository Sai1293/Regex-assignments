def unique(list1):
    list_set = set(list1)
    unique_list = (list(list_set))
    for x in unique_list:
        print (x)
     

list1 = [10, 20, 10, 30, 40, 40]
print("the unique values from 1st list is")
unique(list1)

list2 =[1, 2, 1, 4, 3, 4, 5, 3, 5]
print("\nthe unique values from 2nd list is")
unique(list2)
