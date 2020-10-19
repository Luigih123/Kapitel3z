minuter = int(input('Hur många minuter ringer du per månad?')) # Här frågar jag användaren hur många minuter dem ringer totalt i månaden
if minuter <= 32: # Här räknar den ut om det är mindre eller likamed 32 så får du ut svaret kontant
    print('Kontant')
elif minuter >= 67: # Här räknar den ut om det är mer eller likamed 67 så får du ut svaret plus 
        print('plus')
else: # Här så räkner den om du har skrivit ett tal mellan 33 till 66 och då får du ut svaret normal
    print('normal')