lentoasemat = {'EFHK':'Helsinki-Vantaa', 'ESSA':'Arlandan asema', 'EGLL':'Heathrow Airport'}

def airport(haku):
    if haku in lentoasemat:
        print(f'ICAO-Koodilla {haku} löytyy lentoasema nimeltä {lentoasemat[haku]}')
    else:
        print(f'Haulla {haku} ei löytynyt lentoasemaa')
    return

def airport_add(icao, nimi):
    lentoasemat[icao] = nimi
    print(f'Lentoasema {nimi} lisätty ICAO-koodilla {icao}.')
    return lentoasemat

valinta = input('Hae lentoasemaa "Hae". Lisää lentoasema "Lisää". Lopeta toiminnot "Lopeta": ')

while valinta =='Hae' or 'Lisää' or 'Lopeta':
    if valinta=='Hae':
        koodi = input('Anna ICAO-Koodi: ')
        koodi = airport(koodi)
        valinta = input('Hae lentoasemaa "Hae". Lisää lentoasema "Lisää". Lopeta toiminnot "Lopeta": ')

    if valinta =='Lisää':
        uusi_ICAO = input('Anna lisättävän lentoaseman ICAO-Koodi: ')
        uusi_lentoasema = input('Anna lisättävän lentoaseman nimi: ')
        airport_add(uusi_ICAO, uusi_lentoasema)
        valinta = input('Hae lentoasemaa "Hae". Lisää lentoasema "Lisää". Lopeta toiminnot "Lopeta": ')

    if valinta =='Lopeta':
        break
print('Lopetettu.')