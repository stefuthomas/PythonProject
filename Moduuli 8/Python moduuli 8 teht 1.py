import mysql.connector

def hakeminen(koodi):
    sql = "SELECT name FROM Airport"
    sql += " WHERE ident ='" + koodi + "'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(rivi)


yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='yAXDyg2T',
         autocommit=True
         )
koodi = input('Anna ICAO-koodi: ')
hakeminen(koodi)