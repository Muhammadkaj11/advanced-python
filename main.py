def process_lists(list1,list2):
    zipped_list=list(zip(list1,list2))
    reversed_zip=list(zip(list1,list2))
    return zipped_list,reversed_zip,zipped_list
list1=[1,2,3]
list2=['a','b','c']
zipped,reversed_zipped,dictionary=process_lists(list1,list2)
print("zipped list:",zipped)
print("zipped list Reversed second list:",reversed_zipped)
print("zipped dictionary:",dictionary)