# **Einführung in Datenstrukturen – Teil 3: Sets**

---

## 1. Was sind Sets?

Stell dir vor, du veranstaltest ein **Mega-Festival** und erstellst eine **Gästeliste**. Du möchtest sicherstellen, dass **keine Person** doppelt aufgeführt ist – jeder Gast soll nur **einmal** auf der Liste stehen.  

**Genau hier kommen Sets ins Spiel!**  

- Ein **Set** in Python ist eine Sammlung **einzigartiger** Elemente – **Duplikate** werden automatisch ausgeschlossen.  
- Du greifst nicht über Indizes auf die Elemente zu, sondern Sets sind **ungeordnet**.  
- Jedes Set wird in **einer** Variablen gespeichert und kann eine beliebige Anzahl von Einträgen enthalten (ohne Wiederholungen).

> 💡 **Tipp**: Ein Set ist wie eine **exklusive Gästeliste** – jedes Element darf nur einmal vorkommen!

---

### ⭐ Formale Definitionen

**Definition: Set**  
> Ein *Set* ist eine **ungeordnete**, **unveränderliche** (im Sinne der Inhalte selbst, nicht der Referenz) Sammlung einzigartiger Elemente. In Python ist ein Set veränderlich, du kannst also Elemente hinzufügen oder entfernen. Aber die *Elemente* selbst müssen hashbar sein (z.B. Strings, Zahlen).

**Definition: Einzigartigkeit**  
> In einem Set kann jedes Element nur **einmal** vorkommen. Fügt man ein dupliziertes Element hinzu, wird es **stillschweigend ignoriert**.

---

## 2. Warum Sets verwenden?

- **Keine Duplikate**: Wenn du sicherstellen möchtest, dass jedes Element nur **einmal** auftaucht.  
- **Effiziente Prüfung**: Du kannst rasch überprüfen, ob ein Element im Set enthalten ist (z.B. `if gast in gaesteliste:`).  
- **Mengenoperationen**: Sets bieten dir **Schnittmengen**, **Vereinigungen** und mehr – nützlich für mathematische Aufgaben oder das Finden gemeinsamer Elemente.

**In der Festival-Welt 🎶**:  
- Deine **Festival-Gästeliste** (`gaesteliste`) enthält die Namen aller bestätigten Gäste **ohne** doppelte Einträge.  
- Du möchtest schnell checken, ob `"Max Mustermann"` schon auf der Liste steht.

```python
gaesteliste = {"Alice", "Bob", "Charlie"}
gaesteliste.add("Diana")
gaesteliste.add("Alice")  # Duplikat, wird ignoriert
print(gaesteliste)        # {"Alice", "Bob", "Charlie", "Diana"}
```

> 💡 **Tipp**: Sets sind perfekt, wenn du dich **nicht** um Reihenfolgen kümmerst, sondern nur darum, ob etwas enthalten ist oder nicht!

---

## 3. Aufbau und Funktionsweise eines Sets

### 3.1 Einzigartige Elemente

Ein Set wird in Python mit geschweiften Klammern `{}` (ähnlich wie Dictionaries) oder mit der Funktion `set()` angelegt. **Unterschied** zu Dictionaries: Es gibt **keine** Schlüssel-Wert-Paare, sondern nur **Werte**.

```python
gaesteliste = {"Alice", "Bob", "Charlie"}
# oder
gaesteliste = set(["Alice", "Bob", "Charlie"])
```

**Analogie**:  
Denk an **Eintrittsbändchen** für dein Festival – jeder Gast soll exakt **ein** Bändchen bekommen.  

---

### 3.2 Operationen mit Sets

### ⭐ Definition: Set-Operation  
> Eine *Set-Operation* ist ein Schritt wie Hinzufügen, Entfernen von Elementen oder die Durchführung von Mengenoperationen (Schnittmenge, Vereinigung, Differenz) auf einem Set.

---

1. **Element hinzufügen (add)**  
   ```python
   gaesteliste.add("Diana")
   ```
   - **Erklärung**: `add("Diana")` legt `"Diana"` ins Set, falls sie noch nicht drin ist.  

2. **Element entfernen (remove / discard)**  
   ```python
   gaesteliste.remove("Bob")     # entfernt "Bob", wirft Fehler, wenn nicht vorhanden
   gaesteliste.discard("Alice")  # entfernt "Alice", wirft KEINEN Fehler, falls nicht vorhanden
   ```
   - **Erklärung**:  
     - `remove("Bob")` löscht `"Bob"` und bricht mit einem `KeyError` ab, wenn `"Bob"` nicht drin ist.  
     - `discard("Alice")` löscht `"Alice"`, aber gibt **keinen** Fehler, falls `"Alice"` schon fehlt.  

3. **Prüfen, ob etwas enthalten ist**  
   ```python
   if "Charlie" in gaesteliste:
       print("Charlie ist eingeladen!")
   ```
   - **Erklärung**: Super einfach, um zu checken, ob ein Element bereits im Set existiert.  

4. **Schnittmenge (intersection / `&`)**  
   ```python
   premium_gaeste = {"Alice", "Bob"}
   normale_gaeste = {"Bob", "Charlie", "Diana"}
   
   gemeinsame_gaeste = premium_gaeste & normale_gaeste
   print(gemeinsame_gaeste)  # {"Bob"}
   ```
   - **Erklärung**: `&` gibt die **gemeinsamen** Einträge zurück.  

5. **Vereinigung (union / `|`)**  
   ```python
   alle_gaeste = premium_gaeste | normale_gaeste
   print(alle_gaeste)  # {"Alice", "Bob", "Charlie", "Diana"}
   ```
   - **Erklärung**: `|` kombiniert alle Elemente beider Sets (ohne Duplikate).  

6. **Differenz**  
   ```python
   nur_premium = premium_gaeste - normale_gaeste
   print(nur_premium)  # {"Alice"}
   ```
   - **Erklärung**: `-` gibt die Elemente zurück, die **nur** im linken Set sind und nicht im rechten.  

> 💡 **Tipp**: Set-Operationen sind extrem praktisch, um Überschneidungen oder Differenzen in Daten herauszufinden – zum Beispiel, wer Zugang zum VIP-Bereich (Premium-Set) und wer zum Allgemeinen Bereich (Normale-Gästeliste) hat.

🧐 **Merke**:

| **🛠️ Operation**                | **📌 Beschreibung**                                                                                                               | **✅ Beispiel**                                    |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| ➕ **Element hinzufügen**        | Fügt ein neues Element ins Set ein, falls es nicht existiert                                                                      | `gaesteliste.add("Diana")`                         |
| ❌ **Element entfernen**         | `remove()` bricht ab, wenn nicht vorhanden, `discard()` bleibt still                                                              | `gaesteliste.remove("Bob")` / `gaesteliste.discard("Alice")` |
| ❓ **Mitgliedschaft prüfen**     | Check, ob ein Element im Set ist                                                                                                  | `"Charlie" in gaesteliste`                         |
| 🔗 **Schnittmenge (`&`)**       | Gibt die **gemeinsamen** Elemente zweier Sets zurück                                                                               | `set1 & set2`                                      |
| 🔀 **Vereinigung (`|`)**         | Fasst beide Sets zusammen (ohne Duplikate)                                                                                         | `set1 | set2`                                      |
| 🌓 **Differenz (`-`)**          | Gibt die Elemente zurück, die **nur** im linken Set liegen                                                                         | `set1 - set2`                                      |

---

## 4. Beispiel: Festival-VIP-Liste 🎫

Angenommen, wir verwalten mehrere **Set-Listen**:

```python
# Gäste, die ein Premium-Ticket (VIP) haben
vip_gaeste = {"Alice", "Bob", "Eve"}

# Gäste mit normalem Ticket
normale_gaeste = {"Charlie", "Diana", "Bob"}

# 1. Element hinzufügen
vip_gaeste.add("Frank")
print("VIP-Gäste:", vip_gaeste)  
# "Frank" wird hinzugefügt

# 2. Element entfernen
normale_gaeste.discard("Bob")  
print("Normale Gäste:", normale_gaeste)
# "Bob" wird entfernt, falls vorhanden (keine Fehlermeldung)

# 3. Mitgliedschaft prüfen
if "Alice" in vip_gaeste:
    print("Alice hat ein VIP-Ticket!")

# 4. Schnittmenge: Gäste, die VIP & normal gebucht haben
beide_tickets = vip_gaeste & normale_gaeste
print("Haben zwei Tickets:", beide_tickets)

# 5. Vereinigung: Alle Gäste, egal welches Ticket
alle_gaeste = vip_gaeste | normale_gaeste
print("Alle Gäste:", alle_gaeste)
```

**Zusammengefasst**:  
- Ein Set ignoriert **Duplikate**.  
- Mit den **Mengenoperationen** findest du heraus, wer wo reingehört oder welche Listen sich überschneiden.  

---

## 5. Typische Anwendungsfälle

Sets findest du in vielen Bereichen, wo **Einzigartigkeit** oder **Mengenlogik** gefragt ist:

1. **E-Mail-Filtersysteme**  
   - Du möchtest eine Liste ungewünschter Absender verwalten (Spam-Liste) – ohne doppelte Einträge.  

2. **Hashtag-Sammlungen**  
   - In Social-Media-Apps werden oft Hashtags in Sets gespeichert, um doppelte Hashtags zu vermeiden.  

3. **Nutzerauswahl / Berechtigungen**  
   - Eine App speichert Nutzer-IDs in einem Set, um schnell zu prüfen, wer Zugriff hat (z.B. Premium vs. Standard).  

4. **Duplikate aussortieren**  
   - Du hast eine lange Liste von Einträgen, möchtest aber nur unique Werte behalten. `set(liste)` löscht automatisch alle Doppelungen.  

5. **Mathematische Aufgaben**  
   - Schnittmenge, Vereinigung, Differenz – Sets eignen sich perfekt, um zum Beispiel Mengen in einer statistischen Analyse zu behandeln.  

> 💡 **Tipp**: Immer wenn du fragen würdest: „Enthält die Sammlung dieses Element bereits?“ oder „Will ich Duplikate rausfiltern?“, dann sind **Sets** die richtige Wahl!

---

## 7. Häufige Fehler & Stolpersteine 🚨

- **Ungeordnete Struktur**: Du kannst **nicht** einfach `mein_set[0]` machen. Sets haben keine Indizes.  
- **remove vs. discard**: `remove("X")` wirft einen Fehler, wenn „X“ nicht drin ist; `discard("X")` bleibt still.  
- **Unveränderliche (hashbare) Elemente**: Du kannst z.B. keine **Listen** in ein Set packen, nur **Strings**, **Zahlen**, **Tuples** usw.

### ⛔ Zugriff über Index

```python
gaesteliste = {"Alice", "Bob"}
print(gaesteliste[0])  # FALSCH: Sets sind ungeordnet, das funktioniert nicht!
```

**Fehlermeldung**: `TypeError: 'set' object is not subscriptable`

**Richtig** wäre z.B. eine Iteration:

```python
for gast in gaesteliste:
    print(gast)
```

### 🛑 Falsche Elemente

```python
mein_set = {["Liste", "Geht", "Nicht"]}  # FALSCH
```

**Fehlermeldung**: `TypeError: unhashable type: 'list'`

**Richtig**:

```python
mein_set = {("Tuple", "Funktioniert")}
```

### ➡️ remove vs. discard

```python
gaesteliste = {"Alice", "Bob"}
gaesteliste.remove("Charlie")  # Fehler, wenn "Charlie" nicht drin ist

# Richtig mit discard:
gaesteliste.discard("Charlie")  # Ignoriert, falls nicht vorhanden
```

---

## 8. Zusammenfassung und Ausblick

Sets sind eine **mächtige** Datenstruktur in Python:

- **Keine Duplikate** – ideal, um Mehrfach-Einträge zu vermeiden.  
- **Hervorragend** für schnelle Mitgliedsprüfungen (`in`).  
- Ermöglichen dir **Mengenoperationen** (Schnittmenge, Vereinigung, Differenz).  

**Nächster Schritt**: Probier, wie du Sets mit **Listen** oder **Dictionaries** kombinieren kannst – z.B. ein Dictionary, das pro Schlüssel ein Set von Werten speichert. Außerdem lohnen sich andere Datenstrukturen wie **Stacks** oder **Queues** zu erkunden.

> 💡 **Tipp**: Hast du Listen mit vielen Duplikaten und willst sie loswerden? Einfach `set(meine_liste)`!  

---


**Viel Spaß beim Ausprobieren!**  

Probiere Sets in deinen eigenen Projekten aus – ob du **E-Mail-Adressen** ohne Dubletten sammelst, **Berechtigungen** verwaltest oder **Mengenoperationen** durchführst. Sets helfen dir, Ordnung zu halten und **Duplikate** zu vermeiden.  

**Happy Coding!** ✨