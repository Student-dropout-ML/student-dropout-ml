# Predikce předčasného ukončení studia (Student Dropout Prediction)

Tento repozitář obsahuje naši týmovou semestrální práci na předmět Strojové učení. 

**Náš byznys cíl:** Identifikovat studenty, u kterých hrozí vysoké riziko, že nedokončí studium (dropout). Těmto studentům chceme následně nabídnout cílenou pomoc (např. stipendium nebo úpravu studijní zátěže), čímž škola ušetří peníze za ztracené školné a zlepší svou reputaci.

**Zdroj dat:** [Student Dropout Prediction Dataset (Kaggle)](https://www.kaggle.com/datasets/meharshanali/student-dropout-prediction-dataset).

---

## Struktura repozitáře a pravidla

Abychom si nepřemazávali kód a nevznikal nám tu chaos, dodržujeme tuto strukturu:

* `data/` -> Sem si stáhněte dataset z Kagglu. **Tato složka je v `.gitignore`, data nikdy nepushujte na GitHub!**
* `notebooks/` -> Zde tvoříme kód. Každý si vytvoří svůj notebook podle své role (např. `01_EDA_Matej.ipynb`).
* `models/` -> Sem budeme ukládat hotové natrénované modely (`.pkl` soubory) pro finální evaluaci a vysvětlitelnost.
* `docs/` -> Podklady pro textovou zprávu a závěrečnou prezentaci.

**Zlaté pravidlo (Data Leakage):** Předzpracování dat (škálování, doplňování hodnot) se smí učit POUZE z trénovací množiny. Používejte prosím `scikit-learn Pipeline` podle připravené šablony.

---

## Tým a rozdělení rolí

Práci jsme si rozdělili do následujících logických bloků, ať si nelezeme do zelí:

### 1. Byznys a Prezentace (Klára)
* **Role:** Storyteller a garant výstupu.
* **Úkoly:** Sepsání úvodu a byznys plánu. Definice cílového atributu, "zájmové instance" a návrh matice nákladů. Shrnutí celkových výsledků do závěru (co fungovalo nejlépe, co je nejdůležitější). Finální úprava textu zprávy.

### 2. Data & Modelování (Kozub & Matěj)
* **Role:** Strojovna projektu (Supervised i Unsupervised learning).
* **Úkoly:** Exploratorní analýza (EDA), histogramy a korelační grafy. Sestavení Pipeline pro předzpracování (čištění dat, škálování). Trénování klasifikačních modelů (Stromy, Lesy) vč. ladění metaparametrů. Provedení shlukování na vybrané podmnožině.

### 3. Quality Assurance (Alex)
* **Role:** Strážce kvality a checklistu.
* **Úkoly:** Kontrola naplnění finálního checklistu zadání. Hlídání, zda jsou všechny kroky předzpracování zdůvodněné a zda modely testují různé metaparametry. Průběžná podpora týmu.

### 4. Evaluace a Metriky (Martin)
* **Role:** Vyhodnocení, zda se to škole vyplatí.
* **Úkoly:** Výběr správných metrik (Accuracy/F1). Aplikace Klářiny matice nákladů na výsledky modelů. Hledání optimálního prahu (threshold), který škole ušetří nejvíce peněz. Vyhodnocení kvality shlukování (loketní křivka).

### 5. Integrace a XAI (Honza)
* **Role:** Architektura repozitáře a Safe AI (Vysvětlitelnost).
* **Úkoly:** Spojení notebooků a modelů dohromady (zajištění opakovatelnosti kódu). Zpracování kapitoly "Vysvětlení" – určení důležitosti proměnných, použití XAI nástrojů (SHAP/LIME/ICE) pro simulaci toho, jak vybranému studentovi pomůže např. přidělení stipendia.

---

## Jak začít (Pro členy týmu)

1. Naklonujte si tento repozitář k sobě do PC: `git clone <odkaz-na-repo>`
2. Stáhněte si `.csv` data z Kagglu a vložte je do lokální složky `data/`.
3. Vytvořte si ve svém IDE (DataSpell) virtuální prostředí (conda/venv) a nainstalujte závislosti (`scikit-learn`, `pandas`, atd.).
4. Otevřete si v `notebooks/` připravenou šablonu pro Pipeline a můžete začít psát svou část!
