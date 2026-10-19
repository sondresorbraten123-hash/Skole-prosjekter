
import os

#Funksjon registrere bruker
def reg_bruker():
    #While betingelse
    reg_bet = True
    
    while reg_bet:
        #Åpner og lukker fil i append for å unngå feilmeldinger
        brukerfil = open("bruker.txt", "a")
        brukerfil.close()

        duplikat = False

        brukerfil = open("bruker.txt", "r")
        bruker = brukerfil.readline()
        brukerID = input("Oppgi BrukerID: ")

        #Sjekker etter duplikat
        while bruker != "":
            bruker = bruker.rstrip("\n")

            if bruker == brukerID:
                duplikat = True

            bruker = brukerfil.readline()
        
        brukerfil.close()
        brukerfil = open("bruker.txt", "a")
        
        #skriver bruker til fil hvis bruker ikke finnes
        if duplikat == False:
            fornavn = input("Oppgi fornavn: ")
            etternavn = input("Oppgi etternavn: ")
            epost = input("Oppgi e-post: ")

            brukerfil.write(brukerID + "\n")
            brukerfil.write(fornavn + "\n")
            brukerfil.write(etternavn + "\n")
            brukerfil.write(epost + "\n")

            brukerfil.close()
            reg_bet = False
        else:
            print("BrukerID allerede i bruk, velg noe annet")



#Funksjon for bilde opplasting
def bilde_opplasting():
    #While betingelse
    bilde_bet = True
    
    while bilde_bet:
        #Åpner og lukker filer i append for å unngå feilmeldinger
        bildefil = open("bilde.txt", "a")
        bildefil.close()
        brukerfil = open("bruker.txt", "a")
        brukerfil.close()

        bildefil = open("bilde.txt", "r")
        bilde = bildefil.readline()
        brukerfil = open("bruker.txt", "r")
        bruker = brukerfil.readline()
        bilde_duplikat = False
        bruker_finnes = False

        bildeID = input("Oppgi bildeID: ")
        fotograf = input("Oppgi bruker/fotograf: ")

        #Sjekker om bildet eksisterer fra før
        while bilde != "":
            bilde = bilde.rstrip("\n")

            if bilde == bildeID:
                bilde_duplikat = True
            
            bilde = bildefil.readline()
        
        #Sjekker at bruker finnes
        while bruker != "":
            bruker = bruker.rstrip("\n")

            if bruker == fotograf:
                bruker_finnes = True
            
            bruker = brukerfil.readline()
        
        bildefil.close()
        brukerfil.close()

        #Skriver bilde til fil hvis bildet ikke finnes fra før og bruker finnes
        if bilde_duplikat == False and bruker_finnes == True:
            bildefil = open("bilde.txt", "a")

            beskrivelse = input("Oppgi beskrivelse: ")
            opplastet_dato = input("Oppgi opplastet dato: ")

            bildefil.write(bildeID + "\n")
            bildefil.write(beskrivelse + "\n")
            bildefil.write(opplastet_dato + "\n")
            bildefil.write(fotograf + "\n")

            bildefil.close()
            bilde_bet = False
        
        if bilde_duplikat:    
            print("Dette bildet er allerede lastet opp")
        
        if bruker_finnes == False:
            print("Denne brukeren eksisterer ikke")



#Funksjon for å kommentere
def kommenter():
    #While betingelse
    kommentar_bet = True

    while kommentar_bet:
        #Åpner og lukker filer i append for å unngå feilmeldinger
        brukerfil = open("bruker.txt", "a")
        brukerfil.close()
        bildefil = open("bilde.txt", "a")
        bildefil.close()

        kommentarfil = open("kommentar.txt", "a")
        brukerfil = open("bruker.txt", "r")
        bildefil = open("bilde.txt", "r")
        bruker = brukerfil.readline()
        bilde = bildefil.readline()

        bruker_finnes = False
        bilde_finnes = False
        bildeID = input("Oppgi bilde du skal kommentere: ")
        brukerID = input("Oppgi din brukerID: ")
        kommentar = input("Oppgi kommentar: ")

        #Sjekker at bildet finnes
        while bilde != "":
            bilde = bilde.rstrip("\n")

            if bilde == bildeID:
                bilde_finnes = True
            
            bilde = bildefil.readline()

        #Sjekker at bruker finnes
        while bruker != "":
            bruker = bruker.rstrip("\n")

            if bruker == brukerID:
                bruker_finnes = True
            
            bruker = brukerfil.readline()

        brukerfil.close()
        bildefil.close()

        #Skriver kommentar til fil hvis bruker og bildet finnes
        if bruker_finnes and bilde_finnes:
            kommentarfil.write(bildeID + "\n")
            kommentarfil.write(brukerID + "\n")
            kommentarfil.write(kommentar + "\n")
        
            kommentarfil.close()
            kommentar_bet = False

        if bruker_finnes == False:
            print("Oppgitt bruker eksisterer ikke")
        
        if bilde_finnes == False:
            print("Oppgitt bilde eksisterer ikke")



#Funskjon for å like et bilde
def like():
    #While betingelse
    like_bet = True

    while like_bet:
        #Åpner og lukker filer i append for å unngå feilmeldinger
        brukerfil = open("bruker.txt", "a")
        brukerfil.close()
        bildefil = open("bilde.txt", "a")
        bildefil.close()

        likefil = open("likes.txt", "a")
        bildefil = open("bilde.txt", "r")
        brukerfil = open("bruker.txt", "r")
        bilde = bildefil.readline()
        bruker = brukerfil.readline()

        bilde_finnes = False
        bruker_finnes = False
        bildeID = input("Oppgi bilde du ønsker å like: ")
        brukerID = input("Oppgi din brukerID: ")

        #Sjekker at bildet finnes
        while bilde != "":
            bilde = bilde.rstrip("\n")

            if bilde == bildeID:
                bilde_finnes = True
            
            bilde = bildefil.readline()
        
        #Sjekker at bruker finnes
        while bruker != "":
            bruker = bruker.rstrip("\n")

            if bruker == brukerID:
                bruker_finnes = True

            bruker = brukerfil.readline()
        
        bildefil.close()
        brukerfil.close()

        #Skriver like til fil hvis bilde og bruker finnes
        if bilde_finnes and bruker_finnes:
            likefil.write(bildeID + "\n")
            likefil.write(brukerID + "\n")
            
            likefil.close()
            like_bet = False
        
        if bilde_finnes == False:
            print("Oppgitt bilde eksisterer ikke")
        
        if bruker_finnes == False:
            print("Oppgitt bruker eksisterer ikke")


#Funksjon for å slette bilde samt kommentarer og likes
def bilde_slett():
    #While betingelse
    slett_bet = True

    while slett_bet:
        #Åpner og lukker filer i append for å unngå feilmeldinger
        bildefil = open("bilde.txt", "a")
        bildefil.close()
        kommentarfil = open("kommentar.txt", "a")
        kommentarfil.close()
        likefil = open("likes.txt", "a")
        likefil.close()

        bildefil = open("bilde.txt", "r")
        kommentarfil = open("kommentar.txt", "r")
        likefil = open("likes.txt", "r")
        bilde = bildefil.readline()
        kommentar = kommentarfil.readline()
        like = likefil.readline()

        #Åpner tempfiler som skal bli de nye filene
        bilde_tempfil = open("bilde_temp.txt", "w")
        kommentar_tempfil = open("kommentar_temp.txt", "w")
        like_tempfil = open("like_temp.txt", "w")

        bilde_finnes = False
        slett = input("Oppgi bilde du ønsker å slette: ")
        
        #Sjekker at bildet finnes og 
        #skriver alt annet enn dette bilde til tempfil
        while bilde != "":
            bilde = bilde.rstrip("\n")

            if bilde == slett:
                bilde_finnes = True
                bilde = bildefil.readline()
                bilde = bildefil.readline()
                bilde = bildefil.readline()
            else:
                bilde_tempfil.write(bilde + "\n")

            bilde = bildefil.readline()

        #Sjekker om kommentarer for bildet finnes og
        #skriver alle andre kommentarer til tempfil
        while kommentar != "":
            kommentar = kommentar.rstrip("\n")

            if kommentar == slett:
                kommentar = kommentarfil.readline()
                kommentar = kommentarfil.readline()
            else:
                kommentar_tempfil.write(kommentar + "\n")
            
            kommentar = kommentarfil.readline()
        
        #Sjekker om det finnes likes for dette bildet og
        #skriver alle andre likes til tempfil
        while like != "":
            like = like.rstrip()

            if like == slett:
                like = likefil.readline()
            else:
                like_tempfil.write(like + "\n")

            like = likefil.readline()
        
        bildefil.close()
        bilde_tempfil.close()
        kommentarfil.close()
        kommentar_tempfil.close()
        likefil.close()
        like_tempfil.close()

        #Sletter gamle filer og renamer nye filer
        os.remove("bilde.txt")
        os.rename("bilde_temp.txt", "bilde.txt")
        os.remove("kommentar.txt")
        os.rename("kommentar_temp.txt", "kommentar.txt")
        os.remove("likes.txt")
        os.rename("like_temp.txt", "likes.txt")

        if bilde_finnes:
            print("Bilde, kommentarer og likes slettet")
            slett_bet = False
        else:
            print("Bilde eksisterer ikke")



#Funksjon for å skrive ut informasjon om et bilde
def utskrift_bilde():
    #While betingelse
    utskrift_bet = True
    
    while utskrift_bet:
        #Åpner og lukekr filer i append for å unngå feilmeldinger
        bildefil = open("bilde.txt", "a")
        bildefil.close()
        brukerfil = open("bruker.txt", "a")
        brukerfil.close()
        kommentarfil = open("kommentar.txt", "a")
        kommentarfil.close()

        bildefil = open("bilde.txt", "r")
        bilde = bildefil.readline()
        brukerfil = open("bruker.txt", "r")
        bruker = brukerfil.readline()
        kommentarfil = open("kommentar.txt", "r")
        kommentar_linje = kommentarfil.readline()

        bildeID = input("Oppgi bilde du vil ha informasjon om: ")
        bilde_finnes = False
        kommentar_finnes = False
        #Definerer liste til kommentarer
        kommentarliste = []

        #Sjekker om bildet finnes og lagrer informasjonen som trengs
        while bilde != "":
            bilde = bilde.rstrip("\n")

            if bilde == bildeID:
                bilde_finnes = True
                beskrivelse = bildefil.readline().rstrip("\n")
                dato = bildefil.readline().rstrip("\n")
                brukerID = bildefil.readline().rstrip("\n")

            bilde = bildefil.readline()
        
        #Søker etter fornavn og etternavn i brukerfil ved hjelp av brukerID
        while bruker != "":
            bruker = bruker.rstrip("\n")

            if bruker == brukerID:
                fornavn = brukerfil.readline().rstrip("\n")
                etternavn = brukerfil.readline().rstrip("\n")
            
            bruker = brukerfil.readline()
        
        #Ser etter kommentarer til bildet og legger de til i kommentarliste
        while kommentar_linje != "":
            kommentar_linje = kommentar_linje.rstrip("\n")

            if kommentar_linje == bildeID:
                kommentar_finnes = True
                kommentar_bruker = kommentarfil.readline().rstrip("\n")
                kommentar = kommentarfil.readline().rstrip("\n")
                kommentarliste = kommentarliste + [kommentar]
            
            kommentar_linje = kommentarfil.readline()

        bildefil.close()
        brukerfil.close()
        kommentarfil.close()
        
        #Setter while betingelse til false for å komme ut av loopen når den er ferdig
        utskrift_bet = False

        #Sjekker at bildet finnes og skriver ut informasjon eller feilmelding
        if bilde_finnes == False:
            print("Oppgitt bilde finnes ikke")

        else:
            print(f"Informasjon for bilde: {bildeID}")
            print(f"Beskrivelse: {beskrivelse}")
            print(f"Fornavn: {fornavn}")
            print(f"Etternavn: {etternavn}")

            #Sjekker om kommentarer finnes og bruker for løkke til å 
            #skrive ut alle kommentarer til bildet
            if kommentar_finnes == False:
                print("Dette bildet har ingen kommentarer")
            else:
                print("Kommentar/kommentarer:")
                for linje in range(len(kommentarliste)):
                    print(kommentarliste[linje])



#Funskjon hovedmeny for å gjøre valg etter hva du ønsker å gjøre
def main():
    main_bet = True

    while main_bet:
        print("\n--Hovedmeny--")
        print("[1] Registrer ny bruker")
        print("[2] Last opp nytt bilde")
        print("[3] Kommenter ett bilde")
        print("[4] Like ett bilde")
        print("[5] Slett ett bilde")
        print("[6] Vis informasjon om ett bilde")
        print("[9] Avslutt program")

        valg = input("Velg ett alternativ: ")

        if valg == "1":
            print()
            reg_bruker()

        if valg == "2":
            print()
            bilde_opplasting()

        if valg == "3":
            print()
            kommenter()

        if valg == "4":
            print()
            like()

        if valg == "5":
            print()
            bilde_slett()
        
        if valg == "6":
            print()
            utskrift_bilde()

        if valg == "9":
            main_bet = False

        if valg != "1" and valg != "2" and valg != "3" and valg != "4" and valg != "5" and valg != "6" and valg != "9":
            print("Ugyldig valg, prøv igjen")

    print("Program Avsluttet")

main()