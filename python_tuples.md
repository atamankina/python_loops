# **Einführung in Datenstrukturen – Teil 4: Tuples**

---

## 1. Was sind Tuples?

Stell dir vor, du möchtest **mehrere Werte** speichern, die stets **zusammen** gehören und sich **nie** (oder nur sehr selten) ändern sollen. In einem Videospiel könntest du z.B. die **Position** eines Spielers als `(x, y)` festlegen, wo beide Koordinaten **fest miteinander** verbunden sind.

**Genau hier kommen Tuples (Tupel) ins Spiel!**  

- Ein **Tuple** ist eine **geordnete** Sammlung von Elementen, so ähnlich wie eine Liste.  
- **Unterschied**: Tuples sind in Python **unveränderlich** (*immutable*). Das bedeutet, du kannst nicht einfach ein neues Element hinzufügen, entfernen oder überschreiben, nachdem das Tuple erstellt wurde.  
- Jedes Tuple wird in **einer** Variablen gespeichert und kann mehrere Werte verschiedener Datentypen enthalten, genau wie Listen.

> 💡 **Tipp**: Ein Tuple ist wie ein **Koordinatenpunkt** – du speicherst `(x, y)` und möchtest diese Koordinaten nicht versehentlich verändern.

---

### ⭐ Formale Definitionen

**Definition: Tuple**  
> Ein *Tuple* ist eine **geordnete** Folge von Elementen, die unveränderlich ist. Du kannst die Größe und die Werte nach Erzeugung nicht mehr anpassen.

**Definition: Unveränderlichkeit (Immutability)**  
> „Unveränderlich“ bedeutet, dass du einem Tuple **keine** neuen Elemente hinzufügen, vorhandene Werte entfernen oder Elemente an bestimmten Positionen überschreiben kannst.

---

## 2. Warum Tuples verwenden?

- **Datenkonsistenz**: Wenn du sicherstellen willst, dass bestimmte Werte **zusammen** gehören und sich nicht (versehentlich) ändern dürfen.  
- **Schneller Zugriff**: Du kannst per Index auf die einzelnen Elemente zugreifen (z.B. `mein_tuple[0]`).  
- **Gute Lesbarkeit**: Tuples sind hervorragend geeignet, um **Festwerte** oder **Konstanten** darzustellen.  

**In der Spielewelt 🕹**:  

- Du könntest z.B. die **Start- und Endposition** eines Gegners in `(start_x, start_y)` und `(end_x, end_y)` speichern – so weißt du, dass es sich um **zusammengehörige Koordinaten** handelt, die du nicht aus Versehen ändern solltest.  

```python
position = (10, 20)
print(position[0])  # 10
print(position[1])  # 20
```

> 💡 **Tipp**: Nutze Tuples, wenn du Werte als „Paket“ an Funktionen weitergeben oder zurückgeben möchtest, ohne dass sie nachträglich verändert werden.

---

## 3. Aufbau und Funktionsweise eines Tuples

### 3.1 Erstellung eines Tuples

Ein Tuple wird in Python meistens in runden Klammern geschrieben, z.B. `(` und `)`:

```python
position = (10, 20)
farben = ("Rot", "Grün", "Blau")
```

> Du kannst auch einfach Kommas verwenden (ohne Klammern), z.B. `mein_tuple = 10, 20`, aber die runden Klammern machen den Code **lesbarer**.

### 3.2 Zugriff über Index

Tuples sind **geordnete** Sequenzen, daher kannst du mit Indexzugriff (genau wie bei Listen) auf Elemente zugreifen:

```python
farben = ("Rot", "Grün", "Blau")
print(farben[0])  # "Rot"
print(farben[1])  # "Grün"
print(farben[2])  # "Blau"
```

- In Python beginnt der Index bei 0.  
- Du kannst jedoch nicht `farben[0] = "Gelb"` machen, weil das Tuple **unveränderlich** ist.

### 3.3 Unveränderbarkeit (Immutable)

Versuchst du einen Wert in einem Tuple zu ändern, kommt eine Fehlermeldung:

```python
farben = ("Rot", "Grün", "Blau")
farben[0] = "Gelb"  # FALSCH → TypeError
```

> **Hintergrund**: Tuples sind bewusst so designed, dass du sie nach Erstellung **nicht** verändern kannst.

---

## 4. Wichtige Tuple-Operationen

### ⭐ Definition: Tuple-Operation
> Eine *Tuple-Operation* ist eine Handlung wie das Auslesen von Elementen, das Zerlegen (Unpacking) oder das Zusammenfügen mehrerer Tuples.

---

1. **Indexzugriff**  
   ```python
   print(farben[1])  # "Grün"
   ```
   - **Erklärung**: Du kannst das 2. Element ausgeben, darfst es aber nicht überschreiben.

2. **Länge abfragen (len)**  
   ```python
   farben = ("Rot", "Grün", "Blau")
   print(len(farben))  # 3
   ```
   - **Erklärung**: `len(farben)` zeigt, wie viele Elemente das Tuple hat.

3. **„Unpacking“**  
   ```python
   farbe1, farbe2, farbe3 = farben
   # farbe1 → "Rot", farbe2 → "Grün", farbe3 → "Blau"
   ```
   - **Erklärung**: Damit kannst du ein Tuple automatisch in mehrere Variablen aufteilen.  

4. **Konkatenation (Zusammenfügen)**  
   ```python
   tuple1 = (1, 2)
   tuple2 = (3, 4)
   tuple3 = tuple1 + tuple2
   print(tuple3)  # (1, 2, 3, 4)
   ```
   - **Erklärung**: `+` ergibt ein **neues** Tuple, da Tuples selbst ja nicht verändert werden können.

5. **Nach Elementen suchen (in)**  
   ```python
   if "Grün" in farben:
       print("Grün ist enthalten.")
   ```
   - **Erklärung**: Du kannst wie in einer Liste prüfen, ob ein Wert vorhanden ist.

> 💡 **Tipp**: Das Unpacking ist besonders nützlich, wenn du z.B. Funktionen hast, die mehrere Werte zurückgeben. Statt ein Dictionary oder eine Liste zu verwenden, kannst du einfach ein Tuple zurückgeben.

---

## 5. Typische Anwendungsfälle

Tuples sind ideal, wenn du **feste Datensätze** hast, die nicht bearbeitet werden sollen:

1. **Koordinaten und Vektoren**  
   - `(x, y)`, `(x, y, z)` in einem Spiel oder einer Grafik-Anwendung.  

2. **Konfigurationen / Konstanten**  
   - Farbcodes, z.B. `RGB = (255, 0, 0)` für Rot.  

3. **Funktionsrückgaben**  
   - Eine Funktion kann mehrere Werte gleichzeitig zurückgeben, indem sie ein Tuple liefert, z.B. `(erfolg, nachricht)`.  

4. **Datenlogging**  
   - Wenn du protokollierst, z.B. `("INFO", "01-01-2025", "Alles läuft normal.")`. Du willst nicht, dass diese Werte nachträglich verändert werden.

5. **Unveränderliche Schlüssel in Dictionaries**  
   - Da ein Tuple **hashbar** ist (wenn es nur unveränderliche Inhalte hat), kannst du `(x, y)` als Key in einem Dictionary benutzen. Eine Liste wäre dafür nicht geeignet.

> 💡 **Tipp**: Tuples sind praktisch, wenn du das **Risiko** ausschließen möchtest, dass jemand (oder du selbst) diese Daten versehentlich ändert.

---

## 7. Häufige Stolpersteine 🚨

1. **Verwechslung mit Listen**  
   - Tuples sehen ähnlich aus, sind aber **nicht veränderlich**. Probierst du `tuple[0] = irgendwas`, bekommst du einen `TypeError`.

2. **Ein-Element-Tuples**  
   - Ein besonderes Problem kann ein Tupel mit **nur einem** Element sein: `(42)` sieht aus wie ein Tuple, ist in Python aber eine **Klammerausdruck**.  
   - Richtig: `(42,)` (mit Komma!) – erst dadurch erkennt Python es als Tuple.

3. **IndexError**  
   - Genauso wie bei Listen kann ein falscher Index (z.B. `position[2]` bei `(x, y)`) zu einem `IndexError` führen.

4. **Leere Tuples**  
   - Ein leeres Tuple wird einfach mit `()` erstellt. Es hat dann Länge 0: `len(()) → 0`.

---

## 8. Zusammenfassung und Ausblick

Tuples sind eine **wertvolle** Ergänzung zu den anderen Datenstrukturen:

- **Geordnet** wie eine Liste, aber **unveränderlich**.  
- Hervorragend geeignet, um **mehrere Werte** zusammenzufassen, die **nicht** manipuliert werden sollen.  
- Du kannst sie bequem entpacken und für **Funktionsrückgaben** oder **Koordinaten** nutzen.  

**Nächster Schritt**: Erkunde, wie du mit Tuples (als Keys) auf Dictionaries zugreifst oder wie du Listen von Tuples (oder Tuples von Listen!) aufbauen kannst. Python ist sehr flexibel bei der Kombination verschiedener Datenstrukturen!

> 💡 **Tipp**: Wenn du im Zweifel bist, ob du eine Liste oder ein Tuple verwenden sollst, frag dich: „Möchte ich die Reihenfolge und Anzahl der Elemente später ändern können?“ – Wenn **Nein**, ist ein Tuple oft die bessere Wahl.

---


**Viel Spaß beim Ausprobieren!**  

Tuples sind eine tolle Möglichkeit, **unveränderliche** Gruppen von Werten anzulegen. Ob du nun 2D-/3D-Koordinaten speicherst, feste Parameter in einer App festlegst oder mehrere Rückgabewerte bündeln willst – Tuples können deinen Code **strukturierter** und **sicherer** machen.  

**Happy Coding!** ✨