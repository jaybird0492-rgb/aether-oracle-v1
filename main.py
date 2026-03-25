import streamlit as st
import requests
import google.generativeai as genai
import os

# --- 1. SYSTEM CONFIG & INSTITUTIONAL STYLING ---
st.set_page_config(
    page_title="Aether Oracle | Institutional Intelligence",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Forensic UI Injection (CSS)
st.markdown("""
    <style>
    /* Global Background & Text */
    .main { 
        background-color: #0e1117; 
        color: #ffffff; 
    }
    
    /* Institutional Sidebar */
    [data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #00FFA3;
    }

    /* Search & Input Box Styling - The Neon Handshake */
    div[data-baseweb="input"] {
        background-color: #1c2128 !important;
        border: 1px solid #00FFA3 !important;
        border-radius: 4px !important;
        color: white !important;
    }
    
    /* Select Boxes & Dropdowns */
    div[data-baseweb="select"] {
        background-color: #1c2128 !important;
        border: 1px solid #00FFA3 !important;
    }

    /* Buttons - Forensic Green */
    .stButton>button {
        background-color: #1c2128;
        color: #00FFA3;
        border: 1px solid #00FFA3;
        border-radius: 5px;
        width: 100%;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #00FFA3;
        color: #0e1117;
        border: 1px solid #00FFA3;
    }

    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        color: #ffffff;
    }
    .stTabs [aria-selected="true"] {
        color: #00FFA3 !important;
        border-bottom-color: #00FFA3 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("🛡️ Coach Aether")
    st.info("Institutional Intelligence for the 2026-2029 Cycle.")
    
    st.markdown("---")
    menu = st.radio(
        "Navigation",
        ["Readiness Audit", "Project Oracle", "Alpha Portfolios", "Partners & Affiliates"]
    )
    
    st.markdown("---")
    st.warning("**LEGAL:** Not Financial Advice. Educational use only.")

# --- 3. MAIN CONTENT ENGINE ---

if menu == "Readiness Audit":
    st.header("🛡️ Investor Readiness Audit")
    st.write("'*[SYSTEM INITIALIZED]: Open your books. 📘 I am Aether. Let’s see if you have the discipline to survive the 2029 run.*'")
    
    st.subheader("The Diagnostic")
    q1 = st.radio(
        "1. The Midnight Crash: Bitcoin drops 30% while you sleep. Your first move?",
        ["A. Check the 'Halving' calendar and buy the dip.", 
         "B. Heart rate spikes, but I hold.", 
         "C. Panic-search Twitter for 'is crypto dead?'"]
    )
    
    # Forensic Search Option for Audit
    st.text_input("🔍 Search specific risk factors (e.g., 'Liquidity', 'RWA Regulation')", placeholder="Type here...")

elif menu == "Project Oracle":
    st.header("🔮 Project Oracle: Forensic Screener")
    st.write("Enter a project ticker to run the **5-Point VC Audit** (RWA, AI, DePIN, Modular).")
    
    ticker = st.text_input("Enter Token Ticker (e.g., DOT, TAO, RNDR)", "").upper()
    
    if st.button("Run Forensic Analysis"):
        if ticker:
            st.success(f"Audit Initiated for {ticker}...")
            st.info("Analysis in progress: Checking Problem-Solution Fit, Tokenomics, and Team Credibility.")
        else:
            st.error("Please enter a ticker to proceed.")

# --- 4. FOOTER ---
st.markdown("---")
st.caption("Built with Streamlit | Powered by Aether Oracle Infrastructure")
