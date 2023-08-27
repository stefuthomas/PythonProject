kuha = int(input("Anna kuhan pituus(cm): "))
if kuha>=37:
    print("kuha on sallitun mittainen!")
elif kuha==36:
    print("kuha on sentin alimittainen, laske se takaisin veteen!")
elif kuha==35:
    print("kuha on 2 senttiä alimittainen, laske se takaisin veteen!")
elif kuha==34:
    print("kuha on 3 senttiä alimittainen laske se takaisin veteen!")
elif kuha==33:
    print("kuha on 4 senttiä alimittainen laske se takaisin veteen!")
elif kuha==32:
    print("kuha on 5 senttiä alimittainen laske se takaisin veteen!")
elif kuha==31:
    print("kuha on 6 senttiä alimittainen laske se takaisin veteen!")
elif kuha==30:
    print("kuha on 7 senttiä alimittainen laske se takaisin veteen!")
else:
    print("alle 30 senttiset kuhat eivät ole lähelläkään sallittua mittaa! Sopiva pituus on 37 cm! Laske se takaisin veteen.")