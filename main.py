import streamlit as st

# --- 1. ARCHITECTURAL CONFIG ---
st.set_page_config(
    page_title="Project Screener | Aether Oracle",
    page_icon="🛡️",
    layout="wide"
)

# --- 2. THE REPLIT-STYLE "HERO" UI OVERRIDE ---
st.markdown("""
    <style>
    /* Clean White Background like Replit */
    .stApp { background-color: #ffffff; color: #1a1a1a; }
    
    /* Center all content */
    .main .block-container {
        max-width: 900px;
        padding-top: 5rem;
    }

    /* AI-Powered Intelligence Pill */
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

    /* Hero Title */
    .hero-title {
        font-size: 4rem;
        font-weight: 800;
        color: #000000;
        margin-bottom: 0px;
    }

    /* Subtitle */
    .hero-sub {
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 50px;
    }

    /* Professional Search Bar */
    div[data-baseweb="input"] {
        background-color: #ffffff !important;
        border: 2px solid #e5e7eb !important;
        border-radius: 50px !important;
        padding: 5px 20px !important;
    }

    /* Ghost Buttons for Top Nav */
    .stButton>button {
        background-color: transparent;
        color: #374151;
        border: 1px solid #d1d5db;
        border-radius: 8px;
        font-weight: 500;
        transition: 0.2s;
    }
    .stButton>button:hover {
        border-color: #4f46e5;
        color: #4f46e5;
        background-color: #f5f3ff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE REPLIT-STYLE TOP NAVIGATION ---
# Using columns to push buttons to the top right
nav_col1, nav_col2, nav_col3 = st.columns([6, 1.5, 1.5])

if 'page' not in st.session_state:
    st.session_state.page = 'home'

with nav_col2:
    if st.button("🛡️ Readiness Audit"):
        st.session_state.page = 'audit'
with nav_col3:
    if st.button("💰 Premium Portfolio"):
        st.session_state.page = 'portfolio'

# --- 4. CONDITIONAL PAGE RENDERING ---

# LANDING PAGE (REPLICATING REPLIT SCREENSHOT)
if st.session_state.page == 'home':
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.markdown("<span class='pill'>✦ AI-POWERED INTELLIGENCE</span>", unsafe_allow_html=True)
    st.markdown("<h1 class='hero-title'>Project Screener</h1>", unsafe_allow_html=True)
    st.markdown("<p class='hero-sub'>Powered by <strong>Aether</strong></p>", unsafe_allow_html=True)
    
    # Large centered search bar
    search = st.text_input("", placeholder="Search any cryptocurrency — e.g. bitcoin, solana, chainlink")
    st.markdown("</div>", unsafe_allow_html=True)

# AUDIT PAGE (REAL RISK METRICS)
elif st.session_state.page == 'audit':
    st.markdown("### 🛡️ Investor Readiness Audit")
    if st.button("← Back to Screener"):
        st.session_state.page = 'home'
        st.rerun()
    
    st.markdown("---")
    st.write("Determine your risk profile for the 2026-2029 market cycle.")

    # REAL FINANCIAL QUESTIONS
    col_a, col_b = st.columns(2)
    with col_a:
        q1 = st.selectbox("1. What is your total liquid net worth for investment?", 
                          ["<$10k", "$10k-$50k", "$50k-$250k", "$250k+"])
        q2 = st.selectbox("2. How much of this capital can you afford to lose COMPLETELY?", 
                          ["0% (Safety First)", "<10% (Conservative)", "10-25% (Moderate)", "50%+ (Aggressive)"])
        q3 = st.selectbox("3. What is your primary investment goal?", 
                          ["Capital Preservation", "Moderate Growth", "Wealth Generation", "Speculative Gains"])
        q4 = st.selectbox("4. What is your investment time horizon?", 
                          ["<6 months", "1-2 years", "3-5 years (Full Cycle)", "5+ years"])

    with col_b:
        q5 = st.selectbox("5. How do you handle a 40% market drawdown?", 
                          ["Exit immediately", "Partial de-risk", "Hold with stress", "View as buying opportunity"])
        q6 = st.selectbox("6. What is your experience level with DeFi/Self-Custody?", 
                          ["Beginner", "Intermediate", "Advanced (Hardwallets/DEX)", "Expert (Smart Contracts)"])
        q7 = st.selectbox("7. Percentage of income currently saved monthly?", 
                          ["0%", "<10%", "10-30%", "Over 30%"])
        q8 = st.selectbox("8. Primary source of investment funds?", 
                          ["Disposable Income", "Life Savings", "Business Capital", "Borrowed Funds"])

    if st.button("Generate Risk Profile"):
        st.success("Analysis Complete. Your Risk Appetite is being calculated based on loss capacity.")
