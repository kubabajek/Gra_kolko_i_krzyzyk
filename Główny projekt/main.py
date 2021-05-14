import time
import os
import basicnobot
def Zliczanie():
    global ulubionytryb #nie ma go w pliku
    global zagran # nie ma go w pliku
    global uruchomien
    global t11
    global t12
    global t13
    global t21
    uruchomien=1
    ulubionytryb = 'Nieustalony'
    if os.path.exists('zliczenia.txt') == False:
        plikzliczenia = open('zliczenia.txt','w')
        plikzliczenia.write("1\n0\n0\n0\n0\n")
        plikzliczenia.close()
    plikzliczenia = open('zliczenia.txt', 'r')

    t11 =0
    t12 =0
    t13 =0
    t21 = 0





    if (t11 > max(t12,t13,t21)) :
        ulubionytryb = '3x3 z kolega'
    if (t12 > max(t11,t13,t21)) :
        ulubionytryb = '3x3 z komputerem'
    zagran = t11 + t12 + t13 + t21
def Zapis_zliczen():
    print()
def Wstep () :
    print ('\n###################################\nProfesjonalna gra w kolko i krzyzyk\n###################################')
    print ('Uruchomien:',uruchomien)
    print ('Lacznie zagranych partii:',zagran)
    print ('Ulubiony tryb gry:',ulubionytryb)
    print ('###################################')
    print ('Loading...')
    time.sleep(5)
def main() :
    Zliczanie()
    Wstep()
    tryb =1
    while (tryb != 0) :
        tryb = int(input('\n\n\n\n\n\n\nWybierz tryb gry:\n1 - Gra na planszy 3x3 \n2 - \n0 - Wyjscie\n'))
        if (tryb == 1) :
            tryb2 = int (input('Wybrales gre 3x3, wybierz rodzaj\n1 - Z kolega \n2 - Z komputerem \n0 - Cofnij\n'))
            if (tryb2 == 0) :
                print ("Cofam...")
            elif (tryb2 == 1) :
                print ('\nRozpoczynam gre na planszy 3x3 bez bota\n')
                basicnobot.main()
            elif (tryb2 == 2) :
                print ('Gra z botem niezaimplementowana') #3x3 GRA Z KOMPUTEREM TO DO
    Zapis_zliczen()
    print ('Zegnaj')
    exit(0)
if __name__ == '__main__' :
    main()
