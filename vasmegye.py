# 1-980227-1258

#3. feladat
def CdvE11(szám):
    '''Ez egy személyi szám ellenőrző függvény, amely helyes szám esetén True értékkel tér vissza.'''
    s = szám.replace('-','')
    if not (len(s) == 11):
        return False
    if not s.isnumeric():
        return False
#    summa = 10*int(s[0])+9*int(s[1])+8*int(s[2])+7*int(s[3])+6*int(s[4])+5*int(s[5])+4*int(s[6])+3*int(s[7])+2*int(s[8])+1*int(s[9])
    summa = 0
    for i in range(10):
        summa += (10-i) * int(s[i])
    k11 = summa % 11
    return k11 == int(s[10])

def évszám(s):
    if s[0] == '1' or s[0] == '2':
        század = 1900
    else:
        század = 2000
    év = század + int(s[1:3])
    return év

#1-2. feladat
with open('vas.txt', 'r') as f:
    nyers = [sor.strip().replace('-','') for sor in f]
    
#4. feladat
print(        f'4. feladat: Ellenőrzés')
matrix = []
for sor in nyers:
    if CdvE11(sor):
        matrix.append(sor)
    else:
        print(f'        Hibás a {sor[0]}-{sor[1:7]}-{sor[7:]} személyi azonosító!')
        
#5. feladat
print(f'5. feladat: Vas megyében a vizsgált évek alatt {len(matrix)} csecsemő született.')

#6. feladat
fiu = 0
for sor in matrix:
    if sor[0] == '1' or sor[0] == '3':
        fiu += 1
print(f'6. feladat: Fiúk száma: {fiu}')

#7. feladat
halmaz = set()
for sor in matrix:
    év = évszám(sor)
    halmaz.add(év)
print(f'7. feladat: Vizsgált időszak: {min(halmaz)}-{max(halmaz)}')

#8. feladat
for sor in matrix:
    év = évszám(sor)
    szökőév = év % 4 == 0
    szökőnap = sor[3:7] == '0224'
    if  szökőév and szökőnap:
        print(f'8. feladat: Szökőnapon született baba!')
        break
    
#9. feladat
print(f'9. feladat: Statisztika')
szotar = dict()
for sor in matrix:
    év = évszám(sor)
    szotar[év] = 0
    
for sor in matrix:
    év = évszám(sor)
    szotar[év] += 1

for ev, db in szotar.items():
    print(f'            {ev} - {db} fő')
    









    