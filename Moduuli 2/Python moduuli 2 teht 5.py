suurinLuku = float(input("Anna leiviskät: "))
keskiLuku = float(input("Anna naulat: "))
pieninLuku = float(input("Anna luodit: "))

luoditGramma = float(13.3 * pieninLuku)
naulatGramma = float(32 * 13.3 * keskiLuku)
leiviskätGramma = float((32 * 13.3 * 20) * suurinLuku)

massa = float(luoditGramma+naulatGramma+leiviskätGramma)
massaGrammat = massa % 1000
massaKilogrammat = int(massa / 1000)

print(f"Massa nykymittojen mukaan: \n {massaKilogrammat} kilogrammaa ja {massaGrammat:.2f} grammaa.")