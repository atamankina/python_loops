pizza_price = float(input("Wie viel kostet eine Pizza? "))
number_pieces = int(input("Wie viele Stuecke von Pizza wurden gegessen? "))

pieces_eaten = {}
pieces_eaten_total = 0

while True:
    name = input("Was ist der Name der Person? (schreibe 'fertig', um die Eingabe zu beenden) ")

    if name == "fertig":
        break

    pieces_per_person = int(input("Wie viele Stuecke hat diese Person gegessen? "))
    pieces_eaten[name] = pieces_per_person
    pieces_eaten_total += pieces_per_person

print("Sie haben folgende Daten eingetragen:")
print(f"Pizzapreis: {pizza_price}")
print(f"Anzahl Stuecke: {number_pieces}")
print(f"Dictionary: {pieces_eaten}")

if pieces_eaten_total > number_pieces:
    print(f"Fehler, Anzahl gegessenen Stuecke {pieces_eaten_total} groesser als gesamte Stuecke {number_pieces}.")
    exit()

price_per_piece = pizza_price / number_pieces

print("Die Rechnungen sind wie folgt:")
for person in pieces_eaten:
    bill = round(price_per_piece * pieces_eaten[person], 2)
    print(f"{person} hat {pieces_eaten[person]} Stueck Pizza gegessen. Zu zahlen sind {bill}.")
