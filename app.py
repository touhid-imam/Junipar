import streamlit as st
from openai import OpenAI
import base64

# --- 1. HELPER FUNCTIONS (Must be at the top) ---


def get_image_base64(path):
    """Reads a local image and converts it to base64 for HTML injection."""
    try:
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception:
        return None


# --- 2. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Touhid Imam | AI Portfolio",
    page_icon="👤",
    layout="wide"
)

# --- 3. YOUR DATA (Knowledge Base) ---
FULL_CV_CONTENT = """
NAME: TOUHID IMAM
CONTACT: 6745 W Coolidge St, Phoenix, AZ 85033 | Phone: (712) 577-(8084) | Touhid.Imam@coyotes.usd.edu
LINKS: github.com/touhid-imam/data-analyst | linkedin.com/in/touhidimam/

SUMMARY:
Data Analyst with 5+ years of experience in data integration, analysis, and visualization.
Expert in leveraging Databricks and cloud-based environments to deliver actionable business insights across industries like healthcare.

EXPERIENCE:
- Intern Data Analyst at UpSkill (Sept 2025 - Present): Healthcare data analysis, Power BI/Tableau dashboards, NLP, and automated workflows.
- Data Analyst at RockIT Fuel Design And Tech (Nov 2020 - Aug 2023): Python automation, SQL querying, and dynamic visualizations.
- Programmer & Data Analyst at Magic Technologies Group (Apr 2018 - Oct 2020): Automated reporting, EDA, and customer segmentation.

TECHNICAL SKILLS:
- Data Engineering & Analysis: Databricks, SQL, Python (Pandas, NumPy, Scikit-learn), Excel, Data Wrangling.
- Visualization: Tableau, Power BI, Matplotlib, Seaborn, Excel Dashboards.
- Machine Learning: Supervised Learning (Regression, Classification), Unsupervised Learning (Clustering), and Reinforcement Learning.
- Advanced Modeling: CNNs, NLP, XGBoost, CatBoost, Stacking Ensembles.
- Tools & Platforms: VS Code, Git, Azure, Jupyter, RStudio.

TECHNICAL PROJECTS:
- Website Behavior Analysis: Used SQL, Python, and Google Analytics to automate reporting. Developed dashboards in Tableau/Power BI and conducted A/B testing on UI elements, resulting in a 20% increase in user retention.
- Social Media Sentiment Prediction: Built NLP models (SVM, KNN, Bagging) to analyze Amazon Help Twitter interactions. Identified KNN and SVM as optimal for predicting sentiment shifts to improve support strategies.
- Alzheimer's Early Detection: Processed OASIS MRI datasets using Python and CNNs. Achieved highest accuracy and AUC scores for imaging pattern identification compared to Random Forest and Logistic Regression.
- Lung Cancer Prognostication: Built a stacking ensemble model (XGBoost, LightGBM, CatBoost). Used ADASYN for class imbalance, RFECV for feature selection, and Optuna for Bayesian hyperparameter optimization. Validated with Stratified K-Fold Cross-Validation.

CERTIFICATIONS:
- SQL Intermediate Certificate, HackerRank (May 2025).
- Fundamentals of Data Governance, Edureka (Oct 2025).
- Healthcare Data Security, Privacy, and Compliance, Johns Hopkins University (Oct 2025).
- Process Data from Dirty to Clean, Google (Nov 2025).
- Supervised Machine Learning: Regression and Classification, Stanford CPD (Aug 2024).

EDUCATION:
- Masters in Computer Science, University of South Dakota (May 2025).

RESEARCH & PUBLICATIONS:
- Alzheimer's Disease Diagnosis using CNN on MRI Datasets (IEEE).
- Lung Carcinoma Prognostication via Stacking & SMOTE (IEEE).
- Thyroid Pathology Prediction with Neural Architectures (IEEE).
- Social Media Sentiment Analysis for Amazon Help (IJASCE).

REFERENCES:
- KC Santosh, University of South Dakota, Department Chair | Email: kc.santosh@usd.edu | Phone: (929) 264-1429
- Andrew Oldroyd, Rock IT Fuel Design and Tech, Founder | Email: andrew@atmwebdesign.ca
- Mike Robles, Magic Web Studios, CEO | Email: mrobles@mtgi.net | Phone: (605) 677-3184
- Md Mahfujul Islam, Fora Financial LLC, Senior Software Engineer | Email: Mahfujul.islam@forafinancial.com | Phone: (929) 264-1429

NOTE: You are welcome to contact any of these references directly for professional inquiries.
"""

# --- 4. CUSTOM CSS ---
st.markdown("""
    <style>
    /* 1. Base App Styling */
    .stApp { background-color: #0e1117; color: #ffffff; }

    /* 2. Target the Sidebar Container */
    section[data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #30363d;
        width: 350px !important;
    }

    /* 3. CENTER CONTENT BUT KEEP BUTTON RIGHT */
    /* Target the inner container of the sidebar */
    [data-testid="stSidebarUserContent"] {
        display: flex;
        flex-direction: column;
        align-items: center !important;
        text-align: center;
    }
            
    /* Hide only the GitHub and Fork icons in the top right */
    .stToolbarActionButton {
            display: none;
        }
            
    # Remove Streamlit icon and profile 
    a._container_gzau3_1._viewerBadge_nim44_23, ._profileContainer_gzau3_53 {
            display: none !important;
        }
            


    /* 4. FORCE THE COLLAPSE BUTTON TO THE RIGHT */
    /* We target the header container specifically */
    [data-testid="stSidebarHeader"] {
        display: flex !important;
        justify-content: flex-end !important;
        background-color: transparent !important;
    }
    .center-alignment{
            display: flex;
            justify-content: center;
            align-items: center;
            }
    .flex-column{
            flex-direction: column;
            }

    /* 5. Image & Card Styling */
    .portfolio-image-wrapper {
        display: flex;
        justify-content: center;
        margin: 20px 0;
    }
    .profile-wrap {
        width: 180px;
        height: 180px;
        border-radius: 50%;
        overflow: hidden;
        border: 3px solid #00d4ff;
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.4);
    }
    .profile-wrap img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .cv-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
        width: 90%;
        text-align: left; /* Keep text inside cards readable */
    }

    .glow-text {
        color: #00d4ff;
        text-shadow: 0 0 10px #00d4ff;
        font-weight: bold;
        margin-bottom: 5px;
    }

    /* Target the chat input focus state */
    [data-testid="stChatInput"] textarea:focus {
        border-color: rgb(0, 212, 255) !important;
        box-shadow: 0 0 10px rgba(0, 212, 255, 0.5) !important;
        outline: none !important;
    }

    /* Optional: Removes the default Streamlit focus ring to keep it clean */
    [data-testid="stChatInput"] div {
        border-color: transparent !important;
    }

    .stChatMessage {
        background-color: #1c2128 !important;
        border-radius: 10px !important;
        border: 1px solid #30363d !important;
    }

    /* 1. Global Text Color Override */
    html, body, [data-testid="stWidgetLabel"], .stMarkdown, p, h1, h2, h3, h4, h5, h6, span {
        color: #ffffff !important;
    }

    /* 2. Specific fix for Sidebar text which often defaults to grey */
    [data-testid="stSidebar"] .stMarkdown p {
        color: #ffffff !important;
    }
    
    /* 3. Ensure Chat Input text is white */
    [data-testid="stChatInput"] textarea {
        color: #ffffff !important;
    }
            

    /* 1. Force Header Background to be Dark (Fixes mobile white bar) */
    [data-testid="stHeader"] {
        background-color: #0e1117 !important;
    }

    /* 2. Fix Button Visibility (White background/White text fix) */
    div.stButton > button {
        background-color: #1c2128 !important; /* Dark background */
        color: #ffffff !important;            /* White text */
        border: 1px solid #00d4ff !important; /* Blue border to make it pop */
        transition: all 0.3s ease;
    }

    /* 3. Fix Button Hover/Active state for Mobile */
    div.stButton > button:hover, div.stButton > button:active, div.stButton > button:focus {
        background-color: #00d4ff !important; /* Blue background on tap */
        color: #0e1117 !important;            /* Dark text on tap */
        border: 1px solid #00d4ff !important;
    }

    /* 4. Fix Chat Input Background for Mobile */
    [data-testid="stChatInput"] {
        background-color: #0e1117 !important;
    }

    </style>
    """, unsafe_allow_html=True)

# --- 5. SIDEBAR - PROFILE SECTION ---
with st.sidebar:
    # Header
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    st.markdown('<div class="center-alignment flex-column"><h1 class="glow-text">TOUHID IMAM</h1></div>',
                unsafe_allow_html=True)
    st.markdown('<div class="center-alignment flex-column"><h4 class="glow-text">DATA ANALYST & AI RESEARCHER</h4></div>',
                unsafe_allow_html=True)

    # Image logic
    img_path = "assets/images/touhid.JPG"
    img_base64 = get_image_base64(img_path)

    if img_base64:
        st.markdown(
            f'<div class="portfolio-image-wrapper"><div class="profile-wrap"><img src="data:image/jpeg;base64,{img_base64}" class="profile-img"></div></div>', unsafe_allow_html=True)
    else:
        st.image("https://via.placeholder.com/140",
                 caption="Photo Placeholder")

    st.markdown(
        f"""
    <div style="display: flex; justify-content: center; gap: 10px; font-size: 0.9rem;">
        <a href="https://linkedin.com/in/touhidimam/" target="_blank" style="color: #00d4ff; text-decoration: none;">🔗 LinkedIn</a>
        <span style="color: white;">|</span>
        <a href="https://github.com/touhid-imam/data-analyst" target="_blank" style="color: #00d4ff; text-decoration: none;">🐙 GitHub</a>
    </div>
    """,
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # Quick Summary Card
    # --- Professional Snapshot (Denser Content) ---
    st.markdown(f"""
    <div style="font-size: 1rem; line-height: 1.4;">
        <b>🎓 Education:</b> MS in CS, USD (May 2025)<br>
        <hr style="margin:5px 0; border-top: 1px solid #30363d; opacity: 0.3;">
        <b>📍 Location:</b> Phoenix, AZ<br>
        <hr style="margin:5px 0; border-top: 1px solid #30363d; opacity: 0.3;">
        <b>💼 Recent:</b> Intern Analyst @ UpSkill<br>
        <hr style="margin:5px 0; border-top: 1px solid #30363d; opacity: 0.3;">
        <b>📚 Pubs:</b> 3 IEEE Research Papers
        <hr style="margin:5px 0; border-top: 1px solid #30363d; opacity: 0.3;">
        <b>🛠️ Top Skills:</b> SQL, Python, Power BI, Tableu
        <div style="margin-bottom: 30px"></div>
    </div>
    """, unsafe_allow_html=True)

# --- NEW: DOWNLOAD CV BUTTON ---
    try:
        with open("assets/docs/Touhid_Imam.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(
            label="📄 Download My CV",
            data=PDFbyte,
            file_name="Touhid_Imam_CV.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    except FileNotFoundError:
        st.error("CV File not found in assets folder.")


# --- SECURITY CHECK ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    # Title for the login screen
    st.markdown("<h2 style='text-align: center; color: #00d4ff;'>🔒 Junipar AI Access</h2>",
                unsafe_allow_html=True)

    st.info(
        f"This AI agent is password-protected to manage API usage. | 🔑 **Agent Password: {st.secrets['PORTFOLIO_PASSWORD']}**")
    password_input = st.text_input(
        "Enter password to chat with Junipar:", type="password")

    if st.button("Unlock Agent"):
        if password_input == st.secrets["PORTFOLIO_PASSWORD"]:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Incorrect password. Please try again.")

    # Stop execution here so the chat isn't shown
    st.stop()

# --- If authenticated, the rest of the code below will run ---

# --- 6. MAIN CHAT INTERFACE ---
st.subheader("👤 Touhid Imam | AI Professional Representative")
st.write("""
    Welcome. I am an AI agent representing Touhid Imam.
    I can provide specific insights into his **5+ years of Data Analytics experience**,
    his technical proficiency in **Databricks and SQL**, and
    his expertise in **Supervised and Reinforcement Learning**.
""")

# Predefined Prompts
st.write("Quick Inquiries:")
# Using two rows for a clean grid layout
# Create 4 columns in a single row
cols1 = st.columns(4)

# Experience Button: Focuses on "Transferable Skills"
if cols1[0].button("Experience 💼"):
    st.session_state.messages.append(
        {"role": "user", "content": "Explain Touhid's professional background, focusing on his impact at UpSkill and RockIT Fuel. Highlight his 5+ years of data experience."})
    st.rerun()

# Skills Button: Focuses on "Industry-Ready Tools"
if cols1[1].button("Skills 💻"):
    st.session_state.messages.append(
        {"role": "user", "content": "What is Touhid's technical stack? Specifically mention his proficiency in Databricks, SQL, and the three types of Machine Learning."})
    st.rerun()

# Projects Button: This is your "Experience Substitute"
if cols1[2].button("Projects 🛠️"):
    st.session_state.messages.append(
        {"role": "user", "content": "Provide a detailed overview of his technical projects, especially the Lung Cancer Stacking Ensemble and the A/B testing that improved user retention."})
    st.rerun()

# Certs Button: Builds "Credential Authority"
if cols1[3].button("Certification 📜"):
    st.session_state.messages.append(
        {"role": "user", "content": "List ALL of Touhid's certifications from Stanford, JHU, Google, Edureka, and HackerRank with their dates."})
    st.rerun()


cols2 = st.columns(4)
# Education Button: Highlights "Advanced Foundations"
if cols2[0].button("Education 🎓"):
    st.session_state.messages.append(
        {"role": "user", "content": "Tell me about his MS in Computer Science from the University of South Dakota and his current academic focus."})
    st.rerun()

# Research Button: Highlights "Specialized Expertise"
if cols2[1].button("Research 🔬"):
    st.session_state.messages.append(
        {"role": "user", "content": "List his IEEE research publications and provide his Google Scholar link: https://scholar.google.com/citations?user=v2CiY6sAAAAJ"})
    st.rerun()

if cols2[2].button("References 📞"):
    st.session_state.messages.append(
        {"role": "user", "content": "Provide a list of Touhid's professional references including their names, titles, and contact information. Also, mention that I can contact them if needed."})
    st.rerun()

# --- 7. OPENAI LOGIC ---
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": f"You are Junipar, Touhid Imam's professional AI assistant. Use his CV data: {FULL_CV_CONTENT}. Answer only based on this info. If asked about unrelated topics, politely redirect to his career."},
        {"role": "assistant", "content": "Hello! I am Junipar. I can tell you about Touhid's MS in Computer Science, his research in ML, or his 5+ years of data analysis experience. How can I help you today?"}
    ]

# Display Chat History
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"], avatar="👤"):
            st.markdown(msg["content"])

# Handle User Input
if prompt := st.chat_input("Ask about Touhid..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.rerun()

# Generate Response
if st.session_state.messages[-1]["role"] == "user":
    with st.chat_message("assistant", avatar="👤"):
        stream = client.chat.completions.create(
            model="gpt-4o",
            messages=st.session_state.messages,
            stream=True
        )
        response = st.write_stream(stream)
    st.session_state.messages.append(
        {"role": "assistant", "content": response})
