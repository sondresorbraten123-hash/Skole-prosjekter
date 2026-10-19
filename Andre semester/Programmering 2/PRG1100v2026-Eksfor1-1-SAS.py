from tkinter import *

# Funksjon for å søke etter hunden med feilbehandling
def finn_opplysninger():
    finnes = False
    sok = hundeID_var.get()

    try:
        hundenavn_var.set(hunder[sok]["hundenavn"])
        kjonn_var.set(hunder[sok]["hundekjonn"])

        kennelID = hunder[sok]["oppdretterID"]
        eierID = hunder[sok]["hundeeierID"]

        kennelnavn_var.set(oppdrettere[kennelID]["kennelnavn"])
        eier_fornavn_var.set(hundeeiere[eierID]["eier_fornavn"])
        eier_etternavn_var.set(hundeeiere[eierID]["eier_etternavn"])


    except KeyError:
        hundenavn_var.set("Hund finnes ikke")
        kennelnavn_var.set("")
        eier_fornavn_var.set("")
        kjonn_var.set("")
        eier_etternavn_var.set("")

# Lager vinduet
vindu = Tk()
vindu.title("Finn hund med opplysninger om kennel og eier")

# Labeller for vinduet
lbl_hundeID = Label(vindu, text = "Oppgi HundeID:")
lbl_hundeID.grid(row = 0, column = 0, padx = 5, pady = 20, sticky = E)

lbl_hundenavn = Label(vindu, text = "Hundenavn:")
lbl_hundenavn.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = E)

lbl_kennelnavn = Label(vindu, text = "Kennelnavn:")
lbl_kennelnavn.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = E)

lbl_eier_fornavn = Label(vindu, text = "Eiers fornavn:")
lbl_eier_fornavn.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = E)

lbl_kjonn = Label(vindu, text = "Kjønn:")
lbl_kjonn.grid(row = 1, column = 2, padx = 5, pady = 5, sticky = E)

lbl_eier_etternavn = Label(vindu, text = "Eiers etternavn:")
lbl_eier_etternavn.grid(row = 3, column = 2, padx = 5, pady = 5, sticky = E)

# Entryer for vinduet
hundeID_var = StringVar()
ent_hundeID = Entry(vindu, width = 8, textvariable = hundeID_var)
ent_hundeID.grid(row = 0, column = 1, padx = 5, pady = 20, sticky = W)

hundenavn_var = StringVar()
ent_hundenavn = Entry(vindu, width = 15, textvariable = hundenavn_var, state = "readonly")
ent_hundenavn.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = W)

kennelnavn_var = StringVar()
ent_kennelnavn = Entry(vindu, width = 20, textvariable = kennelnavn_var, state = "readonly")
ent_kennelnavn.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = W)

eier_fornavn_var = StringVar()
ent_eier_fornavn = Entry(vindu, width = 12, textvariable = eier_fornavn_var, state = "readonly")
ent_eier_fornavn.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = W)

kjonn_var = StringVar()
ent_kjonn = Entry(vindu, width = 8, textvariable = kjonn_var, state = "readonly")
ent_kjonn.grid(row = 1, column = 4, padx = 5, pady = 5, sticky = W)

eier_etternavn_var = StringVar()
ent_eier_etternavn = Entry(vindu, width = 12, textvariable = eier_etternavn_var, state = "readonly")
ent_eier_etternavn.grid(row = 3, column = 4, padx = 5, pady = 5, sticky = W)

# Knapper for vinduet
btn_finn_opplysninger = Button(vindu, text = "Finn hundeopplysninger", command = finn_opplysninger)
btn_finn_opplysninger.grid(row = 0, column = 2, padx = 5, pady = 20, sticky = E)

btn_avslutt = Button(vindu, text = "Avslutt", command = vindu.destroy)
btn_avslutt.grid(row = 5, column = 5, padx = 5, pady = 5, sticky = SE)


# Legger tekstfiler i dictionary med feilbehandling
try:
    # Legger hund.txt i flernivå dictionary
    hundefil = open("hund.txt", "r", encoding = "utf-8")
    hundeID = hundefil.readline()
    hunder = {}

    while hundeID != "":
        hundeID = hundeID.rstrip("\n")
        oppdretterID = hundefil.readline().rstrip("\n")
        hundeeierID = hundefil.readline().rstrip("\n")
        hundenavn = hundefil.readline().rstrip("\n")
        hundekjonn = hundefil.readline().rstrip("\n")
        hund_fodt = hundefil.readline().rstrip("\n")

        hunder[hundeID] = {"oppdretterID": oppdretterID, "hundeeierID": hundeeierID, "hundenavn": hundenavn, "hundekjonn": hundekjonn, "hund_fodt": hund_fodt}

        hundeID = hundefil.readline()
    
    hundefil.close()

    # Legger hundeeier.txt i flernivå dictionary
    eierfil = open("hundeeier.txt", "r", encoding = "utf-8")
    hundeeierID = eierfil.readline()
    hundeeiere = {}

    while hundeeierID != "":
        hundeeierID = hundeeierID.rstrip("\n")
        eier_fornavn = eierfil.readline().rstrip("\n")
        eier_etternavn = eierfil.readline().rstrip("\n")

        hundeeiere[hundeeierID] = {"eier_fornavn": eier_fornavn, "eier_etternavn": eier_etternavn}

        hundeeierID = eierfil.readline()

    eierfil.close()


    # Legger oppdretter.txt i en flernivå dictionary
    oppdretterfil = open("oppdretter.txt", "r", encoding = "utf-8")
    oppdretterID = oppdretterfil.readline()
    oppdrettere = {}

    while oppdretterID != "":
        oppdretterID = oppdretterID.rstrip("\n")
        kennelnavn = oppdretterfil.readline().rstrip("\n")
        kenneleier_fornavn = oppdretterfil.readline().rstrip("\n")
        kenneleier_etternavn = oppdretterfil.readline().rstrip("\n")

        oppdrettere[oppdretterID] = {"kennelnavn": kennelnavn, "kenneleier_fornavn": kenneleier_fornavn, "kenneleier_etternavn": kenneleier_etternavn}

        oppdretterID = oppdretterfil.readline()

    oppdretterfil.close()

except FileNotFoundError:
    hundenavn_var.set("Fil(er) finnes ikke")


vindu.mainloop()
