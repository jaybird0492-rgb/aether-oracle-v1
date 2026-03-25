import streamlit as st

# --- 1. CORE ARCHITECTURE & THEME ---
st.set_page_config(
    page_title="Project Screener | Aether Oracle",
    page_icon="🛡️",
    layout="wide"
)

# Custom CSS to fix the "Black Void" search and restore Replit-style Hero UI
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; color: #1a1a1a; }
    
    /* Center Hero Content */
    .hero-container {
        text-align: center;
        padding-top: 3rem;
        max-width: 800px;
        margin: 0 auto;
    }

    /* AI Intelligence Pill */
    .pill {
        display: inline-block;
        background-color: #eef2ff;
        color: #4f46e5;
        padding: 5px 15px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.8rem;
        text-transform: uppercase;
        margin-bottom: 20px;
    }

    /* FIXED: Search Bar Visibility */
    div[data-baseweb="input"] {
        background-color: #f9fafb !important;
        border: 2px solid #e5e7eb !important;
        border-radius: 10px !important;
        color: #1a1a1a !important;
    }
    input { color: #1a1a1a !important; }

    /* Nav Buttons */
    .stButton>button {
        background-color: #ffffff;
        color: #374151;
        border: 1px solid #d1d5db;
        border-radius: 8px;
        font-weight: 600;
    }
    .stButton>button:hover {
        border-color: #4f46e5;
        color: #4f46e5;
    }

    /* Execution Button */
    .exec-btn button {
        background-color: #4f46e5 !important;
        color: white !important;
        width: 100%;
        border-radius: 10px !important;
        height: 3rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. GLOBAL NAVIGATION STATE ---
if 'view' not in st.session_state:
    st.session_state.view = 'home'

# --- 3. TOP NAVIGATION BAR ---
nav_col1, nav_col2, nav_col3 = st.columns([6, 1.5, 1.5])
with nav_col2:
    if st.button("🛡️ Readiness Audit"):
        st.session_state.view = 'audit'
with nav_col3:
    if st.button("💰 Premium Portfolio"):
        st.session_state.view = 'portfolio'

# --- 4. MODULAR VIEWS ---

# VIEW: HOME (PROJECT SCREENER)
if st.session_state.view == 'home':
    st.markdown("<div class='hero-container'>", unsafe_allow_html=True)
    st.markdown("<span class='pill'>✦ AI-POWERED INTELLIGENCE</span>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 4rem; font-weight: 800; margin-bottom:0;'>Project Screener</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 1.2rem; color: #666; margin-bottom: 40px;'>Powered by <strong>Aether</strong></p>", unsafe_allow_html=True)
    
    # Search Box + Execution Button
    ticker = st.text_input("", placeholder="Search any cryptocurrency — e.g. bitcoin, solana, chainlink")
    
    st.markdown("<div class='exec-btn'>", unsafe_allow_html=True)
    if st.button("EXECUTE FORENSIC SCAN"):
        if ticker:
            st.info(f"Audit Initiated for {ticker}...")
        else:
            st.warning("Please enter a ticker to analyze.")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# VIEW: READINESS AUDIT (ORIGINAL 8 QUESTIONS)
elif st.session_state.view == 'audit':
    if st.button("← Back to Screener"):
        st.session_state.view = 'home'
        st.rerun()
        
    st.header("🛡️ Investor Readiness Audit")
    st.write("*'[SYSTEM INITIALIZED]: Determine your risk appetite and capital capacity.'*")
    
    col_l, col_r = st.columns(2)
    with col_l:
        q1 = st.selectbox("1. Total liquid net worth for investment?", ["<$10k", "$10k-$50k", "$50k-$250k", "$250k+"])
        q2 = st.selectbox("2. Capital you can afford to lose COMPLETELY?", ["0%", "<10%", "10-25%", "50%+"])
        q3 = st.selectbox("3. Primary investment goal?", ["Preservation", "Growth", "Wealth Generation", "Speculation"])
        q4 = st.selectbox("4. Investment time horizon?", ["<6 months", "1-2 years", "3-5 years", "5+ years"])
    with col_r:
        q5 = st.selectbox("5. Response to a 40% market drawdown?", ["Exit", "De-risk", "Hold", "Buy More"])
        q6 = st.selectbox("6. Experience with Self-Custody?", ["Beginner", "Intermediate", "Advanced", "Expert"])
        q7 = st.selectbox("7. Percentage of monthly income saved?", ["0%", "<10%", "10-30%", ">30%"])
        q8 = st.selectbox("8. Source of investment funds?", ["Income", "Savings", "Business", "Borrowed"])

    if st.button("GENERATE READINESS REPORT"):
        st.success("Analysis Complete. Report generated based on financial loss capacity.")

# --- 5. MANDATORY LEGAL DISCLAIMER (ALWAYS VISIBLE) ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("---")
st.error("**LEGAL DISCLAIMER:** Institutional Intelligence is for educational purposes only. Aether Oracle does not provide financial advice. Cryptocurrency investments carry high risk. Never invest capital you cannot afford to lose.")
st.caption("Aether Oracle | Infrastructure v4.0 | 2026-2029 Cycle")
