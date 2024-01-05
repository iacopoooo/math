from scipy.optimize import linprog

# Funzione per controllare l'input numerico
def input_numerico(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Errore: inserisci un numero valido.")
# Funzione per controllare l'input della funzione obiettivo
def input_funzione_obiettivo(prompt):
    while True:
        input_str = input(prompt)
        try:
            return [float(num) for num in input_str.split()]
        except ValueError:
            print("Errore: inserisci solo numeri separati da spazi.")


while True:
    tipo_problema = input("Scegli il tipo di problema (min o max): ").lower()
    if tipo_problema in ['min', 'max']:
        inverti_segni = tipo_problema == 'max'
        break
    else:
        print("Errore: inserisci 'min' o 'max'.")

# Funzione per controllare l'input per i coefficienti dei vincoli
def input_coefficienti_vincolo(prompt):
    while True:
        input_str = input(prompt)
        coefficienti = input_str.split()
        if len(coefficienti) == num_variabili:
            try:
                return [float(num) for num in coefficienti]
            except ValueError:
                print("Errore: inserisci solo numeri separati da spazi.")
        else:
            print(f"Errore: devi inserire esattamente {num_variabili} coefficienti.")


# Input per la funzione obiettivo
c = input_funzione_obiettivo("Inserisci i coefficienti della funzione obiettivo separati da spazi: ")
if inverti_segni:
    c = [-num for num in c]

# Numero di vincoli
while True:
    num_vincoli = input("Inserisci il numero di vincoli: ")
    if num_vincoli.isdigit() and int(num_vincoli) > 0:
        num_vincoli = int(num_vincoli)
        break
    else:
        print("Errore: inserisci un numero intero positivo.")

A_eq = []  # Per vincoli ==
b_eq = []  # Per vincoli ==

A_ub = []  # Per vincoli <=
b_ub = []  # Per vincoli <=


# Numero di variabili
num_variabili = len(c)

# Limiti per le variabili
bounds = [(0, None)] * num_variabili
# Input per i vincoli
for i in range(num_vincoli):
    tipo_vincolo = input(f"Inserisci il tipo del vincolo {i+1} (== o <=):\nNota: per vincoli >=, inserisci i coefficienti con segno opposto: ")

    vincolo = input_coefficienti_vincolo(f"Inserisci i coefficienti per il vincolo {i+1} separati da spazi: ")
    valore_limite = input_numerico(f"Inserisci il valore limite per il vincolo {i+1}: ")

    if tipo_vincolo == '==':
        A_eq.append(vincolo)
        b_eq.append(valore_limite)
    elif tipo_vincolo == '<=':
        A_ub.append(vincolo)
        b_ub.append(valore_limite)
    else:
        print("Tipo di vincolo non riconosciuto.")


# Gestisci automaticamente se includere A_eq e b_eq
if A_eq and b_eq:  # Se A_eq e b_eq non sono vuoti
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
else:  # Se A_eq e b_eq sono vuoti
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

# Inverti il segno del valore ottimale se l'utente ha scelto la massimizzazione
if inverti_segni:
    res.fun = -res.fun
print(res)

