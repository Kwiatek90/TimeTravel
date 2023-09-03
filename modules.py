import sys
import pathlib

from classes import *

def play_first_room():
    while True:
        print(r"Wybierz gdzie chcesz podejśc: \tablica, \stol, \maszyna, \wlaz")
        choose =  input()
        if choose == r"\tablica":
            board.opis()
            choosing_menu()
        elif choose == r"\stol":
            file_reader("table_des.txt")
            play_table()
        elif choose == r"\maszyna":
            file_reader("machine_des.txt")
            play_machine()
        elif choose == r"\wlaz":
            enter_wlaz()
        else:
            print("Źle")
            continue
        
def play_second_room():
    while True:
        print(r"Wybierz gdzie chcesz podejśc: \telefon,  \kufer, \maszyna_czasu, \ksiega, \waga, \szkatulka, \wlaz")
        choose = input()
        if choose == r"\telefon":
            file_reader("telephone_des.txt")
            play_telephone()
        elif choose == r"\kufer":
            file_reader("kufer_des.txt")
            play_kufer()
        elif choose == r"\maszyna_czasu":
            file_reader("time_machine_des.txt")
            play_time_machine()
        elif choose == r"\ksiega":
            file_reader("book_des.txt")
            play_book()
        elif choose == r"\waga":
            file_reader("scales_des.txt")
            play_scales()
        elif choose == r"\szkatulka":
            file_reader("book_des.txt")
            play_casket()
        elif choose == r"\wlaz":
            player.go_room_first()
            print("Przechodzisz do Tajemniczego pokoju\n")
            play_first_room()
        else:
            print("Źle")
            continue
def help_command(): #dopracować
    print("\nDostępne komendy:\n" 
          + r"\use - użyj przedmiotu" + "\n"
          + r"\get - zabierz przedmiotu" + "\n"
          + r"\ekwipunek - wyświetli listę przedmiotów dostępnych w twoim ekwipunku" + "\n"
          + r"\pomoc - wyświetli listę dostępnych instrukcji " + "\n"
          + r"\opisz - opisuje aktualne miejsce" + "\n"
    )
    
def file_reader(file_txt):
    path = pathlib.Path.cwd() / "Descriptions" / file_txt
    with open(path, mode="r", encoding="utf-8") as f:
        text = f.read()
        print(text)
        
def choosing_menu():
    while True:
        print("\nCo dalej?")
        print(r"\ekwipunek \pomoc \wyjdz")
        choose_menu = input()
        if choose_menu == r"\use":
            return r"\use"
        elif choose_menu == r"\get":
            return r"\get"
        elif choose_menu == r"\ekwipunek":
            player.show_backpack()
        elif choose_menu == r"\opis":
            return r"\opis"
        elif choose_menu == r"\pomoc":
            help_command()
            continue
        elif choose_menu == r"\wyjdz":
            print("\nWracasz na środek pokoju")
            if player.active_room == 0:
                play_first_room()
            elif player.active_room == 1:
                play_second_room()
        else:
            print("Źle!")
            continue

def str_to_class(str):
    return getattr(sys.modules[__name__], str)
                
def play_table():
    while True:    
        option = choosing_menu()
        if option == r"\use":
            print("Podaj rozwiązanie tej zagadki:\n")
            solution = input()
            if solution == table.solution:
                print("Po wpisaniu hasła, nagle właz się poruszył, być może się otworzyl?")
                player.add_level()
                continue
            else:
                print("Błedna odpowiedz")######################dodac opcje kiedy hasło zostało odgadnięte
                
def play_machine():
    while True:
        option = choosing_menu()
        if option == r"\use":
            throw = input("Wrzuć medaliony do maszyny: ")
            if throw == "Czarny medalion" or  throw == "Zielony medalion" or  throw == "Żółty medalion" or  throw == "Niebieski medalion":    
                for item in player.backpack:
                    if throw == item.name:  
                        if len(machine.content_of_the_machine) <= 3:
                            machine.content_of_the_machine.append(item)
                            player.backpack.remove(item)
                            print("Medalion został dodany do twojej maszyny")
                            continue
                        else:
                            print("Wygrałeś")
            else:
                print("Źle wpisany przedmiot!")
                continue
        if option == r"\get":
            file_reader("machine_des2.txt")
            play_machine()
            
def enter_wlaz():
    if player.level == 0:
        print("Właz jest zamknięty")
        play_first_room()
    elif player.level == 1:
        file_reader("entry_wlaz.txt")
        player.go_room_second()
        play_second_room()
                
def play_telephone():
    while True:
        option = choosing_menu()
        if option == r"\use":
            print("Wykręć numer telefonu na kole: \n")
            solution = input()
            if solution == str(telephone.password):
                print("Dryyyyn, dryyyn\n"
                    + "Telefon zaczął dzwonić w daleką czasoprzestrzeń\n"
                    + "Po chwili z odpowietrznika maszyny wypadł klucz na ziemie")
                key.actived()
            else:
                print("Po przekręceniu koła nic się nie dzieje")
                continue
        elif option == r"\get":
            if key.active == 1:
                print("Zdobyłeś klucz!")
                player.add_backpack(key)
            else: 
                continue
        elif option == r"\opis":
            file_reader("telephone_des.txt")
            continue
        else:
            print("Źle")
            continue

def play_kufer():
    while True:
        option = choosing_menu()
        if option == r"\use":
            if player.check_item(key): # mozna zebrac dwa razy modul 
                print("Po użyciu klucza z twojego ekwipunku otwiera się szkatułka!\n"
                    + "Patrząc do środka zauważyć można coś na podobę modułu,\n"
                    + "który może zostać użyty do budowy czegoś")
                module.actived()
            else:
                print("Szkatułka jest zamknięta")
        elif option == r"\get":
            if module.active == 1 and module not in player.backpack: #przetestować
                print("Moduł został dodany do twojego ekwipunku!")
                player.add_backpack(module)
            else: 
                continue
        elif option == r"\opis":
            file_reader("kufer_des.txt")
            continue
        else:
            print("Źle")
            continue
        
def play_time_machine():
    while True:
                option = choosing_menu()
                if option == r"\use":
                    if player.check_item(module):
                        print("Umieszczasz w maszynie modul czasu. Maszyna zaczyna się trząść, wibrować\n"
                              + "Nagle utworzył się portal w maszynie z któego wyskoczył niebieski\n "
                              + "medalion zamykając portal za sobą\n")
                        blue_medalion.actived() 
                    else:
                        print("Maszyna zaczyna pracować, lecz po chwili wydobywa się buczenie z silnika\n"
                              + "i maszyna się wyłącza\n")
                elif option == r"\get":
                    if blue_medalion.active == 1:
                        print("Niebieski medalion został dodany do Twojego ekwipunku!")
                        player.add_backpack(blue_medalion)
                    else:
                        continue
                elif option == r"\opis":
                    file_reader("time_machine_des.txt")
                    continue
                else:
                    print("Nie ma takiej komendy")
                    continue
                
def play_book():
    while True:
        option = choosing_menu()
        if option == r"\use":
            print("Podaj rozwiązanie tej zagadki:\n")
            solution = input()
            if solution == book.solution:
                print("Po wpisaniu imienia w księge czasu nagle pojawia się z niej światło\n"
                        + ",które otwiera nową stronę w księdze ukazującą ciąg liczb zapisanych na kartce\n"
                        + "Kartke można zabrać do ekwipunku"
                        + "Po chwili księga się zamyka na zatrzask i wypada z niej medalion!")
                paper.actived()
                green_medalion.actived()
            else:
                "Po wpisaniu rozwiązania nic się nie dzieje, spróbuj ponownie!\n"
                continue
        elif option == r"\get":
            if green_medalion.active == 1 :
                    print("Zielony medalion i kartka z cyframi został dodany do Twojego ekwipunku!")
                    player.add_backpack(green_medalion)
                    player.add_backpack(paper)
            else:
                continue
        elif option == r"\opis":
            file_reader("book_des.txt")
            continue
        else:
            print("Nie ma takiej komendy")
            continue

def play_scales():
    while True:
        option = choosing_menu()
        if option == r"\use":
            while True:
                if scales.doors == "closed":
                    weight = float(input("Podaj jaki ciężar chcesz postawić/zdjąć z wagi?\n"))
                    if weight == 5 or weight == 2 or weight == 1 or weight == 0.5:
                        pass
                    elif weight == "\wyjdz":
                        play_second_room()
                    else:
                        print("Żle podana waga!")
                        continue
                    
                    akcja = str(input("Chcesz zdjąć czy postawić ciężar? ( dodaj/zdejmij )\n"))
                    if akcja == "dodaj":
                        scales.weights += weight
                    elif akcja == "zdejmij":
                        scales.weights -= weight
                    elif akcja == "\wyjdz":
                        play_second_room()
                    else:
                        print("Błąd słowa")
                        continue
                    
                    scales.check()
                else:
                    print("Waga jest zrówna i drzwiczki są otwarte!")
                    play_scales()
        elif option == r"\get":
            if scales.doors == "open" and yellow_medalion not in player.backpack:  #dodac to do pozostałych
                player.add_backpack(yellow_medalion)
                player.add_backpack(bonaparte)
                player.add_backpack(mandela)
                player.add_backpack(szekspir)
                player.add_backpack(kleopatra)
                print("Do twojego ekipunku zostaly dodane figurki oraz żółty medalion!")
                continue
            else:
                continue
        elif option == r"\opis":
            file_reader("scales_des.txt")
        else:   
            print("Nie ma takiej komendy")
            continue
            
def play_casket():
    while True:
        option = choosing_menu()
        if option == r"\use":
            if casket.casket_open_close == "close":
                print("Szyfr znajdujący się na szkatułce to:\n "
                      + "AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ\n"
                      + "Wbąp")
                solution = input("Powiedz jakie jest rozwiązanie tego szyfru: \n")
                if solution == casket.solution:
                    print("Po złamaniu szyfru szaktułka magicznie się otwiera\n"
                          + "Patrząc do środka widzimi 4 miejsca na figurki.\n" 
                          + "Na lewej stronie szkatułki napisane jest: 'Najstarsza z postaci'")
                    casket.open_casket()
            else:
                print("Widzimy otwartą szkatułkę\n"
                      + "Spróbuj ułożyc figurki chronologicznie\n")  
                while True: 
                    character = input("Wpisz nazwę figurki: \n")
                    try:         
                        character = str_to_class(character)
                    except:
                        print("Nie masz takiej figurki!")
                        continue
                    if len(casket.content_of_the_casket) <= 3:
                        character_add_casket(character)
                        continue
                    else:
                        casket.check_characters()
                        play_casket()
        elif option == r"\get":
            if black_medalion.active == 1:
                player.add_backpack(black_medalion)
                machine.actived()
            else:
                print("Nic się nie dzieje")
                continue
        elif option == r"\opis":
            file_reader("casket_des.txt")
            continue
                
def character_add_casket(character):        
    if character in player.backpack:
        casket.content_of_the_casket.append(character)
        player.backpack.pop(character)
    else:
        print("Figurka znajduję się już w szkatułce")