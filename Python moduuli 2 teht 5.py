suurinLuku = float(input("Anna leiviskät: "))
keskiLuku = float(input("Anna naulat: "))
pieninLuku = float(input("Anna luodit: "))

luoditGramma = float(13.3 * pieninLuku)
naulatGramma = float(32 * 13.3 * keskiLuku)
leiviskätGramma = float((32 * 13.3 * 20) * suurinLuku)

massa = float(luoditGramma+naulatGramma+leiviskätGramma)
massaGramma = massa % 1000
massaKilogramma = int(massa / 1000)

print(f"Massa nykymittojen mukaan: \n {massaKilogramma} kilogrammaa ja {massaGramma:.2f} grammaa.")