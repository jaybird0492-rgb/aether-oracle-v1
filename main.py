import streamlit as st
import requests
import google.generativeai as genai
import os

# --- 1. SETTINGS & STYLING ---
st.set_page_config(page_title="Project Screener | Aether Oracle", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stTabs [data-baseweb="tab-list"] { gap: 20px; }
    .stTabs [data-baseweb="tab"] { 
        height: 50px; white-space: pre; background-color: #1a1c24; 
        border-radius: 5px; color: white; padding: 10px 20px;
    }
    .stTabs [aria-selected="true"] { background-color: #00c6ff; }
    .report-box { background-color: #1a1c24; padding: 25px; border-radius: 12px; border: 1px solid #30363d; margin-top: 20px; }
    .disclaimer { font-size: 0.75rem; color: #8899ac; border-top: 1px solid #30363d; margin-top: 50px; padding-top: 20px; }
    .metric-card { background: #1a1c24; padding: 15px; border-radius: 10px; border-left: 5px solid #00c6ff; }
    </style>
    """, unsafe_allow_html=True)

# Security & AI Config
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    st.error("🚨 SECRET MISSING: Add 'GEMINI_API_KEY' to Replit Secrets.")
    st.stop()

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

# --- 2. SESSION STATE ---
if 'quiz_finished' not in st.session_state:
    st.session_state.quiz_finished = False

# --- 3. TOP NAVIGATION TABS ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🛡️ Readiness Audit", "🔮 Project Oracle", "💰 Alpha Portfolios", "🤝 Partners & Affiliates", "ℹ️ About & FAQ"
])

# --- 4. SIDEBAR (Persistent Info) ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/ProjectScreener/Assets/main/Aether_Portrait.png", width=200, caption="Coach Aether")
    st.markdown("### **Aether Oracle V8**")
    st.info("Institutional Intelligence for the 2026-2029 Cycle.")
    st.warning("**LEGAL:** Not Financial Advice. Educational use only.")

# --- TAB 1: READINESS AUDIT (The Elite 8) ---
with tab1:
    st.title("🛡️ Investor Readiness Audit")
    st.markdown("### *'[SYSTEM INITIALIZED]: Open your books. 📘 I am Aether. Let’s see if you have the discipline to survive the 2029 run.'*")
    
    with st.form("elite_8_quiz"):
        st.subheader("The Diagnostic")
        q1 = st.radio("1. The Midnight Crash: Bitcoin drops 30% while you sleep. Your first move?", 
                     ["A. Check the 'Halving' calendar and buy the dip.", "B. Heart rate spikes, but I hold.", "C. Panic-search Twitter for 'is crypto dead?'", "D. Market sell everything in a cold sweat."])
        q2 = st.radio("2. The 'Lambo' Reality: When do you expect to 'make it'?", 
                     ["A. 2029 - I play the 4-year cycle.", "B. 2 years of steady growth.", "C. By Christmas this year.", "D. I need a 100x by next week."])
        q3 = st.radio("3. Security Hygiene: Where are your private keys?", 
                     ["A. Air-gapped Hardware Wallet (Tangem/Ledger).", "B. Encrypted and stored offline.", "C. On an Exchange (Coinbase/Binance).", "D. In a photo on my phone / 'Trust me' bro."])
        q4 = st.radio("4. The Life Support: If your portfolio went to zero tomorrow...", 
                     ["A. My lifestyle wouldn't change. Rent is paid.", "B. I'd be upset, but I'm financially safe.", "C. I'd have to move back with my parents.", "D. I'm using rent/loan money to play."])
        q5 = st.radio("5. Narrative IQ: Do you know what 'DePIN' or 'RWA' means?", 
                     ["A. Yes, I track the 2026 megatrends.", "B. I've heard of them, need to learn more.", "C. I only buy what Elon Musk tweets.", "D. I just buy the coins with the funniest dogs."])
        q6 = st.radio("6. The Exit Strategy: A coin you hold does a 5x. You...", 
                     ["A. Sell initial capital, let the 'house money' ride.", "B. Hold for a 10x or nothing.", "C. Forget I even owned it.", "D. Buy MORE because I'm feeling FOMO."])
        q7 = st.radio("7. Technical Self-Reliance: Can you move funds without help?", 
                     ["A. I use DEXs and bridges with ease.", "B. I'm comfortable on exchanges.", "C. I struggle with 'Gas fees' and 'Networks'.", "D. My friend does all the clicking for me."])
        q8 = st.radio("8. Research Commitment: How much time do you spend auditing?", 
                     ["A. 5+ hours weekly on whitepapers/tokenomics.", "B. I read the 'Aether' reports fully.", "C. I watch 10-minute YouTube recaps.", "D. I buy based on the 'Vibe'."])
        
        submit_quiz = st.form_submit_button("🏁 RUN DIAGNOSTIC")

        if submit_quiz:
            with st.spinner("Aether is calculating your survival probability..."):
                prompt = f"Analyze these 8 crypto investor answers: {q1}, {q2}, {q3}, {q4}, {q5}, {q6}, {q7}, {q8}. Persona: Coach Aether (Skeptical Teacher). Give 3 bullet points of feedback and a verdict: STATUS: OPTIMIZED or STATUS: RECALIBRATE. Be blunt but encouraging."
                res = model.generate_content(prompt)
                st.session_state.user_profile = res.text
                st.session_state.quiz_finished = True

    if st.session_state.quiz_finished:
        st.markdown(f"<div class='report-box'>{st.session_state.user_profile}</div>", unsafe_allow_html=True)

# --- TAB 2: PROJECT ORACLE ---
with tab2:
    st.title("🔮 Project Narrative Oracle")
    coin_id = st.text_input("Enter Asset ID (e.g. bittensor, cardano, xrp):").lower().strip()
    
    if st.button("🚀 EXECUTE FORENSIC AUDIT"):
        if coin_id:
            with st.spinner("Extracting blockchain data..."):
                url = f"https://api.coingecko.com/api/v3/coins/{coin_id}?localization=false&market_data=true"
                res = requests.get(url)
                if res.status_code == 200:
                    d = res.json()
                    m = d['market_data']
                    
                    # Attention-Grabbing Header
                    st.header(f"{d['name']} ({d['symbol'].upper()}) Audit")
                    
                    # Top Metrics
                    c1, c2, c3, c4 = st.columns(4)
                    c1.metric("Current Price", f"${m['current_price']['usd']:,.2f}")
                    c2.metric("Market Cap", f"${m['market_cap']['usd']:,.0f}")
                    c3.metric("ATH Distance", f"{m['ath_change_percentage']['usd']:.1f}%")
                    c4.metric("Circulating Supply", f"{int(m['circulating_supply']):,}")

                    # The Aether Prompt (Following your strict forensic structure)
                    prompt = f"""
                    Act as Aether, Senior Crypto VC Analyst. Audit {d['name']}.
                    Structure:
                    1. THE VERDICT (1-sentence punchy intro to grab attention).
                    2. HISTORY & SURVIVAL (If old, highlight bull run survival. If new, predict 2029 staying power).
                    3. TOKENOMICS FORENSICS: 
                       - Total Supply: {m['total_supply']}
                       - Circulating: {m['circulating_supply']}
                       - Analyze VC/Team concentration and unlock integrity. Use numbers.
                    4. CONSERVATIVE PRICE ANALYSIS: Based on historical halving performance and 2026 narratives (AI/DePIN/RWA). Be realistic, not hype-driven.
                    5. THE "RED FLAG" SUMMARY: Top 3 risks.
                    """
                    audit = model.generate_content(prompt)
                    st.markdown(f"<div class='report-box'>{audit.text}</div>", unsafe_allow_html=True)

# --- TAB 3: PORTFOLIOS ---
with tab3:
    st.title("💰 Alpha Wealth Strategies")
    st.warning("All portfolios are theoretical models for educational purposes.")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.subheader("🛡️ The 'Safe-Haven' Basket")
        st.write("Target: 10-12% APR | Risk: Low")
        st.info("50% BTC | 30% ETH | 10% SOL | 10% LINK")
        
    with col_b:
        st.subheader("🚀 The 'Aether Growth' Basket")
        st.write("Target: 25-40% Speculative | Risk: High")
        st.info("40% BTC | 20% ETH | 15% TAO (AI) | 15% RNDR (DePIN) | 10% RWA (Ondo)")

# --- TAB 4: PARTNERS & AFFILIATES ---
with tab4:
    st.title("🤝 Trusted Gateways")
    st.write("Professional tools for the 2026 cycle. Use our links to support the platform.")
    
    aff1, aff2, aff3 = st.columns(3)
    aff1.image("https://img.icons8.com/color/96/bitcoin.png", width=50)
    aff1.markdown("**Swyftx (AU Focus)**\n[Register Here >](#)")
    
    aff2.image("https://img.icons8.com/color/96/wallet.png", width=50)
    aff2.markdown("**Tangem Hardware Wallet**\n[Secure Your Keys >](#)")
    
    aff3.image("https://img.icons8.com/color/96/binance.png", width=50)
    aff3.markdown("**Binance Global**\n[Trade with Alpha >](#)")

# --- TAB 5: ABOUT & FAQ ---
with tab5:
    st.title("ℹ️ About Project Screener")
    st.write("We are an institutional-grade intelligence platform designed to filter out the noise of the crypto market.")
    
    with st.expander("💬 Chat with Aether (FAQ)"):
        user_q = st.text_input("Ask Aether anything about the platform:")
        if user_q:
            answer = model.generate_content(f"Answer this FAQ as Aether: {user_q}")
            st.write(answer.text)

# --- FOOTER DISCLOSURE ---
st.markdown(f"""
    <div class='disclaimer'>
        <b>MANDATORY FINANCIAL DISCLOSURE:</b> Project Screener, including its AI persona 'Aether,' is an educational 
        simulated environment. We are not licensed financial advisors. Cryptocurrency is an extremely volatile asset 
        class where 100% loss of capital is possible. All price targets are speculative. <b>This is NOT financial advice.</b>
    </div>
    """, unsafe_allow_html=True)
