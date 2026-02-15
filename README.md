# 👤 Junipar | The AI Portfolio Agent

**Junipar** is a professional AI representative built to showcase my career as a Data Analyst and AI Researcher. Instead of a static resume, Junipar provides an interactive experience where recruiters can "interview" my digital twin about my 5+ years of experience, research publications, and technical stack.

---

## 🚀 Key Features

- **Junipar AI Chat:** A GPT-4o powered agent trained on my professional background (CV, Projects, and Certifications).
- **Quick Inquiries:** A grid-based UI for instant access to my Experience, Skills, Research, and References.
- **Secure Access:** Integrated password protection to manage API costs and prevent automated bot usage.
- **Dynamic UI:** Custom CSS-styled Streamlit interface with a "Blue Glow" professional theme.
- **Direct Assets:** One-click access to download my full CV in PDF format.

---

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/) (Python-based Web Framework)
- **AI Engine:** [OpenAI API](https://openai.com/api/) (GPT-4o Model)
- **Styling:** Custom CSS & HTML Injection
- **Deployment:** Streamlit Community Cloud

---

## 🔬 Featured Projects Highlighted by Junipar

- **Lung Cancer Prognostication:** Stacking ensemble models (XGBoost, LightGBM, CatBoost) with ADASYN for class imbalance.
- **Alzheimer’s Early Detection:** CNN-based MRI analysis achieving state-of-the-art AUC scores.
- **Social Media Sentiment Analysis:** NLP pipeline for predicting customer sentiment shifts in real-time.

---

## 📂 Project Structure

```text
.
├── assets/
│   ├── images/
│   │   └── touhid.JPG       # Profile Image
│   └── docs/                # Recommended to put CV in a 'docs' subfolder
│       └── Touhid_Imam.pdf  # Downloadable Resume
├── .streamlit/
│   └── secrets.toml         # Local API & Password storage (Git-ignored)
├── app.py                   # Main Streamlit Application logic
├── requirements.txt         # Project Dependencies
└── README.md                # Project Documentation
```
