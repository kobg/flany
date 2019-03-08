import os

from zawodnik import Zawodnik
import csv
import random

def losowanie_druzyn():
    druzyny = []
    f = open('druzyny.txt', 'r')
    while True:
        line = f.readline()
        l = line.strip('\n')
        if not line:
            f.close()
            break
        druzyny.append(l)
    d1 = random.randint(0,3)
    d2 = random.randint(0,3)
    while d1==d2:
        d2 = random.randint(0,3)

    return druzyny[d1],druzyny[d2]

def przeciwnicy():
    team1sq = []
    team2sq = []
    sparing = losowanie_druzyn()
    team1 = sparing[0]
    team2 = sparing[1]
    with open('zawodnicy.txt', newline='') as f:
        zawodnicy = csv.reader(f, delimiter = ';')

        for zawodnik in zawodnicy:
            nowy = Zawodnik(zawodnik[0], zawodnik[1], zawodnik[2], zawodnik[3], zawodnik[4], zawodnik[5], zawodnik[6])
            if (nowy.druzyna == team1):
                team1sq.append(nowy)
            elif (nowy.druzyna == team2):
                team2sq.append(nowy)
    return [team1sq,team2sq]


def tabela(array):
    for el in array:
        print("==========================")
        for elem in el:
            print(elem.imie," | ",elem.druzyna," | ",elem.zawartosc_butelki)


def gra(teams):
    zaczynajacy = random.randint(2,4)
    return zaczynajacy


def main():
    grajacy = przeciwnicy()
    team1count = 0
    team2count = 0
    team1name = grajacy[0][0].druzyna
    team2name = grajacy[1][0].druzyna
    x =  gra(grajacy)
    t1y = 0
    t2y = 0
    runda = 0
    while True:
        runda += 1
        #print(runda)
        input()
        os.system("cls")
        if(x%2==0):
            t1y +=1
            print("t1y",t1y)
            if t1y > len(grajacy[0]):
                t1y = 1
            if grajacy[0][t1y-1].rzut() == True:
                for elem in grajacy[0]:
                    elem.picie(random.randint(30,60))
                    if elem.skonczyl_grac() == True:
                        grajacy[0].remove(elem)
                        team1count += 1


        else:

            t2y += 1
            print("t2y",t2y)
            if t2y > len(grajacy[0]):
                t2y = 1
            if grajacy[1][t2y - 1].rzut() == True:
                for elem in grajacy[1]:
                    elem.picie(random.randint(30,60))
                    if elem.skonczyl_grac() == True:
                        grajacy[1].remove(elem)
                        team2count += 1

        if team1count == 5:
            print(team1name,"WYGRALA")
            input()
            break
        if team2count == 5:
            print(team2name, "WYGRALA")
            input()
            break
        tabela(grajacy)
        x += 1





main()