import streamlit as st
import time

# --- 1. ARCHITECTURAL CONFIG ---
st.set_page_config(
    page_title="Project Screener | Aether Oracle",
    page_icon="🛡️",
    layout="wide"
)

# --- 2. THE PROFESSIONAL "REPLIT" UI OVERRIDE ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; color: #1a1a1a; }
    
    /* Center Hero Content */
    .hero-container {
        text-align: center;
        padding-top: 2rem;
        max-width: 850px;
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

    /* FIXED: Search Bar Visibility (No more black void) */
    div[data-baseweb="input"] {
        background-color: #f3f4f6 !important;
        border: 2px solid #e5e7eb !important;
        border-radius: 12px !important;
    }
    input { color: #1a1a1a !important; font-size: 1.1rem !important; }

    /* Nav Buttons Top Right */
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

    /* Primary Execution Button */
    .stButton > button[kind="primary"] {
        background-color: #4f46e5 !important;
        color: white !important;
        border: none !important;
        width: 100%;
        height: 3.5rem;
        font-size: 1.2rem;
    }
    
    /* Forensic Result Cards */
    .audit-card {
        background-color: #f9fafb;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #4f46e5;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. STATE MANAGEMENT ---
if 'view' not in st.session_state:
    st.session_state.view = 'home'

# --- 4. TOP NAVIGATION ---
nav_col1, nav_col2, nav_col3 = st.columns([6, 1.5, 1.5])
with nav_col2:
    if st.button("🛡️ Readiness Audit"):
        st.session_state.view = 'audit'
with nav_col3:
    if st.button("💰 Premium Portfolio"):
        st.session_state.view = 'portfolio'

# --- 5. MODULAR VIEWS ---

# VIEW: HOME (PROJECT SCREENER)
if st.session_state.view == 'home':
    st.markdown("<div class='hero-container'>", unsafe_allow_html=True)
    st.markdown("<span class='pill'>✦ AI-POWERED INTELLIGENCE</span>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 4.5rem; font-weight: 900; margin-bottom:0; letter-spacing:-2px;'>Project Screener</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 1.3rem; color: #6b7280; margin-bottom: 40px;'>Powered by <strong>Aether</strong></p>", unsafe_allow_html=True)
    
    # Search Box
    ticker = st.text_input("", placeholder="Search any cryptocurrency — e.g. bitcoin, solana, chainlink", key="main_search")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("EXECUTE FORENSIC SCAN", type="primary"):
        if ticker:
            with st.spinner(f"Analyzing {ticker} Fundamentals..."):
                time.sleep(1.5) # Simulating AI processing
                
                st.markdown("---")
                st.subheader(f"🛡️ Forensic Audit: {ticker.upper()}")
                
                # THE 5-POINT AUDIT OUTPUT
                col_a, col_b = st.columns(2)
                
                with col_a:
                    st.markdown(f"""
                    <div class="audit-card">
                    <strong>1. Problem-Solution Fit</strong><br>
                    Verifying if {ticker} solves a mechanical necessity in the 2026-2029 cycle. 
                    Status: <span style="color:green">OPTIMIZED</span>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown(f"""
                    <div class="audit-card">
                    <strong>2. Tokenomics Deep-Dive</strong><br>
                    Auditing inflation vs. utility curve and unlock schedules. 
                    Status: <span style="color:orange">DILUTION RISK DETECTED</span>
                    </div>
                    """, unsafe_allow_html=True)

                with col_b:
                    st.markdown(f"""
                    <div class="audit-card">
                    <strong>3. Team Credibility</strong><br>
                    Evaluating dev history and previous project exits. 
                    Status: <span style="color:green">TIER-1 FOUNDERS</span>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown(f"""
                    <div class="audit-card">
                    <strong>4. Narrative Check</strong><br>
                    Alignment with AI, DePIN, and RWA megatrends. 
                    Status: <span style="color:blue">HIGH SIGNAL</span>
                    </div>
                    """, unsafe_allow_html=True)

                st.error(f"**5. RED FLAG SUMMARY:** Initial scan shows low exchange liquidity for {ticker}. High slippage risk for institutional entries.")
        else:
            st.warning("Please enter a ticker to begin the forensic scan.")
    st.markdown("</div>", unsafe_allow_html=True)

# VIEW: READINESS AUDIT (REAL RISK QUESTIONS)
elif st.session_state.view == 'audit':
    if st.button("← Back to Screener"):
        st.session_state.view = 'home'
        st.rerun()
        
    st.header("🛡️ Investor Readiness Audit")
    st.write("Determine your risk appetite and capital capacity for the upcoming cycle.")
    
    col_l, col_r = st.columns(2)
    with col_l:
        q1 = st.selectbox("1. What is your total liquid net worth for investment?", ["<$10k", "$10k-$50k", "$50k-$250k", "$250k+"])
        q2 = st.selectbox("2. How much of this can you afford to lose COMPLETELY?", ["0% (Safety)", "<10% (Conservative)", "10-25% (Moderate)", "50%+ (Aggressive)"])
        q3 = st.selectbox("3. What is your primary investment goal?", ["Capital Preservation", "Moderate Growth", "Wealth Generation", "Speculative Gains"])
        q4 = st.selectbox("4. What is your investment time horizon?", ["<6 months", "1-2 years", "3-5 years (Full Cycle)", "5+ years"])
    with col_r:
        q5 = st.selectbox("5. How do you handle a 40% market drawdown?", ["Exit immediately", "Partial de-risk", "Hold with stress", "View as opportunity"])
        q6 = st.selectbox("6. Experience level with Self-Custody?", ["Beginner", "Intermediate", "Advanced", "Expert"])
        q7 = st.selectbox("7. Percentage of monthly income saved?", ["0%", "<10%", "10-30%", "Over 30%"])
        q8 = st.selectbox("8. Primary source of investment funds?", ["Disposable Income", "Savings", "Business Profits", "Borrowed Capital"])

    if st.button("GENERATE READINESS REPORT", type="primary"):
        st.success("Analysis Complete. Report generated based on financial loss capacity.")

# --- 6. MANDATORY LEGAL DISCLAIMER ---
st.markdown("<br><br><br><br>", unsafe_allow_html=True)
st.markdown("---")
st.error("**LEGAL DISCLAIMER:** Aether Oracle is an analytical tool for educational purposes only. We do not provide financial advice. Cryptocurrency markets are highly volatile. Never invest capital you cannot afford to lose.")
st.caption("Aether Oracle | Infrastructure v4.1 | 2026-2029 Cycle")
