#Python orqali Exel birlashtirish
import os
import time as vaqt
import random as r



#Ishni osonlashtiradi

#100% samarali
#Yordamchi extection hosil bo'lai

#
#
ishora = True
while ishora:


    print("***************************************************")
    print("* :1: SEVGI TEST                                  *")
    print("* :2: Sevgim                                      *")
    print("* :3: Qayta yuklash                               *")
    print("* :4: Info                                        *")
    print("* :5: Dasturchi                                   *")
    print("* :6: Chiqish                                     *")
    print("*                                                 *")
    print("*                                                 *")
    print("*                                                 *")
    print("***************************************************")

    main = int(input("Tanlang: "))
    if main == 1:
            print("Please wait....")
            vaqt.sleep(3)

            from test import sevgi_test
            sevgi_test()


    if main == 2:
        print("Loading main files...")
        vaqt.sleep(3)

        from test import sevgim
        sevgim()

    if main == 3:
        print("5 sekunda qayta yuklanadi..")
        print("Iltimos kuting..")
        vaqt.sleep(4)
        from test import restart
        restart()
    if main == 4:
        print("Ma'lumotlar ko'rib chiqilmoqda..")
        from  test import info
        info()

    if main ==5:
        print("Yaratuvchi: Asadbek Abdubannopov\n"
              "Tel: +998(99)635-8714\n"
              "Telegram: @coder_18_03\n"
              "Yaratilgan vaqt: 03.20.2023\n"
              "All rights reserved\n"
              "Ushbu dastur orqali o'z sevgingizni o'lchashingiz mumkin\n"
              "Diqqat! Buning hammasi tasodif..")

    if main == 6:
        print("Dasturdan chiqilmoqda!")
        print("Iltimos kuting..")
        vaqt.sleep(3)
        ishora = False
        os.system('cls')
        os.system('exit')
    if main == '19041803':
        print("***************************************************")
        print("*        ________        ________                 *")
        print("*       /        \      /          |              *")
        print("*      /          \    /           /              *")
        print("*      |            \/            /               *")
        print("*       \                        /                *")
        print("*        \                      /                 *")
        print("*          \                   /                  *")
        print("*           \                 /                   *")
        print("*             \              /                    *")
        print("*              \____________/                     *")
        print("*            SEVISHGANLA PANELI                   *")
        print("*                                                 *")
        print("*                                                 *")
        print("***************************************************")
        tox = True
        while tox:
            password = str(input("Secure pass code: "))
            if password == 'marjonam':
                print("Your password succesful!")
                sekret = str(input(""))
            else:
                print("Xato!")
                tox = False