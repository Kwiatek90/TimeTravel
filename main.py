class Player():
    level = 0 
    active_room = 1
    
    def __init__(self):
        self.backpack = []
    
    @classmethod
    def add_level(cls):
        cls.level += 1
     
    @classmethod   
    def go_room_first(cls):
        cls.active_room -= 1
    
    @classmethod
    def go_room_second(cls):
        cls.active_room += 1
         
    def show_backpack(self):
        print(f"Twoje przedmioty w ekwipunku:")
        for item in self.backpack:
            print(item.name)
    
    def add_backpack(self, item):
        self.backpack.append(item)
        
    def check_item(self, item):
        if item in self.backpack:
            return True
        else:
            return False
    

#klasa z pomieszczeniami ogólna

class Furniture():
    description = "Znajdujesz się przy"
    
    def __init__(self, name):
        self.name = name
        
    def opis(self):
        print(self.description + f"{self.name}")
        

        
   
        

#klasa z pomieszczeniami
class Board(Furniture):
    def __init__(self, name, year, telephon_number):
        super().__init__(name)
        self.year = year
        self.telephone_number = telephon_number
        Telephone.telephone_solution(telephon_number)
        
        
    def opis(self):
        print(f"\nPodchodząc pod ściane zauważasz tablicę.\n"
              + f"Znajdują się na niej liczby. Przypatrując się bardziej\n"
              + f"widzisz ciąg liczb {self.year}|{self.telephone_number}")

    
class Table(Furniture):
    def __init__(self, name, solution):
        super().__init__(name)
        self.solution = solution
        
    def opis(self):
        print(f"\nNa stole leży stary, zżółkły pergamin.\n"
              + "'Przez ocean żeglarz dzielny,\n"
              + "Nowe lądy odkrył ciekawy,\n"
              + "Amerykę znalazł pewnego dnia,\n"
              + "Nazwisko jego brzmi jak...?'\n"
              + "Pod tekstem znajduję się klawiatura, a nad nią mały ekran\n" 
              + "ktory wyświetla wpisane litery przez klawiaturę\n"
        )
              
      
class Machine(Furniture):
    #tablica do wrzucania monet
    def __init__(self, name):
        super().__init__(name)
        
    def opis(self):
        print(f"\nMaszyna jest największym elementem pomieszczenia. Jej konstrukcja przypomina\n"
            + "kombinację zegara, urządzenia muzycznego i maszyny do gry. Skomplikowane rury i\n"
            + "przewody prowadzą do różnych sekcji, a każdy element jest zdobiony symbolami\n"
            + "związanymi z podróżami w czasie.\n")
     
    def get(self):
        print("Przechodzisz zza maszynę, widzisz na niej instrukcję obsługi:\n"
              + "Musisz odnależć medaliony, by dostosować maszynę w odpowiedni sposób i\n"
              + "aktywować magiczne pole energii, które umożliwi Ci podróż w czasie!\n"
              + "Aby to osiągnąć, musisz zidentyfikować właściwe wzorce i sekwencje, które reprezentują różne okresy czasu.\n")
         
class Telephone(Furniture):
    password = ""
    key = 0
    def __init__(self, name):
        super().__init__(name)
        
    def opis(self):
        print(f"\nCentralnym punktem pokoju jest olbrzymi mechanizm\n"
              + "składający się z obracających się kół, przycisków i trybików. Być może trzeba ustawić\n"
              + "odpowiednią kombinację, korzystając z wskazówek pozostawionych w poprzednim\n"
              + "pomieszczeniu oraz znajdujących się na ścianach?\n")
        
    def telephone_solution(solution):
        Telephone.password = solution
        
        
    @classmethod   
    def active_key(cls):
        cls.key += 1
        
class Kufer(Furniture):
    def __init__(self, name):
        super().__init__(name)
        
    def opis(self):
        print(f"Na stole stoi starożytne zamknięte na klucz pudło, które jest znane jako 'Kufer Czasu'\n")
        
        
        
        
        
   
        
#klasa z przedmiotami
class item():
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        
    



#main


def help_command():
    print("\nDostępne komendy:\n" 
          + r"\use - użyj przedmiotu\n" 
          + r"\get - zabierz przedmiotu" 
          + r"\ekwipunek - wyświetli listę przedmiotów dostępnych w twoim ekwipunku" 
          + r"\pomoc - wyświetli listę dostępnych instrukcji " 
          + r"\opisz - opisuje aktualne miejsce" 
    )
    
def furniture_activites(furniture):
    furniture.opis()
    choosing_menu()
    
def play_first_room():
    while True:
        print(r"Wybierz gdzie chcesz podejśc: \tablica, \stol, \maszyna, \wlaz")
        choose =  input()
        if choose == r"\tablica":
            board.opis()
            choosing_menu()
        elif choose == r"\stol":
            table.opis()
            option = choosing_menu()
            if option == r"\use":
                print("Podaj rozwiązanie tej zagadki:\n")
                solution = input()
                if solution == table.solution:
                    print("Po wpisaniu hasła, nagle właz się poruszył, być może się otworzyl?")
                    Player.add_level()
                    choosing_menu()
                else:
                    print("Błedna odpowiedz")
                    pass
        elif choose == r"\maszyna":
            machine.opis()
            option = choosing_menu()
            if option == r"\get":
                machine.get()
                choosing_menu() #to jest żle
        elif choose == r"\wlaz":
            if Player.level == 0:
                print("Właz jest zamknięty")
                continue
            elif Player.level == 1:
                print("\nPrzechodząc przez otwarty właz, znajdujesz się w kolejnym pomieszczeniu. Tym\n"
                      + "razem jest ono wypełnione skomplikowanymi mechanizmami, starożytnymi artefaktami i\n"
                      + "tajemniczymi urządzeniami. Pokój emanuje poczuciem tajemnicy i magii podróży w czasie.\n"
                      + "")
                play_second_room()
        else:
            print("Źle")
            continue
        
def play_second_room():
    while True:
        print(r"Wybierz gdzie chcesz podejśc: \telefon,  \kufer, \maszyna_czasu, \ksiega, \waga, \szkatulka, \wlaz")
        choose = input()
        if choose == r"\telefon":
            telephone.opis()
            while True:
                option = choosing_menu()
                if option == r"\use":
                    print("Wykręć numer telefonu na kole: \n")
                    solution = input()
                    if solution == str(telephone.password):
                        print("Dryyyyn, dryyyn\n"
                            + "Telefon zaczął dzwonić w daleką czasoprzestrzeń\n"
                            + "Po chwili z odpowietrznika maszyny wypadł klucz na ziemie")
                        key = item("Key", "Klucz do kufra")
                    else:
                        print("Po przekręceniu koła nic się nie dzieje")
                        continue
                elif option == r"\get":
                    if 'key' in dir():
                        print("Zdobyłeś klucz!")
                        player.add_backpack(key)
                    else: 
                        continue
                elif option == r"\opis":
                    telephone.opis()
                    continue
                else:
                    print("Źle")
                    continue
        elif choose == r"\kufer":
            kufer.opis()
            option = choosing_menu()
            if option == r"\use":
                if player.check_item(key): #######################################################################################################################################
                    print("Jest")
                else:
                    print("NIema")
        elif choose == r"\maszyna_czasu":
            pass
        elif choose == r"\ksiega":
            pass
        elif choose == r"\waga":
            pass
        elif choose == r"\szkatulka":
            pass
        elif choose == r"\wlaz":
            Player.go_room_first()
            print("Przechodzisz do Tajemniczego pokoju\n")
            play_first_room()
        else:
            print("Źle")
            continue
        
        
    
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
            if Player.active_room == 0:
                play_first_room()
            elif Player.active_room == 1:
                play_second_room()
        else:
            print("Źle!")
            continue
     
    
print("W grze wcielasz się w rolę utalentowanego archeologa, który przypadkowo odkrywa\n"
      + "tajemnicze pomieszczenie w jednym z budynków w Barcelonie. Okazuje się, że to jest\n"
      + "wejście do niewyobrażalnego świata podróży w czasie. Twoim zadaniem jest odkrycie\n"
      + "sekretów tego miejsca i ocalenie historii.\n")


print("Tajemniczy pokój\n"
      + "Przy wejściu do pomieszczenia znajdujesz się w pokoju o stonowanej kolorystyce.\n"
      + "Ściany zdobią starodawne mapy i tablice związane z podróżami w czasie. Na środku stoi stół\n"
      + "z metalowym blatem, na którym leży zakurzony stary pergamin.\n"
      + "W rogu stoju tajemnicza maszyna. Obok niej znajduję się stary, trudny do zauważenia właz\n")


telephone = Telephone("Mechanizm Kombinacji Czasowych")
table = Table("Stół z zagadką", "Kolumb")
board = Board("Tablica", 1453, 515675200)
machine = Machine("Maszyna")
kufer = Kufer("Kufer Czasu")

player = Player()
play_second_room()