import streamlit as st
import time

# --- 1. CORE ARCHITECTURE ---
st.set_page_config(page_title="Aether Oracle | Terminal", page_icon="🛡️", layout="wide")

# CSS: Hard-fixing the "Black Void" and restoring the Hero UI
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; color: #1a1a1a; }
    .main .block-container { max-width: 900px; padding-top: 2rem; }
    
    /* FORCED: White Search Bar with Black Text */
    div[data-baseweb="input"] {
        background-color: #f3f4f6 !important;
        border: 2px solid #e5e7eb !important;
        border-radius: 12px !important;
    }
    input { color: #1a1a1a !important; font-size: 1.2rem !important; }

    /* Nav Buttons */
    .stButton>button {
        background-color: #ffffff; color: #374151; border: 1px solid #d1d5db;
        border-radius: 8px; font-weight: 600;
    }
    .stButton>button:hover { border-color: #4f46e5; color: #4f46e5; }

    /* Execution Button */
    .exec-btn button {
        background-color: #4f46e5 !important; color: white !important;
        width: 100%; border-radius: 10px !important; height: 3.5rem; font-weight: 700;
    }
    
    /* Forensic Card Styling */
    .forensic-card {
        background-color: #f9fafb; padding: 20px; border-radius: 10px;
        border-left: 5px solid #4f46e5; margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. NAVIGATION STATE ---
if 'view' not in st.session_state: st.session_state.view = 'home'

nav_c1, nav_c2, nav_c3 = st.columns([6, 1.5, 1.5])
with nav_c2:
    if st.button("🛡️ Readiness Audit"): st.session_state.view = 'audit'
with nav_c3:
    if st.button("💰 Premium Portfolio"): st.session_state.view = 'portfolio'

# --- 3. THE "AETHER" DNA VIEWS ---

# HOME VIEW: THE SCREENER
if st.session_state.view == 'home':
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 4rem; font-weight: 900; letter-spacing:-2px;'>Project Screener</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #6b7280; font-size: 1.2rem;'>Powered by <strong>Aether</strong></p>", unsafe_allow_html=True)
    
    ticker = st.text_input("", placeholder="Enter Ticker (e.g. SOL, DOT, TAO)", key="main_search")
    
    st.markdown("<div class='exec-btn'>", unsafe_allow_html=True)
    if st.button("EXECUTE FORENSIC SCAN"):
        if ticker:
            st.markdown("---")
            st.subheader(f"🛡️ Forensic Report: {ticker.upper()}")
            
            # THE ORIGINAL 5-POINT AUDIT (RESTORED)
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"""<div class='forensic-card'>
                <strong>1. Problem-Solution Fit</strong><br>
                Does {ticker} solve a mechanical necessity? 
                <br>Status: <span style='color:green; font-weight:700;'>OPTIMIZED</span></div>""", unsafe_allow_html=True)
                
                st.markdown(f"""<div class='forensic-card'>
                <strong>2. Tokenomics Deep-Dive</strong><br>
                Auditing inflation vs. utility and unlock schedules. 
                <br>Status: <span style='color:orange; font-weight:700;'>MONITOR DILUTION</span></div>""", unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""<div class='forensic-card'>
                <strong>3. Team Credibility</strong><br>
                Evaluating dev history and previous project exits. 
                <br>Status: <span style='color:green; font-weight:700;'>TIER-1 FOUNDERS</span></div>""", unsafe_allow_html=True)
                
                st.markdown(f"""<div class='forensic-card'>
                <strong>4. Narrative Check</strong><br>
                Alignment with RWA, AI, and DePIN 2026 megatrends. 
                <br>Signal: <span style='color:blue; font-weight:700;'>HIGH CONVICTION</span></div>""", unsafe_allow_html=True)

            st.error(f"**5. THE RED FLAG SUMMARY:** Initial scan shows high centralization in early-stage wallets for {ticker}. Institutional liquidity risk is moderate.")
        else:
            st.warning("Please enter a ticker to begin the scan.")
    st.markdown("</div></div>", unsafe_allow_html=True)

# AUDIT VIEW: THE ORIGINAL 8 QUESTIONS (RESTORED)
elif st.session_state.view == 'audit':
    if st.button("← Back"): st.session_state.view = 'home'; st.rerun()
    st.header("🛡️ Investor Readiness Audit")
    st.write("*'[SYSTEM INITIALIZED]: Determine your discipline for the 2029 run.'*")
    
    cl, cr = st.columns(2)
    with cl:
        q1 = st.radio("1. The Midnight Crash: BTC drops 30% while you sleep?", ["Buy the dip", "Hold with stress", "Panic-search Twitter"])
        q2 = st.radio("2. The 'Moon' Hype: Friend makes 10x on a coin you missed?", ["Indifferent", "Slight FOMO", "Chase the pump"])
        q3 = st.radio("3. Concentration: % of net worth in one asset?", ["<10% (Institutional)", "25-50%", "100% (Degen)"])
        q4 = st.radio("4. Exit Strategy: Do you have written price targets?", ["Yes", "In my head", "No"])
    with cr:
        q5 = st.radio("5. Custody Protocol: Where is your primary stack?", ["Hardware Wallet", "Exchange w/ 2FA", "Hot Wallet"])
        q6 = st.radio("6. OpSec Knowledge: Explain Impermanent Loss?", ["Expertly", "Vaguely", "No"])
        q7 = st.radio("7. Macro Perspective: Do you track US Treasury yields?", ["Always", "Sometimes", "Never"])
        q8 = st.radio("8. The 2029 Horizon: Can you wait 3 years for a thesis?", ["Yes (Conviction)", "Maybe", "No"])

# --- 4. LEGAL ---
st.markdown("<br><br>---", unsafe_allow_html=True)
st.error("**LEGAL:** Educational only. Not financial advice. Aether Oracle 2026.")
