from tkinter import *
from tkinter import messagebox,filedialog
from PIL import ImageTk, Image
import matplotlib.pyplot as plt 
import matplotlib.pyplot as plt
from scipy.signal import  find_peaks, peak_prominences
import pandas as pd
from tkinter import Toplevel
import os 
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import datetime


root = Tk()

page1_login=Frame(root)  
page2_administrator=Frame(root)
spis_administrator=Frame(root)
edytuj_uzytkownika=Frame(root)
page2_stworz=Frame(root)
page3_sygnal=Frame(root)
page3_wyswietla_syganl=Frame(root)
page4_wynik_analizy=Frame(root)
page5_administrator = Frame(root)
page6_sygnal=Frame(root)

#definicja zmiennych globalnych
currently_logged = ""
who=0
#funkcja logowania użytkownika
def login():
    global currently_logged,who
    with open("login.txt", "r") as file:
        lines = file.readlines()

    users = [line.strip().split(';') for line in lines]

    entered_login = login_podaj.get()
    entered_password = haslo_podaj.get()

    for user in users:
        if (entered_login == user[2] and entered_password == user[3]) or (entered_login == 'admin' and entered_password == 'admin'):
            currently_logged = f"{user[0]} {user[1]}"
            if user[4] == "Administrator" or entered_login == 'admin':
                who=1
                page2_administrator.tkraise()
            else: # Dla Doctor
                page3_sygnal.tkraise()
                who=0
            break
    else:
        messagebox.showerror("Błąd logowania", "Nieprawidłowy login lub hasło")
        login_podaj.delete(0,END)
        haslo_podaj.delete(0,END)


#fukncja wywoływanie po liknięciu w zębatkę
def on_zebatka_click(event):
    print("Zebatka Clicked!") 
    spis_administrator.tkraise()
    #page2_stworz.tkraise()
    
# funkcja do wyświetlania sygnału
def wyswietl_sygnal():
    #print("Image Clicked!")
    page3_wyswietla_syganl.tkraise()

#funkcja do pokazywania wyniku
def pokaz_wynik():
    #print("Image Clicked!")
    page4_wynik_analizy.tkraise()

# funkcja dodawania użytkownika
def adding_user():
    page2_stworz.tkraise()

#funkcja powrotu
def goBack():
    page2_administrator.tkraise()

#funkcja powrotu do spisu
def goBackToSpis():
    spis_administrator.tkraise()

personal = ''
#funkcja edycji użytkownika
def editing_user():
    personal = getPersonals()
    if personal:
        edytuj_uzytkownika.rowconfigure(0, weight=1)
        edytuj_uzytkownika.rowconfigure(1, weight=1)
        edytuj_uzytkownika.rowconfigure(2, weight=1)
        edytuj_uzytkownika.rowconfigure(3, weight=1)
        edytuj_uzytkownika.rowconfigure(4, weight=1)
        edytuj_uzytkownika.rowconfigure(5, weight=1)
        edytuj_uzytkownika.rowconfigure(6, weight=1)
        edytuj_uzytkownika.rowconfigure(7, weight=1)
        edytuj_uzytkownika.rowconfigure(8, weight=1)

        edytuj_uzytkownika.columnconfigure(0, weight=1)
        edytuj_uzytkownika.columnconfigure(1, weight=1)
        edytuj_uzytkownika.columnconfigure(2, weight=1)
        edytuj_uzytkownika.columnconfigure(3, weight=1)
        edytuj_uzytkownika.columnconfigure(4, weight=1)

        label_edycja = Label(edytuj_uzytkownika, text='Edycja użytkownika:', font=("Arial", 14, "bold"))
        label_edycja.grid(row=0,column=2, sticky='w')
        
        imie_label = Label(edytuj_uzytkownika, text=f'Obecne imię: ', anchor='w')
        imie_label.grid(row=1, column=1, sticky='w')

        imie_value = Label(edytuj_uzytkownika, text=f'{personal[0]}', anchor='w')
        imie_value.grid(row=1, column=2, sticky='w')

        nazwisko_label = Label(edytuj_uzytkownika, text=f'Obecne nazwisko: ', anchor='w')
        nazwisko_label.grid(row=3, column=1, sticky='w')

        nazwisko_value = Label(edytuj_uzytkownika, text=f'{personal[1]}', anchor='w')
        nazwisko_value.grid(row=3, column=2, sticky='w')

        nazwa_label = Label(edytuj_uzytkownika, text=f'Obecna nazwa: ', anchor='w')
        nazwa_label.grid(row=5, column=1, sticky='w')

        nazwa_value = Label(edytuj_uzytkownika, text=f'{personal[2]}', anchor='w')
        nazwa_value.grid(row=5, column=2, sticky='w')

        noweImieLabel = Label(edytuj_uzytkownika, text='Nowe imię: ', anchor='w')
        noweImieLabel.grid(row=2, column=1, sticky='w')
        imie_entry = Entry(edytuj_uzytkownika)
        imie_entry.grid(row=2, column=2, sticky='w')

        noweNazwiskoLabel = Label(edytuj_uzytkownika, text='Nowe nazwisko: ', anchor='w')
        noweNazwiskoLabel.grid(row=4, column=1, sticky='w')
        nazwisko_entry = Entry(edytuj_uzytkownika)
        nazwisko_entry.grid(row=4, column=2, sticky='w')

        nowaNazwaLabel = Label(edytuj_uzytkownika, text='Nowa nazwa: ', anchor='w')
        nowaNazwaLabel.grid(row=6, column=1, sticky='w')
        nazwa_entry = Entry(edytuj_uzytkownika)
        nazwa_entry.grid(row=6, column=2, sticky='w')

        cancelButton = Button(edytuj_uzytkownika, text='Wróć', width=10, bg="navy", fg="white", font=("Arial", 10), command=goBackToSpis)
        cancelButton.grid(row=8, column=1)

        okButton = Button(edytuj_uzytkownika, text='OK', width=10, bg="navy", fg="white", font=("Arial", 10), command=lambda: confirm(personal, imie_entry, nazwisko_entry, nazwa_entry))
        okButton.grid(row=8, column=3)

    edytuj_uzytkownika.update()
    edytuj_uzytkownika.update_idletasks()
    edytuj_uzytkownika.tkraise()

#funkcja zmiany hasła
def change_password_window():
    change_password_window = Toplevel()
    change_password_window.title("Zmiana hasła")
    change_password_window.geometry("300x100")

    def change_password():
        new_password = new_password_entry.get()
        repeat_password = repeat_password_entry.get()

        if new_password == repeat_password:
            try:
                with open("login.txt", "r") as f:
                    lines = f.readlines()
                with open("login.txt", "w") as f:
                    linijki = []
                    for line in lines:
                        linijki.append(line.strip().split(';'))
                    for i in range(len(linijki)):
                        if i == list(current_users.curselection())[0]:
                            linijki[i][3] = new_password  # Indeks 3 oznacza pole z hasłem
                        f.write(';'.join(linijki[i]) + '\n')

                change_password_window.destroy()
                messagebox.showinfo("Sukces", "Hasło zostało zmienione pomyślnie.")
            except Exception as e:
                messagebox.showerror("Błąd", f"Wystąpił błąd: {str(e)}")
        else:
            messagebox.showerror("Błąd", "Podane hasła nie zgadzają się.")

    new_password_label = Label(change_password_window, text="Nowe hasło: ")
    new_password_label.grid(row=1, column=0)
    new_password_entry = Entry(change_password_window, show="*")
    new_password_entry.grid(row=1, column=1)

    repeat_password_label = Label(change_password_window, text="Powtórz hasło: ")
    repeat_password_label.grid(row=2, column=0)
    repeat_password_entry = Entry(change_password_window, show="*")
    repeat_password_entry.grid(row=2, column=1)

    change_button = Button(change_password_window, text="Zmień hasło", width=10, bg="navy", fg="white", font=("Arial", 10), command=change_password)
    change_button.grid(row=3, columnspan=2)

change_password_button = Button(edytuj_uzytkownika, text="Zmień hasło", width=10, bg="navy", fg="white", font=("Arial", 10), command=change_password_window)
change_password_button.grid(row=8, column=2, pady=10)

#funkcja potwierdzenia
def confirm(personal, imie_entry, nazwisko_entry, nazwa_entry):
    with open("login.txt", "r") as f:
        lines = f.readlines()
    with open("login.txt", "w") as f:
        linijki = []
        for line in lines:
            linijki.append(line)
        for i in range(len(linijki)):
            if i != list(current_users.curselection())[0]:
                f.write(linijki[i])
            else:
                daneOsoby = linijki[i].split(';')
                if imie_entry.get() != '':
                    daneOsoby[0] = imie_entry.get()
                if nazwisko_entry.get() != '':
                    daneOsoby[1] = nazwisko_entry.get()
                if nazwa_entry.get() != '':
                    daneOsoby[2] = nazwa_entry.get()
                f.write(';'.join(daneOsoby))

    messagebox.showinfo("Potwierdzenie", "Edycja użytkownika powiodła się")

    # Aktualizacja listy użytkowników po zatwierdzeniu edycji
    current_users.delete(0, END)  # Usunięcie aktualnej zawartości listy
    with open('login.txt') as dane:
        for line in dane:
            dane2 = line.split(';')
            imie = dane2[0]
            nazwisko = dane2[1]
            current_users.insert(END, f"{imie} {nazwisko}")  # Dodanie użytkownika do listy


selected_file=None
# Funkcja aby plik wczytywał i czas i napięcie 
def load_file():
    global selected_file
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
   
    if file_path:
        selected_file = file_path
        try:  
            # Przetworzenie danych i wyświetlenie ich w oknie analizy
            show_data(file_path)
        except Exception as e:
            print(f"Error processing txt file: {e}")

canvas=None
nazwa=StringVar()
Checkbutton1 = IntVar()   

#Funkcja aby wykres sie wyswietlał
def show_data(file_path):
    global canvas,selected_file,nazwa,who # Deklarujemy `canvas` jako zmienną globalną, aby mieć do niej dostęp w funkcji
    print(f"Debug: who = {who}")
    try:
        if canvas:
            canvas.get_tk_widget().destroy()
        # Utworzenie wykresu EKG o mniejszych rozmiarach
        figure = plt.figure(figsize=(7, 2.5))  # Rozmiar wykres np 6x3 to 6-szerokosc, 3-wysokosc
        df = pd.read_csv(file_path, delimiter=' ', header=None, names=['czas', 'napięcie'])
        plt.plot(df['czas'], df['napięcie'])
        plt.grid(True)
        plt.xlabel('czas [ms]')
        plt.ylabel('napięcie [mV]')
        
        if who==1:
            page5_administrator.tkraise()
            # Tworzenie obiektu FigureCanvasTkAgg z wykresem i wstawienie go do okna aplikacji Tkinter  
            figure = plt.gcf()
            canvas = FigureCanvasTkAgg(figure, master=sygnal_label)
            canvas.draw()
            canvas.get_tk_widget().pack()
        
            selected_file = file_path
            nazwa.set(f'Nazwa pliku: {os.path.basename(selected_file)}')
            wyswietla_peaks_CB.deselect()  #Checkbutton jest ustawiony na wartość 0, po wybraniu nowego pliku
        else:
            page6_sygnal.tkraise()
            # Tworzenie obiektu FigureCanvasTkAgg z wykresem i wstawienie go do okna aplikacji Tkinter  
            figure = plt.gcf()
            canvas = FigureCanvasTkAgg(figure, master=sygnal_label1)
            canvas.draw()
            canvas.get_tk_widget().pack()
        
            selected_file = file_path
            nazwa.set(f'Nazwa pliku: {os.path.basename(selected_file)}')
            wyswietla_peaks_CB.deselect()  #Checkbutton jest ustawiony na wartość 0, po wybraniu nowego pliku
    except Exception as e:
        print(f"Error processing data: {e}")


#Funkcja do klikania chechboxa i pojawienia się pików
def isChecked():
    global selected_file
    if Checkbutton1.get()==1:
        df = pd.read_csv(selected_file, delimiter=' ', header=None, names=['czas', 'napięcie'])
        fs = 160
        peaks, _ = find_peaks(df['napięcie'], height=0.5, distance=fs)

        prominences = peak_prominences(df['napięcie'], peaks)[0]
        refined_peaks = peaks[prominences > 0.5]
        
        # Plot the ECG signal with detected peaks
        plt.close()
        plt.figure(figsize=(10, 6))
        plt.plot(df['czas'], df['napięcie'], label='ECG Signal')
        plt.plot(df['czas'].values[refined_peaks], df['napięcie'].values[refined_peaks], 'rx', label='Detected Peaks')
        plt.title('ECG Signal with Detected Peaks')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Amplitude (mV)')
        plt.legend()
        plt.grid(True)
        plt.show()
        wyswietla_peaks_CB.deselect()
    else:
        plt.close()

def compute_measures(r_peaks): 
    measures = {}
    measures = 60 / np.mean(np.diff(r_peaks)) 
    return measures

# Funkcja do obliczania tętna
def calculate_pulse_rate(file_path):
    try:
        df = pd.read_csv(file_path, delimiter=' ', header=None, names=['czas', 'napięcie'])

        fs = 160

        peaks, _ = find_peaks(df['napięcie'], height=0.5, distance=fs)

        prominences = peak_prominences(df['napięcie'], peaks)[0]
        refined_peaks = peaks[prominences > 0.5]

        pulse_rate = compute_measures(df['czas'].values[refined_peaks])

        return pulse_rate

    except Exception as e:
        print(f"Error calculating pulse rate: {e}")
        return None
    
#Funkcja do szacowania poziomu stresu
def calculate_stress_level(heart_rate):
    
    if heart_rate < 60:
        return "Niski poziom stresu"
    elif 60 <= heart_rate <= 100:
        return "Sredni poziom stresu"
    else:
        return "Wysoki poziom stresu"

def calculate_heart_rhythm(file_path):
    try:
        df = pd.read_csv(file_path, delimiter=' ', header=None, names=['czas', 'napięcie'])

        peaks, _ = find_peaks(df['napięcie'], height=0.5, distance=160)  

        heart_rhythm = check_heart_rhythm(df['czas'].values[peaks])

        return heart_rhythm

    except Exception as e:
        print(f"Błąd przy kalkulacji rytmu serca {e}")
        return None

def check_heart_rhythm(r_peaks):
    try:
        # Oblicz odstępy czasowe między załamkami R
        r_peak_intervals = np.diff(r_peaks)
        print(r_peak_intervals)
        # Zakładamy, że rytm serca jest regularny, jeśli odstępy między załamkami R są w przybliżeniu jednakowe
        is_regular_rhythm = np.allclose(r_peak_intervals, np.mean(r_peak_intervals), rtol=0.25)  # tolerancja 20%
        
        if is_regular_rhythm:
            heart_rhythm = "Regularny"
        else:
            heart_rhythm = "Nieregularny"

        return heart_rhythm

    except Exception as e:
        print(f"Błąd przy sprawdzaniu rytmu serca {e}")
        return None

 
#Funkcja do obliczenia odchylenia standardowego
def calculate_standard_deviation(file_path):
    try:
        df = pd.read_csv(file_path, delimiter=' ', header=None, names=['czas', 'napięcie'])
        std_deviation = np.std(df['napięcie'])
        return std_deviation

    except Exception as e:
        print(f"Error calculating standard deviation: {e}")
        return None
    
# Funkcja do wywołania wyników po kliknięciu przycisku "Oblicz"
def pokaz_wynik():
    global selected_file
    try:
        result = None

        if checkbox_var.get() == 3:  # Jeśli wybrano tętno
            pulse_rate = calculate_pulse_rate(selected_file)
            if pulse_rate is not None:
                result = f"Tetno: {pulse_rate:.2f} uderzen/min"
            else:
                messagebox.showerror("Błąd", "Wystąpił błąd podczas obliczania tętna.")
            checkbox_var.set(0)

        elif checkbox_var.get() == 4:  # Jeśli wybrano poziom stresu
            pulse_rate = calculate_pulse_rate(selected_file)
            if pulse_rate is not None:
                # Zakładamy, że tempo pracy serca jest proporcjonalne do poziomu stresu
                stress_level = calculate_stress_level(pulse_rate)
                result = f"Poziom stresu: {stress_level}"
            else:
                messagebox.showerror("Błąd", "Wystąpił błąd podczas obliczania tętna.")
            checkbox_var.set(0)

        elif checkbox_var.get() == 5:  # Jeśli wybrano rytm serca
            heart_rhythm = calculate_heart_rhythm(selected_file)
            if heart_rhythm is not None:
                result = f"Rytm serca: {heart_rhythm}"
            else:
                messagebox.showerror("Błąd", "Wystąpił błąd podczas obliczania rytmu serca.")
            checkbox_var.set(0)

        elif checkbox_var.get() == 6:  # Jeśli wybrano odchylenie standardowe
            std_deviation = calculate_standard_deviation(selected_file)
            if std_deviation is not None:
                result = f"Odchylenie standardowe: {std_deviation:.4f}"
            else:
                messagebox.showerror("Błąd", "Wystąpił błąd podczas obliczania odchylenia standardowego.")
            checkbox_var.set(0)

        if result is not None:
            messagebox.showinfo("Wynik analizy", result)

    except Exception as e:
        print(f"Error processing data: {e}")
        messagebox.showerror("Błąd", "Wystąpił błąd podczas przetwarzania danych.")

# Zapis wyników do pliku po kliknięciu przycisku "Zapisz"
def zapisz_wynik():
    global selected_file
    try:
        result = None

        if checkbox_var.get() == 3:  # Jeśli wybrano tętno
            pulse_rate = calculate_pulse_rate(selected_file)
            if pulse_rate is not None:
                result = f"Tetno: {pulse_rate:.2f} uderzen/min"
            else:
                messagebox.showerror("Błąd", "Wystąpił błąd podczas obliczania tętna.")
            checkbox_var.set(0)

        elif checkbox_var.get() == 4:  # Jeśli wybrano poziom stresu
            pulse_rate = calculate_pulse_rate(selected_file)
            if pulse_rate is not None:
                # Zakładamy, że tempo pracy serca jest proporcjonalne do poziomu stresu
                stress_level = calculate_stress_level(pulse_rate)
                result = f"Poziom stresu: {stress_level}"
            else:
                messagebox.showerror("Błąd", "Wystąpił błąd podczas obliczania tętna.")
            checkbox_var.set(0)

        elif checkbox_var.get() == 5:  # Jeśli wybrano rytm serca
            heart_rhythm = calculate_heart_rhythm(selected_file)
            if heart_rhythm is not None:
                result = f"Rytm serca: {heart_rhythm}"
            else:
                messagebox.showerror("Błąd", "Wystąpił błąd podczas obliczania rytmu serca.")
            checkbox_var.set(0)

        elif checkbox_var.get() == 6:  # Jeśli wybrano odchylenie standardowe
            std_deviation = calculate_standard_deviation(selected_file)
            if std_deviation is not None:
                result = f"Odchylenie standardowe: {std_deviation:.4f}"
            else:
                messagebox.showerror("Błąd", "Wystąpił błąd podczas obliczania odchylenia standardowego.")
            checkbox_var.set(0)

        if result is not None:
            # Zapisz wynik do pliku tekstowego z nazwą pliku
            filename = os.path.basename(selected_file)
            with open('wyniki.txt', 'a') as file:
                file.write(f"Plik: {filename}, Lekarz: {currently_logged}, Data analizy: {datetime.datetime.now()}, Wynik: {result}\n")
                messagebox.showinfo("Zapisano", "Wynik został zapisany do pliku.")

    except Exception as e:
        print(f"Error processing data: {e}")
        messagebox.showerror("Błąd", "Wystąpił błąd podczas przetwarzania danych.")

#funkcja służąca do pobierania danych personalnych
def getPersonals():
    with open("login.txt", "r") as f:
        lines = f.readlines()
        linijki = []
        for line in lines:
            linijki.append(line.strip().split(';'))
        for i in range(len(linijki)):
            if i == list(current_users.curselection())[0]:
                return linijki[i]

#funkcja usuwanie użytkownika
def deleteUser():
    with open("login.txt", "r") as f:
        lines = f.readlines()
    with open("login.txt", "w") as f:
        linijki = []
        for line in lines:
            linijki.append(line)
        for i in range(len(linijki)):
            if i != list(current_users.curselection())[0]:
                f.write(linijki[i])
            else:
                print(f"Usunięto: {linijki[i]}")
        current_users.delete(list(current_users.curselection())[0])

#funkcja rejestracji    
def registration():
    imie = podaj_imie.get()
    nazwisko = podaj_nazwisko.get()
    login = podaj_login.get()
    haslo = podaj_haslo.get()
    powtorz_haslo = podaj_powhaslo.get()

    if not all([imie, nazwisko, login, haslo, powtorz_haslo]):
        messagebox.showerror("Błąd rejestracji", "Wszystkie pola muszą być wypełnione.")
        return

    if haslo != powtorz_haslo:
        messagebox.showerror("Błąd rejestracji", "Hasła nie są identyczne.")
        return

    pelniona_funkcja = "Lekarz" if checkbox_var.get() == 1 else "Administrator"

    file_path = "login.txt"
   
    result = messagebox.askquestion("Pomyślna rejestracja", "Dane zostały zapisane.\nCzy chcesz dodać nową osobę?")
    
    if result == 'yes':
        with open("login.txt", 'a+') as file:
            file.seek(0, 2)  # Ustawienie wskaźnika na koniec pliku
            position = file.tell()  # Pozycja wskaźnika

            if position > 0:  # Jeśli plik nie jest pusty
                file.seek(position - 1, 0)  # Ustawienie wskaźnika na ostatni znak

                last_char = file.read(1)
                if last_char != '\n':  # Jeśli ostatni znak nie jest nową linią
                    file.write('\n')  # Dodaj nową linię przed nowym wpisem

            file.write(f"{imie};{nazwisko};{login};{haslo};{pelniona_funkcja}")
        podaj_imie.delete(0, 'end')
        podaj_nazwisko.delete(0, 'end')
        podaj_login.delete(0, 'end')
        podaj_haslo.delete(0, 'end')
        podaj_powhaslo.delete(0, 'end')
        checkbox_var.set(0)
        
        # Aktualizacja listy użytkowników po dodaniu nowego użytkownika
        current_users.delete(0, END)  # Usunięcie aktualnej zawartości listy
        with open('login.txt') as dane:
            for line in dane:
                dane2 = line.split(';')
                imie = dane2[0]
                nazwisko = dane2[1]
                current_users.insert(END, f"{imie} {nazwisko}")  # Dodanie użytkownika do listy
    else:
        pass

############# OKNA APLIKACJI #####################
root.geometry("700x500")
root.resizable(1,1)
root.title("ECG")
root.option_add('*Font', 'Arial 12')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.tk_setPalette(background='white')

page1_login.grid(row=0, column=0,sticky='NSEW')
page2_administrator.grid(row=0, column=0,sticky='NSEW')
page2_stworz.grid(row=0, column=0,sticky='NSEW')
spis_administrator.grid(row=0,column=0,sticky='NSEW')
edytuj_uzytkownika.grid(row=0,column=0,sticky='NSEW')
page3_sygnal.grid(row=0, column=0,sticky='NSEW')
page3_wyswietla_syganl.grid(row=0, column=0,sticky='NSEW')
page4_wynik_analizy.grid(row=0, column=0,sticky='NSEW')
page5_administrator.grid(row=0, column=0,sticky='NSEW') 
page6_sygnal.grid(row=0, column=0,sticky='NSEW')
page1_login.tkraise()

### LOGOWANIE
page1_login.rowconfigure( 0, weight=1)
page1_login.rowconfigure( 1, weight=1)
page1_login.rowconfigure( 2, weight=1) 
page1_login.rowconfigure( 3, weight=1)
page1_login.rowconfigure( 4, weight=1)

page1_login.columnconfigure( 0, weight=1)
page1_login.columnconfigure( 1, weight=1)

logowanie_label = Label(page1_login, text='Logowanie:', font=("Arial", 18, "bold"))
logowanie_label.grid(row=0, columnspan=2, pady=(50, 20))

login_podaj = Label(page1_login, text="Login:")
login_podaj.grid(row=1, column=0, sticky='e', padx=20)
login_podaj = Entry(page1_login, width=50)
login_podaj.grid(row=1, column=1, padx=20)

haslo_podaj= Label(page1_login, text="Hasło:")
haslo_podaj.grid(row=2, column=0, sticky='e', padx=20)
haslo_podaj = Entry(page1_login, show="*", width=50)
haslo_podaj.grid(row=2, column=1, padx=20)

zaloguj = Button(page1_login, text="Zaloguj", width=20, bg="navy", fg="white", font=("Arial", 12), command=login)
zaloguj.grid(row=3, columnspan=2, pady=50)
### KONIEC LOGOWANIA

### PIERWSZE OKNO DLA ADMINISTRATORA
page2_administrator.columnconfigure(0, weight=1)
page2_administrator.columnconfigure(1, weight=1)
page2_administrator.rowconfigure(0, weight=1)
page2_administrator.rowconfigure(1, weight=1)
page2_administrator.rowconfigure(2, weight=1)
page2_administrator.rowconfigure(3, weight=1)

original_image = Image.open('ust.jpg')
resized_image = original_image.resize((75, 75))
image = ImageTk.PhotoImage(resized_image)

image_label = Label(page2_administrator, image=image)
image_label.grid(row=0, column=1, sticky='NE', padx=10, pady=10)
image_label.bind("<Button-1>", on_zebatka_click)

wybierzecg_label = Label(page2_administrator, text='Wybierz i wczytaj plik EKG:', font=("Arial", 14, "bold"))
wybierzecg_label.grid(row=0, columnspan=2, pady=(50, 20))

# Tworzenie przycisku "Kliknij i wybierz plik EKG" w page2_administrator
wybierz_plik = Button(page2_administrator, text="Kliknij i wybierz plik txt", command=load_file, font=("Arial", 12))
wybierz_plik.grid(row=1, column=0, columnspan=2, sticky='NSEW', padx=10, pady=10)
### KONIEC 1 OKNA DLA ADMINISTRATORA

### DRUGIE OKNO DLA ADMINISTRATORA
page5_administrator.columnconfigure(0, weight=1)
page5_administrator.columnconfigure(1, weight=1)
page5_administrator.rowconfigure(0, weight=1)
page5_administrator.rowconfigure(1, weight=1)
page5_administrator.rowconfigure(2, weight=1)
page5_administrator.rowconfigure(3, weight=1)
page5_administrator.rowconfigure(4, weight=1)

wybierz_label = Label(page5_administrator, text='Wybrany plik EKG:', font=("Arial", 14, "bold"))
wybierz_label.grid(row=0, column=0, columnspan=2, pady=(50, 20))

nazwa_pliku_label = Label(page5_administrator, textvariable=nazwa, font=("Arial", 12))
nazwa_pliku_label.grid(row=1, column=0, columnspan=2)

sygnal_label = Label(page5_administrator)
sygnal_label.grid(row=2, column=0, columnspan=2)

wyswietla_peaks_CB = Checkbutton(page5_administrator, text='Wyświetl załamek R',variable=Checkbutton1, onvalue=1, offvalue=0, command=isChecked, font=("Arial", 12))
wyswietla_peaks_CB.grid(row=3, column=0)

analiza_button = Button(page5_administrator, text='Analizuj', command=wyswietl_sygnal, width=12, bg='navy', fg='white', font=("Arial", 10)) 
analiza_button.grid(row=4, column=1, pady=10, padx=(0, 10), sticky='e')

def goBackToPage2():
    page2_administrator.tkraise()

back_button = Button(page5_administrator, text='Wróć', command=goBackToPage2, bg='navy', fg='white', font=("Arial", 10), width=10)
back_button.grid(row=4, column=0, pady=10, padx=(10, 0), sticky='w')
### KONIEC 2 OKNA DLA ADMINISTRATORA


### SPIS UŻYTKOWNIKÓW
spis_administrator.rowconfigure(0,weight=1)
spis_administrator.rowconfigure(1,weight=1)
spis_administrator.rowconfigure(2,weight=1)
spis_administrator.rowconfigure(3,weight=1)
spis_administrator.rowconfigure(4,weight=1)
spis_administrator.rowconfigure(5,weight=1)
spis_administrator.rowconfigure(6,weight=1)
spis_administrator.rowconfigure(7,weight=1)
spis_administrator.rowconfigure(8,weight=1)
spis_administrator.columnconfigure(0,weight=1)
spis_administrator.columnconfigure(1,weight=1)
spis_administrator.columnconfigure(2,weight=1)
spis_administrator.columnconfigure(3,weight=1)
spis_administrator.columnconfigure(4,weight=1)

label_spis = Label(spis_administrator, text='Spis użytkowników:', font=("Arial", 14, "bold"))
label_spis.grid(row=0, column=1, sticky='ew')

current_users = Listbox(spis_administrator,selectmode=SINGLE)

imiona = []
nazwiska = []
nazwy = []
hasla = []
funkcje = []

with open('login.txt') as dane:
    i = 0
    for line in dane:    
        dane2 = line.split(';')
        imiona.append(dane2[0])
        nazwiska.append(dane2[1])
        nazwy.append(dane2[2])
        hasla.append(dane2[3])
        funkcje.append(dane2[4])
        current_users.insert(i, f"{imiona[i]} {nazwiska[i]}")
        i += 1
current_users.grid(row=1,column=1,rowspan=4,sticky='NESW')

add_user = Button(spis_administrator,text='Dodaj',command=adding_user, bg='navy', fg='white', font=("Arial", 12),width=15)
add_user.grid(column=3, row=1)
delete_user = Button(spis_administrator,text='Usuń',command=deleteUser, bg='navy', fg='white', font=("Arial", 12),width=15)
delete_user.grid(column=3, row=2)
edit_user = Button(spis_administrator,text='Edytuj',command=editing_user, bg='navy', fg='white', font=("Arial", 12),width=15)
edit_user.grid(column=3, row=3)
back_user = Button(spis_administrator, text='Wróć',command=goBack, bg='navy', fg='white', font=("Arial", 12),width=15)
back_user.grid(column=1, row=5)
### KONIEC SPISU UŻYTKOWNIKÓW


###       REJESTRACJA 
page2_stworz.rowconfigure(0,weight=1)
page2_stworz.rowconfigure(1,weight=1)
page2_stworz.rowconfigure(2,weight=1)
page2_stworz.rowconfigure(3,weight=1)
page2_stworz.rowconfigure(4,weight=1)
page2_stworz.rowconfigure(5,weight=1)
page2_stworz.rowconfigure(6,weight=1)
page2_stworz.rowconfigure(7,weight=1)
page2_stworz.rowconfigure(8,weight=1)
page2_stworz.rowconfigure(9,weight=1)
page2_stworz.rowconfigure(10,weight=1)
page2_stworz.rowconfigure(11,weight=1)
page2_stworz.rowconfigure(12,weight=1)
page2_stworz.rowconfigure(13,weight=1)
page2_stworz.rowconfigure(14,weight=1)
page2_stworz.rowconfigure(15,weight=1)
page2_stworz.rowconfigure(16,weight=1)

page2_stworz.columnconfigure(0,weight=1)
page2_stworz.columnconfigure(1,weight=1)
page2_stworz.columnconfigure(2,weight=1)


checkbox_var=IntVar()

rejestracja_label = Label(page2_stworz, text='Rejestracja:', font=("Arial", 18, "bold"))
rejestracja_label.grid(row=1, columnspan=3, pady=10)

imie_label = Label(page2_stworz, text="Imię:")
imie_label.grid(row=2, column=0, sticky='w', padx=10)
podaj_imie = Entry(page2_stworz)
podaj_imie.grid(row=2, column=1, columnspan=2, sticky='ew', padx=10, pady=5)

nazwisko_label = Label(page2_stworz, text="Nazwisko:")
nazwisko_label.grid(row=4, column=0, sticky='w', padx=10)
podaj_nazwisko = Entry(page2_stworz)
podaj_nazwisko.grid(row=4, column=1, columnspan=2, sticky='ew', padx=10, pady=5)

login_label = Label(page2_stworz, text="Login:")
login_label.grid(row=6, column=0, sticky='w', padx=10)
podaj_login = Entry(page2_stworz)
podaj_login.grid(row=6, column=1, columnspan=2, sticky='ew', padx=10, pady=5)

haslo_label = Label(page2_stworz, text="Hasło:")
haslo_label.grid(row=8, column=0, sticky='w', padx=10)
podaj_haslo = Entry(page2_stworz, show="*")
podaj_haslo.grid(row=8, column=1, columnspan=2, sticky='ew', padx=10, pady=5)

powtorz_haslo_label = Label(page2_stworz, text="Powtórz hasło:")
powtorz_haslo_label.grid(row=10, column=0, sticky='w', padx=10)
podaj_powhaslo = Entry(page2_stworz, show="*")
podaj_powhaslo.grid(row=10, column=1, columnspan=2, sticky='ew', padx=10, pady=5)

stanowisko_label = Label(page2_stworz, text='Stanowisko:')
stanowisko_label.grid(row=12, column=0, sticky='w', padx=10)

doctor_button = Radiobutton(page2_stworz, text='Lekarz', variable=checkbox_var, value=1)
doctor_button.grid(row=13, column=1, sticky='w', padx=10)

administrator_button = Radiobutton(page2_stworz, text='Administrator', variable=checkbox_var, value=2)
administrator_button.grid(row=14, column=1, sticky='w', padx=10)

stworz = Button(page2_stworz, text='Stwórz', bg="navy", fg="white", command=registration, font=("Arial", 10), width=5, height=1)
stworz.grid(row=15, column=2, pady=20, padx=(10, 5), sticky='ew')

back_user = Button(page2_stworz, text='Wróć', command=goBackToSpis, bg='navy', fg='white', font=("Arial", 10), width=1, height=1)
back_user.grid(row=15, column=0, pady=20, padx=(5, 10), sticky='ew')
### KONIEC REJESTRACJI 


### PIERWSZE OKKNO DLA DOKTORA
page3_sygnal.columnconfigure(0, weight=1)
page3_sygnal.columnconfigure(1, weight=1)
page3_sygnal.rowconfigure(0, weight=1)
page3_sygnal.rowconfigure(1, weight=1)
page3_sygnal.rowconfigure(2, weight=1)
page3_sygnal.rowconfigure(3, weight=1)

page3_sygnal.config(width=1000, height=1000)

wybierzecg1_label = Label(page3_sygnal, text='Wybierz i wczytaj plik EKG:', font=("Arial", 14, "bold"))
wybierzecg1_label.grid(row=0, columnspan=2, pady=(50, 20))

wybierz_plik1 = Button(page3_sygnal, text="Kliknij i wybierz plik txt", command=load_file, font=("Arial", 12))
wybierz_plik1.grid(row=1, column=0, columnspan=2, sticky='NSEW', padx=10, pady=10)
### KONIEC PIERWSZEGO OKNA DLA DOKTORA

### DRUGIE OKNO DLA DOKTORA
page6_sygnal.columnconfigure(0, weight=1)
page6_sygnal.columnconfigure(1, weight=1)
page6_sygnal.rowconfigure(0, weight=1)
page6_sygnal.rowconfigure(1, weight=1)
page6_sygnal.rowconfigure(2, weight=1)
page6_sygnal.rowconfigure(3, weight=1)
page6_sygnal.rowconfigure(4, weight=1)

wybierz_label1 = Label(page6_sygnal, text='Wybrany plik EKG:', font=("Arial", 14, "bold"))
wybierz_label1.grid(row=0, column=0, columnspan=2, pady=(50, 20))

nazwa_pliku_label1 = Label(page6_sygnal, textvariable=nazwa, font=("Arial", 12))
nazwa_pliku_label1.grid(row=1, column=0, columnspan=2)

sygnal_label1 = Label(page6_sygnal)
sygnal_label1.grid(row=2, column=0, columnspan=2)

wyswietla_peaks_CB = Checkbutton(page6_sygnal, text='Wyświetl załamek R',variable=Checkbutton1, onvalue=1, offvalue=0, command=isChecked, font=("Arial", 12))
wyswietla_peaks_CB.grid(row=3, column=0)

analiza_button1 = Button(page6_sygnal, text='Analizuj', command=wyswietl_sygnal, width=12, bg='navy', fg='white', font=("Arial", 10)) 
analiza_button1.grid(row=4, column=1, pady=10, padx=(0, 10), sticky='e')

def goBackToPage2():
    page3_sygnal.tkraise()

back_button1 = Button(page6_sygnal, text='Wróć', command=goBackToPage2, bg='navy', fg='white', font=("Arial", 10), width=10)
back_button1.grid(row=4, column=0, pady=10, padx=(10, 0), sticky='w')
### KONIEC 2 OKNA DLA DOKTORA


### OKNO ANALIZY 
page3_wyswietla_syganl.rowconfigure(0,weight=1)
page3_wyswietla_syganl.rowconfigure(1,weight=1)
page3_wyswietla_syganl.rowconfigure(2,weight=1)
page3_wyswietla_syganl.rowconfigure(3,weight=1)
page3_wyswietla_syganl.rowconfigure(4,weight=1)
page3_wyswietla_syganl.rowconfigure(5,weight=1)
page3_wyswietla_syganl.rowconfigure(6,weight=1)
page3_wyswietla_syganl.rowconfigure(7,weight=1)
page3_wyswietla_syganl.rowconfigure(8,weight=1)
page3_wyswietla_syganl.rowconfigure(9,weight=1)
page3_wyswietla_syganl.rowconfigure(10,weight=1)
page3_wyswietla_syganl.rowconfigure(11,weight=1)

page3_wyswietla_syganl.columnconfigure(0,weight=1)
page3_wyswietla_syganl.columnconfigure(1,weight=1)
page3_wyswietla_syganl.columnconfigure(2,weight=1)

wybierz_label = Label(page3_wyswietla_syganl, text='Wybrany plik EKG:', font=("Arial", 14, "bold"))
wybierz_label.grid(row=0, column=1, pady=(50, 20))

nazwa_pliku_label = Label(page3_wyswietla_syganl, textvariable=nazwa, font=("Arial", 12))
nazwa_pliku_label.grid(row=1, column=1)

wybierz_label = Label(page3_wyswietla_syganl, text='Wybierz co chcesz analizować:', font=("Arial", 12, "bold"))
wybierz_label.grid(row=2, column=1, pady=(50, 20))

tetno_button = Radiobutton(page3_wyswietla_syganl, text='Tetno', variable=checkbox_var, value=3)
tetno_button.grid(row=3, column=0, columnspan=1, sticky='NW')

stres_button=Radiobutton(page3_wyswietla_syganl,text='Szacowany poziom stresu',variable=checkbox_var,value=4)
stres_button.grid(row=3,column=2,columnspan=1,sticky='NW')

rytm_button=Radiobutton(page3_wyswietla_syganl,text='Rytm serca',variable=checkbox_var,value=5)
rytm_button.grid(row=4,column=0,columnspan=1,sticky='NW')

odchylenie_button=Radiobutton(page3_wyswietla_syganl,text='Odchylenie standardowe',variable=checkbox_var,value=6)
odchylenie_button.grid(row=4,column=2,columnspan=1,sticky='NW')

analiza_button = Button(page3_wyswietla_syganl, text='Oblicz', command=pokaz_wynik, width=12, bg='navy', fg='white', font=("Arial", 10)) 
analiza_button.grid(row=11, column=2, pady=10, padx=(0, 10), sticky='e')

button_zapisz = Button(page3_wyswietla_syganl, text="Zapisz", command=zapisz_wynik, width=12, bg='green', fg='white', font=("Arial", 10))
button_zapisz.grid(row=11, column=1, pady=10, padx=10)

def goBackToPage3():
    global who
    if who==0:
        page6_sygnal.tkraise()
    else: 
        page5_administrator.tkraise()

back_button = Button(page3_wyswietla_syganl, text='Wróć', command=goBackToPage3, bg='navy', fg='white', font=("Arial", 10), width=10)
back_button.grid(row=11, column=0, pady=10, padx=(10, 0), sticky='w')
#### KONIEC ANALIZY DLA ADMINISTRATORA

root.mainloop() 
