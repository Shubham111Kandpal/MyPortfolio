import streamlit as st
from pathlib import Path

# Set page config for better appearance
st.set_page_config(page_title="Shubham Kandpal | Portfolio", page_icon="Images/Logo.png", layout="wide")

def run():
    
    # --- Load Profile Picture ---
    profile_pic = Path("Images/Shubham_pic.png")

    # --- Sidebar ---
    with st.sidebar:
        st.image(profile_pic, width=150)
        st.title("Shubham Kandpal")
        st.markdown("""
        **AI & Data Science Professional**  
        MSc Distinction – University of Surrey
        
        📍 London, UK  
        📧 [Email](mailto:shubham.kandpal@gmail.com)   
        
        [![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/shubham-kandpal-035711165)  
        [![GitHub](https://img.shields.io/badge/-GitHub-black?style=flat-square&logo=github)](https://github.com/Shubham111Kandpal)
        """)

    # --- Main Content ---
    st.title("👋 Welcome to My Portfolio")
    st.markdown("---")

    # --- Summary ---
    st.subheader("👨‍💻 About Me")
    st.write("""
    An innovative and results-driven Data Scientist with 4+ years of experience, specializing in AI and machine learning technologies, having a good problem-solving skillset. 
    Currently working at Outlier.ai, focusing on training AI chatbots using Reinforcement Learning with Human Feedback (RLHF). 
    Recently earned an MSc in Data Science with distinction from The University of Surrey, with a dissertation on Adversarial Machine Learning in Facial Recognition Systems. 
    Expertise includes building end-to-end machine learning solutions including skills in NLP, Time Series Analysis, and cloud computing. 
    Strong background in Python, AWS, Statistics, Algorithms, Docker, and CI/CD pipeline development. 
    Actively seeking opportunities to advance in AI, ML, and data science solutions in dynamic environments.
    """)

    # --- Work Experience ---
    st.subheader("💼 Work Experience")
    st.markdown("""
    **AI Trainer — Outlier.ai (Sep 2024 – Present)**  
    - Training and optimizing AI chatbots using RLHF across multiple use-cases (code generation, math, Q&A).  
    - Collaborate with cross-functional teams to enhance AI accuracy and interaction quality for Meta, Gemini, OpenAI, and Claude.  

    **Stock Trader — Bombay Stock Exchange (Jun 2022 – Jun 2023)**  
    - Analyzed market trends, technical indicators, and financial statements to make data-driven trading decisions across equity and derivative markets in CNC and commodities.  
    - Developed algorithmic trading strategies using Python and tested models to optimize trade execution and risk management. Utilized models like Prophet, ARIMA, and custom LSTMs while leveraging CNN for an unconventional market shock analysis.

    **Full-Stack Developer & Data Miner — TCS (Dec 2018 – May 2022)**  
    - Developed 8+ web applications with Python and React.js, improving user experience and workflow for airlines ERP. Used Django and Flask for REST API. I also used the SAP UI5 framework for the ERP modules, such as Material Management, EC-PM, Finance, and HR.  
    - Implemented Decision Trees to optimize flight delay predictions based on weather and XGBoost models for classifications in passenger demand forecasting. Built ML-based dashboards to visualize key performance metrics, improving operational efficiency and decision-making.
    - Built full-stack solutions using SAP ABAP, OData, and SAP UI5 within an agile framework for another airlines ERP.
    - Led client interaction, ensuring successful project delivery and high customer satisfaction along with building POCs and KPI dashboards.
    - Earned certifications in ‘SAP ABAP’ and ‘Data Science and Machine Learning’.
    - Built a secure login portal for GXP users, enhancing security and user experience.
    """)

    # --- Key Projects ---
    st.subheader("📌 Key Projects")
    st.markdown("""
    - **[Adversarial Facial Recognition](https://github.com/Shubham111Kandpal/Adversarial-Analysis-of-Facial-Recognition-Model)**  
      Explored various adversarial attack strategies and defense mechanisms on ML-powered facial recognition systems.

    - **[ILP vs ML Churn Prediction](https://github.com/Shubham111Kandpal/Machine_Learning_-_Data_Mining)**  
      Compared traditional ML models with ILP-based Aleph engine to classify churn outcomes using synthetic and real datasets.

    - **[Churn Modeling in R](https://github.com/Shubham111Kandpal/Practical_Business_Analytics)**  
      Used XGBoost, neural networks, and SMOTE to develop robust churn models with extensive feature engineering and EDA.

    - **[Rental Bikes Web App](https://github.com/Shubham111Kandpal/WebApp_BikeRental)**  
      Built a full-stack web app using FastAPI, React.js, Docker, and CI/CD pipeline integration for real-time bike rentals.

    - **[NLP Sequence Labeling](https://github.com/Shubham111Kandpal/NLP/tree/main)**  
      Implemented LSTM, CNN, and BERT-based models with GloVe and Word2Vec embeddings for NLP entity recognition.

    - **[Trading App (AWS + GCP)](https://github.com/Shubham111Kandpal/Trading_API)**  
      Created a trading simulator with Monte Carlo simulations, serverless architecture on AWS Lambda and EC2 instances.
    
    - **[Mathematical Series Visualizations](https://github.com/Shubham111Kandpal/Mathematics_Series_Visualizer)**  
      A Streamlit-based educational app that visually illustrates various mathematical series using 2D plots, 3D plots, animations and spiral plots.  
      🌐 [Live Demo](https://skmathviz.streamlit.app/)

    - **[Trading Tool with Time Series Analysis and Forecasting](https://github.com/Shubham111Kandpal/SK-Portfolio-TradingApp)**  
      A complete time series analysis toolkit to evaluate stock prices and apply various ML models for future forecasting.  
      🌐 [Live Demo](https://sktradingtool.streamlit.app/)
    """)

    # --- Skills ---
    st.subheader("🛠 Technical Skills")
    st.markdown("""
    **Languages**: Python, R, SQL, JS, HTML, CSS, SAP ABAP  
    **ML/DS**: Regression, Classification, NLP, Transformers, Time Series, LSTM  
    **Libraries**: TensorFlow, PyTorch, Keras, Scikit-learn, XGBoost, Spacy  
    **Frameworks**: Flask, FastAPI, Django, Streamlit  
    **Tools**: Docker, Git, Tableau, Jupyter, VS Code  
    **Cloud & DevOps**: AWS (Lambda, EC2, S3), GCP, GitLab CI/CD  
    **Other**: Agile, CRISP-DM, Jira, SCRUM
    """)

    # --- Education ---
    st.subheader("🎓 Education")
    st.markdown("""
    **MSc Data Science – University of Surrey (2023–2024)**  
    Dissertation: *Adversarial ML in Facial Recognition*  
    **B.Tech Electrical Engineering – BTKIT Dwarahat (2014–2018)**
    """)

    # --- Certifications ---
    st.subheader("📜 Certifications")
    st.markdown("""
    - SAP ABAP (TCS Verified)  
    - Foundations of DS/ML in SAP (SAP Verified)  
    - Python 3 (Udemy Verified)
    """)

    # --- Interests ---
    st.subheader("🌱 Interests")
    st.markdown("""
    - Artificial Intelligence & Machine Learning  
    - Adversarial Robustness in AI  
    - Financial Data Science & Quantitative Analysis
    """)
    
if __name__ == "__main__":
    run()


    
