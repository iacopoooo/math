from sympy import symbols
from pulp import LpMaximize, LpMinimize, LpProblem, LpVariable, LpStatus

# Input dell'utente per il tipo di problema
tipo_problema = input("Inserisci il tipo di problema (max o min): ")
if tipo_problema.lower() == 'max':
    tipo_problema = LpMaximize
elif tipo_problema.lower() == 'min':
    tipo_problema = LpMinimize
else:
    print("Tipo di problema non valido. Terminazione del programma.")
    exit()

# Creazione di un problema di programmazione lineare
problem = LpProblem("Problema_di_Programmazione_Lineare", tipo_problema)

# Input dell'utente per la funzione obiettivo
funzione_obiettivo = input("Inserisci la funzione obiettivo (es. 3*x + 2*y): ")
variabili = [str(var) for var in symbols(funzione_obiettivo)]

# Creazione delle variabili
var_dict = LpVariable.dicts("Variabile", variabili, lowBound=0)

# Definizione della funzione obiettivo
problem += sum(var_dict[var] * coef for var, coef in zip(variabili, [int(c) if c.isdigit() or (c[0]=='-' and c[1:].isdigit()) else 1 for c in funzione_obiettivo.split() if c.isdigit() or (c[0]=='-' and c[1:].isdigit())])), "Funzione_Obiettivo"

# Input dell'utente per le restrizioni
while True:
    restrizione = input("Inserisci una restrizione (o premi invio per terminare): ")
    if not restrizione:
        break
    constraint_parts = restrizione.split()
    coefficients = [int(c) if c.isdigit() or (c[0]=='-' and c[1:].isdigit()) else 1 for c in constraint_parts if c.isdigit() or (c[0]=='-' and c[1:].isdigit())]
    rhs_value = int(constraint_parts[-1])
    if tipo_problema == LpMinimize:
        problem += sum(var_dict[var] * coef for var, coef in zip(variabili, coefficients)) >= rhs_value, f"Restrizione_{len(problem.constraints)}"
    else:
        problem += sum(var_dict[var] * coef for var, coef in zip(variabili, coefficients)) <= rhs_value, f"Restrizione_{len(problem.constraints)}"

# Risoluzione del problema
problem.solve()

# Stampa dei risultati
print("Stato:", LpStatus[problem.status])
print("Valore ottimale:", problem.objective.value())
for var in var_dict:
    print(f"Valore di {var}:", var_dict[var].value())


    #ci siamo quasiii
