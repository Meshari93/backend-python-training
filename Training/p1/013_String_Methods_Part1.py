# ------------------------------
# ---String Methods ---
# ------------------------------

a = "I Love Python"
b = "     I Love  Python     "
c = "####I Love  Python#####"

print(len(a))
print(len(b))

# Strip() rstrip() lstrip()

print(b.strip())
print(b.lstrip())
print(b.rstrip())

print("---------------- \n")
print(c.strip("#"))
print(c.rstrip("#"))
print(c.lstrip("#"))


#Title() 

b = "I Love Graphics and 3g Technology and python"
print(b.title())

# capitalize()

b = "I Love 2d Graphics and 3g Technology and Python"
print(b.capitalize())

# zfile  

c, d , e, f ="1", "11", "111", "1111"

print(c)
print(d)
print(e)
print(f)

print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))
print(e.zfill(4))

# upper()

g = "meshari"
print(g.upper())

# lower()
h = "MESHARI"
print(h.lower())