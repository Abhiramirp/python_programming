print("Area of triangle")
s1=float(input("Enter the side 1"))
s2=float(input("Enter the side 2"))
s3=float(input("Enter the side 3"))
s=(s1+s2+s3)/2
area=(s*(s-s1)*(s-s2)*(s-s3))**0.5
print("Area is:",area)
