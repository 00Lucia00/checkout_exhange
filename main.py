def main():
    print("..Välkommen..")
    print("Här kan du se vad du ska få tillbaka i växel. Mata även in ören.")
    
    pris = float(input("Vad blev summan av dina varor?: "))
    betalt = float(input("Och vad betalade du?: "))
    
    total = betalt - pris
    
    print()
    print("Du ska få tillbaka: " + str(total) + "Kr")
    print()
    
    tusen = int(total / 1000)
    print(tusen, "x 1000 Sedel")
    total %= 1000
    
    femhundra = int(total / 500)
    print(femhundra, "x 500 Sedel")
    total %= 500
    
    hundra = int(total / 100)
    print(hundra, "x 100 Sedel")
    total %= 100
    
    femtio = int(total / 50)
    print(femtio, "x 50 Sedel")
    total %= 50
    
    tjugo = int(total / 20)
    print(tjugo, "x 20 Sedel")
    total %= 20
    
    tio = int(total / 10)
    print(tio, "x 10 Kronor")
    total %= 10
    
    fem = int(total / 5)
    print(fem, "x 5 Kronor")
    total %= 5
    
    en = int(total / 1)
    print(en, "x 1 Krona")
    total %= 1
    
    if total < 0.25:
        total = 0
    elif 0.25 <= total < 0.75:
        total = 0.50
        print("1 x 50 öre")
    elif total >= 0.75:
        total = 1
    
    input()  # Pause before exit

if __name__ == "__main__":
    main()