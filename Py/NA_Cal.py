import Optical_Fibre 
n1=int(input("Enter the first refrative index:"))
n2=int(input("Enter the second refractive index"))
NA=Optical_Fibre.numerical_aperture(n1,n2)
print("Numerical Aperture is:",NA)
