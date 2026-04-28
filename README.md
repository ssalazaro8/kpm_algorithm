# 🔍 KMP Algorithm – Assignment 2

> 📚 *Formal Languages and Automata — Lexical Analysis*  
> 🔗 *Continuation of Assignment 1 (Failure Function)*

---

## 📌 Course Information

| Field | Details |
|-------|---------|
| 🎓 Course | Formal Languages and Automata |
| 📖 Topic | Lexical Analysis – KMP Algorithm |
| ✍️ Authors | Samuel Salazar Ospina, [Partner's Name] |
| 📕 Reference | Aho, Lam, Sethi & Ullman — *Compilers: Principles, Techniques, & Tools* (2nd ed., 2007) |

---

## 🎯 Objective

This project implements the **Knuth-Morris-Pratt (KMP) string matching algorithm** described in:

- 📖 Section **3.4.5** of the reference book
- 📊 Algorithm from **Figure 3.20 (page 138)**
- 🧪 Solution to **Exercise 3.4.6 (page 138)**

This assignment builds directly on Assignment 1: the failure function computed in `failure_function.py` is reused here as the backbone of the KMP search.

---

## 🖥️ Environment

| Component | Tool / Version |
|-----------|---------------|
| 🪟 Operating System | Windows 11 |
| 🐍 Programming Language | Python 3.11.4 |
| 📝 Editor | Visual Studio Code |
| 📦 Virtual Environment | Python venv |

---

## 📂 Project Structure

```
kmp-assignment-2/
│
├── 📁 src/
│   ├── __init__.py
│   ├── failure_function.py   ← reused from Assignment 1
│   ├── kmp_algorithm.py      ← KMP search (Figure 3.20)
│   └── main.py               ← entry point (user input)
│
├── 🧪 tests/
│   └── test_kmp_algorithm.py ← unit tests for Exercise 3.4.6
│
├── venv/
├── README.md
└── .gitignore
```

---

## ▶️ How to Run the Program

**🔹 Step 1 – Clone the repository**

```bash
git clone <repository-url>
cd kmp-assignment-2
```

**🔹 Step 2 – Create and activate the virtual environment**

```bash
python -m venv venv
venv\Scripts\activate
```

> 🐧 On Linux/macOS use: `source venv/bin/activate`

**🔹 Step 3 – Run the program**

```bash
python -m src.main
```

**🔹 Step 4 – Enter text and pattern when prompted**

```
Enter the text:    abababaab
Enter the pattern: ababaa
```

✅ Expected output:

```
Text:    abababaab
Pattern: ababaa
Result: YES, the pattern is a substring.
```

---

## 🧪 How to Run the Tests

```bash
python -m unittest discover tests
```

✅ If all tests pass:

```
OK
```

The test suite covers the two cases from Exercise 3.4.6, plus two additional edge cases (guaranteed match and no match at all).

---

## 🔍 What is the KMP Algorithm?

The **Knuth-Morris-Pratt (KMP)** algorithm searches for occurrences of a pattern `p` inside a text `t` efficiently. It does so by preprocessing the pattern with the **failure function** (Assignment 1) to avoid redundant character comparisons.

The key idea is: when a mismatch occurs at position `s` of the pattern, instead of restarting from `s = 0`, the algorithm uses `failure[s-1]` to jump to the next valid comparison state — preserving all previously matched characters.

---

## 🧩 What is it Used For?

KMP is used wherever fast substring search is needed:

- 🔧 **Lexical analysis** — recognizing tokens in compilers without backtracking
- 🔎 **Text editors** — find/replace operations
- 🧬 **Bioinformatics** — DNA sequence matching
- 📡 **Network protocols** — pattern detection in data streams

Its time complexity is **O(n + m)**, where `n` is the length of the text and `m` is the length of the pattern, making it significantly faster than the naïve O(n·m) approach.

---

## ⚙️ Algorithm Explanation (Figure 3.20)

The KMP search algorithm works as follows:

1. 🔧 **Preprocess** — compute the failure function `f` for the pattern (see `failure_function.py`)
2. 🔢 Initialize `s = 0` (number of matched characters so far)
3. 🔁 For each character at position `i` in the text:
   - ↩️ While `s > 0` and `text[i] ≠ pattern[s]`, set `s = f[s-1]` *(fall back)*
   - ✅ If `text[i] == pattern[s]`, increment `s`
   - 🏁 If `s == len(pattern)` → **match found**, return `True`
4. 📤 If the loop ends without a full match → return `False`

The crucial difference from a naïve search is step 3's fallback: it never re-examines characters in the text that were already matched.

---

## 📝 Exercise 3.4.6 – Solution

**Pattern:** `ababaa`

**Failure function** (computed by Assignment 1):

| Position | 1 | 2 | 3 | 4 | 5 | 6 |
|:--------:|:-:|:-:|:-:|:-:|:-:|:-:|
| Char     | a | b | a | b | a | a |
| **f(i)** | **0** | **0** | **1** | **2** | **3** | **1** |

---

### 🔸 a) Text: `abababaab`

```
Text:    a  b  a  b  a  b  a  a  b
Pattern: a  b  a  b  a  a
```

The pattern `ababaa` **does appear** as a substring starting at position 3.

> ✅ **Result: YES**

---

### 🔸 b) Text: `abababbaa`

```
Text:    a  b  a  b  a  b  b  a  a
Pattern: a  b  a  b  a  a
```

At position 6 of the text there is a `b`, but the pattern expects `a`. The fallback cannot recover a full match anywhere in the text.

> ❌ **Result: NO**

---

## 📦 Dependencies

> 🟢 This project requires **no external libraries** — only the Python standard library is used.

---

## 💡 Key Insight

The power of KMP lies in never wasting a comparison. The failure function encodes all the "partial match" information about the pattern, so after any mismatch the algorithm already knows the furthest safe position to resume from — without ever moving the text pointer backwards.

Together, Assignments 1 and 2 form a complete implementation of the string matching approach used in real lexical analyzers.



