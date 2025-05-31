# Generator și Analizator pentru Gramatici Libere de Context

Acest proiect permite lucrul cu gramatici libere de context (CFG – Context-Free Grammar) definite într-un fișier, oferind funcționalități precum:
- generarea de șiruri din limbajul descris de gramatică
- derivarea pas cu pas a unui șir dat
- testarea apartenenței unui șir la limbaj

## Fișierul de intrare (`teste.txt`)

Fișierul trebuie să conțină o gramatică liberă de context definită în forma:

```
S -> aSb | $
```

sau pentru mai multe producții pe o linie:

```
S -> aSb | ab
A -> aA | b
```

- **`S`** este neterminalul de start (primul din fișier).
- **`$`** reprezintă epsilon (șirul vid).

## Cum rulezi programul

Asigură-te că ai Python 3 instalat și rulează comanda:

```bash
python nume_program.py teste.txt
```

unde `nume_program.py` este numele fișierului Python care conține codul tău.

### Output-ul va include:

1. **Test funcția CFG:**
   Afișează mulțimile de neterminale, terminale, regulile și simbolul de start.

2. **Test funcția StringGen:**
   Generează 10 șiruri posibile din gramatică.

   Exemplu:
   ```
   ab
   aabb
   aaabbb
   ```

3. **Test funcția Derivation:**
   Selectează un șir generat și afișează pașii de derivare până la obținerea lui (dacă există).

   Exemplu:
   ```
   S
   aSb
   aaSbb
   aaabbb
   ```

4. **Test funcția Membership:**
   Testează dacă un șir aparține limbajului generat de gramatică.

   Exemplu:
   ```
   Merge
   ```

sau

   ```
   Nu merge
   ```

---

## Observații tehnice

- Epsilon este reprezentat prin caracterul `$` în fișier.
- Adâncimea maximă de derivare este limitată la 20 pași pentru a evita recursivitatea infinită.
- Se acceptă doar caractere terminale între `a` și `z`.

---

**Proiect realizat pentru cursul de Limbaje Formale și Automate din cadrul Facultății de Matematică și Informatică – Universitatea din București.**
