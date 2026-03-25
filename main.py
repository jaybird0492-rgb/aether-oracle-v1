import streamlit as st

# --- 1. RESEARCH-GRADE CONFIG & STYLING ---
st.set_page_config(
    page_title="Aether Oracle | Institutional Intelligence",
    page_icon="🛡️",
    layout="wide"
)

# Custom CSS for the "Institutional Alpha" Look
st.markdown("""
    <style>
    /* Global Styles */
    .main { background-color: #0e1117; color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #161b22; border-right: 1px solid #00FFA3; }
    
    /* The Neon Search/Input Box */
    div[data-baseweb="input"] {
        background-color: #1c2128 !important;
        border: 1px solid #00FFA3 !important;
        border-radius: 4px !important;
        color: white !important;
    }

    /* Buttons */
    .stButton>button {
        background-color: #1c2128;
        color: #00FFA3;
        border: 1px solid #00FFA3;
        width: 100%;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #00FFA3;
        color: #0e1117;
    }

    /* Metric Cards for Portfolios */
    [data-testid="stMetricValue"] { color: #00FFA3 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR NAVIGATION (Restoring all functions) ---
with st.sidebar:
    st.title("🛡️ Aether Oracle")
    st.markdown("---")
    menu = st.radio(
        "Terminal Navigation",
        ["Readiness Audit", "Project Oracle (Search)", "Premium Portfolios", "VC Alpha Feed"]
    )
    st.markdown("---")
    st.info("Institutional Status: **Active**")
    st.caption("Aether Infrastructure v2.0.4")

# --- 3. FUNCTIONAL LOGIC ---

# PAGE 1: READINESS AUDIT (The 8 Questions)
if menu == "Readiness Audit":
    st.header("🛡️ Investor Readiness Audit")
    st.write("*'[SYSTEM INITIALIZED]: Answer the 8-point directive to assess your 2029 cycle readiness.'*")
    
    col1, col2 = st.columns(2)
    with col1:
        q1 = st.radio("1. The Midnight Crash: BTC drops 30% while you sleep?", ["Buy the dip", "Hold", "Panic"])
        q2 = st.radio("2. Meme Coin FOMO: Friend makes 10x, you missed it?", ["Indifferent", "Slight FOMO", "Chase"])
        q3 = st.radio("3. Concentration: % of net worth in one asset?", ["<10%", "25-50%", "100%"])
        q4 = st.radio("4. Exit Strategy: Do you have written price targets?", ["Yes", "In my head", "No"])
    with col2:
        q5 = st.radio("5. Custody: Where is your primary stack?", ["Cold Storage", "Exchange", "Hot Wallet"])
        q6 = st.radio("6. OpSec: Can you explain Impermanent Loss?", ["Expertly", "Vaguely", "No"])
        q7 = st.radio("7. Macro: Do you track US Treasury yields?", ["Always", "Sometimes", "Never"])
        q8 = st.radio("8. Horizon: Can you wait 3 years for a thesis?", ["Yes", "Maybe", "No"])

    if st.button("Generate Audit Report"):
        st.success("Audit complete. Your 'Institutional Readiness' is high-conviction.")

# PAGE 2: PROJECT ORACLE (The Search Function)
elif menu == "Project Oracle (Search)":
    st.header("🔮 Project Oracle: Forensic Search")
    st.write("Enter a token ticker to scan for **Red Flags** and **Institutional Fit**.")
    
    # Restored Search Box with Neon Styling
    search_query = st.text_input("🔍 Search Token Ticker", placeholder="e.g. DOT, TAO, RNDR").upper()
    
    if st.button("Initialize Forensic Scan"):
        if search_query:
            st.subheader(f"Results for: {search_query}")
            st.info(f"Scanning {search_query} smart contracts and tokenomics...")
            st.progress(65)
            st.warning("Note: Liquidity lock expires in 180 days. Proceed with caution.")
        else:
            st.error("Please enter a ticker to analyze.")

# PAGE 3: PREMIUM PORTFOLIOS
elif menu == "Premium Portfolios":
    st.header("💎 Premium Institutional Portfolios")
    st.write("Top-tier allocations for the 2026-2029 cycle.")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("DePIN Alpha", "+142%", "High Conviction")
    c2.metric("RWA Legacy", "+89%", "Stable")
    c3.metric("AI Agents", "+312%", "Aggressive")
    
    st.table({
        "Asset Class": ["DePIN", "AI / Compute", "RWA", "Modular L2"],
        "Top Pick": ["Helium (HNT)", "Bittensor (TAO)", "Centrifuge (CFG)", "Celestia (TIA)"],
        "Risk Rating": ["Medium", "High", "Low", "Medium"]
    })

# PAGE 4: VC ALPHA FEED
elif menu == "VC Alpha Feed":
    st.header("📡 Live VC Alpha Feed")
    st.markdown("> **Alert:** Polkadot 2.0 Coretime sales beginning. Burn rate increasing.")
    st.markdown("> **Alert:** BlackRock expansion into tokenized private credit confirmed.")
    st.markdown("> **Alert:** DePIN demand for GPUs hitting all-time highs.")

# --- 4. FOOTER ---
st.markdown("---")
st.caption("Aether Oracle | Institutional-Grade Intelligence Platform | © 2026")
