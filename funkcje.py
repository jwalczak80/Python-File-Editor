import csv
def wczytanie(wart):
    '''
        wczytanie danych i zapisanie kopii w postaci listy i list słowników
    '''
    lista_slownikow=0
    nazwa_pliku=input("Proszę podać nazwę pliku z danymi: ")
    klucze=["id","wartosc"]
    try:    #wyłączenie programu przy złej nazwie pliku
        f=open(nazwa_pliku,"r")
    except:
        print("Nie mozna otworzyć pliku")
        exit()
    dane=f.read()
    dane1=dane.split(",")
    dane1=[int(i) for i in dane1] #zapisanie wartości w postaci liczb całkowitych

    n = len(dane1)
    for i in range (1, n, 2):
        wart.append(dane1[i])
    lista_slownikow = [{klucze[0]: dane1[i], klucze[1]: dane1[i + 1]} for i in range(0, n, 2)] #zamiana listy na listę słowników
    f.close()
    return lista_slownikow

def zakres(dane):
    '''
        obliczanie zakresu wyników
    '''
    max_val=max(dane)
    min_val=min(dane)
    print("Zakres wartości = {}-{}".format(min_val,max_val))

def wart_sr(wart):
    '''
        obliczenie wartosci średniej wyników
    '''
    avg=sum(wart)/len(wart)
    print("Wartosć średnia = ",avg)

def export(l_sl):
    keys = l_sl[0].keys()
    with open('dane_csv.csv', 'w', newline='') as output:
        dict_writer = csv.DictWriter(output, keys)
        dict_writer.writeheader()
        dict_writer.writerows(l_sl)


def operacja(op,dane,l_sl):
    err1=1
    err2=1
    while err1==1:
        print("Dostępne operacje:\n1.Podanie zakresu danych\n2.Obliczenie wartości średniej danych\n3.Export danych do pliku .csv")
        op=int(input("Prosze wybrać operację: "))
        while err2==1:
            if op==1:
                zakres(dane)
                err2=0
            elif op==2:
                wart_sr(dane)
                err2=0
            elif op==3:
                export(l_sl)
                err2=0
            else:
                op=input("Wystąpił bład, proszę ponownie wybrać operację: ")
                err2=1
        io=input("\nCzy wykonać inną operację? t/n:")
        if io=='t':
            err1=1
            err2=1
        else:
            err1=0

