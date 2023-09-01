salasana_laskuri = int(0)
oikea_tunnus = 'python'
oikea_salasana = 'rules'

annettu_tunnus = str(0)
annettu_salasana = str(0)

while annettu_tunnus!=oikea_tunnus or annettu_salasana!=oikea_salasana:
    salasana_laskuri += 1
    annettu_tunnus = str(input('Anna tunnus: '))
    annettu_salasana = str(input('Anna salasana: '))
    if annettu_tunnus == oikea_tunnus and annettu_salasana == oikea_salasana:
            print('Tervetuloa')
    else:
        print('Salasanasi tai tunnuksesi on väärin.')
    if salasana_laskuri == 5:
        print('Tili on lukittu')
        break