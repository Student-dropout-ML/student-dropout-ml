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

Abychom všichni pracovali se stejnými verzemi knihoven a nepadal nám kód, postupujte přesně takto:

1. **Naklonujte si repozitář:** `git clone <odkaz-na-repo>`
2. **Stáhněte data:** Z Kagglu stáhněte `.csv` a vložte ho do lokální složky `data/`. *(Pozor: data se nesmí nahrávat na GitHub, složka je chráněná v .gitignore).*
3. **Vytvořte virtuální prostředí (venv) s Pythonem 3.12:**
   Nejspolehlivější je vytvořit ho přímo přes vaše IDE, abyste měli jistotu správné verze:
   * **DataSpell / PyCharm:** `Settings -> Python Interpreter -> Add Local Interpreter -> Virtualenv`. Jako *Base interpreter* vyberte ze seznamu **Python 3.12**.
   * **VS Code:** Otevřete paletu příkazů (`Ctrl+Shift+P` / `Cmd+Shift+P`), zadejte `Python: Create Environment`, vyberte `Venv` a ze seznamu zvolte **Python 3.12**.
   *(Pokud to děláte čistě přes terminál, ověřte si nejdřív pomocí `python3 --version`, že vám příkaz opravdu ukazuje 3.12, a pak teprve zadejte `python3 -m venv .venv`).*
4. **Aktivujte prostředí:**
   * Mac/Linux: `source .venv/bin/activate`
   * Windows: `.venv\Scripts\activate`
   *(Úspěch poznáte tak, že v terminálu na začátku řádku svítí zelené `(.venv)`).*
5. **Nainstalujte sjednocené knihovny:**
   Zadejte: `pip install -r requirements.txt`
6. **Zkontrolujte IDE:** Ujistěte se, že vaše vývojové prostředí opravdu používá tuto novou složku `.venv` jako kernel/interpreter. Pak si otevřete šablonu `00-shared-pipeline-template.ipynb` a můžete začít kódit!

## Průvodce repozitářem (Jak s ním pracovat a co kam patří)

Abychom předešli "Git konfliktům" (když dva lidé upravují stejný soubor) a chaosu v kódu, dodržujeme tento jednoduchý workflow. Každá složka má svůj jasný účel:

### 1. Složka `data/` (Píseček pro syrová data)
* **Co sem patří:** Náš dataset stažený z Kagglu.
* **Pravidlo:** Složka je záměrně ignorovaná Gitem (přes `.gitignore`). Data si sem stáhněte pouze k sobě lokálně na disk. **Git je na GitHub nikdy nenahraje**, čímž chráníme repozitář před zasekáním obřími soubory.

### 2. Složka `notebooks/` (Zde se tvoří kód)
* **Co sem patří:** Všechny Jupyter notebooky (`.ipynb`).
* **Pravidlo:** Nepracujte všichni v jednom souboru! Každý logický krok projektu má svůj vlastní, jasně očíslovaný notebook. Tím pádem na sebe nebudeme při práci narážet.
* **Logická osa práce (kdo dělá co):**
  * `00-shared-pipeline-template.ipynb` -> Výchozí šablona pro předzpracování. Ošetřuje Data Leakage (připravil Honza).
  * `01-exploratory-data-analysis.ipynb` -> Zde zkoumají data a tvoří grafy Matěj a Kozub.
  * `02-model-training.ipynb` -> Zde Matěj/Kozub trénují a ladí klasifikační modely.
  * `03-evaluation.ipynb` -> Zde Martin aplikuje matici nákladů a vyhodnocuje nejlepší model.
  * `04-xai-explanations.ipynb` -> Zde Honza tvoří vysvětlitelnost a rozpad predikcí (SHAP/LIME).

### 3. Složka `models/` (Sklad hotových modelů)
* **Co sem patří:** Natrénované modely exportované z notebooků (např. pomocí knihovny `joblib` jako `.pkl` soubory).
* **Pravidlo:** Jakmile datoví inženýři v kroku `02` natrénují finální model, uloží ho sem. Evaluátoři (Martin a Honza) v krocích `03` a `04` kód znovu netrénují, ale pouze si ze složky načtou tento hotový uložený model. Tím ušetříme čas a zajistíme konzistenci.

### 4. Složka `docs/` (Kancelář)
* **Co sem patří:** Zadání, závěrečná zpráva (Word/PDF), byznys plán, prezentace a vygenerované HTML exporty našich notebooků.
* **Pravidlo:** Hlavní pracovní prostor pro Kláru (prezentace, texty) a Alexe (Quality Assurance a kontrola zadání).
