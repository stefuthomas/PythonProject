import mysql.connector

from geopy.distance import geodesic

def distance_calculating(koodi, koodi2):
    kursori = yhteys.cursor()
    kursori.execute(f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident = '{koodi1}'")
    tulos1 = kursori.fetchone()
    kursori.close()

    kursori = yhteys.cursor()
    kursori.execute(f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident = '{koodi2}'")
    tulos2 = kursori.fetchone()
    kursori.close()

    if tulos1 and tulos2:
        coords1 = (tulos1[1], tulos1[0])
        coords2 = (tulos2[1], tulos2[0])

        etäisyys = geodesic(coords1, coords2).kilometers

        return etäisyys
    else:
        return None
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='optifly',
         password='huono_salasana',
         autocommit=True
         )
koodi1 = input('Anna ensimmäinen ICAO-koodi: ')
koodi2 = input('Anna toinen ICAO-koodi: ')

etäisyys = distance_calculating(koodi1, koodi2)

print(f'Lentokentän {koodi1} ja {koodi2} on {etäisyys:.2f} kilometriä.')