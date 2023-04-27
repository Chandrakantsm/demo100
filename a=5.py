
CLASS_A={1,2,3,4,5,6,7,8,9,10,21,23,25,27,29,36,33,35,37,39}
CLASS_B={5,6,7,8,9,10,11,12,13,14,22,24,26,28,30,32,34,36,38,40}
CLASS_C={7,8,9,10,11,12,13,14,15,16,23,29,33,37,26,28,34,36,40,38}
# scholl list is created combining scores from all classes as list 
school=list(CLASS_A)+list(CLASS_B)+list(CLASS_C)

#  condition in list to list marks above 20 and store in school20
school20=[x for x in school if x>20 ]

#  convert the list of scores above 20 to a set
print(set(school20))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


