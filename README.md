# 🎓 Predikce předčasného ukončení studia (Student Dropout Prediction)

Tento repozitář obsahuje naši týmovou semestrální práci na předmět Strojové učení. 

[cite_start]**Náš byznys cíl:** Identifikovat studenty, u kterých hrozí vysoké riziko, že nedokončí studium (dropout)[cite: 29]. Těmto studentům chceme následně nabídnout cílenou pomoc (např. stipendium nebo úpravu studijní zátěže), čímž škola ušetří peníze za ztracené školné a zlepší svou reputaci.

[cite_start]**Zdroj dat:** [Student Dropout Prediction Dataset (Kaggle)](https://www.kaggle.com/datasets/meharshanali/student-dropout-prediction-dataset)[cite: 8, 30].

---

## 📂 Struktura repozitáře a pravidla

Abychom si nepřemazávali kód a nevznikal nám tu chaos, dodržujeme tuto strukturu:

* `data/` ➔ Sem si stáhněte dataset z Kagglu. **Tato složka je v `.gitignore`, data nikdy nepushujte na GitHub!**
* `notebooks/` ➔ Zde tvoříme kód. Každý si vytvoří svůj notebook podle své role (např. `01_EDA_Matej.ipynb`).
* `models/` ➔ Sem budeme ukládat hotové natrénované modely (`.pkl` soubory) pro finální evaluaci a vysvětlitelnost.
* `docs/` ➔ Podklady pro textovou zprávu a závěrečnou prezentaci.

[cite_start]⚠️ **Zlaté pravidlo (Data Leakage):** Předzpracování dat (škálování, doplňování hodnot) se smí učit POUZE z trénovací množiny[cite: 56]. [cite_start]Používejte prosím `scikit-learn Pipeline` podle připravené šablony[cite: 57].

---

## 👥 Tým a rozdělení rolí

Práci jsme si rozdělili do následujících logických bloků, ať si nelezeme do zelí:

### 📝 1. Byznys a Prezentace (Klára)
* **Role:** Storyteller a garant výstupu.
* [cite_start]**Úkoly:** Sepsání úvodu a byznys plánu [cite: 28-29]. [cite_start]Definice cílového atributu, "zájmové instance" a návrh matice nákladů[cite: 31]. [cite_start]Shrnutí celkových výsledků do závěru (co fungovalo nejlépe, co je nejdůležitější) [cite: 98-102]. [cite_start]Finální úprava textu zprávy[cite: 112].

### 🛠️ 2. Data & Modelování (Kozub & Matěj)
* **Role:** Strojovna projektu (Supervised i Unsupervised learning).
* [cite_start]**Úkoly:** Exploratorní analýza (EDA), histogramy a korelační grafy [cite: 38-40]. [cite_start]Sestavení Pipeline pro předzpracování (čištění dat, škálování) [cite: 42-55]. [cite_start]Trénování klasifikačních modelů (Stromy, Lesy) vč. ladění metaparametrů [cite: 63-68]. [cite_start]Provedení shlukování na vybrané podmnožině [cite: 69-72].

### 🕵️‍♂️ 3. Quality Assurance (Alex)
* **Role:** Strážce kvality a checklistu.
* [cite_start]**Úkoly:** Kontrola naplnění finálního checklistu zadání[cite: 106]. [cite_start]Hlídání, zda jsou všechny kroky předzpracování zdůvodněné a zda modely testují různé metaparametry [cite: 107-108]. Průběžná podpora týmu.

### 📊 4. Evaluace a Metriky (Martin)
* **Role:** Vyhodnocení, zda se to škole vyplatí.
* [cite_start]**Úkoly:** Výběr správných metrik (Accuracy/F1)[cite: 75]. [cite_start]Aplikace Klářiny matice nákladů na výsledky modelů[cite: 77]. [cite_start]Hledání optimálního prahu (threshold), který škole ušetří nejvíce peněz[cite: 78]. [cite_start]Vyhodnocení kvality shlukování (loketní křivka) [cite: 81-83].

### 🧩 5. Integrace a XAI (Honza)
* **Role:** Architektura repozitáře a Safe AI (Vysvětlitelnost).
* [cite_start]**Úkoly:** Spojení notebooků a modelů dohromady (zajištění opakovatelnosti kódu)[cite: 109]. [cite_start]Zpracování kapitoly "Vysvětlení" – určení důležitosti proměnných, použití XAI nástrojů (SHAP/LIME/ICE) pro simulaci toho, jak vybranému studentovi pomůže např. přidělení stipendia [cite: 84-92].

---

## 🚀 Jak začít (Pro členy týmu)

1. Naklonujte si tento repozitář k sobě do PC: `git clone <odkaz-na-repo>`
2. Stáhněte si `.csv` data z Kagglu a vložte je do lokální složky `data/`.
3. Vytvořte si ve svém IDE (DataSpell) virtuální prostředí (conda) a nainstalujte závislosti (`scikit-learn`, `pandas`, atd.).
4. Otevřete si v `notebooks/` připravenou šablonu pro Pipeline a můžete začít psát svou část!
