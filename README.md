# 🏥 Medical Expert System — Rule-Based AI with Forward Chaining

A beginner-friendly Rule-Based Expert System built in Python that diagnoses medical conditions using if-then rules and forward chaining inference. Built as part of my Artificial Intelligence at Syntecxhub.

---

## 🧠 What Is This?

This project simulates how a medical expert system reasons — the same way early AI systems like MYCIN worked. You enter symptoms, and the engine figures out what's wrong step by step, showing you every reasoning step along the way.

---

## ✨ Features

- ✅ Rule Engine — 15 hand-crafted if-then rules written in Python
- ✅ Facts Base — stores known facts (symptoms) in a Python set
- ✅ Forward Chaining — automatically infers new conclusions from known facts
- ✅ Multi-step Chaining — conclusions from one rule become conditions for the next
- ✅ Inference Logger — logs every reasoning step so you can follow the path
- ✅ Zero dependencies — pure Python, no libraries needed

---

## 📁 Project Structure
```
expert_system/
│
├── rules.py     →  All IF-THEN rules + Rule class definition
├── engine.py    →  Forward chaining inference engine
├── main.py      →  User interface (entry point — run this!)
└── README.md    →  This file
```

## 🚀 How to Run

Requirements: Python 3.8 or newer

Clone the repo and run:
python main.py

No installs needed — pure Python!

---

## 💡 Example Output

Symptoms entered: fever, cough, body aches
```
=======================================================
   INFERENCE ENGINE STARTED
=======================================================
Initial facts: ['body_aches', 'cough', 'fever']

  Step 1: Rule-1 fired
          BECAUSE: fever + cough
          CONCLUDED: possible_flu

  Step 2: Rule-6 fired
          BECAUSE: possible_flu + body_aches
          CONCLUDED: severe_flu

  Step 3: Rule-11 fired
          BECAUSE: severe_flu
          CONCLUDED: recommend_antiviral_medication
=======================================================

  🔍 Diagnosis: Severe Flu
  💊 Recommendation: Antiviral Medication
```

---

## ➕ How to Add Your Own Rules

Open rules.py and add a new entry to the RULES list:
```python
Rule(
    name="Rule-16",
    conditions=["chest_pain", "shortness_of_breath"],
    conclusion="possible_heart_issue"
),
```

The engine automatically picks it up — no other changes needed!

---

## 👤 Author

Asna Haris — Artificial Intelligence Intern

GitHub: https://github.com/asnaharis06-bot

LinkedIn: https://www.linkedin.com/in/asna-haris-684058319

---

## 🔗 Project Links

**GitHub:** 

---

## 📄 License

This project is built as part of my Artificial Intelligence Internship Program at Syntecxhub.

**Website:** https://syntecxhub.com/

---
