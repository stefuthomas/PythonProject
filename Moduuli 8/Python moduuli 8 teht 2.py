import mysql.connector

def hakeminen(koodi):
    sql = " SELECT name, type, COUNT(*) FROM airport "
    sql += " WHERE iso_country ='" + koodi + "'"
    sql += " GROUP BY type; "
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
         user='optifly',
         password='huono_salasana',
         autocommit=True
         )
koodi = input('Anna Maa-koodi: ')
hakeminen(koodi)