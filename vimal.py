import streamlit as st
from streamlit_option_menu import option_menu

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Portfolio website",
    page_icon="🧮",
    layout="wide"
)

# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- LOAD SECRET LINKS ---
linkedin = st.secrets["links"]["linkedin"]
github = st.secrets["links"]["github"]
gmail = st.secrets["links"]["gmail"]
project1 = st.secrets["links"]["project1"]
project2 = st.secrets["links"]["project2"]
project3 = st.secrets["links"]["project3"]
project4 = st.secrets["links"]["project4"]

# --- SIDEBAR (Contact Info and Personal Details) ---
with st.sidebar:
    st.image("generated-image.png", width=180)
    st.title("Villarasu S")
    st.subheader("Data Analyst")
    st.divider()
    st.markdown("📞 9042819493")
    st.markdown("📍 Dharmapuri, India")
    st.divider()

    # Contact Buttons (Secure Links)
    st.link_button("🔗 LinkedIn", linkedin)
    st.link_button("💻 GitHub", github)
    st.link_button("📧 Gmail", gmail)

    # --- RESUME DOWNLOAD BUTTON ---
    with open("Villarasu_Resume.pdf", "rb") as file:
        st.download_button(
            label="📄 Download Resume",
            data=file,
            file_name="Villarasu_Resume.pdf",
            mime="application/pdf"
        )

# --- NAVIGATION BAR ---
selected = option_menu(
    menu_title=None,
    options=["About", "Projects", "Education & Skills"],
    icons=["person", "code-slash", "mortarboard"],
    orientation="horizontal",
)

# --- ABOUT ME PAGE ---
if selected == "About":
    st.header("Profile", divider="blue")
    st.write("""
        Motivated entry-level data analyst with a strong foundation in Python, SQL, and Excel. 
        Hands-on experience in basic data cleaning and visualization. Eager to apply and develop analytical 
        skills to support business decision-making and learn in a professional environment.
    """)

    # Optionally, you can show resume button here also
    st.download_button(
        label="📄 Download My Resume",
        data=open("Villarasu_Resume.pdf", "rb").read(),
        file_name="Villarasu_Resume.pdf",
        mime="application/pdf"
    )

# --- PROJECTS PAGE ---
if selected == "Projects":
    st.header("Projects", divider="blue")

    # --- PROJECT 1: SecureCheck ---
    with st.container(border=True):
        st.subheader("SecureCheck: Python SQL Digital Ledger for Police Post")
        st.write("**Key Skills:** Python, PostgreSQL, Streamlit")
        st.markdown("""
        - Built a Streamlit app with PostgreSQL backend to manage 10,000+ police stop records, improving reporting speed by 30%.
        - Designed dashboards to track vehicles, violations, and demographics, enabling faster insights.
        - Integrated predictive models and digital log submission features for efficient record-keeping.
        - Applied SQL queries (joins, aggregations) to identify violation trends and location hotspots.
        """)
        st.link_button("🔒 View Project (Private)", project1)

    # --- PROJECT 2: AgriData Explorer ---
    with st.container(border=True):
        st.subheader("AgriData Explorer")
        st.write("**Key Skills:** PostgreSQL, Power BI, EDA")
        st.markdown("""
        - Analyzed 1M+ agricultural records in PostgreSQL and performed EDA to study crop yields and patterns.
        - Developed interactive Power BI dashboards for state- and district-level insights.
        - Automated data cleaning and loading workflows, reducing manual effort by 40%.
        - Identified key productivity drivers for data-driven agricultural planning.
        """)
        st.link_button("🔒 View Project (Private)", project2)

    # --- PROJECT 3: Employee Attrition Analysis & Prediction ---
    with st.container(border=True):
        st.subheader("Employee Attrition Analysis & Prediction")
        st.write("**Key Skills:** Machine Learning, Data Preparation, Data Visualization, Python, PostgreSQL, Power BI")
        st.markdown("""
        - Built ML models (Random Forest, Logistic Regression) to predict attrition with 82% accuracy.
        - Engineered features and handled missing values to improve model performance.
        - Created Power BI dashboards to visualize attrition trends and key HR metrics.
        - Provided actionable insights for employee retention strategies.
        """)
        st.link_button("🔒 View Project (Private)", project3)

    # --- PROJECT 4: Multiple Disease Prediction ---
    with st.container(border=True):
        st.subheader("Multiple Disease Prediction")
        st.write("**Key Skills:** Python, Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn, Streamlit")
        st.markdown("""
        - Developed ML models to predict diabetes, heart disease, and Parkinson's disease.
        - Applied normalization, feature selection, and visualization to highlight risk factors.
        - Built an interactive Streamlit app for real-time prediction and analysis.
        - Helped users assess health risks with improved accessibility.
        """)
        st.link_button("🔒 View Project (Private)", project4)

# --- EDUCATION & SKILLS PAGE ---
if selected == "Education & Skills":
    st.header("Skills", divider="blue")
    st.markdown("""
    - **Technical Skills:** Python, Excel, PostgreSQL, Power BI  
    - **Currently Learning:** Statistics
    """)

    st.header("Education", divider="blue")
    st.subheader("Master Data Science Program | GUVI")
    st.write("May 2025 - Aug 2025")
    st.subheader("Bachelor of Commerce | Sri Vidhya Mandir Arts and Science College (Autonomous)")
    st.write("Jun 2021 - Mar 2024")

    st.header("Certificates", divider="blue")
    st.write("• ChatGPT for Everyone Certificate - GUVI")
