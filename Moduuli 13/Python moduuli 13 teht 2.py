from flask import Flask, Response
import mysql.connector
import json
def get_airport(icao):
    kursori = yhteys.cursor()
    kursori.execute(f"SELECT name FROM Airport Where ident = '{icao}'")
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            return tulos[0][0]
def get_municipality(icao):
    kursori = yhteys.cursor()
    kursori.execute(f"SELECT municipality FROM Airport Where ident = '{icao}'")
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            return tulos[0][0]

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='optifly',
         password='huono_salasana',
         autocommit=True
         )

app = Flask(__name__)
@app.route("/kentta/<ICAO>")
def kentta(ICAO):
    icao = ICAO
    airport = get_airport(icao)
    municipality = get_municipality(icao)

    response = {
        "ICAO": ICAO,
        "Name": airport,
        "Municipality": municipality
    }

    return response

if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)