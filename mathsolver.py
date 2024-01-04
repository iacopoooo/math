import wolframalpha

#MATEMATICA

# Sostituisci 'YOUR_APP_ID' con il tuo AppID ottenuto da Wolfram Alpha
app_id = 'HRQYHE-R8R5U3HGVG'
client = wolframalpha.Client(app_id)

def query_wolframalpha(query):
    try:
        res = client.query(query)
        return next(res.results).text
    except StopIteration:
        return "Non ho trovato risposte a questa domanda."
    except Exception as e:
        return f"Errore durante la query: {e}"

# Input dell'utente per l'equazione da risolvere
equation_input = input("Inserisci un'equazione da risolvere: ")

# Esegui la query utilizzando l'equazione inserita
result = query_wolframalpha(equation_input)
print(result)
