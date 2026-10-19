from tkinter import *
import mysql.connector


# Brukerbehandling
def vindu_legg_til_bruker():

    # Legger til bruker i databasen med sjekk om bruker finnes
    def legg_til_bruker():
        try:
            brukerID_markor = mindatabase.cursor()
            bruker_data = (brukerID_var.get(), fornavn_var.get(), etternavn_var.get(), epost_var.get())
            finnes = False
            brukerID = brukerID_var.get()

            brukerID_markor.execute("SELECT BrukerID FROM Bruker WHERE BrukerID = %s", (brukerID,))
            for row in brukerID_markor:
                resultat_var.set('[-] BrukerID finnes fra før')
                finnes = True
            brukerID_markor.close()

            if finnes == False:
                ny_bruker_markor = mindatabase.cursor()
                ny_bruker_markor.execute("INSERT INTO Bruker(BrukerID, Fornavn, Etternavn, Epost) VALUES(%s, %s, %s, %s)", bruker_data)
                resultat_var.set('[+] Bruker lagt til')
                mindatabase.commit()
                ny_bruker_markor.close()

        # Hvis bruker skriver inn for lang eller ugyldig data
        except mysql.connector.errors.DataError:
            resultat_var.set('[-] Ugyldig data')


    # Selve vinduet for legg til bruker
    vindu1 = Toplevel()
    vindu1.title('Legg til ny bruker')

    legg_til_bruker_frame = LabelFrame(vindu1, text = 'Ny bruker', font = mindre_tekst, labelanchor = "n")
    legg_til_bruker_frame.grid(row = 0, column = 0, padx = 15, pady = 15)

    lbl_brukerID = Label(legg_til_bruker_frame, text = 'Oppgi brukerID:')
    lbl_brukerID.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = E)

    lbl_fornavn = Label(legg_til_bruker_frame, text = 'Oppgi fornavn:')
    lbl_fornavn.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = E)

    lbl_etternavn = Label(legg_til_bruker_frame, text = 'Oppgi etternavn:')
    lbl_etternavn.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = E)

    lbl_epost = Label(legg_til_bruker_frame, text = 'Oppgi epost:')
    lbl_epost.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = E)

    lbl_resultat = Label(legg_til_bruker_frame, text = 'Resultat:')
    lbl_resultat.grid(row = 4, column = 0, padx = 5, pady = (15, 0), sticky = E)

    brukerID_var = StringVar()
    ent_brukerID = Entry(legg_til_bruker_frame, width = 8, textvariable = brukerID_var)
    ent_brukerID.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = W)

    fornavn_var = StringVar()
    ent_fornavn = Entry(legg_til_bruker_frame, width = 32, textvariable = fornavn_var)
    ent_fornavn.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = W)

    etternavn_var = StringVar()
    ent_etternavn = Entry(legg_til_bruker_frame, width = 22, textvariable = etternavn_var)
    ent_etternavn.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = W)

    epost_var = StringVar()
    ent_epost = Entry(legg_til_bruker_frame, width = 42, textvariable = epost_var)
    ent_epost.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = W)

    resultat_var = StringVar()
    ent_resultat = Entry(legg_til_bruker_frame, width = 25, textvariable = resultat_var, state = "readonly")
    ent_resultat.grid(row = 4, column = 1, padx = 5, pady = (15, 0), sticky = W)

    btn_utfor = Button(legg_til_bruker_frame, text = 'Legg til bruker', command = legg_til_bruker)
    btn_utfor.grid(row = 5, column = 1, padx = 5, pady = 5, sticky = W)


    btn_lukk = Button(vindu1, text = 'Lukk vindu', command = vindu1.destroy)
    btn_lukk.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = SE)


def vindu_endre_epost():

    # Oppdaterer eposten til brukeren med sjekk om bruker finnes
    def endre_epost():
        try:
            brukerID_markor = mindatabase.cursor()
            epost_data = (epost_var.get(), brukerID_var.get())
            finnes = False
            brukerID = brukerID_var.get()

            brukerID_markor.execute("SELECT BrukerID FROM Bruker WHERE BrukerID = %s", (brukerID,))
            for row in brukerID_markor:
                finnes = True
            brukerID_markor.close()

            if finnes:
                epost_markor = mindatabase.cursor()
                epost_markor.execute("UPDATE Bruker SET Epost = %s WHERE BrukerID = %s", epost_data)
                resultat_var.set('[+] Epost endret')
                mindatabase.commit()
                epost_markor.close()
            else:
                resultat_var.set('[-] Bruker finnes ikke')

        # Hvis bruker skriver inn for lang eller ugyldig data
        except mysql.connector.errors.DataError:
            resultat_var.set('[-] Ugyldig data')


    # Vinduet til endre epost funksjonen
    vindu2 = Toplevel()
    vindu2.title('Endre epost til bruker')

    epost_frame = LabelFrame(vindu2, text = 'Endre epost', font = mindre_tekst, labelanchor = "n")
    epost_frame.grid(row = 0, column = 0, padx = 15, pady = 15)

    lbl_brukerID = Label(epost_frame, text = 'Oppgi brukerID:')
    lbl_brukerID.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = E)

    lbl_epost = Label(epost_frame, text = 'Oppgi ny epost:')
    lbl_epost.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = E)

    lbl_resultat = Label(epost_frame, text = 'Resultat:')
    lbl_resultat.grid(row = 2, column = 0, padx = 5, pady = (15, 0), sticky = E)

    brukerID_var = StringVar()
    ent_brukerID = Entry(epost_frame, width = 8, textvariable = brukerID_var)
    ent_brukerID.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = W)

    epost_var = StringVar()
    ent_epost = Entry(epost_frame, width = 42, textvariable = epost_var)
    ent_epost.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = W)

    resultat_var = StringVar()
    ent_resultat = Entry(epost_frame, width = 25, textvariable = resultat_var, state = "readonly")
    ent_resultat.grid(row = 2, column = 1, padx = 5, pady = (15, 0), sticky = W)

    btn_utfor = Button(epost_frame, text = 'Endre eposten', command = endre_epost)
    btn_utfor.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = W)


    btn_lukk = Button(vindu2, text = 'Lukk vindu', command = vindu2.destroy)
    btn_lukk.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = SE)



# Bildebehandling
def vindu_bilde_legg_til():

    # Legger til bildet med sjekk på om bruker og bildet finnes
    def legg_til_bilde():
        try:
            fotograf_markor = mindatabase.cursor()
            bilde_data = (bildeID_var.get(), beskrivelse_var.get(), dato_var.get(), fotograf_var.get())
            fotograf_finnes = False
            bilde_finnes = False
            fotograf = fotograf_var.get()
            bildeID = bildeID_var.get()

            fotograf_markor.execute("SELECT BrukerID FROM Bruker WHERE BrukerID = %s", (fotograf,))
            for row in fotograf_markor:
                fotograf_finnes = True
            fotograf_markor.close()
                        
            if fotograf_finnes:
                bilde_markor = mindatabase.cursor()
                bilde_markor.execute("SELECT BildeID FROM Bilde WHERE BildeID = %s", (bildeID,))
                for row in bilde_markor:
                    bilde_finnes = True
                bilde_markor.close()
            
                if bilde_finnes == False:
                    legg_til_markor = mindatabase.cursor()
                    legg_til_markor.execute("INSERT INTO Bilde(BildeID, Beskrivelse, OpplastetDato, Fotograf) VALUES(%s, %s, %s, %s)", bilde_data)
                    mindatabase.commit()
                    resultat_bilde_var.set('[+] Bilde opplastet')
                    legg_til_markor.close()
                else:
                    resultat_bilde_var.set('[-] BildeID finnes fra før')
            else:
                resultat_bilde_var.set('[-] Bruker finnes ikke')
            

        # Hvis bruker skriver inn for lang eller ugyldig data
        except mysql.connector.errors.DataError:
            resultat_bilde_var.set('[-] Ugyldig data')


    # Vinduet til Legg til bilde funksjonen
    vindu3 = Toplevel()
    vindu3.title('Legg til bilde')

    nytt_bilde_frame = LabelFrame(vindu3, text = 'Nytt bilde', font = mindre_tekst, labelanchor = "n")
    nytt_bilde_frame.grid(row = 0, column = 0, padx = 15, pady = 15)

    lbl_bildeID = Label(nytt_bilde_frame, text = 'Oppgi bildeID:')
    lbl_bildeID.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = E)

    lbl_beskrivelse = Label(nytt_bilde_frame, text = 'Oppgi beskrivelse:')
    lbl_beskrivelse.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = E)

    lbl_dato = Label(nytt_bilde_frame, text = 'Oppgi opplastet dato:')
    lbl_dato.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = E)

    lbl_fotograf = Label(nytt_bilde_frame, text = 'Oppgi fotograf/brukerID:')
    lbl_fotograf.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = E)

    lbl_bilde_resultat = Label(nytt_bilde_frame, text = 'Resultat:')
    lbl_bilde_resultat.grid(row = 4, column = 0, padx = 5, pady = (15, 0), sticky = E)

    bildeID_var = StringVar()
    ent_bildeID = Entry(nytt_bilde_frame, width = 8, textvariable = bildeID_var)
    ent_bildeID.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = W)

    beskrivelse_var = StringVar()
    ent_beskrivelse = Entry(nytt_bilde_frame, width = 32, textvariable = beskrivelse_var)
    ent_beskrivelse.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = W)

    dato_var = StringVar()
    ent_dato = Entry(nytt_bilde_frame, width = 10, textvariable = dato_var)
    ent_dato.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = W)

    fotograf_var = StringVar()
    ent_fotograf = Entry(nytt_bilde_frame, width = 10, textvariable = fotograf_var)
    ent_fotograf.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = W)

    resultat_bilde_var = StringVar()
    ent_bilde_resultat = Entry(nytt_bilde_frame, width = 25, textvariable = resultat_bilde_var, state = "readonly")
    ent_bilde_resultat.grid(row = 4, column = 1, padx = 5, pady = (15, 0), sticky = W)

    btn_utfor = Button(nytt_bilde_frame, text = 'Legg til bildet', command = legg_til_bilde)
    btn_utfor.grid(row = 5, column = 1, padx = 5, pady = 5, sticky = W)


    btn_lukk = Button(vindu3, text = 'Lukk vindu', command = vindu3.destroy)
    btn_lukk.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = SE)



def vindu_endre_beskrivelse():

    # Oppdaterer beskrivelsen med sjekk på at bildet finnes
    def endre_beskrivelse():
        try:
            bildeID_markor = mindatabase.cursor()
            beskrivelse_data = (beskrivelse_var.get(), bildeID_var.get())
            finnes = False
            bildeID = bildeID_var.get()

            bildeID_markor.execute("SELECT BildeID FROM Bilde WHERE BildeID = %s", (bildeID,))
            for row in bildeID_markor:
                finnes = True
            bildeID_markor.close()

            if finnes:
                beskrivelse_markor = mindatabase.cursor()
                beskrivelse_markor.execute("UPDATE Bilde SET Beskrivelse = %s WHERE BildeID = %s", beskrivelse_data)
                resultat_var.set('[+] Beskrivelse endret')
                mindatabase.commit()
                beskrivelse_markor.close()
            else:
                resultat_var.set('[-] BildeID finnes ikke')



        # Hvis bruker skriver inn for lang eller ugyldig data
        except mysql.connector.errors.DataError:
            resultat_var.set('[-] Ugyldig data')



    # Vinduet til endre beskrivelse funksjonen
    vindu4 = Toplevel()
    vindu4.title('Endre bilde beskrivelse')

    beskrivelse_frame = LabelFrame(vindu4, text = 'Endre beskrivelse', font = mindre_tekst, labelanchor = "n")
    beskrivelse_frame.grid(row = 0, column = 0, padx = 15, pady = 15)

    lbl_bildeID = Label(beskrivelse_frame, text = 'Oppgi bildeID:')
    lbl_bildeID.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = E)

    lbl_beskrivelse = Label(beskrivelse_frame, text = 'Oppgi ny beskrivelse:')
    lbl_beskrivelse.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = E)

    lbl_resultat = Label(beskrivelse_frame, text = 'Resultat:')
    lbl_resultat.grid(row = 2, column = 0, padx = 5, pady = (15, 0), sticky = E)

    bildeID_var = StringVar()
    ent_bildeID = Entry(beskrivelse_frame, width = 8, textvariable = bildeID_var)
    ent_bildeID.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = W)

    beskrivelse_var = StringVar()
    ent_beskrivelse = Entry(beskrivelse_frame, width = 32, textvariable = beskrivelse_var)
    ent_beskrivelse.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = W)

    resultat_var = StringVar()
    ent_resultat = Entry(beskrivelse_frame, width = 25, textvariable = resultat_var, state = "readonly")
    ent_resultat.grid(row = 2, column = 1, padx = 5, pady = (15, 0), sticky = W)

    btn_utfor = Button(beskrivelse_frame, text = 'Endre beskrivelse', command = endre_beskrivelse)
    btn_utfor.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = W)


    btn_lukk = Button(vindu4, text = 'Lukk vindu', command = vindu4.destroy)
    btn_lukk.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = SE)



def vindu_tagger():

    # Legger til tag på et bildet med sjekker på at bildet, emneknaggen og taggen finnes
    def legg_til_tag():
        try:
            bildeID_markor = mindatabase.cursor()
            tag_data = (bildeID_var.get(), emneknaggID_var.get())
            bilde_finnes = False
            emneknagg_finnes = False
            tag_finnes = False
            bildeID = bildeID_var.get()
            emneknaggID = emneknaggID_var.get()

            bildeID_markor.execute("SELECT BildeID FROM Bilde WHERE BildeID = %s", (bildeID,))
            for row in bildeID_markor:
                bilde_finnes = True
            bildeID_markor.close()

            if bilde_finnes:
                emneknagg_markor = mindatabase.cursor()
                emneknagg_markor.execute("SELECT EmneknaggID FROM Emneknagg WHERE EmneknaggID = %s", (emneknaggID,))
                for row in emneknagg_markor:
                    emneknagg_finnes = True
                emneknagg_markor.close()

                if emneknagg_finnes:
                    tag_finnes_markor = mindatabase.cursor()
                    tag_finnes_markor.execute("SELECT BildeID FROM TagForBilde WHERE BildeID = %s and EmneknaggID = %s", tag_data)
                    for row in tag_finnes_markor:
                        tag_finnes = True
                    tag_finnes_markor.close()

                    if tag_finnes == False:
                        legg_til_markor = mindatabase.cursor()
                        legg_til_markor.execute("INSERT INTO TagForBilde(BildeID, EmneknaggID) VALUES(%s, %s)", tag_data)
                        mindatabase.commit()
                        resultat_var.set('[+] Bilde tagget')
                        legg_til_markor.close()
                    else:
                        resultat_var.set('[-] Tag finnes på bilde allerede')
                else:
                    resultat_var.set('[-] Emneknagg finnes ikke')
            else:
                resultat_var.set('[-] BildeID finnes ikke')

            

        # Hvis bruker skriver inn for lang eller ugyldig data
        except mysql.connector.errors.DataError:
            resultat_var.set('[-] Ugyldig data')

    # Sletter taggen fra bildet med sjekker på at bilde, emneknagg og taggen finnes
    def slett_tag():
        bilde_markor = mindatabase.cursor()
        tag_data = (bildeID_var.get() ,emneknaggID_var.get())
        bilde_finnes = False
        emneknagg_finnes = False
        tag_finnes = False
        bildeID = bildeID_var.get()
        emneknaggID = emneknaggID_var.get()

        bilde_markor.execute("SELECT BildeID FROM Bilde WHERE BildeID = %s", (bildeID,))
        for row in bilde_markor:
            bilde_finnes = True
        bilde_markor.close()

        if bilde_finnes:
            emneknagg_markor = mindatabase.cursor()
            emneknagg_markor.execute("SELECT EmneknaggID FROM Emneknagg WHERE EmneknaggID = %s", (emneknaggID,))
            for row in emneknagg_markor:
                emneknagg_finnes = True
            emneknagg_markor.close()

            if emneknagg_finnes:
                tag_markor = mindatabase.cursor()
                tag_markor.execute("SELECT BildeID, EmneknaggID FROM TagForBilde WHERE BildeID = %s and EmneknaggID = %s", tag_data)
                for row in tag_markor:
                    tag_finnes = True
                tag_markor.close()

                if tag_finnes:
                    slett_tag_markor = mindatabase.cursor()
                    slett_tag_markor.execute("DELETE FROM TagForBilde WHERE BildeID = %s and EmneknaggID = %s", tag_data)
                    mindatabase.commit()
                    resultat_var.set('[+] Tag slettet fra bilde')
                    slett_tag_markor.close()
                else:
                    resultat_var.set('[-] Taggen er ikke på bildet')
            else:
                resultat_var.set('[-] Emneknaggen finnes ikke')
        else:
            resultat_var.set('[-] BildeID finnes ikke')


    # Vinduet til legg til/slett tagg funksjonen
    vindu5 = Toplevel()
    vindu5.title('Legg til/slett tagger på et bilde')

    tag_frame = LabelFrame(vindu5, text = 'Legg til/slett tagger på et bilde', font = mindre_tekst, labelanchor = "n")
    tag_frame.grid(row = 0, column = 0, padx = 15, pady = 15)

    lbl_BildeID = Label(tag_frame, text = 'Oppgi bildeID:')
    lbl_BildeID.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = E)

    lbl_emneknaggID = Label(tag_frame, text = 'Oppgi emneknaggID:')
    lbl_emneknaggID.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = E)

    lbl_resultat = Label(tag_frame, text = 'Resultat:')
    lbl_resultat.grid(row = 2, column = 0, padx = 5, pady = (15, 0), sticky = E)

    bildeID_var = StringVar()
    ent_bildeID = Entry(tag_frame, width = 8, textvariable = bildeID_var)
    ent_bildeID.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = W)

    emneknaggID_var = StringVar()
    ent_emneknaggID = Entry(tag_frame, width = 8, textvariable = emneknaggID_var)
    ent_emneknaggID.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = W)

    resultat_var = StringVar()
    ent_resultat = Entry(tag_frame, width = 25, textvariable = resultat_var, state = "readonly")
    ent_resultat.grid(row = 2, column = 1, padx = 5, pady = (15, 0), sticky = W)

    btn_utfor_ny = Button(tag_frame, text = 'Legg til tagg', command = legg_til_tag)
    btn_utfor_ny.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = W)

    btn_utfor_slett = Button(tag_frame, text = 'Slett tagg', command = slett_tag)
    btn_utfor_slett.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = E)


    btn_lukk = Button(vindu5, text = 'Lukk vindu', command = vindu5.destroy)
    btn_lukk.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = SE)




def vindu_slett_bilde():

    # Sletter bildet og eventuelle kommentarer, likes og tagger
    # Med sjekk på om bildet, likes, kommentarer og tagger finnes
    # Utfører bare sletting på det som trengs sletting
    def slett_bilde():
        bildeID = bildeID_var.get()
        bilde_finnes = False
        like_finnes = False
        kommentar_finnes = False
        tag_finnes = False

        bilde_markor = mindatabase.cursor()
        bilde_markor.execute("SELECT BildeID FROM Bilde WHERE BildeID = %s", (bildeID,))
        for row in bilde_markor:
            bilde_finnes = True
        bilde_markor.close()

        if bilde_finnes:
            # Sletting av likes hvis de finnes
            like_markor = mindatabase.cursor()
            like_markor.execute("SELECT BildeID FROM Likes WHERE BildeID = %s", (bildeID,))
            for row in like_markor:
                like_finnes = True
            like_markor.close()

            if like_finnes:
                slett_like_markor = mindatabase.cursor()
                slett_like_markor.execute("DELETE FROM Likes WHERE BildeID = %s", (bildeID,))
                slett_like_markor.close()
            
            # Sletting av kommentarer hvis de finnes
            kommentar_markor = mindatabase.cursor()
            kommentar_markor.execute("SELECT BildeID FROM Kommentar WHERE BildeID = %s", (bildeID,))
            for row in kommentar_markor:
                kommentar_finnes = True
            kommentar_markor.close()

            if kommentar_finnes:
                slett_kommentar_markor = mindatabase.cursor()
                slett_kommentar_markor.execute("DELETE FROM Kommentar WHERE BildeID = %s", (bildeID,))
                slett_kommentar_markor.close()

            # Sletting av tags på bildet hvis de finnes
            tag_markor = mindatabase.cursor()
            tag_markor.execute("SELECT BildeID FROM TagForBilde WHERE BildeID = %s", (bildeID,))
            for row in tag_markor:
                tag_finnes = True
            tag_markor.close()
            
            if tag_finnes:
                slett_tag_markor = mindatabase.cursor()
                slett_tag_markor.execute("DELETE FROM TagForBilde WHERE BildeID = %s", (bildeID,))
                slett_tag_markor.close()
            
            # Sletting av selve bildet
            slett_bilde_markor = mindatabase.cursor()
            slett_bilde_markor.execute("DELETE FROM Bilde WHERE BildeID = %s", (bildeID,))
            slett_bilde_markor.close()
            mindatabase.commit()
            resultat_var.set('[+] Bildet slettet')
        else:
            resultat_var.set('[-] BildeID finnes ikke')


    # Vindu for bilde sletting
    vindu6 = Toplevel()
    vindu6.title('Slett bilde med kommentarer og likes')

    slett_bilde_frame = LabelFrame(vindu6, text = 'Slett bilde', font = mindre_tekst, labelanchor = "n")
    slett_bilde_frame.grid(row = 0, column = 0, padx = 15, pady = 15)

    lbl_bildeID = Label(slett_bilde_frame, text = 'Oppgi bildeID')
    lbl_bildeID.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = E)

    lbl_resultat = Label(slett_bilde_frame, text = 'Oppgi bildeID')
    lbl_resultat.grid(row = 1, column = 0, padx = 5, pady = (15, 0), sticky = E)

    bildeID_var = StringVar()
    ent_bildeID = Entry(slett_bilde_frame, width = 8, textvariable = bildeID_var)
    ent_bildeID.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = W)

    resultat_var = StringVar()
    ent_resultat = Entry(slett_bilde_frame, width = 25, textvariable = resultat_var, state = "readonly")
    ent_resultat.grid(row = 1, column = 1, padx = 5, pady = (15, 0), sticky = W)

    btn_utfor = Button(slett_bilde_frame, text = 'Slett bilde', command = slett_bilde)
    btn_utfor.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = W)


    btn_lukk = Button(vindu6, text = 'Lukk vindu', command = vindu6.destroy)
    btn_lukk.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = SE)



# Generell administrering
def vindu_legg_til_emneknagg():

    # Legger til emneknagg med sjekk på om emneknaggen finnes
    def legg_til_emne():
        try:
            emneknaggID_markor = mindatabase.cursor()
            finnes = False
            emneknagg_data = (emneknaggID_var.get(), emneknagg_var.get())
            emneknaggID = emneknaggID_var.get()

            emneknaggID_markor.execute("SELECT EmneknaggID FROM Emneknagg WHERE EmneknaggID = %s", (emneknaggID,))
            for row in emneknaggID_markor:
                finnes = True
                resultat_emne_var.set('[-] EmneknaggID finnes fra før')
            emneknaggID_markor.close()

            if finnes == False:
                legg_til_emneknagg_markor = mindatabase.cursor()
                legg_til_emneknagg_markor.execute("INSERT INTO Emneknagg(EmneknaggID, Emneknaggen) VALUES(%s, %s)", emneknagg_data)
                mindatabase.commit()
                resultat_emne_var.set('[+] Emneknagg lagt til')
                legg_til_emneknagg_markor.close()
            

        # Hvis bruker skriver inn for lang eller ugyldig data
        except mysql.connector.errors.DataError:
            resultat_emne_var.set('[-] Ugyldig data')


    # Vindu for å legge til emneknagg i systemet
    # Slette emneknagg er ikke en funksjon i oppgaven
    vindu7 = Toplevel()
    vindu7.title('Legg til emneknagg')

    emneknagg_frame = LabelFrame(vindu7, text = 'Ny emneknagg', font = mindre_tekst, labelanchor = "n")
    emneknagg_frame.grid(row = 0, column = 0, padx = 15, pady = 15)

    lbl_emneknaggID = Label(emneknagg_frame, text = 'Oppgi emneknaggID:')
    lbl_emneknaggID.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = E)

    lbl_emneknagg = Label(emneknagg_frame, text = 'Oppgi emneknaggen:')
    lbl_emneknagg.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = E)

    lbl_emne_resultat = Label(emneknagg_frame, text = 'Resultat:')
    lbl_emne_resultat.grid(row = 2, column = 0, padx = 5, pady = (15, 0), sticky = E)

    emneknaggID_var = StringVar()
    ent_emneknaggID = Entry(emneknagg_frame, width = 8, textvariable = emneknaggID_var)
    ent_emneknaggID.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = W)

    emneknagg_var = StringVar()
    ent_emneknagg = Entry(emneknagg_frame, width = 42, textvariable = emneknagg_var)
    ent_emneknagg.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = W)

    resultat_emne_var = StringVar()
    ent_emne_resultat = Entry(emneknagg_frame, width = 25, textvariable = resultat_emne_var, state = "readonly")
    ent_emne_resultat.grid(row = 2, column = 1, padx = 5, pady = (15, 0), sticky = W)

    btn_utfor = Button(emneknagg_frame, text = 'Legg til emneknaggen', command = legg_til_emne)
    btn_utfor.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = W)

    
    btn_lukk = Button(vindu7, text = 'Lukk vindu', command = vindu7.destroy)
    btn_lukk.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = SE)



def vindu_likes():
    
    # Liker bildet med sjekk på at bruker, bildet, og like finnes
    def like():
        try:
            like_data = (bildeID_var.get(), brukerID_var.get())
            bildeID = bildeID_var.get()
            brukerID = brukerID_var.get()
            bruker_finnes = False
            bilde_finnes = False
            like_finnes = False

            bruker_markor = mindatabase.cursor()
            bruker_markor.execute("SELECT BrukerID FROM Bruker WHERE BrukerID = %s", (brukerID,))
            for row in bruker_markor:
                bruker_finnes = True
            bruker_markor.close()

            if bruker_finnes:
                bilde_markor = mindatabase.cursor()
                bilde_markor.execute("SELECT BildeID FROM Bilde WHERE BildeID = %s", (bildeID,))
                for row in bilde_markor:
                    bilde_finnes = True
                bilde_markor.close()

                if bilde_finnes:
                    sjekk_like_markor = mindatabase.cursor()
                    sjekk_like_markor.execute("SELECT BildeID, BrukerID FROM Likes WHERE BildeID = %s and BrukerID = %s", like_data)
                    for row in sjekk_like_markor:
                        like_finnes = True
                    sjekk_like_markor.close()

                    if like_finnes == False:
                        like_markor = mindatabase.cursor()
                        like_markor.execute("INSERT INTO Likes(BildeID, BrukerID) VALUES(%s, %s)",like_data)
                        mindatabase.commit()
                        resultat_var.set('[+] Bildet liket')
                        like_markor.close()
                    else:
                        resultat_var.set('[-] Like finnes fra før')
                else:
                    resultat_var.set('[-] Bildet finnes ikke')
            else:
                resultat_var.set('[-] Bruker finnes ikke')


        # Hvis bruker skriver inn for lang eller ugyldig data
        except mysql.connector.errors.DataError:
            resultat_var.set('[-] Ugyldig data')

    # Fjerner like fra bildet med sjekk om bildet, bruker og like finnes
    def unlike():
        unlike_data = (bildeID_var.get(), brukerID_var.get())
        bildeID = bildeID_var.get()
        brukerID = brukerID_var.get()
        like_finnes = False
        bruker_finnes = False
        bilde_finnes = False

        bruker_markor = mindatabase.cursor()
        bruker_markor.execute("SELECT BrukerID FROM Bruker WHERE BrukerID = %s", (brukerID,))
        for row in bruker_markor:
            bruker_finnes = True
        bruker_markor.close()

        if bruker_finnes:
            bilde_markor = mindatabase.cursor()
            bilde_markor.execute("SELECT BildeID FROM Bilde WHERE BildeID = %s", (bildeID,))
            for row in bilde_markor:
                bilde_finnes = True
            bilde_markor.close()

            if bilde_finnes:
                sjekk_like_markor = mindatabase.cursor()
                sjekk_like_markor.execute("SELECT BildeID, BrukerID FROM Likes WHERE BildeID = %s and BrukerID = %s", unlike_data)
                for row in sjekk_like_markor:
                    like_finnes = True
                sjekk_like_markor.close()

                if like_finnes:
                    unlike_markor = mindatabase.cursor()
                    unlike_markor.execute("DELETE FROM Likes WHERE BildeID = %s and BrukerID = %s", unlike_data)
                    mindatabase.commit()
                    resultat_var.set('[+] Like slettet')
                    unlike_markor.close()
                else:
                    resultat_var.set('[-] Like finnes ikke')
            else:
                resultat_var.set('[-] Bildet finnes ikke')
        else:
            resultat_var.set('[-] Bruker finnes ikke')


    # Vindu for å legge til/slette likes
    vindu8 = Toplevel()
    vindu8.title('Legg til/slett likes')

    like_frame = LabelFrame(vindu8, text = 'legg til og fjern likes', font = mindre_tekst, labelanchor = "n")
    like_frame.grid(row = 0, column = 0, padx = 15, pady = 15)

    lbl_brukerID = Label(like_frame, text = 'Oppgi brukerID:')
    lbl_brukerID.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = E)

    lbl_bildeID = Label(like_frame, text = 'Oppgi bildeID:')
    lbl_bildeID.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = E)

    lbl_resultat = Label(like_frame, text = 'Resultat:')
    lbl_resultat.grid(row = 2, column = 0, padx = 5, pady = (15, 0), sticky = E)

    brukerID_var = StringVar()
    ent_brukerID = Entry(like_frame, width = 8, textvariable = brukerID_var)
    ent_brukerID.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = W)

    bildeID_var = StringVar()
    ent_bildeID = Entry(like_frame, width = 8, textvariable = bildeID_var)
    ent_bildeID.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = W)

    resultat_var = StringVar()
    ent_resultat = Entry(like_frame, width = 25, textvariable = resultat_var, state = "readonly")
    ent_resultat.grid(row = 2, column = 1, padx = 5, pady = (15, 0), sticky = W)

    btn_utfor_like = Button(like_frame, text = 'Like', command = like)
    btn_utfor_like.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = W)

    btn_utfor_unlike = Button(like_frame, text = 'Unlike', command = unlike)
    btn_utfor_unlike.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = E)


    btn_lukk = Button(vindu8, text = 'Lukk vindu', command = vindu8.destroy)
    btn_lukk.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = SE)


def vindu_kommenter():

    # Søker opp bildet og gir info med sjekk på om det finnes
    def sok_bilde():
        bildeID = bildeID_var.get()
        finnes = False
        beskrivelse_var.set('')
        dato_var.set('')

        bilde_markor = mindatabase.cursor()
        bilde_markor.execute("Select BildeID, Beskrivelse, OpplastetDato FROM Bilde WHERE BildeID = %s", (bildeID,))
        for row in bilde_markor:
            finnes = True
            beskrivelse_var.set(row[1])
            dato_var.set(row[2])
            sok_resultat_var.set('[+] Bildet funnet')
        bilde_markor.close()

        if finnes == False:
            sok_resultat_var.set('[-] Bildet finnes ikke')


    # Legger til kommentar med sjekk på at bruker, bilde og kommentar finnes
    def kommenter():
        try:
            kommentar_data = (bildeID_var.get(), brukerID_var.get(), kommentar_var.get())
            brukerID = brukerID_var.get()
            bildeID = bildeID_var.get()
            bruker_finnes = False
            bilde_finnes = False
            kommentar_finnes = False

            bruker_markor = mindatabase.cursor()
            bruker_markor.execute("SELECT BrukerID FROM Bruker WHERE BrukerID = %s", (brukerID,))
            for row in bruker_markor:
                bruker_finnes = True
            bruker_markor.close()

            if bruker_finnes:
                bilde_markor = mindatabase.cursor()
                bilde_markor.execute("SELECT BildeID FROM Bilde WHERE BildeID = %s", (bildeID,))
                for row in bilde_markor:
                    bilde_finnes = True
                bilde_markor.close()

                if bilde_finnes:
                    sjekk_kommentar_markor = mindatabase.cursor()
                    sjekk_kommentar_markor.execute("SELECT BildeID, BrukerID FROM Kommentar WHERE BildeID = %s and BrukerID = %s", (bildeID, brukerID))
                    for row in sjekk_kommentar_markor:
                        kommentar_finnes = True
                    sjekk_kommentar_markor.close()

                    if kommentar_finnes == False:
                        kommenter_markor = mindatabase.cursor()
                        kommenter_markor.execute("INSERT INTO Kommentar(BildeID, BrukerID, Kommentaren) VALUES(%s, %s, %s)", kommentar_data)
                        mindatabase.commit()
                        kommentar_resultat_var.set('[+] Kommentert')
                    else:
                        kommentar_resultat_var.set('[-] Allerede kommentert')
                else:
                    kommentar_resultat_var.set('[-] Bildet finnes ikke')
            else:
                kommentar_resultat_var.set('[-] Bruker finnes ikke')


        # Hvis bruker skriver inn for lang eller ugyldig data
        except mysql.connector.errors.DataError:
            kommentar_resultat_var.set('[-] Ugyldig data')


    # Vindu for å "se" og kommentere et bilde
    vindu9 = Toplevel()
    vindu9.title('Se og kommenter et bilde')

    kommentar_frame = LabelFrame(vindu9, text = 'Kommenter', labelanchor = "n")
    kommentar_frame.grid(row = 0, column = 0, padx = 15, pady = 15)

    sok_frame = LabelFrame(kommentar_frame, text = 'Søk bilde', labelanchor = "n")
    sok_frame.grid(row = 0, column = 0, padx = 15, pady = 15)

    kommenter_frame = LabelFrame(kommentar_frame, text = 'Kommenter bilde', labelanchor = "n")
    kommenter_frame.grid(row = 0, column = 1, padx = 15, pady = 15)

    # Søk bilde
    lbl_bildeID = Label(sok_frame, text = 'Oppgi bildeID:')
    lbl_bildeID.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = E)

    lbl_beskrivelse = Label(sok_frame, text = 'Beskrivelse')
    lbl_beskrivelse.grid(row = 1, column = 0, padx = 5, pady = (15, 0), sticky = E)

    lbl_dato = Label(sok_frame, text = 'Opplastet dato:')
    lbl_dato.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = E)

    lbl_sok_resultat = Label(sok_frame, text = 'Resultat:')
    lbl_sok_resultat.grid(row = 3, column = 0, padx = 5, pady = (15, 0), sticky = E)

    bildeID_var = StringVar()
    ent_bildeID = Entry(sok_frame, width = 8, textvariable = bildeID_var)
    ent_bildeID.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = W)

    beskrivelse_var = StringVar()
    ent_beskrivelse = Entry(sok_frame, width = 32, textvariable = beskrivelse_var, state = "readonly")
    ent_beskrivelse.grid(row = 1, column = 1, padx = 5, pady = (15, 0), sticky = W)
    
    dato_var = StringVar()
    ent_dato = Entry(sok_frame, width = 10, textvariable = dato_var, state = "readonly")
    ent_dato.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = W)

    sok_resultat_var = StringVar()
    ent_sok_resultat = Entry(sok_frame, width = 25, textvariable = sok_resultat_var, state = "readonly")
    ent_sok_resultat.grid(row = 3, column = 1, padx = 5, pady = (15, 0), sticky = W)

    # Kommenter
    lbl_brukerID = Label(kommenter_frame, text = 'Oppgi brukerID:')
    lbl_brukerID.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = E)

    lbl_kommentar = Label(kommenter_frame, text = 'Oppgi kommentaren:')
    lbl_kommentar.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = E)

    lbl_kommentar_resultat = Label(kommenter_frame, text = 'Resultat:')
    lbl_kommentar_resultat.grid(row = 2, column = 0, padx = 5, pady = (15, 0), sticky = E)

    brukerID_var = StringVar()
    ent_brukerID = Entry(kommenter_frame, width = 8, textvariable = brukerID_var)
    ent_brukerID.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = W)

    kommentar_var = StringVar()
    ent_kommentar = Entry(kommenter_frame, width = 32, textvariable = kommentar_var)
    ent_kommentar.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = W)

    kommentar_resultat_var = StringVar()
    ent_kommentar_resultat = Entry(kommenter_frame, width = 25, textvariable = kommentar_resultat_var, state = "readonly")
    ent_kommentar_resultat.grid(row = 2, column = 1, padx = 5, pady = (15, 0), sticky = W)

    btn_utfor_kommentar = Button(kommenter_frame, text = 'Legg til kommentar', command = kommenter)
    btn_utfor_kommentar.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = W)

    btn_sok_bilde = Button(sok_frame, text = 'Søk bilde', command = sok_bilde)
    btn_sok_bilde.grid(row = 4, column = 1, padx = 5, pady = 5, sticky = W)


    btn_lukk = Button(vindu9, text = 'Lukk vindu', command = vindu9.destroy)
    btn_lukk.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = SE)



def vindu_slett_kommentar():
    
    # Sletter kommentar med sjekk på at bruker, bilde og kommentar finnes
    def slett_kommentar():
            kommentar_data = (bildeID_var.get(), brukerID_var.get())
            brukerID = brukerID_var.get()
            bildeID = bildeID_var.get()
            bruker_finnes = False
            bilde_finnes = False
            kommentar_finnes = False

            bruker_markor = mindatabase.cursor()
            bruker_markor.execute("SELECT BrukerID FROM Bruker WHERE BrukerID = %s", (brukerID,))
            for row in bruker_markor:
                bruker_finnes = True
            bruker_markor.close()

            if bruker_finnes:
                bilde_markor = mindatabase.cursor()
                bilde_markor.execute("SELECT BildeID FROM Bilde WHERE BildeID = %s", (bildeID,))
                for row in bilde_markor:
                    bilde_finnes = True
                bilde_markor.close()

                if bilde_finnes:
                    sjekk_kommentar_markor = mindatabase.cursor()
                    sjekk_kommentar_markor.execute("SELECT BildeID, BrukerID FROM Kommentar WHERE BildeID = %s and BrukerID = %s", kommentar_data)
                    for row in sjekk_kommentar_markor:
                        kommentar_finnes = True
                    sjekk_kommentar_markor.close()

                    if kommentar_finnes:
                        slett_kommentar_markor = mindatabase.cursor()
                        slett_kommentar_markor.execute("DELETE FROM Kommentar WHERE BildeID = %s and BrukerID = %s", kommentar_data)
                        mindatabase.commit()
                        slett_kommentar_markor.close()
                        resultat_var.set('[+] Kommentar slettet')
                    else:
                        resultat_var.set('[-] Kommentar finnes ikke')
                else:
                    resultat_var.set('[-] Bilde finnes ikke')
            else:
                resultat_var.set('[-] Bruker finnes ikke')


    # Vindu for å slette kommentar fra et bilde
    vindu10 = Toplevel()
    vindu10.title('Slett kommentar fra bilde')

    slett_kommentar_frame = LabelFrame(vindu10, text = 'Slett kommentar', labelanchor = "n")
    slett_kommentar_frame.grid(row = 0, column = 0, padx = 15, pady = 15)

    lbl_brukerID = Label(slett_kommentar_frame, text = 'Oppgi brukerID:')
    lbl_brukerID.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = E)

    lbl_bildeID = Label(slett_kommentar_frame, text = 'Oppgi bildeID:')
    lbl_bildeID.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = E)

    lbl_resultat = Label(slett_kommentar_frame, text = 'Resultat:')
    lbl_resultat.grid(row = 2, column = 0, padx = 5, pady = (15, 0), sticky = E)

    brukerID_var = StringVar()
    ent_brukerID = Entry(slett_kommentar_frame, width = 8, textvariable = brukerID_var)
    ent_brukerID.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = W)

    bildeID_var = StringVar()
    ent_bildeID = Entry(slett_kommentar_frame, width = 8, textvariable = bildeID_var)
    ent_bildeID.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = W)

    resultat_var = StringVar()
    ent_resultat = Entry(slett_kommentar_frame, width = 25, textvariable = resultat_var, state = "readonly")
    ent_resultat.grid(row = 2, column = 1, padx = 5, pady = (15, 0), sticky = W)

    btn_utfor = Button(slett_kommentar_frame, text = 'Slett kommentar', command = slett_kommentar)
    btn_utfor.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = W)

    btn_lukk = Button(vindu10, text = 'Lukk vindu', command = vindu10.destroy)
    btn_lukk.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = SE)



# Oversikt
def vindu_sok_bruker():

    # Søker på bruker og gir alle bildene til brukeren i listbox
    # Med sjekk om bruker og bilde finnes
    def sok_brukere():
        bruker_finnes = False
        bilder_finnes = False
        brukerID = brukerID_var.get()
        bilde_innhold = []
        kommentar_liste.set([''])

        bruker_markor = mindatabase.cursor()
        bruker_markor.execute("SELECT BrukerID FROM Bruker WHERE BrukerID = %s", (brukerID,))
        for row in bruker_markor:
            bruker_finnes = True
        bruker_markor.close()

        if bruker_finnes:
            bilde_markor = mindatabase.cursor()
            bilde_markor.execute("SELECT Fotograf, Beskrivelse FROM Bilde WHERE Fotograf = %s", (brukerID,))
            for row in bilde_markor:
                bilder_finnes = True
                bilde_innhold = bilde_innhold + [row[1]]
            bilde_markor.close()
            
            if bilder_finnes:
                bilde_liste.set(tuple(bilde_innhold))
            else:
                bilde_liste.set(['[-] Bruker har ikke bilder'])
        else:
            bilde_liste.set(['[-] Bruker finnes ikke'])


    # Legger alle kommentarene til valgt bilde i listbox
    # Med sjekk på at kommentarer finnes
    def vis_kommentarer(event):
        # Denne er bare så funksjonen ikke kjører med tom selection, for å slippe error
        if not bilde_box.curselection():
            return

        beskrivelse = bilde_box.get(bilde_box.curselection())
        brukerID = brukerID_var.get()
        kommentar_innhold = []
        kommentar_finnes = False

        kommentar_markor = mindatabase.cursor()
        kommentar_markor.execute("SELECT BildeID, Kommentaren FROM Kommentar WHERE BildeID IN (SELECT BildeID FROM Bilde WHERE Fotograf = %s and Beskrivelse = %s)", (brukerID, beskrivelse))
        for row in kommentar_markor:
            kommentar_finnes = True
            kommentar_innhold = kommentar_innhold + [row[1]]
        kommentar_markor.close()

        if kommentar_finnes:
            kommentar_liste.set(tuple(kommentar_innhold))
        else:
            kommentar_liste.set(['[-] Bildet har ikke kommentarer'])


    # Vindu for å finne bilder til bruker og kommentarer
    vindu11 = Toplevel()
    vindu11.title('Søk på bruker med oversikt over bilder og kommentarer')

    brukersok_frame = LabelFrame(vindu11, text = 'Søk bruker med oversikt over bilder og kommentarer')
    brukersok_frame.grid(row = 0, column = 0, padx = 15, pady = 15)

    lbl_brukerID = Label(brukersok_frame, text = 'Oppgi brukerID:')
    lbl_brukerID.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = E)

    lbl_bilder = Label(brukersok_frame, text = 'Bilder:')
    lbl_bilder.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = (15, 0))

    lbl_kommentarer = Label(brukersok_frame, text = 'Kommentarer:')
    lbl_kommentarer.grid(row = 1, column = 3, padx = (5,0), pady = (15, 0))

    brukerID_var = StringVar()
    ent_brukerID = Entry(brukersok_frame, width = 8, textvariable = brukerID_var)
    ent_brukerID.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = W)

    bilde_scroll = Scrollbar(brukersok_frame, orient = VERTICAL)
    bilde_scroll.grid(row = 2, column = 2, rowspan = 5, padx = (0,5), pady = 5, sticky = NS)

    Kommentar_scroll = Scrollbar(brukersok_frame, orient = VERTICAL)
    Kommentar_scroll.grid(row = 2, column = 4, rowspan = 5, padx = (0,5), pady = 5, sticky = NS)

    bilde_liste = StringVar()
    bilde_box = Listbox(brukersok_frame, width = 32, height = 5, listvariable = bilde_liste, yscrollcommand = bilde_scroll.set)
    bilde_box.grid(row = 2, column = 0, columnspan = 2, rowspan = 5, padx = (5,0), pady = 5, sticky = E)

    kommentar_liste = StringVar()
    kommentar_box = Listbox(brukersok_frame, width = 42, height = 5, listvariable = kommentar_liste, yscrollcommand = Kommentar_scroll.set)
    kommentar_box.grid(row = 2, column = 3, rowspan = 5, padx = (5,0), pady = 5, sticky = E)

    bilde_scroll["command"] = bilde_box.yview
    Kommentar_scroll["command"] = kommentar_box.yview
    bilde_box.bind("<<ListboxSelect>>", vis_kommentarer)

    btn_utfor = Button(brukersok_frame, text = 'Finn bilder til bruker', command = sok_brukere)
    btn_utfor.grid(row = 0, column = 3, padx = 5, pady = 5, sticky = W)


    btn_lukk = Button(vindu11, text = 'Lukk vindu', command = vindu11.destroy)
    btn_lukk.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = SE)



def vindu_sok_bilde():

    # Søker på bildet og legger alle kommentarer til bildet i listbox
    # Med sjekk på at bildet og kommentarer finnes
    def sok_bilde():
        fornavn_var.set('')
        etternavn_var.set('')
        bilde_finnes = False
        kommentarer_finnes = False
        bildeID = bildeID_var.get()
        kommentarer_innhold = []

        bilde_markor = mindatabase.cursor()
        bilde_markor.execute("SELECT BildeID FROM Bilde WHERE BildeID = %s", (bildeID,))
        for row in bilde_markor:
            bilde_finnes = True
        bilde_markor.close()

        if bilde_finnes:
            kommentar_markor = mindatabase.cursor()
            kommentar_markor.execute("SELECT Kommentaren FROM Kommentar WHERE BildeID = %s", (bildeID,))
            for row in kommentar_markor:
                kommentarer_finnes = True
                kommentarer_innhold = kommentarer_innhold + [row[0]]
            kommentar_markor.close()

            if kommentarer_finnes:
                kommentar_liste.set(tuple(kommentarer_innhold))
            else:
                kommentar_liste.set(['[-] Bildet har ingen kommentarer'])
        else:
            kommentar_liste.set(['[-] Bildet finnes ikke'])


    # Gir info til hvem som la igjen kommentaren som er valgt
    def brukerinfo(event):
        # Denne er bare så funksjonen ikke kjører med tom selection, for å slippe error
        if not kommentar_box.curselection():
            return

        bildeID = bildeID_var.get()
        kommentar = kommentar_box.get(kommentar_box.curselection())

        bruker_markor = mindatabase.cursor()
        bruker_markor.execute("SELECT Fornavn, Etternavn, BrukerID FROM Bruker WHERE BrukerID IN (SELECT BrukerID FROM Kommentar WHERE BildeID = %s and Kommentaren = %s)", (bildeID, kommentar))
        for row in bruker_markor:
            fornavn_var.set(row[0])
            etternavn_var.set(row[1])
        bruker_markor.close()


    # Vindu for å se kommentarer på bildet med info på hvem som kommenterte
    vindu12 = Toplevel()
    vindu12.title('Søk på bilde med oversikt over kommentarer')

    bilde_sok_frame = LabelFrame(vindu12, text = 'Søk på bilde og se kommentarer', labelanchor = "n")
    bilde_sok_frame.grid(row = 0, column = 0, padx = 15, pady = 15)

    brukerinfo_frame = LabelFrame(bilde_sok_frame, text = 'Bruker som kommenterte', labelanchor = "n")
    brukerinfo_frame.grid(row = 2, column = 3, padx = 5, pady = 5)

    lbl_bildeID = Label(bilde_sok_frame, text = 'Oppgi bildeID:')
    lbl_bildeID.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = E)

    lbl_kommentarer = Label(bilde_sok_frame, text = 'Kommentarer:')
    lbl_kommentarer.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = (5,0))

    lbl_fornavn = Label(brukerinfo_frame, text = 'Fornavn:')
    lbl_fornavn.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = E)

    lbl_etternavn = Label(brukerinfo_frame, text = 'Etternavn:')
    lbl_etternavn.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = E)

    bildeID_var = StringVar()
    ent_bildeID = Entry(bilde_sok_frame, width = 8, textvariable = bildeID_var)
    ent_bildeID.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = W)

    fornavn_var = StringVar()
    ent_fornavn = Entry(brukerinfo_frame, width = 32, textvariable = fornavn_var, state = "readonly")
    ent_fornavn.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = W)

    etternavn_var = StringVar()
    ent_etternavn = Entry(brukerinfo_frame, width = 22, textvariable = etternavn_var, state = "readonly")
    ent_etternavn.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = W)

    kommentar_scroll = Scrollbar(bilde_sok_frame, orient = VERTICAL)
    kommentar_scroll.grid(row = 2, column = 2, padx = (0, 5), pady = 5, sticky = NS)

    kommentar_liste = StringVar()
    kommentar_box = Listbox(bilde_sok_frame, width = 42, height = 5, listvariable = kommentar_liste, yscrollcommand = kommentar_scroll.set)
    kommentar_box.grid(row = 2, column = 0, columnspan = 2, padx = (5, 0), pady = 5, sticky = E)

    kommentar_scroll["command"] = kommentar_box.yview
    kommentar_box.bind("<<ListboxSelect>>", brukerinfo)

    btn_utfor = Button(bilde_sok_frame, text = 'Finn kommentarer til bilde', command = sok_bilde)
    btn_utfor.grid(row = 0, column = 3, padx = 5, pady = 5, sticky = W)


    btn_lukk = Button(vindu12, text = 'Lukk vindu', command = vindu12.destroy)
    btn_lukk.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = SE)




# Kobler opp databasen
mindatabase = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'Bildesjef',
    passwd = 'eksfor2026',
    db = 'eksfor2026'
)



# Meny vinduet
main = Tk()
main.title('Meny')

stor_tekst = ("Helvetica", 16, "bold")
mindre_tekst = ("Helvetica", 10, "bold")


# Brukerbehandling
bruker_frame = LabelFrame(main, text = 'Brukerbehandling', font = stor_tekst, labelanchor = "n")
bruker_frame.grid(row = 0, column = 0, padx = 15, pady = 15, sticky = NSEW)
bruker_frame.columnconfigure(0, weight=1)

# Legge til ny bruker
btn_legg_til_bruker = Button(bruker_frame, text = 'Legg til bruker', font = mindre_tekst, command = vindu_legg_til_bruker, padx = 25, pady = 15)
btn_legg_til_bruker.grid(row = 0, column = 0, padx = 15, pady = 15, sticky = NSEW)

# Endre epost til bruker
btn_endre_epost = Button(bruker_frame, text = 'Endre epost', font = mindre_tekst, command = vindu_endre_epost, padx = 25, pady = 15)
btn_endre_epost.grid(row = 1, column = 0, padx = 15, pady = 15, sticky = NSEW)


# Bildebehandling
bilde_frame = LabelFrame(main, text = 'Bildebehandling', font = stor_tekst, labelanchor = "n")
bilde_frame.grid(row = 0, column = 1, padx = 15, pady = 15, sticky = NSEW)
bilde_frame.columnconfigure(0, weight=1)

# Legge til nytt bilde
btn_bilde_legg_til = Button(bilde_frame, text = 'Legg til bilde', font = mindre_tekst, command = vindu_bilde_legg_til, padx = 25, pady = 15)
btn_bilde_legg_til.grid(row = 0, column = 0, padx = 15, pady = 15, sticky = NSEW)

# Endre beskrivelse på bilde
btn_endre_beskrivelse = Button(bilde_frame, text = 'Endre beskrivelse', font = mindre_tekst, command = vindu_endre_beskrivelse, padx = 25, pady = 15)
btn_endre_beskrivelse.grid(row = 1, column = 0, padx = 15, pady = 15, sticky = NSEW)

# Legge til/slette tagger på et bilde
btn_tagger = Button(bilde_frame, text = 'Legg til/slett tagger', font = mindre_tekst, command = vindu_tagger, padx = 25, pady = 15)
btn_tagger.grid(row = 2, column = 0, padx = 15, pady = 15, sticky = NSEW)

# Slette bilde med alle kommentarer og likes
btn_slett_bilde = Button(bilde_frame, text = 'Slett bilde', font = mindre_tekst, command = vindu_slett_bilde, padx = 25, pady = 15)
btn_slett_bilde.grid(row = 3, column = 0, padx = 15, pady = 15, sticky = NSEW)


# Generell administrering
generell_frame = LabelFrame(main, text = 'Generelt', font = stor_tekst, labelanchor = "n")
generell_frame.grid(row = 1, column = 0, padx = 15, pady = 15, sticky = NSEW)
generell_frame.columnconfigure(0, weight=1)

# Legge til emneknagger
btn_emneknagger = Button(generell_frame, text = 'Legg til emneknagg', font = mindre_tekst, command = vindu_legg_til_emneknagg, padx = 25, pady = 15)
btn_emneknagger.grid(row = 0, column = 0, padx = 15, pady = 15, sticky = NSEW)

# Legge til/slette likes
btn_likes = Button(generell_frame, text = 'Legg til/slett likes', font = mindre_tekst, command = vindu_likes, padx = 25, pady = 15)
btn_likes.grid(row = 1, column = 0, padx = 15, pady = 15, sticky = NSEW)

# Legge til kommentar på et bilde
btn_kommenter = Button(generell_frame, text = 'Bilde info og kommenter', font = mindre_tekst, command = vindu_kommenter, padx = 25, pady = 15)
btn_kommenter.grid(row = 2, column = 0, padx = 15, pady = 15, sticky = NSEW)

# Slette kommentar på et bilde
btn_slett_kommentar = Button(generell_frame, text = 'Slett kommentar', font = mindre_tekst, command = vindu_slett_kommentar, padx = 25, pady = 15)
btn_slett_kommentar.grid(row = 3, column = 0, padx = 15, pady = 15, sticky = NSEW)


# Oversikt
sok_frame = LabelFrame(main, text = 'Oversikt', font = stor_tekst, labelanchor = "n")
sok_frame.grid(row = 1, column = 1, padx = 15, pady = 15, sticky = NSEW)
sok_frame.columnconfigure(0, weight=1)

# Søk på BrukerID, med info om bilder og kommentarer
btn_sok_bruker = Button(sok_frame, text = 'Finn bilder til en bruker', font = mindre_tekst, command = vindu_sok_bruker, padx = 25, pady = 15)
btn_sok_bruker.grid(row = 0, column = 0, padx = 15, pady = 15, sticky = NSEW)

# Søk på BildeID, vise kommentarer og brukerinfo bak kommentaren
btn_sok_bilde = Button(sok_frame, text = 'Finn kommentarer til et bilde', font = mindre_tekst, command = vindu_sok_bilde, padx = 25, pady = 15)
btn_sok_bilde.grid(row = 1, column = 0, padx = 15, pady = 15, sticky = NSEW)


btn_avslutt = Button(main, text = "Avslutt program", command = main.destroy)
btn_avslutt.grid(row = 2, column = 1, padx = 5, pady = 10, sticky = SE)

main.mainloop()
mindatabase.close()