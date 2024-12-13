list1=[1,2,3,4]
list2=[5,6,7,8]
added_list=list(map(lambda x,y:x+y,list1,list2))
print("list after addition:",added_list)
list3=[2,3,4,5]
squared_list=list(map(lambda x:x**2,list3,))
print("list of squares:",squared_list)