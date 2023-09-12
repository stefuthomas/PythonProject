vuodenajat = ('talvi', 'talvi', 'kevät', 'kevät', 'kevät', 'kesä', 'kesä', 'kesä', 'syksy', 'syksy', 'syksy', 'talvi')
numero = int(input('Anna kuukauden numero: '))
if 1 <= numero <= 12:
    tulos = vuodenajat[numero-1]
    print(f'{numero}. kuukauden vuodenaika on {tulos}')
else:
    print('Kuukauden numero ei ole välillä 1-12.')