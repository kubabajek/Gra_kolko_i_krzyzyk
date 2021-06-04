import time
import os
import basicnobot
import nobot4x4
import nobot5x5
import bot3x3
def Zliczanie():
    global ulubionytryb #nie ma go w pliku
    global zagran # nie ma go w pliku
    global uruchomien
    global t11
    global t12
    global t21
    global t22
    global t31
    global t32
    ulubionytryb = 'Brak, pokaze sie wkrotce =]'
    if os.path.exists('zliczenia.txt') == False:
        plikzliczenia = open('zliczenia.txt','w') #STRUKTURA PLIKU: uruchomien, kolejnetryby11, 12, 13, 21, 22 ... wszystko w innych wierszach
        plikzliczenia.write("1\n0\n0\n0\n0\n0\n0")
        plikzliczenia.close()
    plikzliczenia = open('zliczenia.txt', 'r')
    linie=plikzliczenia.readlines()
    plikzliczenia.close()
    uruchomien=int(linie[0])
    t11=int(linie[1])
    t12=int(linie[2])
    t21=int(linie[3])
    t22=int(linie[4])
    t31=int(linie[5])
    t32=int(linie[6])

#Ustalanie ulubionego trybu gry
    if (t11 > max(t12,t21,t22,t31,t32)) :
        ulubionytryb = '3x3 z kolega'
    if (t12 > max(t11,t21, t22,t31,t32)) :
        ulubionytryb = '3x3 z komputerem'
    if (t21 > max(t11, t12, t22,t31,t32)) :
        ulubionytryb = '4x4 z kolega'
    if (t22 > max(t11, t12, t21,t31,t32)) :
        ulubionytryb = '4x4 z komputerem'
    if (t31 > max(t11, t12, t21,t22,t32)) :
        ulubionytryb = '5x5 z kolega'
    if (t32 > max(t11, t12, t21,t22,t31)) :
        ulubionytryb = '5x5 z komputerem'
    zagran = t11 + t12 + t21 + t22 + t31 + t32
def Zapis_zliczen():
    plikzliczenia = open('zliczenia.txt','w')
    plikzliczenia.write(str(uruchomien+1))
    plikzliczenia.write("\n")
    plikzliczenia.write(str(t11))
    plikzliczenia.write("\n")
    plikzliczenia.write(str(t12))
    plikzliczenia.write("\n")
    plikzliczenia.write(str(t21))
    plikzliczenia.write("\n")
    plikzliczenia.write(str(t22))
    plikzliczenia.write("\n")
    plikzliczenia.write(str(t31))
    plikzliczenia.write("\n")
    plikzliczenia.write(str(t32))
    plikzliczenia.close()
def Wstep () :
    print ('\n###################################\nProfesjonalna gra w kolko i krzyzyk\n###################################')
    print ('Uruchomien:',uruchomien)
    print ('Lacznie zagranych partii:',zagran)
    print ('Ulubiony tryb gry:',ulubionytryb)
    print ('###################################')
    print ('Loading...')
    time.sleep(5)
    print("\n\n\n\n\n\n\n\n")
def main() :
    Zliczanie()
    Wstep()
    tryb =1
    while (tryb != 0) :
        tryb = int(input('\nWybierz tryb gry:\n1 - Gra na planszy 3x3 dodatkowe funkcjonalnosci \n2 - Gra na planszy 4x4 w dwie osoby\n3 - Gra na planszy 5x5 w dwie osoby\n0 - Wyjscie\n'))
        if (tryb == 1) :
            tryb1 = int (input('Wybrales gre 3x3, wybierz rodzaj\n1 - Z kolega \n2 - Z komputerem \n 3 - Z kolega na czas\n4 - Z komputerem na czas\n0 - Cofnij\n'))
            if (tryb1 == 0) :
                print ("Cofam...")
            elif (tryb1 == 1) :
                print ('\nRozpoczynam gre na planszy 3x3 bez bota\n')
                global t11
                t11+=basicnobot.main()
            elif (tryb1 == 2) :
                print ('Rozpoczynam gre na planszy 3x3 z botem')
                global t12
                t12+=bot3x3.main()
            elif (tryb1 == 3) :
                print ('Rozpoczynam gre na planszy 3x3 bez bota na czas')
                global t13
                t13+=bot3x3.main() #BEZ BOTA NA CZAS 3x3 NAZWA PLIKU DO DODANIA!!!!!!!
            elif (tryb1 == 4) :
                print ('Rozpoczynam gre na planszy 3x3 z botem na czas')
                global t14
                t14+=bot3x3.main() #Z BOTEM NA CZAS 3x3 NAZWA PLIKU DO DODANIA!!!!


        if (tryb == 2) :
            tryb2 = int (input('Wybrales gre 4x4, wybierz rodzaj\n1 - Z kolega \n2 - Z komputerem \n0 - Cofnij\n'))
            if (tryb2 == 0) :
                print ("Cofam...")
            elif (tryb2 == 1) :
                print ('\nRozpoczynam gre na planszy 4x4 bez bota\n')
                global t21
                t21+= nobot4x4.main()
            elif (tryb2 == 2) :
                print ('Gra z botem niezaimplementowana') #4x4 GRA Z KOMPUTEREM TO DO
                global t22
                t22+=1

        if (tryb == 3) :
            tryb3 = int (input('Wybrales gre 5x5, wybierz rodzaj\n1 - Z kolega \n2 - Z komputerem \n0 - Cofnij\n'))
            if (tryb3 == 0) :
                print ("Cofam...")
            elif (tryb3 == 1) :
                print ('\nRozpoczynam gre na planszy 5x5 bez bota\n')
                global t31
                t31+= nobot5x5.main()
            elif (tryb3 == 2) :
                print ('Gra z botem niezaimplementowana') #5x5 GRA Z KOMPUTEREM TO DO
                global t32
                t32+=1
    Zapis_zliczen()
    print ('Zegnaj')
    exit(0)


if __name__ == '__main__':
    main()