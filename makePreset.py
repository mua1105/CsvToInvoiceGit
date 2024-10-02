
print(r"Vorlage Erstellen (\\ eingeben für Zeilenumbruch): ")
firmenName = str(input("Bitte den Namen des Empfängers eingeben: "))
firmenAdresse = str(input("Bitte die Adresse des Empfängers eingeben: "))
name = str(input("Bitte deinen Namen eingeben: "))
adress = input("Bitte deine Adresse (Straße + Nr) eingeben (Bitte kein 'ß' eingeben): ")
print(adress)
plz = str(input("Bitte deine Postleitzahl und Stadt eingeben: "))
phoneNr = str(input("Bitte deine Telefonnummer eingeben: "))
email = str(input("Bitte deine Email-Adresse eingebn: "))
iban = str(input("Bitte deine IBAN eingeben: "))

preset = r"""\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{simpleinvoice,eurosym}
\pagenumbering{gobble}

\begin{document}
\setinvoicetitle{Rechnung Nr: }
"""
firmenName = r"\setreceivername{"+firmenName +"}"
firmenAdresse = r"\setreceiveraddress{"+firmenAdresse+"}"
name = r"\setname{"+name+"}"
adress = r"\setaddress{"+adress+ r" \\ "+ plz+"}{"+adress+ r"\\"+plz+"}"
iban = r"\setaccountnumber{"+iban+"}"
email = r"\setemail{"+email+"}"
phoneNr = r"\setphonenumber{"+phoneNr+"}"



with open("Preset.txt", "w") as file:
    file.write(preset + firmenName + firmenAdresse + name + adress + phoneNr + email + iban + r"\setinvoicedate{\today}")
