# **Einführung in Datenstrukturen – Bonus-Kapitel: Listen als Stacks**

---

## 1. Was ist ein Stack?

Stell dir vor, du hast einen **Stapel** mit Karten oder Büchern. Du legst immer **oben** ein neues Buch drauf und nimmst das **oberste** Buch wieder ab. So ein Stapel heißt in der Programmierung **Stack**.

- Das Motto eines Stacks lautet: **„Last In – First Out (LIFO)“**.  
- Das **letzte** Element, das hinzukommt, wird als **erstes** wieder entfernt.

> 💡 **Tipp**: Ein Stack ist wie ein Stapel Teller in der Cafeteria – du nimmst immer nur den **obersten** Teller.

---

### ⭐ Formale Definition: Stack

> Ein *Stack* ist eine Datenstruktur, bei der das **Hinzufügen** (push) und **Entfernen** (pop) nur am „oberen“ Ende stattfindet – **LIFO**-Prinzip.

---

## 2. Warum Listen als Stacks verwenden?

In Python kannst du eine **Liste** problemlos als Stack benutzen:

- **append()** fügt ein Element **am Ende (oben)** an.  
- **pop()** entfernt das **letzte (oberste)** Element.  

**Vorteile**:

1. **Intuitiv**: Die Aktionen `append()` (Push) und `pop()` (Pop) sind leicht zu merken.  
2. **Perfekt für LIFO-Aufgaben**: z.B. Rückgängig-Listen (Undo-Funktionen), Rekursionen verwalten, Syntax-Prüfungen (Klammern in Quelltexten), u.v.m.  

**In der Spielewelt 🕹**:  
- Du könntest eine **„Aktions-Historie“** als Stack speichern. Die zuletzt getätigte Aktion (z.B. Tür öffnen, Item aufheben) kann als erstes rückgängig gemacht werden.

---

## 3. Aufbau und Funktionsweise eines Stacks mit Listen

### 3.1 Push (append)

Wenn du bei einem Stack ein neues Element **oben** auflegst, nennt man das in vielen Sprachen „push“. In Python kannst du das ganz einfach so machen:

```python
stack = []
stack.append("Erstes Element")  # push
stack.append("Zweites Element")
print(stack)  # ["Erstes Element", "Zweites Element"]
```

- Die Liste wächst nach hinten, sodass das „obenliegende“ Element am Ende der Liste steht.

### 3.2 Pop (pop)

Möchtest du das **oberste** Element vom Stack nehmen, nutzt du `pop()` in Python:

```python
entfernt = stack.pop()  # entfernt "Zweites Element"
print(entfernt)         # "Zweites Element"
print(stack)            # ["Erstes Element"]
```

- `pop()` ohne Index entfernt das letzte Element der Liste.  
- Das **entfernte Element** wird zurückgegeben.

> 💡 **Tipp**: Wenn du einen echten Stack-Effekt möchtest, füge Elemente **nur** mit `append()` hinzu und entferne sie **nur** mit `pop()`. Andere Listenmethoden (z.B. `insert()`) widersprechen dem reinen Stack-Prinzip.

---

## 4. Beispiel: Rückgängig-Funktion („Undo“) im Spiel

Angenommen, du programmierst ein Spiel, in dem der Spieler verschiedene Aktionen ausführen kann. Du möchtest eine **Undo-Funktion** implementieren, die immer die **zuletzt** ausgeführte Aktion rückgängig macht:

```python
def mache_aktion(stack, aktion):
    stack.append(aktion)
    print(f"Aktion '{aktion}' ausgeführt.")

def rueckgaengig(stack):
    if stack:
        letzte_aktion = stack.pop()
        print(f"Aktion '{letzte_aktion}' rückgängig gemacht.")
    else:
        print("Keine Aktion zum Rückgängig machen.")

def main():
    aktions_stapel = []

    # Spieler macht Aktionen
    mache_aktion(aktions_stapel, "Tür öffnen")
    mache_aktion(aktions_stapel, "Item aufheben")
    mache_aktion(aktions_stapel, "Hebel ziehen")

    # Rückgängig
    rueckgaengig(aktions_stapel)  # Hebel ziehen rückgängig
    rueckgaengig(aktions_stapel)  # Item aufheben rückgängig
    rueckgaengig(aktions_stapel)  # Tür öffnen rückgängig
    rueckgaengig(aktions_stapel)  # Nichts mehr da

if __name__ == "__main__":
    main()
```

**Zusammengefasst**:  
- Du speicherst alle **Aktionen** in einem **Stapel** (Liste).  
- Mit `append()` legst du neue Aktionen obendrauf.  
- Mit `pop()` nimmst du die **zuletzt** hinzugefügte Aktion wieder weg und kannst sie rückgängig machen.

---

## 5. Häufige Anwendungsfälle für Stacks

1. **Undo-/Rückgängig-Funktion**  
   - Texteditoren, Grafikprogramme, Spiele – überall brauchst du eine **Historie**, die du von oben rückwärts abarbeitest.

2. **Klammer- oder Syntaxprüfungen**  
   - Solltest du Quelltext auf korrekte Klammern prüfen, legst du jede geöffnete Klammer auf den Stack und nimmst sie ab, sobald du eine passende schließende Klammer findest.

3. **Aufruf-Stack in der Programmierung**  
   - Bei Funktionen, die sich gegenseitig aufrufen, nutzt Python intern auch einen Stack für die **Funktionsrahmen** (Call Stack).

4. **Backtracking-Algorithmen**  
   - Wenn du in einer Suche den Weg zurückverfolgen musst (z.B. Labyrinth), ist der Stack ein ideales Hilfsmittel, um die zuletzt gewählte Abzweigung zurückzunehmen.

> 💡 **Tipp**: Überall, wo das **LIFO**-Prinzip gilt („Zuletzt rein, zuerst raus“), passt ein Stack perfekt.

---

## 7. Häufige Fehler & Stolpersteine 🚨

1. **Benutzen von `insert(0, ...)`**  
   - So würdest du Elemente „unten“ in der Liste einfügen – das entspricht **nicht** dem LIFO-Prinzip eines Stacks.  
2. **Index-Fehler bei Pop**  
   - Ein leerer Stack (`[]`) kann kein Element mehr liefern. Prüfe vorher mit `if stack:` oder fang die **Exception** (IndexError) ab.  
3. **Verwechslung mit Queues**  
   - Ein Stack nimmt immer das **letzte** Element (LIFO). Eine **Queue** entfernt das **erste** (FIFO). Das sind verschiedene Prinzipien.

---

## 8. Zusammenfassung und Ausblick

Mit **Listen** kannst du in Python einen **Stack** sehr einfach simulieren:

- **`append()`** = **Push** (Element oben drauflegen).  
- **`pop()`** = **Pop** (oberstes Element entfernen).  
- Überall einsetzbar, wo LIFO das Ziel ist (Undo-Funktion, Rückverfolgung usw.).  

**Nächster Schritt**: Wenn du Stacks verstanden hast, kannst du auch andere abstrahierte Datenstrukturen wie **Queues** (Warteschlangen, FIFO-Prinzip) oder komplexere Strukturen (z.B. **Bäume**, **Graphen**) erkunden.

> 💡 **Tipp**: Das Stack-Prinzip ist extrem nützlich und wird dir in vielen Algorithmen und Programmlogiken begegnen. Halte Ausschau nach dem „Zuletzt rein, zuerst raus“-Muster!

---

**Viel Spaß beim Stapeln!**  

Egal ob du einen **Undo-Mechanismus** baust oder einfache **Zwischenspeicher** verwaltest – Stacks sind ein grundlegendes Werkzeug. Mit Python-Listen hast du bereits alles Nötige an Bord, um das LIFO-Prinzip umzusetzen.  

**Happy Coding!** ✨