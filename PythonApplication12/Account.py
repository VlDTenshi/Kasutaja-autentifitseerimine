from math import *
from pickle import TRUE
from random import *
from sys import *

kasutaja_list = ["kasutaja1","kasutaja2","kasutaja3"]
salasona_list = ["0987","6543","3210"]

##def registration(login:str,password:str):
##    """zadajem parametr salasona:str"""
##    """zadajem parametr kasutaja:str"""
##    while login == str(login):
##        if login in kasutaja:
##            kasutaja.append(login)
##            """
##            Tanud , te ole registris
##            """
##            if password in salasona:
##                salasona.append(password)
##                print(f'hello {login}')
##                break
##            elif password not in salasona:
##                print('incorrect password')
##                password = input('password:')
##            elif login not in kasutaja:
##                print('incorrect login:')
##                login = input("login:")
##def sign(login:str, password:str):
##    kasutaja.append(login)
##    while True:
##        if len(password)<2:
##            print('vaga nork parool')
##            break
##        elif len(password)>=2:
##            print('te olete registris')
##        return login, password



  
def salasona_loomine(p:int):
    """ See parool tehakse iseseisvalt
    :param p:int : _numb of symb_
    :param _type_: _viib tagasi uus parool_
    """
    str0 = ".,:;!_*-+()/#¤%&"
    str1 = "0123456789"
    str2 = "qwertyuiopasdfghjklzxcvbnm"
    str3 = str2.upper()
    str4 = str0+str1+str2+str3
    act = list(str4)
    shuffle(act)
    #Izvlekajem iz spiska 12 proizvolnih zna4enii
    slsona = ''.join([choice(act) for x in range(p)])
    #parol gotov
    print("Teie uus parrol on : ", slsona)
    return slsona
def kasutaja_valik():
    """ Selle funktsiooni kasutamisel saame tulemuse valik: kas sooviksime luua uus konto või siseneda juba eksisteerimisse"""
    print("Hello new/old user \n" "Choose your way:")
    while True:
        try:
            Suund = str(input("\nKui soovid teha uus konto - valige number 1 \nKui soovid siseneda - valige number 2 \nKui soovid valja minna - valige number 3\n"))
        except:
            print("Sisestage number!")
        if str(Suund) == "2":
            kasutaja_login()
        elif str(Suund) == "1":
            kasutaja_reg()
            kasutaja_login()
        elif str(Suund) =="3":
            print("Naeme sinuga natukene hiljem")
            exit()
def kasutaja_login():
    """See funktsioon teostatakse sisselogimise protsessil
    """
    kasutajanime = input("\nTere!\nPalun sisestage siia oma kasutajanime \n")
    try:
        if kasutajanime in kasutaja_list:
            b = kasutaja_list.index(kasutajanime)
            for i in range(2):
                password = input(f"\nKallis, {kasutajanime}!\nPalun, sisestage parool \n")
                if password == salasona_list[b]:
                    print("\nSisenemine aktsepteeritud")
                    break
                else:
                    print("\nprobleem parooliga",(1+i))
        else:
            for i in range(2):
                print("\nProbleem kasutajanimiga!")
                kasutajanime = input("\nSisetage veel kord oma kasutajanime\n")
                if kasutajanime in kasutaja_list:
                    b = kasutaja_list.index(kasutajanime)
                    break
                else:
                    print("\nMittekorrektne! elemendi lisamine nmbr.:", i+1)
                    if i == 2:
                        break
    except:
        print("Viga!")
def kasutaja_reg():
    """Kasutajal on voimalus luua uus konto.
    """
    kasutajanime = input("Palun , sisetage oma uus kasutajanimi \n")
    while kasutajanime in kasutaja_list:
        print("See kasutajanimi on juba kasutamisel\n")
        kasutajanime = input("Palun, sisetage uus kasutajanimi \n")
    else:
        kasutaja_list.append(kasutajanime)
    salasona = input("Kui te soovite luua uus parool vajutage nr.1,\nKui soovite siseneda oma parooliga vajutage nr.2\n")
    if salasona == "1":
        try:
            num=int(input("Sisetage initsiali hulga -->"))
        except:
            print("On vaja panna number!")
        salasona_list.append(salasona_loomine(num))
    elif salasona == "2":
        salasona = input("Sisestage uus parool \n")
        while salasona_kontroll(salasona) == False:
            salasona = input("Sisestage uus parool \n")
        if salasona_kontroll(salasona) == True:
            salasona_list.append(str(salasona))
            print("\nSinu uus parool on: ",str(salasona))
    return salasona_list
def salasona_kontroll(salasona:str):
    """See funktsioon kontrollib teie salasona
    """
    salasona = list(salasona)
    num = len(salasona)
    y = 0
    u = 0
    o = 0
    for i in range(num):
        if salasona[i].isdigit():
            y += 1
        else:
            y += 0
        if salasona[i].isupper():
            u += 1
        else:
            u += 0
        if salasona[i].isalpha()== True:
            o += 1
        else:
            o += 0
    if y > 0 and u > 0 and o > 0:
        return True
    else:
        print("Salasona peab koosnema numbrist ja suurest algustahest")
        return False

    #for i in range(k):
    #    t=choice(string.ascii_letters)
    #    num=choice([1,2,3,4,5,6,7,8,9,0])
    #    t_num=[t,str(num)]
    #    pass+=choice(t_num)
    #return pass
#def main():
#    """Funkcia generiruet login i parol i sohranjaet ih v faile."""
#    #Poluchit info o polzovatele
#    information=get_info()

#    #Na osnove polchennih dannih sgenerirovat login.
#    login = get_login(information)
#    print("Sgenerirovat dannie:")
#    print(f"login - {login}")

#    #Sgenerirovat parol
#    password = get_password(*parameters)
#    print(f"password - {password}")

#    #Zapisat info v fail
#    save_info(information, login, password)
#    print("info zapissana v fail.")
#def get_login(information):
#    """Funktsia generiruet login na osnovanii dannih o polzovatele."""
#    fullname = information['fullname']
#    name = fullname.split()
#    if len(name)==2:
#        name, firstname = name
#        shortname = f'{name}_{firstname[0]}'
#    else:
#        name, firstname, patronymic = name
#        shortname = f'{name}_{firstname[0]}{patronymic}'
#        login="name"
#    return login
#A_B_C= 'AaBbCcDdEEFfGgHhIiJjKkLlMmNnPpQqRrSsTtUuVvWwXxYyZz'
#NUMBERS = '0123456789'
#SYMBOLS = A_B_C + NUMBERS
#def get_password(A_B_C, SYMBOLS):
#    """Funkcija generiruet parol iz 8 simvolov"""
#    #Sgenerirovat parol v cikle s ispolzovaniem global konstant
#    repeat = Truepassword=''
#    while repeat:
#        password = ''
#        password += A_B_C[random.randint(0,49)]
#        for _ in range (7):
#            password += SYMBOLS[random.randint(0,59)]
#        repeat = check_password(password)
#    return password
#def check_password(password):
#    """Funktsia proverjaet trebovanie k parolju"""
#    #Opredelit peremennie dlja proverki nalicjija v parole cifr,
#    #Strocnih i propisnih bukv
#    is_digit = False
#    is_lower = False
#    is_upper = False
#    #proverit nalichie v parole trebuemih simvolov
#    for symbol in password:
#        if symbol.isdigit():
#            is_digit = True
#        elif symbol.islower():
#            is_lower = True
#        elif symbol.isupper():
#            is_upper = True
#    is_not_valid = True
#    if is_digit and is_lower and is_upper:
#        is_not_valid = False
#    return is_not_valid
#def get_info():
#    """Funktsija poluchajet ot polzovatelei korrektnuju info o polzovatele"""
#    #Poluchit dannie o polzovatele i proverit ih na korrektnost vvoda
#    try:
#        fullname = input('Insert here your name:').split()
#        information = {'fullname':fullname}
#    except (ValueError):
#        #V sluchae oshibki povtoritsja vvod dannih
#        print('Dannie vvedeni neverno! vesti zanovo.')
#        return Error
#    else:
#        #Vernut slovar s dannimi
#        return information
#def save_info(information, login, password):
#    fullname = information['fullname']
#    w_info = [fullname]
#    cur_datetime = datetime.now()
#    w_datetime = f'{cur_datetime.year}-{cur.datetime.month}-{cur.datetime.day}'
#    with open(f'logins_{w_datetime}.csv','a') as file:
#        writer = csv.writer(file)
#        writer.writerow(w_info)
