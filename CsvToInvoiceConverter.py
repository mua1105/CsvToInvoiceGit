#Imports
from sys import argv #Übergabe von Parametern
import os #Befehle ausführen
import subprocess
from datetime import date #Date
import csv  #CSV interpretieren
from progress.spinner import Spinner

stundenlohn = 15 #Stundenlohn
summe = 0.0 #Summe der Stunden
items = "" #Arbeitselemente
reverseDate = date.today().strftime("%d%m%Y")[::-1] #Rechnungsnummer = Datum rückwärts
part1 = "" #vor und 
part2 = "" #nach dem LATEX - Dokument

try:
    csvName = argv[1] #Ist der Dateiname der CSV-Datei übergeben?
except: #Dateinamen eingeben
    print("--- Keine CSV-Datei übergeben! ---")
    csvName = input("Bitte den Namen der CSV-Datei eingeben! ")

#CSV-Datei einlesen
with open(csvName) as csvdatei: 
    print("CSV-Datei wird gelesen...")
    csv_reader_object = csv.reader(csvdatei)
    rowNumb = 0
    for row in csv_reader_object: #Datei Lesen, Rechnungssumme bereichnen
        if rowNumb != 0:
            row1 = row[1].replace(",", ".") #Kommata in Punkte umwandeln wg. Floats
            multyplied = float(row1) * stundenlohn #Stunden mit Stundenlohn multiplizieren
            items = items + r"\additem{Zuarbeit am: "+row[0]+r"}{"+"{:.2f}".format(multyplied) +r" \euro}" #Einfügen
            summe = summe + multyplied #Summe addieren  
        rowNumb += 1
    
    #Überprüfen, ob der Rechnungsbetrag über 500€ liegt (Minijobgrenze)
    if summe > 500:
        if input("Achtung! Der Rechnungsbetrag liegt überhalb von 500€! Trotzdem fortfahren? (J/N) ") == "N":
            exit()

#Den Text vor und nach den geänderten Werten auslesen und speichern
with open(r"Preset.txt")as part1file:
    part1 = part1file.read()

part2 = r"\makeinvoice \end{document}"
#Rechnungsdatum einfügen
invNumber = r"\setinvoicenumber{"+ reverseDate +"}"

#Rechnungssumme einfügen
summe_text = r"\settotal{" + "{:.2f}".format(summe) + r" \euro}"

#Rechnung zusammenfügen
print("Rechnung wird erstellt...")
body =  part1 + invNumber + items + summe_text + part2

#Rechnungsnamen erstellen
rechnungName = r"Rechnung_vom_" + date.today().strftime("%d.%m.%Y")+"_"

#Rechnung speichern
counter = 1
while True: #Namendopplung vermeiden
    try:
        with open(rechnungName + ".tex", "r"): #Falls der Name schon existiert
            print(rechnungName + " Existiert bereits! Name wird geändert.")
            if str(counter - 1) in (rechnungName + ".tex")[-5:]:
                rechnungName = (rechnungName + ".tex")[:-5] + str(counter)
            else:
                rechnungName = rechnungName + str(counter)
            counter += 1
    except:
        rechnungTexName = rechnungName + ".tex"
        break

#Rechnung schreiben
with open(rechnungTexName, "w") as rechnung:
    rechnung.write(body)

#print('Die Rechnung wird als PDF gespeichert...')


#.tex in .pdf konvertieren
#with open(os.devnull, 'wb') as devnull:
#    proc = subprocess.Popen(['latexmk', '-pdf', str(rechnungTexName)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

cmd = ['latexmk', '-pdf', str(rechnungTexName)]
spinner = Spinner("Die Rechnung wird gespeichert ")
with subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True) as p:
    for line in p.stdout:
        #print(line, end='') # process line here
        spinner.next()


if p.returncode != 0:
    pass
    #raise subprocess.CalledProcessError(p.returncode, p.args)

#Cleanup
with open(os.devnull, 'wb') as devnull:
    subprocess.run(['latexmk', '-c'], stdout=devnull, stderr=subprocess.STDOUT)

cmd = ['latexmk', '-c']
spinner = Spinner("Räume auf ")
with subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True) as p:
    for line in p.stdout:
        #print(line, end='') # process line here
        spinner.next()

if p.returncode != 0:
    pass

print('Die Rechnung ist gespeichert!')
print(rechnungName+".pdf")
subprocess.Popen(rechnungName + ".pdf",shell=True)

