import streamlit as st

# --- 1. SYSTEM CONFIG & INSTITUTIONAL STYLING ---
st.set_page_config(
    page_title="Aether Oracle | Institutional Intelligence",
    page_icon="🛡️",
    layout="wide"
)

# Forensic UI Injection (CSS)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #161b22; border-right: 1px solid #00FFA3; }
    div[data-baseweb="input"] { background-color: #1c2128 !important; border: 1px solid #00FFA3 !important; color: white !important; }
    .stButton>button { background-color: #1c2128; color: #00FFA3; border: 1px solid #00FFA3; width: 100%; transition: 0.3s; }
    .stButton>button:hover { background-color: #00FFA3; color: #0e1117; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ Coach Aether")
    st.info("Institutional Intelligence: 2026-2029 Cycle.")
    menu = st.radio("Navigation", ["Readiness Audit", "Project Oracle"])

# --- 3. MAIN CONTENT ENGINE ---

if menu == "Readiness Audit":
    st.header("🛡️ Investor Readiness Audit")
    st.write("'*[SYSTEM INITIALIZED]: Answer all 8 directives. I am Aether. Let’s see if you have the discipline to survive the 2029 run.*'")
    
    # --- THE 8-QUESTION FORENSIC SUITE ---
    with st.container():
        st.subheader("Section 1: Psychological Resilience")
        q1 = st.radio("1. The Midnight Crash: Bitcoin drops 30% while you sleep. Your first move?",
                      ["Buy the dip (Calculated)", "Hold with high heart rate", "Panic-search Twitter"])
        
        q2 = st.radio("2. The 'Moon' Hype: A friend makes 10x on a meme coin you missed. How do you feel?",
                      ["Indifferent (My strategy is sovereign)", "Slight FOMO but I stay the course", "I chase the next pump immediately"])

        st.markdown("---")
        st.subheader("Section 2: Capital Allocation")
        q3 = st.radio("3. Portfolio Concentration: What percentage of your net worth is in one asset?",
                      ["Less than 10% (Institutional)", "25-50% (High Risk)", "100% (Degenerate)"])
        
        q4 = st.radio("4. Exit Strategy: Do you have a price target written down for your 'Main Bag'?",
                      ["Yes, with tiered sell orders", "I have a vague number in my head", "I'll sell when it 'feels' like the top"])

        st.markdown("---")
        st.subheader("Section 3: Security Hygiene")
        q5 = st.radio("5. Custody Protocol: Where is your primary stack held?",
                      ["Hardware Wallet / Cold Storage", "Reputable Exchange with 2FA", "Phone Wallet / Hot Wallet"])
        
        q6 = st.radio("6. OpSec Knowledge: Can you explain 'Slippage' or 'Impermanent Loss' to a 5-year-old?",
                      ["Yes (Expert)", "Vaguely (Intermediate)", "No (Retail)"])

        st.markdown("---")
        st.subheader("Section 4: Market Intelligence")
        q7 = st.radio("7. Macro Perspective: Does your portfolio account for US Treasury yields or CPI data?",
                      ["Yes, macro is my anchor", "I follow it but don't trade on it", "I only watch token charts"])
        
        q8 = st.radio("8. The 2029 Horizon: Are you prepared to wait 3 years for your thesis to play out?",
                      ["Yes (Conviction)", "Maybe (Emotional)", "No (I need gains this month)"])

    if st.button("Generate Readiness Report"):
        st.success("Analysis Complete. Score: [SYSTEM CALCULATING...]")
        st.info("Institutional Feedback: Most users fail on Q4 and Q5. Review your exit strategy.")

elif menu == "Project Oracle":
    st.header("🔮 Project Oracle: Forensic Screener")
    ticker = st.text_input("Enter Token Ticker (e.g., DOT, TAO, RNDR)", "").upper()
    if st.button("Run Forensic Analysis"):
        st.info(f"Audit Initiated for {ticker}...")

# --- 4. FOOTER ---
st.markdown("---")
st.caption("Aether Oracle | Infrastructure v1.2")
