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
    plikzliczenia = open('zliczenia.txt', 'w')
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
                Zapis_zliczen()
            elif (tryb1 == 2) :
                print ('Rozpoczynam gre na planszy 3x3 z botem')
                global t12
                t12+=bot3x3.main()
                Zapis_zliczen()
            elif (tryb1 == 3) :
                print ('Rozpoczynam gre na planszy 3x3 bez bota na czas')
                global t13
                t13+=bot3x3.main() #BEZ BOTA NA CZAS 3x3 NAZWA PLIKU DO DODANIA!!!!!!!
                Zapis_zliczen()
            elif (tryb1 == 4) :
                print ('Rozpoczynam gre na planszy 3x3 z botem na czas')
                global t14
                t14+=bot3x3.main() #Z BOTEM NA CZAS 3x3 NAZWA PLIKU DO DODANIA!!!!
                Zapis_zliczen()
        if (tryb == 2) :
            print ('\nRozpoczynam gre na planszy 4x4\n')
            global t21
            t21+= nobot4x4.main()

        if (tryb == 3) :
            print ('\nRozpoczynam gre na planszy 5x5\n')
            global t31
            t31+= nobot5x5.main()
            Zapis_zliczen()

    print ('Zegnaj')
    exit(0)


if __name__ == '__main__':
    main()