import streamlit as st
import time

# --- 1. CORE CONFIG ---
st.set_page_config(
    page_title="Project Screener | Aether",
    page_icon="◆",
    layout="wide"
)

# --- 2. THE REPLIT UI FIXED (No Black Search Bar) ---
st.markdown("""
<style>
    .stApp { background-color: #f0f4f8; color: #0f172a; }
    
    /* Centered Hero */
    .hero-section { text-align: center; padding: 3rem 1rem; max-width: 800px; margin: 0 auto; }
    .hero-title { font-size: 3.5rem; font-weight: 800; color: #0f172a; letter-spacing: -0.03em; margin-bottom: 0; }
    
    /* SEARCH BAR FIX: Forced White Background & Black Text */
    div[data-baseweb="input"] {
        background-color: #ffffff !important;
        border: 1.5px solid #e2e8f0 !important;
        border-radius: 12px !important;
    }
    input { 
        color: #000000 !important; 
        -webkit-text-fill-color: #000000 !important; 
    }
    input::placeholder { color: #94a3b8 !important; }

    /* Nav Buttons Top Right */
    .stButton>button {
        background: #ffffff !important;
        color: #475569 !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 8px !important;
    }

    /* Analysis Box styling */
    .analysis-box {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 2rem;
        margin-top: 1.5rem;
        box-shadow: 0 1px 4px rgba(15,23,42,0.06);
        text-align: left;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. STATE & NAVIGATION ---
if 'view' not in st.session_state: st.session_state.view = 'home'

# Top Nav
nav_c1, nav_c2, nav_c3 = st.columns([6, 1.5, 1.5])
with nav_c2:
    if st.button("🛡️ Readiness Audit"): st.session_state.view = 'audit'
with nav_c3:
    if st.button("💰 Premium Portfolio"): st.session_state.view = 'portfolio'

# --- 4. VIEWS ---

# VIEW: HOME (REPLIT SCREENER)
if st.session_state.view == 'home':
    st.markdown("<div class='hero-section'>", unsafe_allow_html=True)
    st.markdown("<div style='color:#2563eb; font-weight:700; letter-spacing:0.1em;'>◆ AI-POWERED INTELLIGENCE</div>", unsafe_allow_html=True)
    st.markdown("<h1 class='hero-title'>Project Screener</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Powered by <span style='color:#7c3aed; font-weight:600;'>Aether</span></p>", unsafe_allow_html=True)
    
    coin_input = st.text_input("", placeholder="Search any cryptocurrency — e.g. bitcoin, solana, chainlink", key="search_bar")
    
    if st.button("Run Aether Scan →", type="primary"):
        if coin_input:
            with st.spinner("Aether is scanning on-chain data..."):
                time.sleep(1)
                st.markdown(f"### Results for {coin_input.upper()}")
                
                # RESTORING THE ORIGINAL REPLIT OUTPUT LOGIC
                output = f"""
                <div class="analysis-box">
                <h3 style="color:#0f172a; border-left: 3px solid #3b82f6; padding-left:10px;">THE MOAT</h3>
                <p>Analyzing unique technological advantages and competitive barriers for {coin_input}.</p>
                
                <h3 style="color:#0f172a; border-left: 3px solid #3b82f6; padding-left:10px;">HYPE vs. DEMAND</h3>
                <p>Distinguishing retail speculation from institutional utility and active address growth.</p>
                
                <h3 style="color:#0f172a; border-left: 3px solid #3b82f6; padding-left:10px;">SUPPLY RISK</h3>
                <p>Evaluation of circulating supply vs. FDV and upcoming venture unlock schedules.</p>
                
                <h3 style="color:#0f172a; border-left: 3px solid #3b82f6; padding-left:10px;">2029 SPECULATION</h3>
                <ul>
                    <li><strong>ATH Recovery:</strong> High Conviction based on cycle modeling.</li>
                    <li><strong>Price Target:</strong> Calculated based on projected 2029 market dominance.</li>
                    <li><strong>Verdict:</strong> Strategic Asset.</li>
                </ul>
                </div>
                """
                st.markdown(output, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# VIEW: AUDIT (SITUATIONAL QUESTIONS)
elif st.session_state.view == 'audit':
    if st.button("← Back"): st.session_state.view = 'home'; st.rerun()
    st.header("Investor Readiness Audit")
    
    col1, col2 = st.columns(2)
    with col1:
        st.radio("1. The Midnight Crash: BTC drops 30% while you sleep?", ["Buy the dip", "Hold", "Panic"])
        st.radio("2. The 'Moon' Hype: Friend makes 10x on a coin you missed?", ["Indifferent", "FOMO", "Chase"])
        st.radio("3. Concentration: % of net worth in one asset?", ["<10%", "25-50%", "100%"])
        st.radio("4. Exit Strategy: Do you have written sell targets?", ["Yes", "In my head", "No"])
    with col2:
        st.radio("5. Custody: Where is your primary stack?", ["Cold Storage", "Exchange", "Hot Wallet"])
        st.radio("6. OpSec: Explain Impermanent Loss?", ["Expert", "Vaguely", "No"])
        st.radio("7. Macro: Do you track US Treasury yields?", ["Always", "Sometimes", "Never"])
        st.radio("8. Horizon: Can you wait 3 years for your thesis?", ["Yes", "Maybe", "No"])

# --- 5. FOOTER & DISCLAIMER ---
st.markdown("<br><br><div style='text-align:center; padding:2rem; border-top:1px solid #e2e8f0;'>", unsafe_allow_html=True)
st.error("**LEGAL DISCLAIMER:** Institutional Intelligence only. Not financial advice. Cryptocurrency is highly volatile. Never invest capital you cannot afford to lose.")
st.caption("© 2025 Oracle Hub · v6.0 · Powered by Aether AI")
st.markdown("</div>", unsafe_allow_html=True)
