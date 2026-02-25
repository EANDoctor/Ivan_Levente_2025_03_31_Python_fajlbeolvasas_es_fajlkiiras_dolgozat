"""
Olvasd be az f1.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány versenyző szerepel a fájlban?
2. Melyik versenyző nyerte a legtöbb futamot?
3. Melyik versenyző nyerte a legkevesebb futamot?
4. Ki teljesítette a legtöbb futamot?
5. Átlagosan hány futamot teljesítettek a versenyzők?"

***EXTRA - nehezebb feladat*** (nem kötelező, de érdemes megpróbálni):
6. Melyik csapat szerezte a legtöbb futamgyőzelmet?

A megoldott feladatokat a kiirt_adatok nevű mappába hozd létre statisztika.txt néven!
"""


# File beolvasás ---------------------------------------------------------------
forma1 = []
with open('beolvasando_adatok/f1.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        f1 = {'Név': adatok[0], 'Csapat': adatok[1], 'Győzelmek száma': adatok[2],'Teljesített futamok száma': adatok[3]}
        forma1.append(adatok)
print(forma1)

# 1.Feladat -------------------------------------------------------------------

for f1 in forma1:
    print(f1[0])
print(f"Összesen {len(forma1)} versenyző szerepel.")


# 2.Feladat -------------------------------------------------------------------

legtobb_nyert_futam_szama = 0
legtobb_nyert_futam = forma1
for f1 in forma1:
    if int(f1[2]) > legtobb_nyert_futam_szama:
        legtobb_nyert_futam_szama = int(f1[2])
        legtobb_nyert_futam = f1[0]


print(f"Legtöbb futamot nyert versenyző: {legtobb_nyert_futam}")

# 3.Feladat -------------------------------------------------------------------

legkevesebb_nyert_futam_szama = int(forma1[0][2])
legkevesebb_nyert_futam = forma1[0][0]
for f1 in forma1:
    if int(f1[2]) < legkevesebb_nyert_futam_szama:
        legkevesebb_nyert_futam_szama = int(f1[2])
        legkevesebb_nyert_futam = f1[0]

print(f"Legkevesebb futamot nyert versenyző: {legkevesebb_nyert_futam}")

# 4.Feladat -------------------------------------------------------------------

legtobb_teljesitett_futam_szama = 0
legtobb_teljesített_futam = forma1
for f1 in forma1:
    if int(f1[3]) > legtobb_teljesitett_futam_szama:
        legtobb_teljesitett_futam_szama = int(f1[3])
        legtobb_teljesített_futam = f1[0]

print(f"Legtöbb futamot teljesített versenyző: {legtobb_teljesített_futam}")

# 5.Feladat -------------------------------------------------------------------

atlagos_futamszam = 0
for f1 in forma1:
    atlagos_futamszam += int(f1[3])
atlagos_futamszam /= len(forma1)

print(f"Átlagos futamszám: {atlagos_futamszam}")

# Végső statisztika:
with open('kiirt_adatok/statisztika.txt', 'w', encoding='utf8') as c:
    c.write(f"1. A beolvasott fájlban összesen {len(forma1)} versenyző szerepel.\n")
    c.write(f"2. A legtöbb futamot nyert versenyző: {legtobb_nyert_futam}\n")
    c.write(f"3. A legkevesebb futamot nyert versenyző: {legkevesebb_nyert_futam}\n")
    c.write(f"4. A legtöbb futamot teljesített versenyző: {legtobb_teljesített_futam}\n")
    c.write(f"5. Az átlagos futamszám: {atlagos_futamszam}")