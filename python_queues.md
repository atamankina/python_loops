# **Einführung in Datenstrukturen – Bonus-Kapitel: Listen als Queues**

---

## 1. Was ist eine Queue?

Stell dir eine **Warteschlange** vor – zum Beispiel im Supermarkt. **Der erste** Kunde in der Schlange wird **zuerst** bedient, während neue Kunden sich **hinten** anstellen. Diesen Vorgang nennt man **Queue**:

- Das Motto einer Queue lautet: **„First In – First Out (FIFO)“**.  
- Das **erste** Element, das hinzukommt, wird als **erstes** wieder entfernt (wie in einer realen Schlange: Wer zuerst da war, geht auch zuerst weg).

> 💡 **Tipp**: Eine Queue ist wie eine **Schlange** im Kino oder Supermarkt: Hinten stellen sich neue Leute an, vorne verlässt einer nach dem anderen die Schlange.

---

### ⭐ Formale Definition: Queue

> Eine *Queue* ist eine Datenstruktur, bei der das **Hinzufügen** (enqueue) am Ende stattfindet, und das **Entfernen** (dequeue) am Anfang – **FIFO**-Prinzip.

---

## 2. Warum Listen als Queues verwenden?

In Python kannst du eine **Liste** grundsätzlich als Queue verwenden, indem du:

- **append()** nutzt, um **hinten** ein Element anzuhängen (das Enqueue).  
- **pop(0)** nutzt, um das **erste** Element zu entfernen (das Dequeue).

**Vorteile**:

1. **Intuitiv**: Die Aktionen `append()` und `pop(0)` beschreiben genau das Hinten-Anstellen und Vorn-Wegnehmen.  
2. **FIFO-Prinzip**: Perfekt, um Warteschlangen oder Auftragslisten zu verwalten.

**In der Spielewelt 🕹**:

- Du könntest eine **Auftragsliste** für NPCs programmieren: Eine Liste an Aktionen, die sie abarbeiten. Die **älteste** Aktion (ganz vorne) wird als erste erledigt, neue Befehle kommen **hinten** rein.

> ⚠️ **Achtung**: `pop(0)` ist bei großen Listen **nicht** sehr effizient, da alle Elemente umgeschoben werden müssen. Für professionelle Anwendungen nutzt man oft `collections.deque`, aber zum Lernen reicht eine Liste.

---

## 3. Aufbau und Funktionsweise einer Queue mit Listen

### 3.1 Enqueue (append)

Wenn du in einer Queue ein neues Element **hinten** anstellst, nennt man das in vielen Sprachen „enqueue“. In Python geht das per:

```python
queue = []
queue.append("Erster Kunde")   # enqueue
queue.append("Zweiter Kunde")
print(queue)  # ["Erster Kunde", "Zweiter Kunde"]
```

- Du hängst den neuen „Kunden“ (oder das neue Item) ans **Ende** der Liste.

### 3.2 Dequeue (pop(0))

Möchtest du das **vorderste** Element entfernen und zurückgeben, rufst du `pop(0)` auf:

```python
entfernt = queue.pop(0)  # entfernt "Erster Kunde"
print(entfernt)          # "Erster Kunde"
print(queue)             # ["Zweiter Kunde"]
```

- `pop(0)` entfernt das **erste** Element (Index 0) der Liste.  
- Das **entfernte Element** wird zurückgegeben.

> 💡 **Tipp**: `pop(0)` ist die **Simulation** des FIFO-Prinzips. Nur beachte, dass dies in einer normalen Python-Liste ineffizient sein kann, da die restlichen Elemente nachrücken müssen.

---

## 4. Beispiel: Kundenwarteschlange im Shop

Angenommen, wir wollen eine kleine **Kundenwarteschlange** simulieren, in der Kunden ankommen und bedient werden:

```python
def kunde_kommt(queue, kunde):
    queue.append(kunde)
    print(f"{kunde} hat sich angestellt.")

def kunde_bedienen(queue):
    if queue:
        bedient = queue.pop(0)
        print(f"{bedient} wird bedient und verlässt die Schlange.")
    else:
        print("Niemand da zum Bedienen.")

def main():
    warte_schlange = []

    kunde_kommt(warte_schlange, "Alice")
    kunde_kommt(warte_schlange, "Bob")
    kunde_kommt(warte_schlange, "Charlie")

    kunde_bedienen(warte_schlange)  # Alice verlässt die Schlange
    kunde_bedienen(warte_schlange)  # Bob verlässt die Schlange
    kunde_bedienen(warte_schlange)  # Charlie verlässt die Schlange
    kunde_bedienen(warte_schlange)  # Schlange ist leer

if __name__ == "__main__":
    main()
```

**Zusammengefasst**:  
- Du speicherst alle Kunden in einer Liste.  
- Mit `append()` (enqueue) stellst du neue Kunden an.  
- Mit `pop(0)` (dequeue) bedienst du den **ersten** Kunden.

---

## 5. Häufige Anwendungsfälle für Queues

1. **Warteschlangen & Bestellsysteme**  
   - Sei es eine **Kundenliste** im Supermarkt oder Aufträge in einer Druckerwarteschlange – überall, wo eine faire Reihenfolge (FIFO) wichtig ist.

2. **Echtzeit-Datenstreams**  
   - Wenn du eingehende Ereignisse (Events) in der Reihenfolge verarbeiten möchtest, in der sie eintreffen.

3. **Breitensuche (Breadth-First Search) in Graphen**  
   - In der Algorithmik wird eine Queue verwendet, um Knoten nacheinander zu verarbeiten.

4. **Netzwerk-Puffer**  
   - Datenpakete kommen an und werden in einer Warteschlange gehalten, bis sie verarbeitet werden.

> 💡 **Tipp**: Überall, wo das **FIFO**-Prinzip gilt („Wer zuerst kommt, wird zuerst bedient“), passt eine Queue perfekt.

---

## 6. Aktivität: „Befehle abarbeiten!“

### 🏆 Aufgabe

Implementiere eine Funktion, die eingehende **Befehle** in einer Queue speichert und der Reihe nach abarbeitet:

1. `befehl_hinzufuegen(queue, befehl)`: Legt einen neuen Befehl in die Queue.  
2. `befehl_ausfuehren(queue)`: Nimmt den **ersten** Befehl raus und führt ihn aus – falls keiner vorhanden ist, Hinweis `"Keine Befehle in der Warteschlange!"`.  
3. `queue_anzeigen(queue)`: Zeigt den aktuellen Inhalt der Queue an (in Reihenfolge).

**Mustergerüst**:

```python
def befehl_hinzufuegen(queue, befehl):
    # TODO: enqueue

def befehl_ausfuehren(queue):
    # TODO: dequeue und ausführen

def queue_anzeigen(queue):
    # TODO: gesamten Inhalt zeigen

def main():
    befehle_queue = []

    befehl_hinzufuegen(befehle_queue, "Bewegung nach Norden")
    befehl_hinzufuegen(befehle_queue, "Angreifen")
    befehl_hinzufuegen(befehle_queue, "Heiltrank trinken")

    queue_anzeigen(befehle_queue)

    befehl_ausfuehren(befehle_queue)
    befehl_ausfuehren(befehle_queue)
    queue_anzeigen(befehle_queue)

if __name__ == "__main__":
    main()
```

> 💡 **Tipp**: Überprüfe immer, ob die Queue leer ist, bevor du `pop(0)` aufrufst.

---

## 7. Häufige Fehler & Stolpersteine 🚨

1. **Einsatz von `pop()` statt `pop(0)`**  
   - `pop()` ohne Argument nimmt das **letzte** Element (LIFO wie ein Stack) – das wäre falsch für eine Queue.  
2. **Leere Queue**  
   - Ein leerer `pop(0)` führt zu `IndexError`. Prüfe, ob die Liste nicht leer ist (`if queue:`).  
3. **Leistungsprobleme**  
   - `pop(0)` ist in einer Python-Liste **O(n)**, weil alle Elemente danach eine Position verschieben müssen. Für große Datenmengen lieber `collections.deque` verwenden, das `popleft()` in O(1) realisiert.

---

## 8. Zusammenfassung und Ausblick

Mit **Listen** kannst du in Python eine **Queue** simulieren:

- **`append()`** = **enqueue** (Element hinten anhängen).  
- **`pop(0)`** = **dequeue** (erstes Element entfernen).  
- Ideal für das **FIFO**-Prinzip, z.B. Warteschlangen, Bestelllisten, BFS in Graphen usw.

**Nächster Schritt**: Wenn du Queues verstanden hast, solltest du schauen, wann sich eine echte **`deque`** (Double-Ended Queue) aus dem Modul `collections` lohnt: Sie löst das **Performanceproblem** bei `pop(0)`.

> 💡 **Tipp**: In vielen Anwendungen gilt: Wenn du eine Warteschlange brauchst, nimm eine **`deque`**. Zum Lernen jedoch hilft es, das Prinzip erst einmal mit einer Liste zu verstehen!

---

**Viel Erfolg beim Schlangestehen!**  

Mit diesem Kapitel kennst du nun **Stacks** (LIFO) und **Queues** (FIFO) in ihrer einfachsten Umsetzung per Python-Liste. Abhängig vom Szenario kannst du damit wichtige Probleme lösen – ob in Games, Simulationsmodellen oder Systemwarteschlangen.  

**Happy Coding!** ✨