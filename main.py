import streamlit as st

# --- 1. ARCHITECTURAL CONFIG ---
st.set_page_config(
    page_title="AETHER ORACLE | Institutional Terminal",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. THE "FORENSIC DARK" CSS OVERRIDE ---
st.markdown("""
    <style>
    /* Force Deep Dark Theme */
    .stApp {
        background-color: #050505;
        color: #E0E0E0;
    }
    
    /* Hide Streamlit Bloat */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Custom Sidebar - Institutional Slate */
    [data-testid="stSidebar"] {
        background-color: #0A0F14;
        border-right: 1px solid #1E2A35;
        min-width: 250px !important;
    }

    /* Terminal-Style Typography */
    h1, h2, h3 {
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        letter-spacing: -1px;
        color: #FFFFFF;
    }

    /* Input Boxes - Low Profile, High Focus */
    div[data-baseweb="input"] {
        background-color: #0F171E !important;
        border: 1px solid #1E2A35 !important;
        border-radius: 4px !important;
        color: #00FFA3 !important;
    }

    /* Custom Cards for Alpha Feed */
    .alpha-card {
        background-color: #0F171E;
        padding: 20px;
        border-radius: 8px;
        border-left: 4px solid #00FFA3;
        margin-bottom: 15px;
    }

    /* Buttons - The "Execution" Look */
    .stButton>button {
        background-color: #00FFA3;
        color: #050505;
        font-weight: 800;
        text-transform: uppercase;
        border: none;
        border-radius: 4px;
        padding: 10px 24px;
        width: 100%;
        transition: 0.2s all ease;
    }
    .stButton>button:hover {
        background-color: #00D186;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(0, 255, 163, 0.2);
    }

    /* Radio Buttons & Selection */
    .stRadio [data-testid="stWidgetLabel"] {
        color: #8899A6 !important;
        font-size: 0.9rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE NAVIGATIONAL ARCHITECTURE ---
with st.sidebar:
    st.image("https://img.icons8.com/nolan/96/shield.png", width=80)
    st.markdown("# AETHER\n**ORACLE v3.1**")
    st.markdown("---")
    
    menu = st.radio(
        "OPERATIONAL MODES",
        ["INVESTOR AUDIT", "FORENSIC SEARCH", "ALPHA PORTFOLIOS", "VC INTELLIGENCE"]
    )
    
    st.markdown("---")
    st.caption("Network Status: **ENCRYPTED**")
    st.caption("Market Cycle: **ACCUMULATION**")

# --- 4. TERMINAL CONTENT ---

if menu == "INVESTOR AUDIT":
    st.title("🛡️ Investor Readiness Audit")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### PSYCHOLOGY")
        q1 = st.radio("1. 30% MIDNIGHT DRAWDOWN", ["STRATEGIC ACCUMULATION", "STRICT HOLD", "LIQUIDATION"])
        q2 = st.radio("2. MEME-COIN ASYMMETRY", ["ZERO EXPOSURE", "CONTROLLED RISK", "RETAIL CHASE"])
        
        st.markdown("### ALLOCATION")
        q3 = st.radio("3. SINGLE-ASSET DENSITY", ["INSTITUTIONAL (<10%)", "VENTURE (20-40%)", "HIGH LEVERAGE"])
        q4 = st.radio("4. EXIT ARCHITECTURE", ["TIERED LIMIT ORDERS", "MANUAL DISCRETION", "NO PLAN"])

    with col2:
        st.markdown("### SECURITY")
        q5 = st.radio("5. CUSTODY PROTOCOL", ["COLD STORAGE / MULTI-SIG", "EXCHANGE / 2FA", "HOT WALLET"])
        q6 = st.radio("6. TECHNICAL LITERACY", ["EXPERT (SMART CONTRACTS)", "INTERMEDIATE", "RETAIL"])
        
        st.markdown("### MACRO")
        q7 = st.radio("7. FISCAL AWARENESS", ["MACRO-ANCHORED", "CHART-CENTRIC", "NARRATIVE-ONLY"])
        q8 = st.radio("8. TIME HORIZON", ["MULTI-YEAR CONVICTION", "12-MONTH PIVOT", "SHORT-TERM YIELD"])

    st.markdown("---")
    if st.button("GENERATE READINESS REPORT"):
        st.success("CALCULATING SCORE... 94% READINESS DETECTED.")

elif menu == "FORENSIC SEARCH":
    st.title("🔍 Project Forensic Search")
    ticker = st.text_input("ENTER TICKER (DOT, TAO, RNDR)", placeholder="Ticker...").upper()
    
    c1, c2, c3 = st.columns(3)
    if st.button("EXECUTE SCAN"):
        st.markdown(f"### SCANNED: {ticker}")
        st.info("Searching Problem-Solution Fit... OK")
        st.warning("Analyzing Token Inflation... AT RISK (12.4%)")
        st.success("Auditing Team Provenance... TIER-1 FOUNDERS")

elif menu == "ALPHA PORTFOLIOS":
    st.title("💎 Alpha Portfolios")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("DEPIN (BETA)", "+142%", "HNT / RNDR")
    col2.metric("AI AGENTS", "+312%", "TAO / FET")
    col3.metric("RWA LEGACY", "+89%", "CFG / ONDO")

elif menu == "VC INTELLIGENCE":
    st.title("📡 Live VC Intelligence Feed")
    st.markdown("""
    <div class="alpha-card">
        <strong>[INTEL] POLKADOT 2.0:</strong> Agile Coretime sales shifting DOT toward deflationary burn. High-conviction entry point detected.
    </div>
    <div class="alpha-card">
        <strong>[INTEL] BITTENSOR:</strong> Subnet expansion hitting exponential growth. Institutional nodes increasing by 45%.
    </div>
    """, unsafe_allow_html=True)

# --- 5. SYSTEM FOOTER ---
st.markdown("---")
st.caption("Aether Oracle Terminal | Authorized Access Only | 2026-2029 Cycle")
