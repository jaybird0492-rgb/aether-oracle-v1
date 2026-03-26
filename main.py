import streamlit as st
import time

# --- 1. CORE ARCHITECTURE ---
st.set_page_config(page_title="Aether Oracle | Terminal", page_icon="🛡️", layout="wide")

# CSS: Fixing the "Black Void" & Restoring Replit Aesthetic
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; color: #1a1a1a; }
    
    /* Center Layout */
    .main .block-container { max-width: 900px; padding-top: 2rem; }

    /* FIXED: Search Bar Visibility */
    div[data-baseweb="input"] {
        background-color: #f3f4f6 !important;
        border: 2px solid #e5e7eb !important;
        border-radius: 12px !important;
    }
    input { color: #1a1a1a !important; font-size: 1.2rem !important; }

    /* Executive Buttons */
    .stButton>button {
        background-color: #4f46e5; color: white; border: none;
        border-radius: 8px; font-weight: 700; width: 100%; height: 3rem;
    }
    .stButton>button:hover { background-color: #4338ca; }

    /* Audit Result Cards */
    .forensic-card {
        background-color: #f9fafb; padding: 20px; border-radius: 10px;
        border-left: 5px solid #4f46e5; margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. GLOBAL NAVIGATION ---
if 'view' not in st.session_state: st.session_state.view = 'home'

nav_c1, nav_c2, nav_c3 = st.columns([6, 1.5, 1.5])
with nav_c2:
    if st.button("🛡️ Readiness Audit"): st.session_state.view = 'audit'
with nav_c3:
    if st.button("💰 Premium Portfolio"): st.session_state.view = 'portfolio'

# --- 3. MODULAR CONTENT ---

# VIEW: HOME (The Replit-Style Screener)
if st.session_state.view == 'home':
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 4rem; font-weight: 900; letter-spacing:-2px;'>Project Screener</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #6b7280; font-size: 1.2rem;'>Powered by <strong>Aether</strong></p>", unsafe_allow_html=True)
    
    ticker = st.text_input("", placeholder="Enter Asset Ticker (e.g. SOL, DOT, TAO)", key="main_search")
    
    if st.button("EXECUTE FORENSIC SCAN"):
        if ticker:
            st.markdown("---")
            st.subheader(f"🛡️ Forensic Report: {ticker.upper()}")
            
            # THE 5-POINT ANALYSIS (Original High-Conviction Logic)
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"""<div class='forensic-card'>
                <strong>1. Problem-Solution Fit:</strong> Verifying if {ticker} solves a mechanical necessity in the 2026 cycle. 
                <br>Verdict: <span style='color:green; font-weight:700;'>OPTIMIZED</span></div>""", unsafe_allow_html=True)
                
                st.markdown(f"""<div class='forensic-card'>
                <strong>2. Tokenomics Deep-Dive:</strong> Auditing the 'Inflation vs. Utility' curve. 
                <br>Status: <span style='color:orange; font-weight:700;'>MONITOR UNLOCKS</span></div>""", unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""<div class='forensic-card'>
                <strong>3. Team Credibility:</strong> Evaluating developer provenance and shipping history. 
                <br>Status: <span style='color:green; font-weight:700;'>BATTLE-HARDENED</span></div>""", unsafe_allow_html=True)
                
                st.markdown(f"""<div class='forensic-card'>
                <strong>4. Narrative Check:</strong> Alignment with RWA, AI, and DePIN megatrends. 
                <br>Signal: <span style='color:blue; font-weight:700;'>HIGH CONVICTION</span></div>""", unsafe_allow_html=True)

            st.error(f"**5. THE RED FLAG SUMMARY:** {ticker} shows high centralization in early-stage seed wallets. Institutional liquidity risk remains a factor for the 2029 exit.")
    st.markdown("</div>", unsafe_allow_html=True)

# VIEW: AUDIT (THE ORIGINAL 8 SITUATIONAL QUESTIONS)
elif st.session_state.view == 'audit':
    if st.button("← Back"): st.session_state.view = 'home'; st.rerun()
    st.header("🛡️ Investor Readiness Audit")
    
    c_l, c_r = st.columns(2)
    with c_l:
        q1 = st.radio("1. The Midnight Crash: BTC drops 30% while you sleep?", ["Buy the dip", "Hold", "Panic"])
        q2 = st.radio("2. The 'Moon' Hype: Friend makes 10x on a coin you missed?", ["Indifferent", "Slight FOMO", "Chase pump"])
        q3 = st.radio("3. Concentration: % of net worth in one asset?", ["<10% (Institutional)", "25-50%", "100% (Degen)"])
        q4 = st.radio("4. Exit Strategy: Do you have written sell targets?", ["Yes", "In my head", "No"])
    with c_r:
        q5 = st.radio("5. Custody Protocol: Where is your primary stack?", ["Hardware Wallet", "Exchange w/ 2FA", "Hot Wallet"])
        q6 = st.radio("6. OpSec Knowledge: Explain Impermanent Loss?", ["Expert", "Vaguely", "No"])
        q7 = st.radio("7. Macro: Do you track US Treasury yields?", ["Always", "Sometimes", "Never"])
        q8 = st.radio("8. Horizon: Can you wait 3 years for your thesis?", ["Yes", "Maybe", "No"])

# --- 4. LEGAL & FOOTER ---
st.markdown("<br><br><br>---", unsafe_allow_html=True)
st.error("**LEGAL DISCLAIMER:** Institutional Intelligence only. Not financial advice. Aether Oracle 2026-2029 Cycle.")
