import json

FILENAME = "konyvek.json"


def betolt_konyvek():
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return []


def mentes_konyvek(konyvek):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(konyvek, file, indent=4, ensure_ascii=False)


def uj_konyv(konyvek):
    cim = input("Cím: ")
    szerzo = input("Szerző: ")
    ev = input("Kiadási év: ")

    konyv = {
        "cim": cim,
        "szerzo": szerzo,
        "ev": ev
    }

    konyvek.append(konyv)
    print("Könyv hozzáadva!")


def listaz(konyvek):
    if not konyvek:
        print("Nincs könyv.")
        return

    for i, k in enumerate(konyvek, 1):
        print(f"{i}. {k['cim']} - {k['szerzo']} ({k['ev']})")


def keres(konyvek):
    kulcs = input("Keresés cím alapján: ").lower()

    talalatok = [k for k in konyvek if kulcs in k["cim"].lower()]

    for k in talalatok:
        print(f"{k['cim']} - {k['szerzo']} ({k['ev']})")

    if not talalatok:
        print("Nincs találat.")


def torol(konyvek):
    listaz(konyvek)
    index = int(input("Törlendő könyv száma: ")) - 1

    if 0 <= index < len(konyvek):
        torolt = konyvek.pop(index)
        print(f"Törölve: {torolt['cim']}")
    else:
        print("Hibás index!")


def menu():
    konyvek = betolt_konyvek()

    while True:
        print("\n--- Könyvtár ---")
        print("1. Új könyv")
        print("2. Listázás")
        print("3. Keresés")
        print("4. Törlés")
        print("5. Kilépés")

        valasz = input("Választás: ")

        if valasz == "1":
            uj_konyv(konyvek)
        elif valasz == "2":
            listaz(konyvek)
        elif valasz == "3":
            keres(konyvek)
        elif valasz == "4":
            torol(konyvek)
        elif valasz == "5":
            mentes_konyvek(konyvek)
            print("Mentve. Kilépés...")
            break
        else:
            print("Hibás választás!")


menu()