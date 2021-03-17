# ------------------------------
# String Indexing & Slicing
# [1] All Data in Python is Object.
# [2] Object Contain Elements. 
# [3] Every Elements Has Its Own Index 
# [4] Python Use Zero Based Indexing ( Index Start From Zero)
# [5] Use Square Brackets To Access Element.
# [6] Enable Accessing Parts o strings, Tuples, or List.
#--------------------------------


# Indexing ( Access Single Item )

myString = "I Love Python"  # Index 0 => I
print(myString[0])          # Index 9 => t
print(myString[9])


print(myString[-1])         # Index -1 => First Characters from End
print(myString[-6])         # Index -6 => 6th  Characters from End


# Slicing ( Access Multiple Sequence Item )
# [Start:end] End not included
#[Start:End:Step]

print (myString[8:11])  # yth
print(myString[3:5]) # ov

print(myString[:10]) #  If Start Is Not Here will Start from 0 (I Love Pyt)
print(myString[5:]) #  If The end is not here will go to the end(e Python)
 
print(myString[:]) # Full Data

print(myString[0::1]) # Full Data
print(myString[::1]) # Full Data

print(myString[::2])
print(myString[::3])
