##############################################
#@COMMENTI
#@TIPS
#@OPERAZIONI ARITMETICHE
#@OPERATORE +=
#@VARIABILI
#@MODULO OPERATOR %
#@INTERI
#@CONCATENAZIONE DI STRINGHE
#@PRINT
#@ESEMPIO CODICE Negozio
#@INPUT
##############################################


##############################################
# COMMENTI
##############################################
# Un commento è un pezzo di testo all'interno di un programma che non viene eseguito. Può essere utilizzato per fornire informazioni aggiuntive per facilitare la comprensione del codice.

# Il #carattere viene utilizzato per iniziare un commento e continua fino alla fine della riga.
# I commenti sono delle informazioni aggiuntive, completamente ignorate
# dall’interprete Python, e si utilizzano generalmente per dare informazioni

# '# Comment on a single line'
 
# user = "JDoe" # Comment after code

##############################################


##############################################
# OPERAZIONI ARITMETICHE
##############################################
# Python supporta diversi tipi di operazioni aritmetiche che possono essere eseguite su numeri letterali, variabili o qualche combinazione. Gli operatori aritmetici primari sono:

# + per aggiunta
# - per sottrazione
# * per la moltiplicazione
# / per divisione
# % per modulo (restituisce il resto)
# ** per l'elevamento a potenza


# Arithmetic operations
 
# result = 10 + 30
# result = 40 - 10
# result = 50 * 5
# result = 16 / 4
# result = 25 % 2
# result = 5 ** 3
##############################################


##############################################
# OPERATORE +=
##############################################
# L'operatore più uguale a +=fornisce un modo conveniente per aggiungere un valore a una variabile esistente e assegnare il nuovo valore alla stessa variabile. 
# Nel caso in cui la variabile e il valore siano stringhe, questo operatore esegue la concatenazione di stringhe invece dell'addizione.

# L'operazione viene eseguita sul posto, il che significa che verrà aggiornata anche qualsiasi altra variabile che punta alla variabile in fase di aggiornamento.
##############################################


##############################################
#TIPS
##############################################
# aggiuntive o spiegare lo scopo/funzionamento di un blocco di codice.(Cntr+ k) In visual studio code
##############################################


# Comandi base :

#VARIABILE
# La definizione di una variabile in Python non richiede che essa venga definita
# prima dell’utilizzo né che ne venga specificato il tipo di valore.

# variabile = 10
# variabile = “Hello Python”
# variabile = [1, 2, 3]

################################################################################################
#VARIABILI
################################################################################################
# Una variabile viene utilizzata per memorizzare i dati che verranno utilizzati dal programma. Questi dati possono essere un numero, una stringa, 
# un valore booleano, un elenco o un altro tipo di dati. Ogni variabile ha un nome che può essere composto da lettere, numeri e il carattere di sottolineatura _.

# Il segno di uguale =viene utilizzato per assegnare un valore a una variabile. Dopo l'assegnazione iniziale, il valore di una variabile può essere aggiornato a nuovi valori secondo necessità.


# These are all valid variable names and assignment
 
# user_name = "@sonnynomnom"
# user_id = 100
# verified = False
 
# A variable's value can be changed after assignment
 
# points = 100
# points = 120

# Python permette l’assegnamento multiplo delle variabili, cioè la possibilità di
# inizializzare più variabili sulla stessa riga di codice:

a, b = 10, 20

# L’assegnazione multipla permette anche di scambiare (swap) i valori di due
# variabili in maniera molto semplice:

c= 30
d= 40

#dopo questa istruzione a vale 8 e b 3
a, b = b, a

messaggio= "Variabile string"

#dichiarazione variabile int
an_int = 2

#dichiarazione variabile float
a_float = 2.1
coffee_price = 1.50
number_of_coffees = 4

#Concatenazione

greeting_text = "Hey there!"
question_text = "How are you doing?"
full_text = greeting_text + question_text

# First we have a variable with a number saved
number_of_miles_hiked = 12
 
# Then we need to update that variable
# Let's say we hike another two miles today
# Un grande aiuto, da tenere in estreama considerazione !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
number_of_miles_hiked += 2
hike_caption = "What an amazing time to walk through nature!"
# Almost forgot the hashtags!
#Funziona anche con le stringhe,gli int,float.
hike_caption += " #nofilter"
hike_caption += " #blessed"
#Molitiplicare una variabile non ne cambia il contenuto
ciccio= number_of_coffees * 4
#risultato 4 caffe


# We've defined the variable "meal" here to the name of the food we ate for breakfast!
meal = "An english muffin"

# Printing out breakfast
print("Breakfast:")
print(meal)

# Now update meal to be lunch!
meal = "pizza"

# Printing out lunch
print("Lunch:")
print(meal)

# Now update "meal" to be dinner

# Printing out dinner
print("Dinner:")

# Le stringhe Python sono molto flessibili, ma se proviamo a creare una stringa che occupa più righe ci troviamo faccia a faccia con un file SyntaxError.
# Python offre una soluzione: stringhe multilinea . Usando tre virgolette ( """o ''') invece di una, diciamo al programma che la stringa non finisce fino alla successiva virgoletta tripla.
leaves_of_grass = """
Poets to come! orators, singers, musicians to come!
Not to-day is to justify me and answer what I am for,
But you, a new brood, native, athletic, continental, greater than
  before known,
Arouse! for you must justify me.
"""
################################################################################################


##############################################
# MODULO OPERATOR %
##############################################

# Un calcolo modulo restituisce il resto di una divisione tra il primo e il secondo numero. Per esempio:

# Il risultato dell'espressione 4 % 2risulterebbe nel valore 0, perché 4 è uniformemente divisibile per 2 senza lasciare resto.
# Il risultato dell'espressione 7 % 3restituirà 1, perché 7 non è divisibile in modo uniforme per 3, lasciando un resto di 1.

# Modulo operations
 
# zero = 8 % 4
 
# nonzero = 12 % 5
##############################################


##############################################
# INTERI
##############################################
# Un numero intero è un numero che può essere scritto senza una parte frazionaria (senza decimali).
#  Un numero intero può essere un numero positivo, un numero negativo o il numero 0 purché non sia presente una parte decimale.

# Il numero 0rappresenta un valore intero ma lo stesso numero scritto che 0.0rappresenterebbe un numero in virgola mobile

# Example integer numbers
 
# chairs = 4
# tables = 1
# broken_chairs = -2
# sofas = 0
 
# Non-integer numbers
 
# lights = 2.5
# left_overs = 0.0
##############################################


##############################################
# CONCATENAZIONE DI STRINGHE
##############################################
# Python supporta l'unione (concatenazione) di stringhe utilizzando l' +operatore. L' +operatore viene utilizzato anche per le operazioni di addizione matematica. 
# Se i parametri passati +all'operatore sono stringhe, verrà eseguita la concatenazione.
# Se il parametro passato per +avere tipi diversi, Python segnalerà una condizione di errore. È possibile unire più variabili o stringhe letterali utilizzando l' +operatore.


# String concatenation
 
# first = "Hello "
# second = "World"
 
# result = first + second
 
# long_result = first + second + "!"
##############################################


##############################################
# STRINGHE
##############################################
# Una stringa è una sequenza di caratteri (lettere, numeri, spazi o punteggiatura) racchiusi tra virgolette. Può essere racchiuso utilizzando le virgolette doppie "o le virgolette singole '.

# Se una stringa deve essere suddivisa in più righe, il carattere barra rovesciata \può essere utilizzato per indicare che la stringa continua sulla riga successiva.


# user = "User Full Name"
# game = 'Monopoly'
 
# longer = "This string is broken up \
# over multiple lines"
##############################################


##############################################
# NUMERI IN VORGOLA MOBILE
##############################################
# Alle variabili Python possono essere assegnati diversi tipi di dati. Un tipo di dati supportato è il numero in virgola mobile. Un numero in virgola mobile è un valore che contiene una parte decimale. 
# Può essere utilizzato per rappresentare numeri che hanno quantità frazionarie. 
# Ad esempio, a = 3/5non può essere rappresentato come un numero intero, quindi alla variabile aviene assegnato un valore in virgola mobile di 0.6.


# Floating point numbers
 
# pi = 3.14159
# meal_cost = 12.99
# tip_percent = 0.20
 
##############################################


##############################################
#PRINT
##############################################

# La print()funzione viene utilizzata per inviare testo, numeri o altre informazioni stampabili alla console.

# Richiede uno o più argomenti e restituirà ciascuno degli argomenti alla console separati da uno spazio. Se non vengono forniti argomenti, la print()funzione emetterà una riga vuota
print("C\'amma fa mal") #Typing \" is actually typing out an escape sequence: the result of the sequence being a single "
print(leaves_of_grass)
print(meal)
print(a,b,d,messaggio)
print(an_int + 3)
#Si possono eseguire calcoli nel print()
# Prints "500"
print(573 - 74 + 1)
# Prints "50"
print(25 * 2)
# Prints "2.0"
print(10 / 5)
# Prints "6.0"
print(coffee_price * number_of_coffees)
# Prints "1.5"
print(coffee_price)
# Prints "4"
print(number_of_coffees)

# Updating the price 
coffee_price = 2.00
 
# Prints "8.0"
print(coffee_price * number_of_coffees)
# Prints "2.0"
print(coffee_price)
# Prints "4"
print(number_of_coffees)

# 2 to the 10th power, or 1024
print(2 ** 10)
 
# We can even perform fractional exponents
# 4 to the half power, or 2
print(4 ** 0.5)

#Stampa modulo "%"

# Prints 4 because 29 / 5 is 5 with a remainder of 4
print(29 % 5)
 
# Prints 2 because 32 / 3 is 10 with a remainder of 2
print(32 % 3)
 
# Modulo by 2 returns 0 for even numbers and 1 for odd numbers
# Prints 0
print(44 % 2)

print(full_text)
print(number_of_miles_hiked)
print(hike_caption)

######################################
#ESEMPIO CODICE Negozio
######################################
lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""
lovely_loveseat_price=254.00

stylish_settee_description ="""
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""

stylish_settee_price=180.50

luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""
luxurious_lamp_price =52.15

sales_tax = 0.088

customer_one_total=0

customer_one_itemization =""

customer_one_total+=lovely_loveseat_price
customer_one_itemization+=lovely_loveseat_description
customer_one_total+=luxurious_lamp_price
customer_one_itemization+=luxurious_lamp_description
customer_one_tax =customer_one_total * sales_tax
customer_one_total+sales_tax

print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)
######################################

#####################
#INPUT
#####################

# Mentre produciamo il valore di una variabile usando print(), assegniamo informazioni a una variabile usando input().
# La input()funzione richiede un messaggio di prompt, che stamperà per l'utente prima che inserisca le nuove informazioni. Per esempio:

likes_snakes = input("Do you like snakes? ")

#####################
#FUNZIONI
#####################

# Una funzione è una raccolta di diverse righe di codice. Con chiamando una funzione, che possiamo chiamare tutte queste righe di codice in una sola volta, senza dover ripetere noi stessi.

# Quindi, una funzione è uno strumento che puoi usare più e più volte per produrre un output coerente da input diversi.

# Abbiamo già imparato a conoscere una funzione, chiamata print. Sappiamo che chiamiamo printusando questa sintassi:

# print(something_to_print)