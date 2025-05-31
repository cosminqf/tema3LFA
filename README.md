# 📚 CFG Analyzer – Gramatica Liberă de Context

Acest program permite lucrul cu gramatici libere de context (CFG – Context-Free Grammar). Include:

1. **Citirea unei gramatici dintr-un fișier**
2. **Generarea de șiruri posibile**
3. **Verificarea dacă un șir poate fi derivat (Derivation)**
4. **Testul de apartenență a unui șir la limbaj (Membership)**

---

## 📄 Structura fișierului de intrare

Fișierul trebuie să conțină o gramatică în formatul:

```
S -> aSb | $
```

sau

```
S -> aS | aSb | $
A -> bA | b
```

- Regulile sunt scrise linie cu linie
- Simbolul **`$`** reprezintă **epsilon (ε)** — șirul vid

---

## ▶️ Cum rulezi programul

### 🔹 Cerințe:
- Python 3

### 🔹 Comandă de rulare:
```bash
python nume_program.py gramatica.txt
```

Unde `gramatica.txt` este fișierul cu regulile gramaticale.

---

## ✅ Exemple de output

Presupunem că `gramatica.txt` conține:

```
S -> aSb | $
```

### 🔹 Output:

```
Test functia CFG:
Test functia StringGen:
ab
aaabbb
aabbb
ab
aaaabbbb
ab
aabb
aabbbb
aabb
ab

Test functia Derivation:
aaaabbbb
S
aSb
aaSbb
aaaSbbb
aaaabbbb

Test functia Membership:
aabb
Merge
```

---

## 🔍 Descrierea funcționalităților

### 🔹 `CFG()`
- Citește o gramatica din fișier
- Extrage:
  - Neterminale (`V`)
  - Terminale (`Σ`)
  - Reguli (`R`)
  - Simbolul de start (`S`)

### 🔹 `StringGen(V, R, S)`
- Generează un cuvânt aleator de maxim 9 caractere din limbajul generat
- Elimină neterminalele rămase după generare

### 🔹 `Derivation(current_string, target, depth, V, R)`
- Verifică dacă un șir poate fi derivat din simbolul de start
- Returnează pașii derivării (dacă există)
- Se oprește după un număr maxim de pași (default: 20)

### 🔹 `Membership(S, string, V, R)`
- Verifică dacă un șir aparține limbajului generat de gramatică

---

## ℹ️ Observații

- Șirurile generate pot include uneori neterminale, care sunt apoi eliminate înainte de verificare
- Derivarea folosește backtracking pentru a găsi o cale validă până la șirul țintă

---

## ✍️ Autor

Proiect realizat pentru cursul de **Limbaje Formale și Automate** din cadrul **Facultății de Matematică și Informatică – Universitatea din București**