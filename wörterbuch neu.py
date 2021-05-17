woerterbuch_deutsch = ["Apfel" , "Birne" , "Kirsche" , "Melone" , "Marille" , "Pfirsich"]
woerterbuch_english = ["apple" , "pear" , "cherry" , "melone" , "apricot" , "peach"]


auswahl = input("Befehl? [E]ingabe, [L]öschen, [A]bfrage:")


if auswahl == "E" or auswahl == "e" :
    sprache = input("Ins [D]eutsche oder [E]nglische eingeben?")

    if sprache == 'D' or sprache == 'd':
            wort1 = input("Zu einfügendes Wort:")
            woerterbuch_deutsch.append(wort1)
            print(wort1, "wurde eingefügt!")
            print("Neue Liste: " , woerterbuch_deutsch)
        
    
    elif sprache == "e" or sprache == "E":
            wort2 = input("Zu einfügendes Wort:")
            woerterbuch_english().append(wort2)
            print(wort2, "wurde eingefügt!")
            print("Neue Liste: " , woerterbuch_english)
        
elif auswahl == "l" or auswahl == "L":
    löschen = input("Aus dem [D]eutschen oder [E]nglischen löschen?")
    if löschen == "d" or löschen == "D":
        lwortd = input("Zu löschendes Wort:")
        woerterbuch_deutsch.remove(lwortd)
        print(lwortd, "wurde gelöscht!")
        print("Neue Liste: ", woerterbuch_deutsch)
    elif löschen == "e" or löschen == "E":
        lworte = input("Zu löschendes Wort:")
        woerterbuch_english.remove(lworte)
        print(lworte, "wurde gelöscht!")
        print("Neue Liste: ", woerterbuch_english)

 
else:
    max = len(woerterbuch_deutsch)
    eingabe = input("Frucht eingeben:") 
    eingabe.upper()
    index = 0

    while index < max:
        if woerterbuch_deutsch[index].upper() == eingabe.upper():
            print(woerterbuch_english[index] , " [EN]")
            break
        
        if woerterbuch_english[index].upper() == eingabe.upper():
            print(woerterbuch_deutsch[index] , " [DE]")
            break
        index += 1
    
    if index == max:
        print("Kein Wort gefunden!")
        
        
        