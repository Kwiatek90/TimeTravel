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
        print(f"\nPodchodząc do stołu zauważasz tekst.\n"
              + "TUTAJ ZAGADKA\n"
              + "Pod tekstem znajduję się klawiatura, a nad nią mały ekran\n" 
              + "ktory wyświetla wpisany litery przez klawiaturę\n"
        )
              
        
   

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
                    print("Drzwi do pokoju drugie sie otworzyły!")
                    Player.add_level()
                    choosing_menu()
                else:
                    print("Błedna odpowiedz")
                pass
        elif choose == r"\maszyna":
            pass
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
        print("Drugi pokój")
        
    
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
     
    
print("Opis gry\n")
print("Trafiłeś do pokoju w którym znajduje się: \n-tablica na scianie\n-stół metalowy\n-maszyna z otworem u góry\n-właz zamknietym wielki zasuwami\n")
player = Player()
play_first_room()