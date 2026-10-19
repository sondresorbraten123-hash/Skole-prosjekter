
#While betingelser
bet1 = True
bet2 = True
bet3 = True
#While løkke for å kjøre programmet kontinuerlig
while bet1:
    
    #While løkker for test på inndata
    while bet2:
        koffein = int(input("Oppgi mengden koffein i mg i drikken: "))
        if koffein <= 130 and koffein >= 30:
            bet2 = False
    
    while bet3:
        dl = float(input("Oppgi størrelsen på drikken i dl: "))
        if dl <= 5 and dl >= 0.3:
            bet3 = False
    
    #Beregning av mengden koffein rett etter inntak
    time0 = koffein * dl
    
    #For løkke til beregning av koffein etter 1 time og 5 timer
    mengde = time0
    
    for k in range(1,6,1):
        
        mengde = mengde * 0.87
        
        if k == 1:
            time1 = mengde
        
        if k == 5:
            time5 = mengde
    
    #For løkke til beregning av mengden koffein etter inntak hver time i 12 timer
    mengde2 = time0
    
    for t in range(1,13,1):
        
        mengde2 = mengde2 * 0.87 + time0
        
        if t == 12:
            time12 = mengde2
    
    #Print av beregninger
    print("Koffeininnhold i kroppen etter en enhet er:", format(time0,".1f"), "mg")
    print("Koffeininnhold i kroppen etter 1 time er:", format(time1,".1f"), "mg")
    print("Koffeininnhold i kroppen etter 5 timer er:", format(time5,".1f"), "mg")
    print("Koffeininnhold i kroppen etter 12 timer med en enhet i timen er:", format(time12,".1f"), "mg")
    
    #Spør om brukeren ønsker å avslutte programmet og avslutter hvis brukeren svarer ja
    avslutte = input("Vil du avslutte programmet? j/n: ")
    
    if avslutte == "j" or avslutte == "ja":
        bet1 = False
    else:
        bet2 = True
        bet3 = True

print("Program avsluttet")