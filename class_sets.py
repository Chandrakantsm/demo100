#  set operations on marks of students in classes A,B,C
#  36,7,8,9,10 are common in all three sets ,  its a 40 marks test. 20 is cutoff.
CLASS_A={1,2,3,4,5,6,7,8,9,10,21,23,25,27,29,36,33,35,37,39}
CLASS_B={5,6,7,8,9,10,11,12,13,14,22,24,26,28,30,32,34,36,38,40}
CLASS_C={7,8,9,10,11,12,13,14,15,16,23,29,33,37,26,28,34,36,40,38}

# #  union  using |, both below methods give same result
# print(len(CLASS_A|CLASS_B|CLASS_C),CLASS_A|CLASS_B|CLASS_C)

# # union using union()
# print(len(CLASS_A.union(CLASS_B.union(CLASS_C))),CLASS_A.union(CLASS_B.union(CLASS_C)))

# #  intersection using & sign
# students above 20 marks will be segregated
# cutoff=20
for i in CLASS_A:
    if i>20:
        for i in CLASS_B:
            if  i >20:
                for i in CLASS_C:
                    if i>20:
                        Set_above20= CLASS_A&CLASS_B&CLASS_C
print(len(Set_above20),Set_above20)

# #  intersection using intersection()
# print(len(CLASS_A.intersection(CLASS_B.intersection(CLASS_C))),CLASS_A.intersection(CLASS_B.intersection(CLASS_C)))
