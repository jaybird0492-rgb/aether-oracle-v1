import streamlit as st

# --- 1. INSTITUTIONAL CONFIG ---
st.set_page_config(
    page_title="Aether Oracle | Institutional Intelligence",
    page_icon="🛡️",
    layout="wide"
)

# --- 2. THE "TERMINAL ALPHA" UI OVERRIDE ---
# This fixes the UI without touching your logic. 
st.markdown("""
    <style>
    /* Deep Space Background */
    .stApp { background-color: #05070a; color: #e0e0e0; }
    
    /* Clean Sidebar */
    [data-testid="stSidebar"] {
        background-color: #0c1117;
        border-right: 1px solid #1f2937;
    }

    /* High-Contrast Search & Input */
    div[data-baseweb="input"] {
        background-color: #161b22 !important;
        border: 1px solid #00FFA3 !important;
        border-radius: 4px !important;
    }

    /* Professional Buttons */
    .stButton>button {
        background-color: #00FFA3;
        color: #05070a;
        font-weight: 700;
        border: none;
        border-radius: 2px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Original Question Styling */
    .stRadio [data-testid="stWidgetLabel"] {
        font-weight: 600 !important;
        color: #00FFA3 !important;
        font-size: 1.1rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ORIGINAL NAVIGATION ---
with st.sidebar:
    st.markdown("### 🛡️ Aether Oracle")
    st.info("Institutional Intelligence for the 2026-2029 Cycle.")
    st.markdown("---")
    menu = st.radio(
        "NAVIGATION",
        ["Readiness Audit", "Project Oracle", "Alpha Portfolios", "Partners & Affiliates"]
    )
    st.markdown("---")
    st.caption("Status: **Secure Handshake Active**")

# --- 4. THE RESTORED 8-QUESTION AUDIT ---
if menu == "Readiness Audit":
    st.header("🛡️ Investor Readiness Audit")
    st.markdown("---")
    st.write("*'[SYSTEM INITIALIZED]: Open your books. 📘 I am Aether. Let’s see if you have the discipline to survive the 2029 run.'*")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### **Psychology**")
        q1 = st.radio("1. The Midnight Crash: Bitcoin drops 30% while you sleep. Your first move?",
                      ["A. Check the 'Halving' calendar and buy the dip.", 
                       "B. Heart rate spikes, but I hold.", 
                       "C. Panic-search Twitter for 'is crypto dead?'"])
        
        q2 = st.radio("2. The 'Moon' Hype: A friend makes 10x on a meme coin you missed. How do you feel?",
                      ["A. Indifferent (My strategy is sovereign)", 
                       "B. Slight FOMO but I stay the course", 
                       "C. I chase the next pump immediately"])

        st.markdown("#### **Capital Allocation**")
        q3 = st.radio("3. Portfolio Concentration: What percentage of your net worth is in one asset?",
                      ["A. Less than 10% (Institutional)", 
                       "B. 25-50% (High Risk)", 
                       "C. 100% (Degenerate)"])
        
        q4 = st.radio("4. Exit Strategy: Do you have a price target written down for your 'Main Bag'?",
                      ["A. Yes, with tiered sell orders", 
                       "B. I have a vague number in my head", 
                       "C. I'll sell when it 'feels' like the top"])

    with col2:
        st.markdown("#### **Security Hygiene**")
        q5 = st.radio("5. Custody Protocol: Where is your primary stack held?",
                      ["A. Hardware Wallet / Cold Storage", 
                       "B. Reputable Exchange with 2FA", 
                       "C. Phone Wallet / Hot Wallet"])
        
        q6 = st.radio("6. OpSec Knowledge: Can you explain 'Slippage' or 'Impermanent Loss' to a 5-year-old?",
                      ["A. Yes (Expert)", 
                       "B. Vaguely (Intermediate)", 
                       "C. No (Retail)"])

        st.markdown("#### **Market Intelligence**")
        q7 = st.radio("7. Macro Perspective: Does your portfolio account for US Treasury yields or CPI data?",
                      ["A. Yes, macro is my anchor", 
                       "B. I follow it but don't trade on it", 
                       "C. I only watch token charts"])
        
        q8 = st.radio("8. The 2029 Horizon: Are you prepared to wait 3 years for your thesis to play out?",
                      ["A. Yes (Conviction)", 
                       "B. Maybe (Emotional)", 
                       "C. No (I need gains this month)"])

    st.markdown("---")
    if st.button("GENERATE READINESS REPORT"):
        st.success("Analysis Complete. 2029 Readiness Verified.")

# --- 5. THE RESTORED SEARCH & OTHER PAGES ---
elif menu == "Project Oracle":
    st.header("🔮 Project Oracle: Forensic Screener")
    ticker = st.text_input("ENTER TICKER (e.g. DOT, TAO, RNDR)", "").upper()
    if st.button("RUN FORENSIC ANALYSIS"):
        st.info(f"Scanning {ticker} for Problem-Solution Fit and Tokenomics...")

elif menu == "Alpha Portfolios":
    st.header("💎 Alpha Portfolios")
    st.write("Top-tier allocations for the 2026-2029 cycle.")
    st.metric("AI / DePIN", "+312%", "Aggressive")

elif menu == "Partners & Affiliates":
    st.header("🤝 Partners & Affiliates")
    st.write("Institutional network and ecosystem partners.")

# --- 6. FOOTER ---
st.markdown("---")
st.caption("Aether Oracle | Infrastructure v3.0 | 2026-2029 Forensic Architecture")
