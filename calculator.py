# Prosty kalkulator w języku Python

# Funkcja dodawania
def dodawanie(x, y):
   return x + y

# Funkcja odejmowania
def odejmowanie(x, y):
   return x - y

# Funkcja mnożenia
def mnożenie(x, y):
   return x * y

# Funkcja dzielenia
def dzielenie(x, y):
   return x / y

print("Wybierz operację.")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnożenie")
print("4.Dzielenie")

# Prośba o wybór operacji
wybór = input("Wpisz numer operacji (1/2/3/4):")

# Prośba o wprowadzenie liczb
liczba1 = int(input("Wpisz pierwszą liczbę: "))
liczba2 = int(input("Wpisz drugą liczbę: "))

if wybór == '1':
   print(liczba1,"+",liczba2,"=", dodawanie(liczba1,liczba2))

elif wybór == '2':
   print(liczba1,"-",liczba2,"=", odejmowanie(liczba1,liczba2))

elif wybór == '3':
   print(liczba1,"*",liczba2,"=", mnożenie(liczba1,liczba2))

elif wybór == '4':
   print(liczba1,"/",liczba2,"=", dzielenie(liczba1,liczba2))
else:
   print("Nieprawidłowy wybór")