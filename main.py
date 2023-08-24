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


class TimeMachine(Furniture):
    def __init__(self, name):
        super().__init__(name)   
        
    def opis(self):
        print(f"W rogu pokoju stoi tajemnicza maszyna czasu.\n"
              + "Jej imponująca konstrukcja przykuwa wzrok i budzi ogromne zainteresowanie\n"
              + "Wskazówki znajdujące się na maszynie sugerują, że aby aktywować maszynę\n"
              + "musisz naprawić maszynę. WYmaga to identyfikacji odpowiednihc wzorców i sekwencji\n")
        
class Book(Furniture):
    def __init__(self, name):
        super().__init__(name)
        self.solution = "Tutanchamon"      
          
    def opis(self):
        print(f"Leży na stoliku, starannie oprawiona księga, która opisuje historie podróży w\n"
              + "czasie oraz zawiera informacje o kluczowych wydarzeniach w różnych okresach\n"
              + "Na pierwszej stronie księgi widzimy coś na podobę zagadki: \n"
              + "W starożytnym Egipcie chowano mnie z najwyższą troską,\n"
              + "W grobowcach pełnych skarbów, klejnotów i złota.\n"
              + "Na tronie zasiadałem jako faraon potężny,\n"
              + "Moje imię w historii zachowało się pięknie.\n")
      
class Scales(Furniture):
    def __init__(self, name):
        super().__init__(name)
        self.helmet = 9.5
        self.weights = 0
        
    def opis(self):
        print("Na stole znajduje się mała waga oraz kilka drzwiczek. Na wadze znajduję się hełm,\n"
              + ",którego nie możemy poruszyć, jakby był zaczarowany\n"
              + "Po drugiej stronie wagi talerz jest pusty, lecz obok stoją odważniki 5kg, 2kg, 1kg i 0,5kg\n"
              + "Ustaw odważniki w odpowiedni sposób!\n")
    
    def play(self, weight):
        weights += weight
        if self.weights ==  self.helmet:
            print("Waga zrównała się!")
        elif
        ### dodac jak waga jest weiksza i mneijsza           
        
        
        
#klasa z przedmiotami
class item():
    
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.active = 0
        
    classmethod
    def actived(self):
        self.active += 1
        
    



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
                    telephone.opis()
                    continue
                else:
                    print("Źle")
                    continue
        elif choose == r"\kufer":
            kufer.opis()
            while True:
                option = choosing_menu()
                if option == r"\use":
                    if player.check_item(key): 
                        print("Po użyciu klucza z twojego ekwipunku otwiera się szkatułka!\n"
                            + "Patrząc do środka zauważyć można coś na podobę modułu,\n"
                            + "który może zostać użyty do budowy czegoś")
                        module.actived()
                    else:
                        print("Szkatułka jest zamknięta")
                elif option == r"\get":
                    if module.active == 1:
                        print("Moduł został dodany do twojego ekwipunku!")
                        player.add_backpack(module)
                    else: 
                        continue
                elif option == r"\opis":
                    kufer.opis()
                    continue
                else:
                    print("Źle")
                    continue
        elif choose == r"\maszyna_czasu":
            time_machine.opis()
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
                    time_machine.opis()
                    continue
                else:
                    print("Nie ma takiej komendy")
                    continue
        elif choose == r"\ksiega":
            book.opis()
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
                    book.opis()
                    continue
                else:
                    print("Nie ma takiej komendy")
                    continue
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
key = item("Key", "Klucz do kufra")
module = item("Moduł czasu", "Potrzebny do naprawy maszyny czasu")

time_machine = TimeMachine("Maszyna czasu")
blue_medalion = item("Niebieski medalion", "Medalion służy do otwarcia portalu")

book = Book("Księga Czasu")
paper = item("56783958", "Kartka papier z ciągiem liczb")
green_medalion = item("Zielony medalion", "Medalion służy do otwarcia portalu")

scales = 
player = Player()
play_second_room()