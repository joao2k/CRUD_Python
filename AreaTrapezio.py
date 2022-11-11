def areaTrapezio(bMenor,bMaior,altura):
    return ((bMenor+bMaior)*altura)/2
bMenor=float(input("digite a base menor:"))
bMaior=float(input("digite a base maior:"))
altura=float(input("digite a altura:"))
print(f"a area do topazio é {areaTrapezio(bMenor,bMaior,altura)}")