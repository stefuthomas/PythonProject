lux = ("LUX on parvekkeellinen hytti yläkannella.")
a = ("A on ikkunallinen hytti autokannen yläpuolella.")
b = ("B on ikkunaton hytti autokannen yläpuolella.")
c = ("C on ikkunaton hytti autokannen alapuolella.")

hyttiluokka = (input("Anna hyttiluokka(LUX, A, B, C): "))

if hyttiluokka=="lux":
    print(lux)
elif hyttiluokka=="a":
    print(a)
elif hyttiluokka=="b":
    print(b)
elif hyttiluokka=="c":
    print(c)