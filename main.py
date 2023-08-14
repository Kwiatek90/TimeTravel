#klasa z pokojami

class Player():
    level = 0 
    
    @classmethod
    def add_level(cls):
        cls.level += 1

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
        
    def opis(self):
        print(f"\nPodchodząc pod ściane zauważasz tablicę.\n"
              + f"Znajdują się na niej liczby. Przypatrując się bardziej\n"
              + f"widzisz ciąg liczb {self.year}|{self.telephone_number}")
        
    def use():
        pass
    
    def get():
        pass
    
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
        print(f"Maszyna jest największym elementem pomieszczenia. Jej konstrukcja przypomina\n"
            + "kombinację zegara, urządzenia muzycznego i maszyny do gry. Skomplikowane rury i\n"
            + "przewody prowadzą do różnych sekcji, a każdy element jest zdobiony symbolami\n"
            + "związanymi z podróżami w czasie.\n")
     
    def use(self):
        print("Przechodzisz zza maszynę, widzisz na niej instrukcję obsługi:\n"
              + "Musisz odnależć medaliony, by dostosować maszynę w odpowiedni sposób i\n"
              + "aktywować magiczne pole energii, które umożliwi Ci podróż w czasie!\n"
              + "Aby to osiągnąć, musisz zidentyfikować właściwe wzorce i sekwencje, które reprezentują różne okresy czasu.\n")
         
        
   

#klasa z przedmiotami
class item():
    pass



#main


def help_command():
    print("\nDostępne komendy:\n" 
          + r"\use - użyj przedmiotu\n" 
          + r"\get - zabierz przedmiotu" 
          + r"\ekwipunek - wyświetli listę przedmiotów dostępnych w twoim ekwipunku" 
          + r"\pomoc - wyświetli listę dostępnych instrukcji " 
          + r"\opisz - opisuje aktualne pomieszczenie" 
    )

def play_first_room():
    while True:
        print(r"Wybierz gdzie chcesz podejśc: \tablica, \stol, \maszyna, \wlaz")
        choose =  input()
        if choose == r"\tablica":
            board = Board("Tablica", 1453, 515675200)
            board.opis()
            choosing_menu()
        elif choose == r"\stol":
            table = Table("Stół z zagadką", "Kolumb")
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
            maszyna = Machine("Maszyna")
            maszyna.opis()
            option = choosing_menu()
            if option == r"\get":
                maszyna.use()
        elif choose == r"\wlaz":
            if Player.level == 0:
                print("Właz jest zamknięty")
                continue
            elif Player.level == 1:
                play_second_room()
        else:
            print("Źle")
            continue
        
def play_second_room():
    while True:
        print(r"Wybierz gdzie chcesz podejśc: \telefon, \maszyna_czasu, \kufer, \ksiega, \waga, \szkatulka, \wlaz")
        choose = input()
        if choose == r"\telefon":
            pass
        elif choose == r"\maszyna_czasu":
            pass
        elif choose == r"\kufer":
            pass
        elif choose == r"\ksiega":
            pass
        elif choose == r"\waga":
            pass
        elif choose == r"\szkatulka":
            pass
        elif choose == r"\wlaz":
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
        if choose_menu == r"\get":
            return True
        elif choose_menu == r"\ekwipunek":
            pass
        elif choose_menu == r"\pomoc":
            help_command()
            continue
        elif choose_menu == r"\wyjdz":
            print("\nWracasz na środek pokoju")
            play_first_room()  
        else:
            print("Źle!")
            continue
     
    
print("W grze wcielasz się w rolę utalentowanego archeologa, który przypadkowo odkrywa\n"
      + "tajemnicze pomieszczenie w jednym z budynków w Barcelonie. Okazuje się, że to jest\n"
      + "wejście do niewyobrażalnego świata podróży w czasie. Twoim zadaniem jest odkrycie\n"
      + "sekretów tego miejsca i ocalenie historii.\n")


print("Tajemniczy pokój\n"
      + "Przy wejściu do pomieszczenia archeolog znajduje się w pokoju o stonowanej kolorystyce.\n"
      + "Ściany zdobią starodawne mapy i tablice związane z podróżami w czasie. Na środku stoi stół\n"
      + "z metalowym blatem, na którym leży zakurzony stary pergamin.\n"
      + "W rogu stoju tajemnicza maszyna. Obok niej znajduję się stary, trudny do zauważenia właz\n")

player = Player()
play_first_room()