import streamlit as st
import os
print(os.getcwd())
import sqlite3
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')
if not api_key:
    st.error("GOOGLE_API_KEY not found. Please set it in your .env file.")
    st.stop()

genai.configure(api_key=api_key)

prompt = [
    """
    You are an expert in converting English questions to SQL query.
    Return ONLY the SQL query.
    Do not add explanation.
    Do not add extra text.
    
    The table name is STUDENTS.
    Columns: NAME, CLASS, MARKS, COMPANY.
    """
]

def get_response(que,prompt):
    model = genai.GenerativeModel("models/gemini-flash-latest")
    response = model.generate_content([prompt[0],que])
    return response.text

def read_query(sql,db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows

def page_home():
    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            }
            .main-title {
                text-align: center;
                color: #00ff88 !important;
                font-size: 3.5em;
                font-weight: bold;
                margin-bottom: 10px;
                text-shadow: 0 0 10px rgba(0, 255, 136, 0.5);
            }
            .sub-title {
                text-align: center;
                color: #00d4ff !important;
                font-size: 1.8em;
                margin-bottom: 30px;
                font-weight: 500;
            }
            .hero-section {
                background: transparent;
                border-radius: 15px;
                padding: 20px 0;
                margin: 10px 0;
                border: none;
            }
            .offering-card {
                background: linear-gradient(135deg, rgba(42, 82, 152, 0.9), rgba(30, 60, 114, 0.9));
                border-left: 4px solid #00ff88;
                padding: 20px;
                margin: 15px 0;
                border-radius: 10px;
                color: white;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
                transition: transform 0.3s;
            }
            .offering-card:hover {
                transform: translateX(5px);
            }
            .offering-icon {
                font-size: 2em;
                margin-right: 15px;
                display: inline-block;
                min-width: 40px;
            }
            .offerings {
                display: flex;
                flex-direction: column;
                gap: 10px;
            }
            .stat-box {
                background: rgba(0, 255, 136, 0.1);
                border: 1px solid #00ff88;
                border-radius: 10px;
                padding: 20px;
                text-align: center;
                color: #00ff88;
            }
            .stat-number {
                font-size: 2.5em;
                font-weight: bold;
                color: #00d4ff;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='main-title'>🚀 Welcome to IntelliSQL!</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-title'>Revolutionizing Database Querying with Advanced LLM Capabilities</h2>",unsafe_allow_html=True)
    
    # Hero Section
    st.markdown("<div class='hero-section'>", unsafe_allow_html=True)
    st.markdown("""
        <h3 style='color: #00ff88; font-size: 1.8em;'>Transform Your SQL Experience</h3>
        <p style='color: #e0e0e0; font-size: 1.1em; line-height: 1.8;'>
            IntelliSQL leverages cutting-edge AI and Large Language Models to make database querying 
            effortless and intuitive. Convert natural language into powerful SQL queries in seconds.
        </p>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Offerings Section
    st.markdown("<h2 style='color: #00ff88; text-align: center; margin: 40px 0 30px 0;'>✨ Our Offerings</h2>", 
                unsafe_allow_html=True)
    
    offerings = [
        ("🧠", "Intelligent Query Assistance", "Convert natural language to SQL effortlessly", "https://cdn3.iconfinder.com/data/icons/network-4/32/ai-32.png"),
        ("📊", "Data Exploration", "Discover insights in your data with AI-powered analysis", "https://cdn3.iconfinder.com/data/icons/business-analytics-2/100/analytics-09-512.png"),
        ("⚡", "Efficient Retrieval", "Get results instantly with optimized queries", "https://cdn3.iconfinder.com/data/icons/technology-and-multimedia/128/lightning_speed-512.png"),
        ("🚀", "Performance Optimization", "Auto-optimize your SQL for better performance", "https://cdn3.iconfinder.com/data/icons/technology-5/64/rocket-512.png"),
        ("📝", "Syntax Suggestions", "Real-time SQL syntax guidance and corrections", "https://cdn2.iconfinder.com/data/icons/file-and-folder-1/512/file-text-512.png"),
        ("📈", "Trend Analysis", "Identify patterns and trends in your datasets", "https://cdn3.iconfinder.com/data/icons/business-analytics-1/128/chart_line_graph_up-512.png")
    ]
    
    cols = st.columns(3)
    for idx, (icon, title, desc, img_url) in enumerate(offerings):
        with cols[idx % 3]:
            st.markdown(f"""
                <div class='offering-card'>
                    <div style='font-size: 2em; margin-bottom: 10px;'>{icon}</div>
                    <h4 style='color: #00ff88; margin: 0 0 10px 0;'>{title}</h4>
                    <p style='color: #c0c0c0; font-size: 0.95em; margin: 0;'>{desc}</p>
                </div>
            """, unsafe_allow_html=True)
        
def page_about():
    st.markdown("""
        <style>
            .about-section {
                background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
                padding: 0;
            }
            .about-title {
                color: #00ff88;
                font-size: 3em;
                text-align: center;
                margin: 40px 0;
                text-shadow: 0 0 10px rgba(0, 255, 136, 0.5);
            }
            .about-content {
                color: #e0e0e0;
                font-size: 1.15em;
                line-height: 1.8;
                background: rgba(0, 255, 136, 0.05);
                border-left: 4px solid #00ff88;
                padding: 30px;
                border-radius: 10px;
                margin: 20px 0;
            }
            .about-content h3 {
                color: #00d4ff;
                font-size: 1.6em;
                margin-top: 20px;
            }
            .feature-list {
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 20px;
                margin: 30px 0;
            }
            .feature-item {
                background: rgba(0, 212, 255, 0.1);
                border: 1px solid #00d4ff;
                padding: 20px;
                border-radius: 10px;
                color: #c0c0c0;
            }
            .feature-item h4 {
                color: #00ff88;
                margin-top: 0;
            }
        </style>
    """,unsafe_allow_html=True)
    
    st.markdown("<h1 class='about-title'>📚 About IntelliSQL</h1>", unsafe_allow_html=True)
    
    st.markdown("### What is IntelliSQL?")
    st.write("IntelliSQL is an innovative project aimed at revolutionizing database querying using advanced Language Model capabilities. Powered by cutting-edge LLM (Large Language Model) architecture, particularly Google's Gemini Pro, this system offers users an intelligent platform for interacting with SQL databases effortlessly and intuitively.")
    
    st.markdown("### Our Mission")
    st.write("To democratize database access by eliminating the need for advanced SQL knowledge. Whether you're a beginner or an expert, IntelliSQL makes it easy to query databases using natural language.")
    
    st.markdown("### How It Works")
    st.write("Simply describe what data you want in plain English, and our AI engine converts it into optimized SQL queries. Get instant results from your database without writing a single SQL command.")
    
    st.markdown("<h2 style='color: #00ff88; text-align: center; margin: 40px 0;'>🎯 Key Features</h2>", unsafe_allow_html=True)
    
    features = [
        ("Natural Language Processing", "Convert English questions into SQL queries automatically", "https://cdn3.iconfinder.com/data/icons/ai-and-machine-learning-1/128/nlp-natural-language-processing-512.png"),
        ("AI-Powered Assistance", "Leverage Google's Gemini Pro LLM for intelligent suggestions", "https://cdn2.iconfinder.com/data/icons/artificial-intelligence-5/64/machine-learning-256.png"),
        ("Real-time Results", "Get instant database query results", "https://cdn3.iconfinder.com/data/icons/business-analytics-1/128/speed-512.png"),
        ("Error Handling", "Intelligent error detection and recovery", "https://cdn3.iconfinder.com/data/icons/business-icons-1/512/shield-512.png")
    ]
    
    cols = st.columns(2)
    for idx, (title, desc, icon_url) in enumerate(features):
        with cols[idx % 2]:
            st.markdown(f"""
                <div class='feature-item'>
                    <h4>✨ {title}</h4>
                    <p>{desc}</p>
                </div>
            """, unsafe_allow_html=True)

def page_intelligent_query_assistance():
    st.markdown("""
        <style>
            .query-title {
                color: #00ff88;
                font-size: 2.8em;
                text-align: center;
                margin-bottom: 30px;
                text-shadow: 0 0 10px rgba(0, 255, 136, 0.5);
            }
            .query-description {
                color: #e0e0e0;
                text-align: center;
                font-size: 1.1em;
                margin-bottom: 40px;
                line-height: 1.6;
            }
            .input-section {
                background: transparent;
                border: none;
                border-radius: 15px;
                padding: 15px 0;
                margin: 10px 0;
            }
            .query-input-label {
                color: #00ff88;
                font-size: 1.3em;
                font-weight: bold;
                margin-bottom: 15px;
            }
            .button-container {
                display: flex;
                gap: 10px;
                margin: 20px 0;
            }
            .sql-result {
                background: rgba(0, 212, 255, 0.1);
                border-left: 4px solid #00d4ff;
                border-radius: 10px;
                padding: 20px;
                margin: 20px 0;
            }
            .sql-code {
                background: #0a0e27;
                color: #00ff88;
                padding: 15px;
                border-radius: 8px;
                font-family: 'Courier New', monospace;
                overflow-x: auto;
                margin: 10px 0;
                border: 1px solid #00ff88;
            }
            .result-section {
                background: linear-gradient(135deg, rgba(0, 255, 136, 0.05), rgba(0, 212, 255, 0.05));
                border-radius: 10px;
                padding: 20px;
                margin: 20px 0;
            }
            .result-header {
                color: #00ff88;
                font-size: 1.4em;
                font-weight: bold;
                margin-bottom: 15px;
            }
            .side-image {
                text-align: center;
                margin-top: 20px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='query-title'>🔍 Intelligent Query Assistance</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class='query-description'>
            IntelliSQL enhances the querying process by providing intelligent assistance. Whether you're a novice or experienced SQL user,
            our AI guides you through crafting complex queries with ease. Simply describe what data you want, and let the magic happen!
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='input-section'>", unsafe_allow_html=True)
    st.markdown("<div class='query-input-label'>📝 Enter Your Natural Language Query:</div>", unsafe_allow_html=True)
    
    que = st.text_area(
        label="Query input",
        placeholder="Example: Show me all students from INFOSYS company with marks above 85",
        height=100,
        label_visibility="collapsed"
    )
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        submit = st.button("🚀 Get SQL Query", use_container_width=True, key="submit_button")
    with col_btn2:
        st.button("📋 Clear", use_container_width=True, key="clear_button")
    
    st.markdown("</div>", unsafe_allow_html=True)

    if submit and que:
        with st.spinner("🤔 Generating SQL query..."):
            try:
                response = get_response(que, prompt)
                import re
                match = re.search(r"SELECT.*?;", response, re.IGNORECASE | re.DOTALL)
                if match:
                    sql_query = match.group(0)
                    
                    st.markdown("""
                        <div class='sql-result'>
                            <div style='color: #00ff88; font-weight: bold; margin-bottom: 10px;'>✅ Generated SQL Query:</div>
                    """, unsafe_allow_html=True)
                    st.markdown(f"<div class='sql-code'>{sql_query}</div>", unsafe_allow_html=True)
                    st.markdown("</div>", unsafe_allow_html=True)
                    
                    with st.spinner("⏳ Executing query..."):
                        result = read_query(sql_query, "data.db")
                    
                    if result:
                        st.markdown("<div class='result-section'>", unsafe_allow_html=True)
                        st.markdown("<div class='result-header'>📊 Query Results:</div>", unsafe_allow_html=True)
                        
                        # Create a dataframe for better display
                        import sqlite3
                        conn = sqlite3.connect("data.db")
                        cursor = conn.cursor()
                        cursor.execute(sql_query)
                        columns = [description[0] for description in cursor.description]
                        conn.close()
                        
                        import pandas as pd
                        df = pd.DataFrame(result, columns=columns)
                        st.dataframe(df, use_container_width=True, hide_index=True)
                        st.markdown("</div>", unsafe_allow_html=True)
                    else:
                        st.info("ℹ️ Query executed successfully but returned no results.")
                else:
                    st.warning("⚠️ No valid SQL query found in the response. Please try rephrasing your question.")
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")
    elif submit and not que:
        st.warning("⚠️ Please enter a query first!")
    
    st.markdown("""
        <div style='background: rgba(0, 255, 136, 0.1); border: 1px solid #00ff88; 
                    border-radius: 10px; padding: 20px; margin-top: 30px;'>
            <h4 style='color: #00ff88; margin-top: 0;'>💡 Tips:</h4>
            <ul style='color: #c0c0c0; font-size: 0.9em;'>
                <li>Be specific about what data you need</li>
                <li>Mention table names and columns</li>
                <li>Include any conditions or filters</li>
                <li>Ask for sorting or grouping if needed</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
def main():
    st.set_page_config(
        page_title="IntelliSQL",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS for the entire app
    st.markdown("""
        <style>
            [data-testid="stAppViewContainer"] {
                background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            }
            [data-testid="stSidebar"] {
                background: linear-gradient(135deg, #0f1e35 0%, #1a3a52 100%);
            }
            [data-testid="stSidebarNav"] {
                padding-top: 20px;
            }
            .stRadio [role="radio"] {
                color: #00ff88 !important;
            }
            .stRadio label {
                color: #e0e0e0 !important;
                font-weight: bold;
            }
            .stButton>button {
                background: linear-gradient(135deg, #00ff88, #00d4ff);
                color: #000 !important;
                font-weight: bold;
                border-radius: 8px;
                border: none;
                transition: all 0.3s;
            }
            .stButton>button:hover {
                transform: translateY(-2px);
                box-shadow: 0 4px 15px rgba(0, 255, 136, 0.4);
            }
            .stTextInput>div>div>input {
                background: rgba(255, 255, 255, 0.1);
                color: #e0e0e0;
                border: 1px solid #00ff88 !important;
            }
            .stTextArea>div>div>textarea {
                background: rgba(255, 255, 255, 0.1);
                color: #e0e0e0;
                border: 1px solid #00ff88 !important;
            }
            h1, h2, h3, h4, h5, h6 {
                color: #00ff88;
            }
            .stTabs [data-baseweb="tab-list"] button {
                color: #e0e0e0;
            }
            .stTabs [data-baseweb="tab"] {
                color: #00ff88;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.sidebar.title("🎯 Navigation")
    st.sidebar.markdown("---")
    
    pages = {
        "🏠 Home": page_home,
        "📚 About": page_about,
        "🔍 Query Assistance": page_intelligent_query_assistance,
    }
    
    selection = st.sidebar.radio("Select a page:", list(pages.keys()))
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
        <div style='text-align: center; color: #00ff88; font-size: 0.9em;'>
            <p>🚀 <strong>IntelliSQL v1.0</strong></p>
            <p style='font-size: 0.8em; color: #c0c0c0;'>Powered by Google Gemini Pro</p>
        </div>
    """, unsafe_allow_html=True)
    
    page = pages[selection]
    page()

if __name__ == "__main__":
    main()

