class Player():
    level = 0 
    active_room = 0
    
    def __init__(self):
        self.backpack = [blue_medalion, yellow_medalion, green_medalion, black_medalion]
    
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
    

#klasa z casket book table

class Furniture():
    def __init__(self, name, solution):
        self.name = name
        self.solution = solution
               
#klasa z pomieszczeniami
class Board(Furniture):
    def __init__(self, name, year, telephon_number):
        self.name = name
        self.year = year
        self.telephone_number = telephon_number
        Telephone.telephone_solution(telephon_number)
        
        
    def opis(self):
        print(f"\nPodchodząc pod ściane zauważasz tablicę.\n"
              + f"Znajdują się na niej liczby. Przypatrując się bardziej\n"
              + f"widzisz ciąg liczb {self.year}|{self.telephone_number}")

        
class Machine():
    #tablica do wrzucania monet
    def __init__(self, name):
        self.name = name
        self.active = 0 
        self.content_of_the_machine = []  
        
    classmethod
    def actived(self):
        self.active += 1
         
class Telephone():
    password = ""
    key = 0
    def __init__(self, name):
        self.name = name
        
    def telephone_solution(solution):
        Telephone.password = solution
        
    @classmethod   
    def active_key(cls):
        cls.key += 1     
        
class Book(Furniture):
    def __init__(self, name, solution):
        super().__init__(name, solution)    
          
    def opis(self):
        from modules import file_reader as fr
        fr("book_des.txt")
      
class Scales():
    def __init__(self, name):
        self.name = name
        self.helmet = 9.5
        self.weights = 0
        self.doors = "closed"
    
    def check(self):   
        if self.weights ==  self.helmet:
            print("Waga zrównała się!\n")
            print("Gdy waga się zrównała otworzyły się drzwiczki pod stołem, ukazały się cztery figurki i medalion!\n")
            yellow_medalion.actived()
            kleopatra.actived()
            szekspir.actived()
            bonaparte.actived()
            mandela.actived()
            scales.open_doors()
        elif self.weights <= self.helmet:
            print("Ciężarki są niżej niż hełm")
        elif self.weights >= self.helmet:   
            print("Ciężarki są wyżek niż hełm")     
            
    def open_doors(self):
        self.doors = "open"
        
class Casket(Furniture):
    def __init__(self, name, solution):
        super().__init__(name, solution)
        self.casket_close_open = "closed"
        self.content_of_the_casket = []
        self.solution_characters = [kleopatra, szekspir, bonaparte, mandela]
        
    def open_casket(self):
        self.casket_close_open = "open"
        
    def check_characters(self):
        if self.content_of_the_casket == self.solution_characters:
            black_medalion.actived()
            print("Po ułożeniu figurek nagle magicznie z drzwiczek szkatulki wypada czarny medalion!\n")
        else:
            self.content_of_the_casket = []
            player.add_backpack(bonaparte)
            player.add_backpack(mandela)
            player.add_backpack(szekspir)
            player.add_backpack(kleopatra)
            print("Figury zostały żle ułożone!!!")

#klasa z przedmiotami
class item():
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.active = 0
        
    classmethod
    def actived(self):
        self.active += 1
  
   
    
telephone = Telephone("Mechanizm Kombinacji Czasowych")
table = Furniture("Stół z zagadką", "Kolumb")
board = Board("Tablica", 1453, 515675200)
machine = Machine("Maszyna")
key = item("Key", "Klucz do kufra")
module = item("Moduł czasu", "Potrzebny do naprawy maszyny czasu")
blue_medalion = item("Niebieski medalion", "Medalion służy do otwarcia portalu")
book = Book("Księga Czasu", "Tutanchamon")
paper = item("5", "Kartka papier z liczbą")
green_medalion = item("Zielony medalion", "Medalion służy do otwarcia portalu")
scales = Scales("Waga")
yellow_medalion = item("Żółty medalion", "Medalion służy do otwarcia portalu")
kleopatra = item("kleopatra", "Figurka kleopatry")
szekspir = item("szekspir", 'Figurka Szekspira')
bonaparte =  item("bonaparte", "Figurka Bonaparte")
mandela =  item("mandela", "Figurka Mandeli")
casket = Casket("Magiczna szkatułka", "Rzym")
black_medalion = item("Czarny medalion", "Medalion służy do otwarcia portalu")
player = Player()

