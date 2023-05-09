import os
import random as r
import time as vaqt










def sevgi_test():
    """Sevgi test"""
    global son
    global ishora


son = r.randint(10, 100)
ishora = True
while ishora:

    ism = str(input("Sevganingizni ismini kiriting\n: "))
    ism2 = str(input("O'zingizni ismingizni kiriting\n: "))

    if ism == int:
        ishora = False
    if ism == 'stop':
        ishora = False
    print("Tekshirilmoqda.... ")
    vaqt.sleep(2)
    print("[💝💝                   5%]")

    vaqt.sleep(2)
    os.system('cls')
    print("[💝💝💝💝             20%]")
    vaqt.sleep(2)
    os.system('cls')
    print("[💝💝💝💝💝💝        40%]")
    vaqt.sleep(2)
    os.system('cls')
    print("[💝💝💝💝💝💝💝💝   86%]")
    vaqt.sleep(2)
    os.system('cls')
    print("[💝💝💝💝💝💝💝💝💝 99%]")

    vaqt.sleep(2)
    os.system('cls')
    print("[💝💝💝💝💝💝💝💝💝100%]")

    vse = f"{ism} bilan {ism2}ning o'xshashlik darajasi {son}%"
    if son > 50:
        print("Tabriklayman sizlarning sevgilaring mustahkam ekan!")
        print(vse)
        print(f"{ism} sizni sevadi..")

        f = open("sevgi_info.txt", "w")
        f.write(f"{ism} + {ism2} = SEVGI\nHar doim birga bo'ling!\n{vse}")
        f.close()
        ishora = False
    if son < 50:
        print("Sevgilaringni extiyot qilinglar...")
        print(vse)
        print(f"{ism} sizni sevadi!")

        f = open("sevgi_info.txt", "w")
        f.write(f"{ism} + {ism2} = SEVGI\nHar doim birga bo'ling!\n{vse}")
        f.close()
        ishora = False
    if son == 10:
        print("Sizlarga gapim yo'q")
        print(vse)
        print(f"{ism} + {ism2} = SEVGI")

        f = open("sevgi_info.txt", "w")
        f.write(f"{ism} + {ism2} = SEVGI\nHar doim birga bo'ling!\n{vse}")
        f.close()
        ishora = False
    if ism == 'clear':
        os.system("cls")


def sevgim():
        """Main function"""

        global ism
        global ism2
        print(f"{ism} + {ism2} = SEVGI")


def info():
    """O'xshashlik darajasi"""


    print(f"{ism} bilan {ism2}ning o'xshashlik darajasi {son}%")


def restart():
    """Qayta yuklash"""
    os.system("python app.py")