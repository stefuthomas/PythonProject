vuosiluku = int(input("Anna vuosiluku: "))
if vuosiluku%4==0 or vuosiluku%400==0:
    print("vuosi on karkausvuosi")
else:
    print("vuosi ei ole karkausvuosi")
