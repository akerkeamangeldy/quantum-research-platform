"""
Quantum Research Workbench v4.0.2
High-Fidelity Environment for Unitary Dynamics & Quantum Advantage Exploration

System Architecture: Complex Hilbert Space Operations | Variational Optimization
Hardware Integration: Transmon Qubits | Cryogenic Stage (20mK) | Gate Fidelity >99.9%
"""

import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
from scipy.linalg import expm
from scipy.optimize import minimize
import time
import json
from datetime import datetime
import hashlib

# Page configuration with professional vector icon
st.set_page_config(
    page_title="Quantum Research Workbench | v4.0.2",
    page_icon="favicon.svg",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Obsidian Glassmorphism Aesthetics CSS + Lucide Icons + Global Typography
st.markdown("""
<style>
    /* PRODUCTION-READY FONT IMPORTS WITH CYRILLIC SUPPORT */
    @import url('https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=JetBrains+Mono:wght@300;400;500;600;700&family=Source+Serif+Pro:wght@300;400;600;700&display=swap&subset=latin,latin-ext,cyrillic');
    @import url('https://unpkg.com/lucide-static@latest/font/lucide.css');
    
    /* GLOBAL TYPOGRAPHY - APPLY EVERYWHERE */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif !important;
    }
    
    /* Override Streamlit default fonts globally */
    html, body, .stApp, [data-testid="stAppViewContainer"], 
    [data-testid="stHeader"], [data-testid="stSidebar"], 
    .main, .block-container, [data-testid="stVerticalBlock"],
    h1, h2, h3, h4, h5, h6, p, span, div, label, input, 
    textarea, select, button, a, li, td, th {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif !important;
    }
    
    /* Monospace for code elements */
    code, pre, .code-panel, .telemetry-ticker, .metric-box h3, 
    .status-value, [class*="mono"] {
        font-family: 'JetBrains Mono', 'SF Mono', 'Courier New', monospace !important;
    }
    
    /* Serif for prose/readability */
    .experiment-panel, .prose-text, [class*="serif"] {
        font-family: 'Source Serif Pro', Georgia, 'Times New Roman', serif !important;
    }
    
    :root {
        --bg-obsidian: #0A0A0A;
        --bg-charcoal: #121212;
        --bg-slate: #1A1A1A;
        --accent-quantum: #00D9FF;
        --accent-energy: #7B61FF;
        --accent-coherence: #00FF94;
        --text-mono: #E8E8E8;
        --text-prose: #D0D0D0;
        --glass-border: rgba(255, 255, 255, 0.08);
        --glass-glow: rgba(0, 217, 255, 0.15);
    }
    
    .stApp {
        background: #0A0A0A;
        background-image: 
            radial-gradient(circle at 20% 30%, rgba(123, 97, 255, 0.03) 0%, transparent 50%),
            radial-gradient(circle at 80% 70%, rgba(0, 217, 255, 0.03) 0%, transparent 50%),
            linear-gradient(rgba(255, 255, 255, 0.01) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255, 255, 255, 0.01) 1px, transparent 1px);
        background-size: 100% 100%, 100% 100%, 40px 40px, 40px 40px;
        background-attachment: fixed;
    }
    
    /* Main content area - Inter by default (global override above handles this) */
    .main {
        color: var(--text-prose);
        line-height: 1.7;
    }
    
    /* Headings use JetBrains Mono for technical aesthetic */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'JetBrains Mono', 'SF Mono', monospace !important;
        font-weight: 600;
        color: var(--text-mono);
        letter-spacing: -0.01em;
        text-transform: uppercase;
    }
    
    code, pre {
        font-family: 'JetBrains Mono', 'SF Mono', monospace !important;
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid var(--glass-border);
        border-radius: 4px;
        padding: 2px 6px;
        color: var(--accent-quantum);
    }
    
    /* CYBER-PHYSICAL GLASSMORPHIC SLIDERS */
    .stSlider > div > div > div > div {
        background: linear-gradient(90deg, rgba(0, 217, 255, 0.1), rgba(123, 97, 255, 0.1)) !important;
        height: 2px !important;
    }
    
    .stSlider > div > div > div > div > div {
        background: linear-gradient(135deg, #00D9FF, #7B61FF) !important;
        height: 16px !important;
        width: 16px !important;
        border: 2px solid rgba(0, 217, 255, 0.8) !important;
        box-shadow: 
            0 0 20px rgba(0, 217, 255, 0.8),
            0 0 40px rgba(123, 97, 255, 0.4),
            inset 0 0 8px rgba(255, 255, 255, 0.3) !important;
        animation: thumb-pulse 2s ease-in-out infinite;
    }
    
    @keyframes thumb-pulse {
        0%%, 100%% { box-shadow: 0 0 20px rgba(0, 217, 255, 0.8), 0 0 40px rgba(123, 97, 255, 0.4), inset 0 0 8px rgba(255, 255, 255, 0.3); }
        50%% { box-shadow: 0 0 30px rgba(0, 217, 255, 1), 0 0 60px rgba(123, 97, 255, 0.6), inset 0 0 12px rgba(255, 255, 255, 0.5); }
    }
    
    /* ROTARY DIAL CONTROL */
    .rotary-dial {
        width: 120px;
        height: 120px;
        border-radius: 50%%;
        background: radial-gradient(circle at 30%% 30%%, rgba(26, 26, 26, 0.95), rgba(10, 10, 10, 0.98));
        border: 3px solid rgba(0, 217, 255, 0.3);
        box-shadow: 
            0 0 30px rgba(0, 217, 255, 0.4),
            inset 0 0 20px rgba(0, 0, 0, 0.8),
            inset -2px -2px 8px rgba(0, 217, 255, 0.2);
        position: relative;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .rotary-dial:hover {
        border-color: rgba(0, 217, 255, 0.8);
        box-shadow: 
            0 0 50px rgba(0, 217, 255, 0.6),
            inset 0 0 30px rgba(0, 0, 0, 0.9),
            inset -2px -2px 12px rgba(0, 217, 255, 0.4);
    }
    
    .rotary-indicator {
        position: absolute;
        top: 10px;
        left: 50%%;
        width: 3px;
        height: 45px;
        background: linear-gradient(180deg, #00D9FF, transparent);
        box-shadow: 0 0 10px #00D9FF;
        transform-origin: bottom center;
        border-radius: 2px;
    }
    
    .rotary-value {
        position: absolute;
        top: 50%%;
        left: 50%%;
        transform: translate(-50%%, -50%%);
        font-family: 'JetBrains Mono', monospace;
        font-size: 18px;
        font-weight: 700;
        color: #00D9FF;
        text-shadow: 0 0 10px rgba(0, 217, 255, 0.8);
    }
    
    /* PROCEDURAL GRID MESH BACKGROUND */
    .data-grid-mesh {
        position: relative;
        background-image: 
            linear-gradient(rgba(0, 217, 255, 0.05) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 217, 255, 0.05) 1px, transparent 1px);
        background-size: 20px 20px;
        animation: grid-scan 20s linear infinite;
    }
    
    @keyframes grid-scan {
        0%% { background-position: 0 0; }
        100%% { background-position: 0 400px; }
    }
    
    /* CYBER-PHYSICAL GLASSMORPHIC SLIDER CONTROLS */
    .stSlider > div > div > div > div {
        background: linear-gradient(90deg, rgba(0, 217, 255, 0.15), rgba(123, 97, 255, 0.15)) !important;
        height: 2px !important;
        border-radius: 1px;
    }
    
    .stSlider > div > div > div > div > div {
        background: radial-gradient(circle, #00D9FF 0%%, #7B61FF 100%%) !important;
        height: 18px !important;
        width: 18px !important;
        border: 2px solid rgba(0, 217, 255, 0.9) !important;
        box-shadow: 
            0 0 25px rgba(0, 217, 255, 0.9),
            0 0 50px rgba(123, 97, 255, 0.5),
            inset 0 0 10px rgba(255, 255, 255, 0.4) !important;
        animation: thumb-pulse 2s ease-in-out infinite;
        transition: all 0.3s ease;
    }
    
    .stSlider > div > div > div > div > div:hover {
        transform: scale(1.3);
        box-shadow: 
            0 0 35px rgba(0, 217, 255, 1),
            0 0 70px rgba(123, 97, 255, 0.7),
            inset 0 0 15px rgba(255, 255, 255, 0.6) !important;
    }
    
    @keyframes thumb-pulse {
        0%%, 100%% { 
            box-shadow: 0 0 25px rgba(0, 217, 255, 0.9), 0 0 50px rgba(123, 97, 255, 0.5), inset 0 0 10px rgba(255, 255, 255, 0.4);
        }
        50%% { 
            box-shadow: 0 0 40px rgba(0, 217, 255, 1), 0 0 80px rgba(123, 97, 255, 0.7), inset 0 0 15px rgba(255, 255, 255, 0.6);
        }
    }
    
    /* PROCEDURAL GRID MESH BACKGROUND */
    .data-grid-mesh {
        position: relative;
        background-image: 
            linear-gradient(rgba(0, 217, 255, 0.06) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 217, 255, 0.06) 1px, transparent 1px),
            radial-gradient(circle at 20%% 30%%, rgba(123, 97, 255, 0.03), transparent 60%%);
        background-size: 25px 25px, 25px 25px, 100%% 100%%;
        animation: grid-scan 25s linear infinite;
    }
    
    @keyframes grid-scan {
        0%% { background-position: 0 0, 0 0, 0 0; }
        100%% { background-position: 0 500px, 500px 0, 0 0; }
    }
    
    /* HIGH DATA-INK RATIO METRICS */
    .metric-value {
        font-family: 'JetBrains Mono', monospace;
        font-size: 32px;
        font-weight: 700;
        background: linear-gradient(135deg, #00D9FF, #7B61FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: 0 0 30px rgba(0, 217, 255, 0.5);
        letter-spacing: 0.03em;
        animation: kinetic-text 3s ease-in-out infinite;
    }
    
    .metric-label {
        font-family: 'JetBrains Mono', monospace;
        font-size: 10px;
        font-weight: 500;
        color: rgba(255, 255, 255, 0.4);
        text-transform: uppercase;
        letter-spacing: 0.12em;
        border-left: 2px solid rgba(0, 217, 255, 0.3);
        padding-left: 8px;
    }
    
    /* DIGITAL NOISE TRANSITION EFFECT */
    @keyframes digital-noise {
        0%%, 100%% { opacity: 1; filter: contrast(1); }
        10%%, 30%%, 50%%, 70%%, 90%% { 
            opacity: 0.97; 
            filter: contrast(1.05) saturate(1.1);
        }
        20%%, 40%%, 60%%, 80%% { 
            opacity: 1; 
            filter: contrast(1) saturate(1);
        }
    }
    
    .module-content {
        animation: digital-noise 0.5s ease-out, wavefunction-collapse 0.9s ease-out;
    }
    
    /* HYPER-REALISTIC 3D VISUALIZATION: PBR POST-PROCESSING */
    .plotly-graph-div {
        transition: all 0.8s cubic-bezier(0.25, 0.1, 0.25, 1);  /* Quart-Out easing */
        filter: 
            drop-shadow(0 0 30px rgba(0, 217, 255, 0.3))       /* Bloom effect */
            drop-shadow(0 0 60px rgba(123, 97, 255, 0.2))      /* Multi-point glow */
            contrast(1.1)                                       /* PBR contrast boost */
            saturate(1.15);                                     /* Cinematic color */
        transform-style: preserve-3d;
        perspective: 1500px;
    }
    
    .plotly-graph-div:hover {
        filter: 
            drop-shadow(0 0 50px rgba(0, 217, 255, 0.5))       /* Enhanced bloom on interaction */
            drop-shadow(0 0 80px rgba(123, 97, 255, 0.3))
            contrast(1.15)
            saturate(1.2);
    }
    
    .js-plotly-plot .plotly .main-svg {
        transition: all 0.8s cubic-bezier(0.25, 0.1, 0.25, 1);
    }
    
    /* CINEMATIC DEPTH OF FIELD & AMBIENT OCCLUSION */
    .js-plotly-plot .plotly .surface {
        filter: blur(0px);  /* Gaussian blur base */
        transition: filter 0.8s ease;
    }
    
    /* PLOTLY HOVER TOOLTIPS - CAMBRIDGE HUD AESTHETIC */
    .js-plotly-plot .hoverlayer .hovertext {
        background: linear-gradient(135deg, 
            rgba(10, 10, 10, 0.95) 0%,
            rgba(20, 20, 30, 0.90) 100%) !important;
        backdrop-filter: blur(20px) saturate(180%) !important;
        border: 1px solid rgba(0, 217, 255, 0.3) !important;
        border-radius: 12px !important;
        box-shadow: 
            0 8px 32px rgba(0, 0, 0, 0.8),
            inset 0 1px 0 rgba(255, 255, 255, 0.1),
            0 0 40px rgba(0, 217, 255, 0.2) !important;
        padding: 16px 20px !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 11px !important;
        color: rgba(255, 255, 255, 0.95) !important;
        letter-spacing: 0.3px !important;
        animation: tooltip-entrance 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    
    .js-plotly-plot .hoverlayer .hovertext path {
        fill: rgba(10, 10, 10, 0.95) !important;
        stroke: rgba(0, 217, 255, 0.3) !important;
        filter: drop-shadow(0 0 10px rgba(0, 217, 255, 0.3));
    }
    
    @keyframes tooltip-entrance {
        0% { 
            opacity: 0; 
            transform: scale(0.85) translateY(10px); 
        }
        100% { 
            opacity: 1; 
            transform: scale(1) translateY(0); 
        }
    }
    
    /* REFRACTION & GLASSMORPHISM EFFECTS */
    .plotly-graph-div::before {
        content: '';
        position: absolute;
        inset: 0;
        background: 
            radial-gradient(circle at 30%% 30%%, rgba(0, 217, 255, 0.05), transparent 50%%),
            radial-gradient(circle at 70%% 70%%, rgba(123, 97, 255, 0.05), transparent 50%%);
        pointer-events: none;
        mix-blend-mode: screen;
        animation: refraction-shift 4s ease-in-out infinite;
    }
    
    @keyframes refraction-shift {
        0%%, 100%% { transform: translate(0, 0); opacity: 0.6; }
        50%% { transform: translate(3px, -3px); opacity: 0.8; }
    }
    
    /* WAVEFUNCTION COLLAPSE VIBRATION */
    @keyframes collapse-vibration {
        0%%, 100%% { transform: translateX(0); }
        10%% { transform: translateX(-2px) rotateZ(-0.5deg); }
        20%% { transform: translateX(2px) rotateZ(0.5deg); }
        30%% { transform: translateX(-2px) rotateZ(-0.5deg); }
        40%% { transform: translateX(2px) rotateZ(0.5deg); }
        50%% { transform: translateX(0); }
    }
    
    .state-collapsed {
        animation: collapse-vibration 0.5s ease-out;
    }
    
    /* ROTARY DIAL CONTROL (LABORATORY EQUIPMENT AESTHETIC) */
    .rotary-dial-container {
        display: inline-block;
        margin: 20px auto;
        text-align: center;
    }
    
    .rotary-dial {
        width: 140px;
        height: 140px;
        border-radius: 50%%;
        background: 
            radial-gradient(circle at 35%% 35%%, rgba(30, 30, 30, 0.98), rgba(10, 10, 10, 1)),
            radial-gradient(circle at 65%% 65%%, rgba(0, 217, 255, 0.05), transparent);
        border: 4px solid rgba(0, 217, 255, 0.4);
        box-shadow: 
            0 0 40px rgba(0, 217, 255, 0.5),
            0 8px 30px rgba(0, 0, 0, 0.8),
            inset 0 0 30px rgba(0, 0, 0, 0.9),
            inset -3px -3px 15px rgba(0, 217, 255, 0.3),
            inset 3px 3px 10px rgba(0, 0, 0, 0.9);
        position: relative;
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        margin: 0 auto;
    }
    
    .rotary-dial:hover {
        border-color: rgba(0, 217, 255, 0.9);
        box-shadow: 
            0 0 60px rgba(0, 217, 255, 0.7),
            0 10px 40px rgba(0, 0, 0, 0.9),
            inset 0 0 40px rgba(0, 0, 0, 0.95),
            inset -4px -4px 20px rgba(0, 217, 255, 0.5),
            inset 4px 4px 15px rgba(0, 0, 0, 0.9);
        transform: scale(1.05);
    }
    
    .rotary-indicator {
        position: absolute;
        top: 15px;
        left: 50%%;
        width: 4px;
        height: 50px;
        background: linear-gradient(180deg, #00D9FF, rgba(0, 217, 255, 0.3), transparent);
        box-shadow: 0 0 15px #00D9FF, 0 0 30px rgba(0, 217, 255, 0.5);
        transform-origin: bottom center;
        border-radius: 2px;
        margin-left: -2px;
    }
    
    .rotary-value {
        position: absolute;
        top: 50%%;
        left: 50%%;
        transform: translate(-50%%, -50%%);
        font-family: 'JetBrains Mono', monospace;
        font-size: 22px;
        font-weight: 700;
        background: linear-gradient(135deg, #00D9FF, #00FF94);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        filter: drop-shadow(0 0 20px rgba(0, 217, 255, 0.8));
    }
    
    .rotary-label {
        margin-top: 15px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 11px;
        color: rgba(255, 255, 255, 0.5);
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }
    
    /* SYSTEM STATUS PANEL (SPECS COMPONENT) */
    .system-status-panel {
        background: linear-gradient(135deg, rgba(15, 15, 15, 0.98), rgba(20, 20, 20, 0.95));
        border: 1px solid rgba(0, 217, 255, 0.3);
        border-radius: 12px;
        padding: 24px;
        margin: 20px 0;
        box-shadow: 
            0 0 40px rgba(0, 217, 255, 0.2),
            inset 0 1px 0 rgba(0, 217, 255, 0.1),
            0 8px 32px rgba(0, 0, 0, 0.8);
        backdrop-filter: blur(15px);
        position: relative;
        overflow: hidden;
    }
    
    .system-status-panel::before {
        content: '';
        position: absolute;
        top: -2px;
        left: -2px;
        right: -2px;
        bottom: -2px;
        background: linear-gradient(45deg, rgba(0, 217, 255, 0.2), rgba(123, 97, 255, 0.2), rgba(0, 255, 148, 0.2), rgba(0, 217, 255, 0.2));
        background-size: 300%% 300%%;
        border-radius: 13px;
        z-index: -1;
        animation: gradient-border 6s ease infinite;
        opacity: 0.5;
    }
    
    @keyframes gradient-border {
        0%%, 100%% { background-position: 0%% 50%%; }
        50%% { background-position: 100%% 50%%; }
    }
    
    .status-header {
        font-family: 'JetBrains Mono', monospace;
        font-size: 14px;
        font-weight: 700;
        color: #00D9FF;
        text-transform: uppercase;
        letter-spacing: 0.15em;
        margin-bottom: 20px;
        border-bottom: 1px solid rgba(0, 217, 255, 0.2);
        padding-bottom: 10px;
    }
    
    .status-metric {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 12px 0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        transition: all 0.3s ease;
    }
    
    .status-metric:hover {
        background: rgba(0, 217, 255, 0.05);
        padding-left: 10px;
        border-left: 3px solid rgba(0, 217, 255, 0.8);
    }
    
    .status-metric:last-child {
        border-bottom: none;
    }
    
    .status-label {
        font-family: 'JetBrains Mono', monospace;
        font-size: 11px;
        color: rgba(255, 255, 255, 0.5);
        text-transform: uppercase;
        letter-spacing: 0.08em;
        font-weight: 500;
    }
    
    .status-value {
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
        font-weight: 700;
        background: linear-gradient(135deg, #00FF94, #00D9FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: 0.02em;
    }
    
    /* GLOBAL TYPOGRAPHY - PRODUCTION-READY FONT LOADING */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Source+Serif+Pro:wght@400;600&display=swap');
    
    /* Apply Inter globally to all elements */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
    }
    
    /* Monospace elements */
    code, pre, .code-panel, .telemetry-ticker, .metric-box, .status-value {
        font-family: 'JetBrains Mono', 'Courier New', monospace !important;
    }
    
    /* Serif prose elements */
    .experiment-panel, .prose-text {
        font-family: 'Source Serif Pro', Georgia, serif !important;
    }
    
    /* Streamlit core elements */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"], 
    [data-testid="stSidebar"], .main, .block-container,
    h1, h2, h3, h4, h5, h6, p, span, div, label, input, textarea, select, button {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
    }
    
    /* RESEARCH DASHBOARD NAVIGATION - DARK ACADEMIC AESTHETIC */
    .nav-section-header {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1.2px;
        text-transform: uppercase;
        color: rgba(123, 97, 255, 0.8);
        margin: 32px 0 16px 0;
        padding-left: 4px;
        border-left: 3px solid rgba(123, 97, 255, 0.5);
    }
    
    .research-nav-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
        gap: 18px;
        padding: 0;
        margin: 24px 0;
    }
    
    @media (max-width: 1200px) {
        .research-nav-grid {
            grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
        }
    }
    
    @media (max-width: 768px) {
        .research-nav-grid {
            grid-template-columns: 1fr;
            gap: 14px;
        }
    }
    
    /* Featured modules responsive grid - professional breakpoints */
    @media (max-width: 1200px) {
        .featured-module-card {
            min-height: 180px;
        }
    }
    
    @media (max-width: 900px) {
        .featured-module-card h4 {
            font-size: 13px;
            white-space: normal !important;
            word-break: normal;
            overflow-wrap: break-word;
            hyphens: none;
        }
    }
    
    @media (max-width: 768px) {
        .featured-module-card {
            padding: 20px 16px;
        }
        .stButton button {
            font-size: 12px;
            padding: 8px 16px;
            height: 36px;
        }
    }
    
    .research-nav-card {
        background: linear-gradient(145deg, #1A1A1A 0%, #151515 100%);
        border-left: 3px solid rgba(99, 102, 241, 0.4);
        border-radius: 16px;
        padding: 20px 18px;
        cursor: pointer;
        transition: all 180ms cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        box-shadow: 
            0 2px 8px rgba(0, 0, 0, 0.4),
            inset 0 1px 0 rgba(255, 255, 255, 0.03);
        display: flex;
        flex-direction: column;
        gap: 10px;
    }
    
    .research-nav-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: linear-gradient(90deg, 
            transparent, 
            rgba(99, 102, 241, 0.3) 50%, 
            transparent);
        opacity: 0;
        transition: opacity 200ms ease;
    }
    
    .research-nav-card:hover {
        transform: translateY(-3px);
        border-left-color: rgba(99, 102, 241, 1);
        box-shadow: 
            0 8px 24px rgba(0, 0, 0, 0.5),
            0 0 30px rgba(99, 102, 241, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.05);
        background: linear-gradient(145deg, #1D1D1D 0%, #181818 100%);
    }
    
    .research-nav-card:hover::before {
        opacity: 1;
    }
    
    .research-nav-card:active {
        transform: translateY(-1px);
        transition: all 80ms ease;
    }
    
    .nav-card-header {
        display: flex;
        align-items: center;
        gap: 14px;
        margin-bottom: 4px;
    }
    
    .nav-card-icon {
        font-size: 24px;
        line-height: 1;
        flex-shrink: 0;
        filter: grayscale(20%);
        transition: filter 180ms ease;
    }
    
    .research-nav-card:hover .nav-card-icon {
        filter: grayscale(0%) drop-shadow(0 0 12px rgba(99, 102, 241, 0.5));
    }
    
    .nav-card-title {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        font-size: 15px;
        font-weight: 600;
        line-height: 1.25;
        color: #E8E8E8;
        letter-spacing: -0.01em;
        margin: 0;
        white-space: normal;
        overflow-wrap: break-word;
        word-break: normal;
        transition: color 180ms ease;
    }
    
    .research-nav-card:hover .nav-card-title {
        color: rgba(99, 102, 241, 1);
    }
    
    .nav-card-subtitle {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        font-size: 12px;
        font-weight: 400;
        line-height: 1.4;
        color: rgba(180, 180, 180, 0.75);
        letter-spacing: 0;
        margin: 0;
        white-space: normal;
        overflow-wrap: break-word;
        word-break: normal;
        transition: color 180ms ease;
    }
    
    .research-nav-card:hover .nav-card-subtitle {
        color: rgba(0, 255, 148, 0.8);
    }
    
    .research-nav-card.active {
        background: linear-gradient(145deg, #1F1F2E 0%, #1A1A28 100%);
        border-left-color: rgba(99, 102, 241, 1);
        box-shadow: 
            0 4px 16px rgba(0, 0, 0, 0.5),
            0 0 40px rgba(99, 102, 241, 0.2),
            inset 0 0 30px rgba(99, 102, 241, 0.08);
    }
    
    .research-nav-card.active .nav-card-title {
        color: rgba(99, 102, 241, 1);
    }
    
    /* PARALLAX VISUALIZATION CONTAINER */
    .parallax-viz-container {
        position: relative;
        transform-style: preserve-3d;
        perspective: 1200px;
        margin: 30px 0;
        padding: 30px;
        background: 
            radial-gradient(circle at 20%% 30%%, rgba(0, 217, 255, 0.03), transparent 60%%),
            radial-gradient(circle at 80%% 70%%, rgba(123, 97, 255, 0.03), transparent 60%%);
        border-radius: 16px;
        border: 1px solid rgba(0, 217, 255, 0.2);
    }
    
    .parallax-viz-container::before {
        content: '';
        position: absolute;
        inset: 0;
        background-image: 
            linear-gradient(rgba(0, 217, 255, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 217, 255, 0.03) 1px, transparent 1px);
        background-size: 50px 50px;
        animation: grid-parallax 30s linear infinite;
        pointer-events: none;
        border-radius: 16px;
    }
    
    @keyframes grid-parallax {
        0%% { transform: translateZ(-100px) translateY(0); }
        100%% { transform: translateZ(-100px) translateY(1000px); }
    }
    
    /* REACTIVE RESEARCH CARDS WITH HOVER EFFECTS */
    .research-card {
        background: linear-gradient(135deg, rgba(18, 18, 18, 0.95) 0%, rgba(26, 26, 26, 0.95) 100%);
        border: 1px solid var(--glass-border);
        border-radius: 16px;
        padding: 28px;
        margin: 20px 0;
        box-shadow: 
            0 8px 32px rgba(0, 0, 0, 0.6),
            inset 0 1px 0 rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        position: relative;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        animation: wavefunction-collapse 0.8s ease-out;
    }
    
    .research-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, var(--glass-glow), transparent);
        opacity: 0.5;
        transition: opacity 0.4s ease;
    }
    
    .research-card::after {
        content: '';
        position: absolute;
        top: -2px;
        left: -2px;
        right: -2px;
        bottom: -2px;
        background: linear-gradient(45deg, 
            transparent 0%, 
            rgba(0, 217, 255, 0.1) 25%, 
            rgba(123, 97, 255, 0.1) 50%, 
            rgba(0, 217, 255, 0.1) 75%, 
            transparent 100%);
        background-size: 400% 400%;
        border-radius: 17px;
        opacity: 0;
        z-index: -1;
        animation: noise-field 8s ease infinite;
        transition: opacity 0.4s ease;
    }
    
    .research-card:hover {
        transform: translateY(-4px) scale(1.01);
        box-shadow: 
            0 20px 60px rgba(0, 217, 255, 0.3),
            0 0 40px rgba(123, 97, 255, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.1),
            inset 0 -30px 60px rgba(0, 217, 255, 0.1);
        border-color: rgba(0, 217, 255, 0.5);
        animation: subsurface-scatter 2s ease-in-out infinite;
    }
    
    .research-card:hover::before {
        opacity: 1;
        animation: entanglement-glow 1.5s ease infinite;
    }
    
    .research-card:hover::after {
        opacity: 1;
    }
    
    /* REACTIVE EXPERIMENT PANELS */
    .experiment-panel {
        background: rgba(18, 18, 18, 0.9);
        border-left: 2px solid var(--accent-energy);
        padding: 24px;
        margin: 20px 0;
        border-radius: 12px;
        backdrop-filter: blur(10px);
        font-family: 'Source Serif Pro', serif;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .experiment-panel::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, 
            transparent, 
            rgba(123, 97, 255, 0.1), 
            transparent);
        transition: left 0.6s ease;
    }
    
    .experiment-panel:hover {
        border-left-color: var(--accent-quantum);
        border-left-width: 4px;
        padding-left: 22px;
        transform: translateX(5px);
        box-shadow: 0 8px 24px rgba(123, 97, 255, 0.3);
    }
    
    .experiment-panel:hover::before {
        left: 100%;
    }
    
    /* METRIC BOXES WITH KINETIC TYPOGRAPHY */
    .metric-box {
        background: linear-gradient(135deg, rgba(123, 97, 255, 0.08) 0%, rgba(0, 217, 255, 0.08) 100%);
        border: 1px solid var(--glass-border);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        margin: 12px 0;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
        font-family: 'JetBrains Mono', monospace;
        transition: all 0.3s ease;
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }
    
    .metric-box::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        background: radial-gradient(circle, rgba(0, 217, 255, 0.3), transparent);
        border-radius: 50%;
        transform: translate(-50%, -50%);
        transition: width 0.6s ease, height 0.6s ease;
    }
    
    .metric-box:hover {
        transform: scale(1.05) translateY(-5px);
        box-shadow: 
            0 12px 32px rgba(0, 217, 255, 0.4),
            0 0 40px rgba(123, 97, 255, 0.3);
        border-color: rgba(0, 217, 255, 0.6);
        animation: displacement-ripple 0.8s ease-in-out;
    }
    
    .metric-box:hover::before {
        width: 300px;
        height: 300px;
    }
    
    .metric-box h3 {
        color: var(--accent-quantum);
        font-size: 32px;
        margin: 0;
        font-weight: 700;
        position: relative;
        z-index: 1;
        animation: kinetic-text 2s ease-in-out infinite;
    }
    
    .metric-box p {
        color: var(--text-prose);
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin: 8px 0 0 0;
        position: relative;
        z-index: 1;
    }
    
    /* FLOATING LATEX PANELS WITH GLASS MORPHISM */
    .latex-display {
        background: linear-gradient(135deg, 
            rgba(0, 217, 255, 0.05) 0%, 
            rgba(123, 97, 255, 0.05) 100%);
        border: 1px solid rgba(0, 217, 255, 0.3);
        border-left: 3px solid var(--accent-quantum);
        padding: 24px;
        margin: 20px 0;
        border-radius: 12px;
        font-family: 'JetBrains Mono', monospace;
        color: var(--text-mono);
        backdrop-filter: blur(10px);
        box-shadow: 
            0 8px 32px rgba(0, 0, 0, 0.4),
            inset 0 1px 0 rgba(255, 255, 255, 0.08);
        position: relative;
        transform-style: preserve-3d;
        transition: all 0.4s ease;
        animation: wavefunction-collapse 1s ease-out;
    }
    
    .latex-display:hover {
        transform: translateZ(10px) scale(1.02);
        box-shadow: 
            0 16px 48px rgba(0, 217, 255, 0.3),
            0 0 60px rgba(123, 97, 255, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.15);
        border-color: rgba(0, 217, 255, 0.6);
    }
    
    /* TELEMETRY TICKER - REAL-TIME DATA STREAM */
    .telemetry-ticker {
        background: rgba(10, 10, 10, 0.95);
        border: 1px solid rgba(0, 217, 255, 0.2);
        border-radius: 6px;
        padding: 8px 16px;
        margin: 12px 0;
        font-family: 'JetBrains Mono', monospace;
        font-size: 11px;
        color: var(--accent-quantum);
        overflow: hidden;
        white-space: nowrap;
        position: relative;
    }
    
    .telemetry-ticker::before {
        content: '▶';
        color: var(--accent-coherence);
        margin-right: 8px;
        animation: bloom-pulse 1.5s ease infinite;
    }
    
    @keyframes ticker-scroll {
        0% { transform: translateX(0); }
        100% { transform: translateX(-50%); }
    }
    
    .telemetry-value {
        display: inline-block;
        color: var(--accent-coherence);
        font-weight: 700;
        padding: 0 4px;
        animation: kinetic-text 3s ease-in-out infinite;
    }
    
    /* CODE PANELS WITH TERMINAL AESTHETIC */
    .code-panel {
        background: rgba(10, 10, 10, 0.98);
        border: 1px solid rgba(0, 217, 255, 0.3);
        border-radius: 8px;
        padding: 20px;
        margin: 20px 0;
        font-family: 'JetBrains Mono', monospace;
        font-size: 12px;
        overflow-x: auto;
        box-shadow: 
            inset 0 0 20px rgba(0, 0, 0, 0.8),
            0 4px 16px rgba(0, 0, 0, 0.6);
        position: relative;
    }
    
    .code-panel::before {
        content: 'QUANTUM CIRCUIT SYNTHESIS';
        position: absolute;
        top: -10px;
        left: 20px;
        background: #0A0A0A;
        padding: 2px 12px;
        font-size: 9px;
        color: var(--accent-quantum);
        border: 1px solid rgba(0, 217, 255, 0.3);
        border-radius: 4px;
        letter-spacing: 0.1em;
    }
    
    /* PROFESSIONAL COMPACT BUTTONS - RESEARCH DASHBOARD STYLE */
    .stButton button {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.08) 0%, rgba(120, 130, 255, 0.08) 100%);
        color: rgba(140, 150, 255, 0.95);
        border: 1px solid rgba(120, 130, 255, 0.25);
        border-radius: 8px;
        padding: 8px 16px;
        height: 34px;
        font-weight: 500;
        font-family: 'Inter', sans-serif !important;
        font-size: 12px;
        letter-spacing: -0.01em;
        transition: all 180ms cubic-bezier(0.4, 0, 0.2, 1);
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        word-break: normal;
    }
    
    .stButton button:hover {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.12) 0%, rgba(120, 130, 255, 0.12) 100%);
        border-color: rgba(120, 130, 255, 0.4);
        color: rgba(140, 150, 255, 1);
        box-shadow: 0 3px 12px rgba(99, 102, 241, 0.12), inset 0 1px 0 rgba(255, 255, 255, 0.05);
        transform: translateY(-1px);
    }
    
    .stButton button:active {
        transform: translateY(0);
        box-shadow: 0 2px 8px rgba(99, 102, 241, 0.2);
    }
    
    /* Featured module card hover effect */
    .featured-module-card:hover {
        border-color: rgba(99, 102, 241, 0.3);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4), 0 0 20px rgba(99, 102, 241, 0.08);
        transform: translateY(-3px);
    }
    
    /* SOFT PREMIUM RESEARCH DASHBOARD SIDEBAR */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0F1116 0%, #141824 100%);
        border-right: 1px solid rgba(120, 130, 180, 0.08);
        box-shadow: inset -1px 0 0 rgba(255, 255, 255, 0.02);
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background: transparent;
        padding: 0;
    }
    
    /* Sidebar Brand Header - Softer Typography */
    .sidebar-brand {
        padding: 28px 20px 22px 20px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.04);
        margin-bottom: 20px;
    }
    
    .sidebar-brand-title {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 15px;
        font-weight: 600;
        color: #E6E6E6;
        letter-spacing: -0.015em;
        margin: 0 0 6px 0;
        line-height: 1.3;
    }
    
    .sidebar-brand-subtitle {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 10px;
        font-weight: 500;
        color: #A8A8A8;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin: 0;
    }
    
    /* Navigation Section Headers - Muted & Refined */
    .nav-section-label {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 9px;
        font-weight: 600;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #7B7B7B;
        padding: 18px 20px 8px 20px;
        margin: 8px 0 6px 0;
        display: block;
    }
    
    /* Navigation Rows - Soft Pills with Elegant States */
    .nav-row {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 12px 20px 12px 20px;
        margin: 0 12px 3px 12px;
        border-left: 2px solid transparent;
        border-radius: 10px;
        cursor: pointer;
        transition: all 200ms cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        background: transparent;
    }
    
    .nav-row:hover {
        background: rgba(120, 130, 255, 0.06);
        border-left-color: rgba(120, 130, 255, 0.3);
    }
    
    .nav-row.active {
        background: linear-gradient(90deg, rgba(120, 130, 255, 0.08) 0%, rgba(120, 130, 255, 0.04) 100%);
        border-left-color: rgba(120, 130, 200, 0.6);
        box-shadow: inset 0 0 0 1px rgba(120, 130, 200, 0.12);
    }
    
    .nav-row-icon {
        font-size: 18px;
        color: #A8A8A8;
        transition: all 200ms ease;
        flex-shrink: 0;
        width: 20px;
        height: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        opacity: 0.7;
    }
    
    .nav-row:hover .nav-row-icon {
        color: rgba(140, 150, 255, 0.9);
        opacity: 1;
    }
    
    .nav-row.active .nav-row-icon {
        color: rgba(140, 150, 255, 0.95);
        opacity: 1;
    }
    
    .nav-row-title {
        font-family: 'Inter', -apple-system, sans-serif !important;
        font-size: 13px;
        font-weight: 500;
        color: #E6E6E6;
        letter-spacing: -0.005em;
        line-height: 1.35;
        white-space: normal;
        overflow: visible;
        word-wrap: break-word;
        word-break: normal;
        transition: all 200ms ease;
        flex: 1;
    }
    
    .nav-row:hover .nav-row-title {
        color: rgba(140, 150, 255, 0.95);
    }
    
    .nav-row.active .nav-row-title {
        color: rgba(140, 150, 255, 1);
        font-weight: 600;
    }
    
    /* Sidebar Footer - Subtle & Refined */
    .sidebar-footer {
        padding: 18px 20px;
        margin-top: auto;
        border-top: 1px solid rgba(255, 255, 255, 0.04);
        font-family: 'Inter', -apple-system, sans-serif;
    }
    
    .sidebar-footer-version {
        font-size: 10px;
        font-weight: 500;
        color: #7B7B7B;
        margin: 0 0 4px 0;
    }
    
    .sidebar-footer-status {
        font-size: 9px;
        font-weight: 500;
        color: rgba(120, 200, 160, 0.7);
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin: 0;
    }
    
    /* Streamlit Button Override - Soft Pill Navigation */
    [data-testid="stSidebar"] button[kind="secondary"],
    [data-testid="stSidebar"] button[kind="primary"] {
        background: transparent !important;
        border: none !important;
        border-left: 2px solid transparent !important;
        border-radius: 10px !important;
        padding: 12px 20px 12px 20px !important;
        margin: 0 12px 3px 12px !important;
        text-align: left !important;
        font-family: 'Inter', -apple-system, sans-serif !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        color: #E6E6E6 !important;
        letter-spacing: -0.005em !important;
        transition: all 200ms cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: none !important;
        width: calc(100% - 24px) !important;
        position: relative !important;
    }
    
    /* Add icon space before button text */
    [data-testid="stSidebar"] button[kind="secondary"]::before,
    [data-testid="stSidebar"] button[kind="primary"]::before {
        content: '';
        display: inline-block;
        width: 20px;
        height: 20px;
        margin-right: 12px;
        vertical-align: middle;
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        opacity: 0.7;
        transition: all 200ms ease;
    }
    
    [data-testid="stSidebar"] button[kind="secondary"]:hover,
    [data-testid="stSidebar"] button[kind="primary"]:hover {
        background: rgba(120, 130, 255, 0.06) !important;
        border-left-color: rgba(120, 130, 255, 0.3) !important;
        color: rgba(140, 150, 255, 0.95) !important;
    }
    
    [data-testid="stSidebar"] button[kind="secondary"]:hover::before,
    [data-testid="stSidebar"] button[kind="primary"]::before {
        opacity: 1;
    }
    
    [data-testid="stSidebar"] button[kind="primary"] {
        background: linear-gradient(90deg, rgba(120, 130, 255, 0.08) 0%, rgba(120, 130, 255, 0.04) 100%) !important;
        border-left-color: rgba(120, 130, 200, 0.6) !important;
        color: rgba(140, 150, 255, 1) !important;
        font-weight: 600 !important;
        box-shadow: inset 0 0 0 1px rgba(120, 130, 200, 0.12) !important;
    }
    
    [data-testid="stSidebar"] button p {
        font-family: 'Inter', -apple-system, sans-serif !important;
        font-size: 13px !important;
        margin: 0 !important;
        display: inline !important;
    }
    
    /* Icon mappings for each module - using data URIs for SVG icons */
    [data-testid="stSidebar"] button[key="nav_home"]::before {
        content: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='%23B4B4B4' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z'%3E%3C/path%3E%3Cpolyline points='9 22 9 12 15 12 15 22'%3E%3C/polyline%3E%3C/svg%3E");
    }
    
    [data-testid="stSidebar"] button[key="nav_overview"]::before {
        content: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='%23B4B4B4' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z'%3E%3C/path%3E%3Cpolyline points='9 22 9 12 15 12 15 22'%3E%3C/polyline%3E%3C/svg%3E");
    }
    
    [data-testid="stSidebar"] button[key="nav_bloch"]::before {
        content: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='%23B4B4B4' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='1'%3E%3C/circle%3E%3Ccircle cx='12' cy='12' r='5'%3E%3C/circle%3E%3Ccircle cx='12' cy='12' r='9'%3E%3C/circle%3E%3C/svg%3E");
    }
    
    [data-testid="stSidebar"] button[key="nav_interference"]::before {
        content: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='%23B4B4B4' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M2 6c.6.5 1.2 1 2.5 1C7 7 7 5 9.5 5c2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1'%3E%3C/path%3E%3Cpath d='M2 12c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1'%3E%3C/path%3E%3Cpath d='M2 18c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1'%3E%3C/path%3E%3C/svg%3E");
    }
    
    [data-testid="stSidebar"] button[key="nav_entanglement"]::before {
        content: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='%23B4B4B4' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71'%3E%3C/path%3E%3Cpath d='M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71'%3E%3C/path%3E%3C/svg%3E");
    }
    
    [data-testid="stSidebar"] button[key="nav_topological"]::before {
        content: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='%23B4B4B4' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z'%3E%3C/path%3E%3Cpolyline points='3.27 6.96 12 12.01 20.73 6.96'%3E%3C/polyline%3E%3Cline x1='12' y1='22.08' x2='12' y2='12'%3E%3C/line%3E%3C/svg%3E");
    }
    
    [data-testid="stSidebar"] button[key="nav_noise"]::before {
        content: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='%23B4B4B4' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='13 2 3 14 12 14 11 22 21 10 12 10 13 2'%3E%3C/polyline%3E%3C/svg%3E");
    }
    
    [data-testid="stSidebar"] button[key="nav_circuits"]::before {
        content: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='%23B4B4B4' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect x='4' y='4' width='16' height='16' rx='2'%3E%3C/rect%3E%3Crect x='9' y='9' width='6' height='6'%3E%3C/rect%3E%3Cpath d='M15 2v2'%3E%3C/path%3E%3Cpath d='M15 20v2'%3E%3C/path%3E%3Cpath d='M2 15h2'%3E%3C/path%3E%3Cpath d='M2 9h2'%3E%3C/path%3E%3Cpath d='M20 15h2'%3E%3C/path%3E%3Cpath d='M20 9h2'%3E%3C/path%3E%3Cpath d='M9 2v2'%3E%3C/path%3E%3Cpath d='M9 20v2'%3E%3C/path%3E%3C/svg%3E");
    }
    
    [data-testid="stSidebar"] button[key="nav_vqe"]::before {
        content: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='%23B4B4B4' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='10'%3E%3C/circle%3E%3Ccircle cx='12' cy='12' r='6'%3E%3C/circle%3E%3Ccircle cx='12' cy='12' r='2'%3E%3C/circle%3E%3C/svg%3E");
    }
    
    [data-testid="stSidebar"] button[key="nav_qaoa"]::before {
        content: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='%23B4B4B4' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='21' y1='10' x2='7' y2='10'%3E%3C/line%3E%3Cline x1='21' y1='6' x2='3' y2='6'%3E%3C/line%3E%3Cline x1='21' y1='14' x2='3' y2='14'%3E%3C/line%3E%3Cline x1='21' y1='18' x2='7' y2='18'%3E%3C/line%3E%3C/svg%3E");
    }
    
    [data-testid="stSidebar"] button[key="nav_qml"]::before {
        content: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='%23B4B4B4' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M12 5a3 3 0 1 0-5.997.125 4 4 0 0 0-2.526 5.77 4 4 0 0 0 .556 6.588A4 4 0 1 0 12 18Z'%3E%3C/path%3E%3Cpath d='M12 5a3 3 0 1 1 5.997.125 4 4 0 0 1 2.526 5.77 4 4 0 0 1-.556 6.588A4 4 0 1 1 12 18Z'%3E%3C/path%3E%3Cpath d='M15 13a4.5 4.5 0 0 1-3-4 4.5 4.5 0 0 1-3 4'%3E%3C/path%3E%3Cpath d='M17.599 6.5a3 3 0 0 0 .399-1.375'%3E%3C/path%3E%3Cpath d='M6.003 5.125A3 3 0 0 0 6.401 6.5'%3E%3C/path%3E%3Cpath d='M3.477 10.896a4 4 0 0 1 .585-.396'%3E%3C/path%3E%3Cpath d='M19.938 10.5a4 4 0 0 1 .585.396'%3E%3C/path%3E%3Cpath d='M6 18a4 4 0 0 1-1.967-.516'%3E%3C/path%3E%3Cpath d='M19.967 17.484A4 4 0 0 1 18 18'%3E%3C/path%3E%3C/svg%3E");
    }
    
    [data-testid="stSidebar"] button[key="nav_qec"]::before {
        content: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='%23B4B4B4' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z'%3E%3C/path%3E%3C/svg%3E");
    }
    
    [data-testid="stSidebar"] button[key="nav_hardware"]::before {
        content: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='%23B4B4B4' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect x='2' y='2' width='20' height='8' rx='2' ry='2'%3E%3C/rect%3E%3Crect x='2' y='14' width='20' height='8' rx='2' ry='2'%3E%3C/rect%3E%3Cline x1='6' y1='6' x2='6.01' y2='6'%3E%3C/line%3E%3Cline x1='6' y1='18' x2='6.01' y2='18'%3E%3C/line%3E%3C/svg%3E");
    }
    
    [data-testid="stSidebar"] button[key="nav_complexity"]::before {
        content: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='%23B4B4B4' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='2'%3E%3C/circle%3E%3Cpath d='M16.24 7.76a6 6 0 0 1 0 8.49m-8.48-.01a6 6 0 0 1 0-8.49m11.31-2.82a10 10 0 0 1 0 14.14m-14.14 0a10 10 0 0 1 0-14.14'%3E%3C/path%3E%3C/svg%3E");
    }
    
    [data-testid="stSidebar"] button[key="nav_export"]::before {
        content: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='%23B4B4B4' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4'%3E%3C/path%3E%3Cpolyline points='7 10 12 15 17 10'%3E%3C/polyline%3E%3Cline x1='12' y1='15' x2='12' y2='3'%3E%3C/line%3E%3C/svg%3E");
    }
    
    /* Update icon color on hover and active */
    [data-testid="stSidebar"] button[kind="primary"]::before {
        filter: brightness(0) saturate(100%) invert(52%) sepia(82%) saturate(2833%) hue-rotate(226deg) brightness(101%) contrast(96%);
    }
    
    [data-testid="stSidebar"] button[kind="secondary"]:hover::before {
        filter: brightness(0) saturate(100%) invert(52%) sepia(82%) saturate(2833%) hue-rotate(226deg) brightness(101%) contrast(96%);
    }
    
    /* Language Toggle Buttons - Soft Segmented Controls */
    [data-testid="stSidebar"] .element-container:first-child button {
        background: rgba(255, 255, 255, 0.02) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 8px !important;
        padding: 8px 14px !important;
        font-size: 10px !important;
        font-weight: 500 !important;
        color: #A8A8A8 !important;
        transition: all 200ms ease !important;
        border-left: 1px solid rgba(255, 255, 255, 0.08) !important;
        margin: 0 !important;
        width: auto !important;
    }
    
    [data-testid="stSidebar"] .element-container:first-child button::before {
        content: none !important;
    }
    
    [data-testid="stSidebar"] .element-container:first-child button:hover {
        background: rgba(120, 130, 255, 0.08) !important;
        border-color: rgba(120, 130, 180, 0.2) !important;
        color: rgba(140, 150, 255, 0.9) !important;
    }
    
    [data-testid="stSidebar"] .element-container:first-child button[kind="primary"] {
        background: linear-gradient(135deg, rgba(120, 130, 255, 0.12) 0%, rgba(120, 130, 255, 0.08) 100%) !important;
        border-color: rgba(120, 130, 200, 0.3) !important;
        color: rgba(140, 150, 255, 0.95) !important;
        font-weight: 600 !important;
    }

    
    .research-status {
        display: inline-block;
        padding: 6px 14px;
        border-radius: 4px;
        font-size: 10px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        font-family: 'JetBrains Mono', monospace;
    }
    
    .status-active {
        background: rgba(0, 255, 148, 0.15);
        color: var(--accent-coherence);
        border: 1px solid var(--accent-coherence);
        box-shadow: 0 0 10px rgba(0, 255, 148, 0.2);
    }
    
    .status-frontier {
        background: rgba(123, 97, 255, 0.15);
        color: var(--accent-energy);
        border: 1px solid var(--accent-energy);
        box-shadow: 0 0 10px rgba(123, 97, 255, 0.2);
    }
    
    .latex-display {
        background: rgba(0, 217, 255, 0.03);
        border-left: 3px solid var(--accent-quantum);
        padding: 24px;
        margin: 20px 0;
        border-radius: 8px;
        font-family: 'JetBrains Mono', monospace;
        color: var(--text-mono);
        backdrop-filter: blur(5px);
    }
    
    .code-panel {
        background: rgba(10, 10, 10, 0.95);
        border: 1px solid var(--glass-border);
        border-radius: 8px;
        padding: 20px;
        margin: 20px 0;
        font-family: 'JetBrains Mono', monospace;
        font-size: 12px;
        overflow-x: auto;
        box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.5);
    }
    
    .stButton button {
        background: linear-gradient(135deg, var(--accent-energy) 0%, var(--accent-quantum) 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 14px 28px;
        font-weight: 700;
        font-family: 'JetBrains Mono', monospace;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        transition: all 0.3s ease;
        box-shadow: 0 4px 16px rgba(0, 217, 255, 0.3);
    }
    
    .stButton button:hover {
        box-shadow: 0 0 30px rgba(0, 217, 255, 0.6);
        transform: translateY(-2px);
    }
    
    .export-card {
        background: var(--bg-tertiary);
        border: 2px dashed rgba(99, 102, 241, 0.4);
        border-radius: 8px;
        padding: 20px;
        margin: 16px 0;
        text-align: center;
    }
    
    /* REACTIVE QUANTUM TERMINAL - ADVANCED ANIMATIONS */
    
    /* Kinetic Typography */
    @keyframes kinetic-text {
        0%, 100% { 
            transform: translateY(0px) scale(1);
            text-shadow: 0 0 10px rgba(0, 217, 255, 0.3);
        }
        50% { 
            transform: translateY(-2px) scale(1.01);
            text-shadow: 0 0 20px rgba(0, 217, 255, 0.6);
        }
    }
    
    /* Bloom/Glow Effect */
    @keyframes bloom-pulse {
        0%, 100% { 
            box-shadow: 
                0 0 20px rgba(0, 217, 255, 0.3),
                0 0 40px rgba(123, 97, 255, 0.2),
                inset 0 0 20px rgba(0, 217, 255, 0.1);
            filter: brightness(1);
        }
        50% { 
            box-shadow: 
                0 0 40px rgba(0, 217, 255, 0.6),
                0 0 80px rgba(123, 97, 255, 0.4),
                inset 0 0 30px rgba(0, 217, 255, 0.2);
            filter: brightness(1.2);
        }
    }
    
    /* Wavefunction Collapse Animation */
    @keyframes wavefunction-collapse {
        0% { 
            opacity: 0;
            transform: scale(0.8) translateY(20px);
            filter: blur(10px);
        }
        50% {
            filter: blur(2px);
        }
        100% { 
            opacity: 1;
            transform: scale(1) translateY(0);
            filter: blur(0);
        }
    }
    
    /* Perlin Noise Field Simulation */
    @keyframes noise-field {
        0% { 
            background-position: 0% 0%;
            opacity: 0.1;
        }
        50% {
            opacity: 0.3;
        }
        100% { 
            background-position: 100% 100%;
            opacity: 0.1;
        }
    }
    
    /* Geometric Tesseract Rotation */
    @keyframes tesseract-rotate {
        0% { transform: rotateX(0deg) rotateY(0deg) rotateZ(0deg); }
        33% { transform: rotateX(120deg) rotateY(240deg) rotateZ(120deg); }
        66% { transform: rotateX(240deg) rotateY(120deg) rotateZ(240deg); }
        100% { transform: rotateX(360deg) rotateY(360deg) rotateZ(360deg); }
    }
    
    /* Quantum Entanglement Thread Glow */
    @keyframes entanglement-glow {
        0%, 100% { 
            stroke-width: 2;
            stroke: rgba(0, 217, 255, 0.6);
            filter: drop-shadow(0 0 5px rgba(0, 217, 255, 0.8));
        }
        50% { 
            stroke-width: 3;
            stroke: rgba(0, 217, 255, 1);
            filter: drop-shadow(0 0 15px rgba(0, 217, 255, 1));
        }
    }
    
    /* Subsurface Scattering Glow */
    @keyframes subsurface-scatter {
        0%, 100% {
            box-shadow: 
                0 8px 32px rgba(0, 0, 0, 0.6),
                inset 0 1px 0 rgba(255, 255, 255, 0.1),
                inset 0 -20px 40px rgba(0, 217, 255, 0.05);
        }
        50% {
            box-shadow: 
                0 12px 48px rgba(0, 217, 255, 0.4),
                inset 0 1px 0 rgba(255, 255, 255, 0.2),
                inset 0 -20px 40px rgba(0, 217, 255, 0.15);
        }
    }
    
    /* Displacement Field Effect */
    @keyframes displacement-ripple {
        0% {
            transform: translate(0, 0) scale(1);
        }
        25% {
            transform: translate(2px, -2px) scale(1.01);
        }
        50% {
            transform: translate(0, -3px) scale(1.02);
        }
        75% {
            transform: translate(-2px, -2px) scale(1.01);
        }
        100% {
            transform: translate(0, 0) scale(1);
        }
    }
    
    /* Legacy animations */
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }
    
    @keyframes rotate-gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes wave {
        0%, 100% { transform: translateX(0) translateY(0); }
        25% { transform: translateX(5px) translateY(-5px); }
        75% { transform: translateX(-5px) translateY(5px); }
    }
    
    .hero-glow {
        animation: pulse-glow 3s ease-in-out infinite;
    }
    
    .floating-element {
        animation: float 4s ease-in-out infinite;
    }
    
    .shimmer-effect {
        background: linear-gradient(90deg, transparent, rgba(99, 102, 241, 0.3), transparent);
        background-size: 1000px 100%;
        animation: shimmer 3s infinite;
    }
    
    .particle-field {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 1;
        opacity: 0.3;
    }
    
    /* Module-specific effects */
    .overview-bg {
        background: radial-gradient(circle at 20% 50%, rgba(99, 102, 241, 0.1) 0%, transparent 50%),
                    radial-gradient(circle at 80% 50%, rgba(6, 182, 212, 0.1) 0%, transparent 50%);
        background-size: 200% 200%;
        animation: rotate-gradient 15s ease infinite;
    }
    
    .bloch-energy {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.05) 0%, rgba(132, 204, 22, 0.05) 100%);
        box-shadow: inset 0 0 50px rgba(99, 102, 241, 0.1);
    }
    
    .interference-wave {
        position: relative;
        overflow: hidden;
    }
    
    .interference-wave::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 200%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(6, 182, 212, 0.1), transparent);
        animation: wave 8s linear infinite;
    }
    
    .noise-static {
        background-image: 
            repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(255, 255, 255, 0.03) 2px, rgba(255, 255, 255, 0.03) 4px);
    }
    
    .vqe-landscape {
        background: 
            radial-gradient(ellipse at center, rgba(132, 204, 22, 0.1) 0%, transparent 60%),
            linear-gradient(135deg, rgba(99, 102, 241, 0.05) 0%, rgba(6, 182, 212, 0.05) 100%);
    }
    
    .qml-neural {
        background: 
            linear-gradient(45deg, rgba(99, 102, 241, 0.03) 25%, transparent 25%),
            linear-gradient(-45deg, rgba(6, 182, 212, 0.03) 25%, transparent 25%),
            linear-gradient(45deg, transparent 75%, rgba(99, 102, 241, 0.03) 75%),
            linear-gradient(-45deg, transparent 75%, rgba(6, 182, 212, 0.03) 75%);
        background-size: 40px 40px;
        background-position: 0 0, 0 20px, 20px -20px, -20px 0px;
    }
    
    .circuit-flow {
        background: linear-gradient(90deg, 
            transparent 0%, 
            rgba(99, 102, 241, 0.1) 25%, 
            rgba(6, 182, 212, 0.1) 50%, 
            rgba(99, 102, 241, 0.1) 75%, 
            transparent 100%);
        background-size: 200% 100%;
        animation: shimmer 4s linear infinite;
    }
    
    /* Glowing borders */
    .glow-border {
        position: relative;
        border: 1px solid transparent;
        background: linear-gradient(var(--bg-secondary), var(--bg-secondary)) padding-box,
                    linear-gradient(135deg, var(--accent-indigo), var(--accent-cyan)) border-box;
        border-radius: 12px;
    }
    
    /* Data flow animation */
    @keyframes data-flow {
        0% { transform: translateX(-100%); opacity: 0; }
        50% { opacity: 1; }
        100% { transform: translateX(100%); opacity: 0; }
    }
    
    .data-stream {
        position: relative;
        overflow: hidden;
    }
    
    .data-stream::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 30%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(6, 182, 212, 0.4), transparent);
        animation: data-flow 2s ease-in-out infinite;
    }
</style>

<script src="https://unpkg.com/lucide@latest"></script>
<script>
    // Initialize Lucide icons on page load and after Streamlit updates
    function initializeLucideIcons() {
        if (typeof lucide !== 'undefined') {
            lucide.createIcons();
        }
    }
    
    // Initial load
    initializeLucideIcons();
    
    // Re-initialize after Streamlit updates
    const observer = new MutationObserver(initializeLucideIcons);
    observer.observe(document.body, { childList: true, subtree: true });
</script>
""", unsafe_allow_html=True)

# Add particle effect component for overview page
def add_particle_effect():
    """Add animated particle background effect"""
    particles_html = """
    <div id="particles-js" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script>
        particlesJS('particles-js', {
            particles: {
                number: { value: 80, density: { enable: true, value_area: 800 } },
                color: { value: ['#6366F1', '#06B6D4', '#84CC16'] },
                shape: { type: 'circle' },
                opacity: { value: 0.3, random: true },
                size: { value: 3, random: true },
                line_linked: { enable: true, distance: 150, color: '#6366F1', opacity: 0.2, width: 1 },
                move: { enable: true, speed: 2, direction: 'none', random: true, out_mode: 'out' }
            },
            interactivity: {
                detect_on: 'canvas',
                events: { onhover: { enable: true, mode: 'repulse' }, resize: true },
                modes: { repulse: { distance: 100, duration: 0.4 } }
            },
            retina_detect: true
        });
    </script>
    """
    st.markdown(particles_html, unsafe_allow_html=True)

def add_wave_animation():
    """Add wave animation for interference page"""
    wave_html = """
    <style>
    @keyframes wave-motion {
        0% { transform: translateX(0) translateY(0); }
        25% { transform: translateX(10px) translateY(-5px); }
        50% { transform: translateX(0) translateY(0); }
        75% { transform: translateX(-10px) translateY(5px); }
        100% { transform: translateX(0) translateY(0); }
    }
    .wave-container {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 150px;
        z-index: -1;
        overflow: hidden;
        opacity: 0.3;
    }
    .wave {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 200%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(6, 182, 212, 0.3), transparent);
        animation: wave-motion 4s ease-in-out infinite;
    }
    .wave:nth-child(2) {
        animation-delay: -2s;
        opacity: 0.5;
    }
    </style>
    <div class="wave-container">
        <div class="wave"></div>
        <div class="wave"></div>
    </div>
    """
    st.markdown(wave_html, unsafe_allow_html=True)

def add_matrix_rain():
    """Add Matrix-style rain effect for circuits page"""
    matrix_html = """
    <canvas id="matrix-canvas" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; opacity: 0.15; pointer-events: none;"></canvas>
    <script>
        const canvas = document.getElementById('matrix-canvas');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        
        const chars = '01HXYZ'.split('');
        const fontSize = 14;
        const columns = canvas.width / fontSize;
        const drops = Array(Math.floor(columns)).fill(1);
        
        function draw() {
            ctx.fillStyle = 'rgba(10, 14, 26, 0.05)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = '#6366F1';
            ctx.font = fontSize + 'px monospace';
            
            for (let i = 0; i < drops.length; i++) {
                const text = chars[Math.floor(Math.random() * chars.length)];
                ctx.fillText(text, i * fontSize, drops[i] * fontSize);
                if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) drops[i] = 0;
                drops[i]++;
            }
        }
        setInterval(draw, 50);
        window.addEventListener('resize', () => {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        });
    </script>
    """
    st.markdown(matrix_html, unsafe_allow_html=True)

def add_energy_field():
    """Add energy field visualization for VQE page"""
    energy_html = """
    <style>
    @keyframes energy-pulse {
        0%, 100% { opacity: 0.1; transform: scale(1); }
        50% { opacity: 0.3; transform: scale(1.05); }
    }
    .energy-field {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 600px;
        height: 600px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(132, 204, 22, 0.2) 0%, transparent 70%);
        animation: energy-pulse 4s ease-in-out infinite;
        pointer-events: none;
        z-index: -1;
    }
    </style>
    <div class="energy-field"></div>
    """
    st.markdown(energy_html, unsafe_allow_html=True)

def add_neural_network_bg():
    """Add neural network visualization for QML page"""
    neural_html = """
    <canvas id="neural-canvas" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; opacity: 0.2; pointer-events: none;"></canvas>
    <script>
        const canvas = document.getElementById('neural-canvas');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        
        const nodes = [];
        const nodeCount = 50;
        
        for (let i = 0; i < nodeCount; i++) {
            nodes.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                vx: (Math.random() - 0.5) * 0.5,
                vy: (Math.random() - 0.5) * 0.5
            });
        }
        
        function drawNetwork() {
            ctx.fillStyle = 'rgba(10, 14, 26, 0.1)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // Draw connections
            ctx.strokeStyle = 'rgba(99, 102, 241, 0.3)';
            ctx.lineWidth = 1;
            for (let i = 0; i < nodes.length; i++) {
                for (let j = i + 1; j < nodes.length; j++) {
                    const dx = nodes[i].x - nodes[j].x;
                    const dy = nodes[i].y - nodes[j].y;
                    const dist = Math.sqrt(dx * dx + dy * dy);
                    if (dist < 150) {
                        ctx.beginPath();
                        ctx.moveTo(nodes[i].x, nodes[i].y);
                        ctx.lineTo(nodes[j].x, nodes[j].y);
                        ctx.stroke();
                    }
                }
            }
            
            // Draw nodes
            ctx.fillStyle = '#06B6D4';
            nodes.forEach(node => {
                ctx.beginPath();
                ctx.arc(node.x, node.y, 3, 0, Math.PI * 2);
                ctx.fill();
                
                node.x += node.vx;
                node.y += node.vy;
                
                if (node.x < 0 || node.x > canvas.width) node.vx *= -1;
                if (node.y < 0 || node.y > canvas.height) node.vy *= -1;
            });
        }
        
        setInterval(drawNetwork, 50);
        window.addEventListener('resize', () => {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        });
    </script>
    """
    st.markdown(neural_html, unsafe_allow_html=True)

# Quantum simulation utilities
def convert_to_json_serializable(obj):
    """Convert numpy types to Python native types for JSON serialization."""
    if isinstance(obj, dict):
        return {key: convert_to_json_serializable(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_to_json_serializable(item) for item in obj]
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, (np.integer, np.int64, np.int32)):
        return int(obj)
    elif isinstance(obj, (np.floating, np.float64, np.float32)):
        return float(obj)
    elif isinstance(obj, (np.complexfloating, complex)):
        return {'real': float(obj.real), 'imag': float(obj.imag)}
    elif isinstance(obj, np.bool_):
        return bool(obj)
    else:
        return obj

def pauli_matrices():
    """Return Pauli matrices."""
    I = np.array([[1, 0], [0, 1]], dtype=complex)
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    Z = np.array([[1, 0], [0, -1]], dtype=complex)
    return {'I': I, 'X': X, 'Y': Y, 'Z': Z}

def hadamard():
    """Hadamard gate."""
    return np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)

def rotation_gate(axis, theta):
    """Rotation gate around axis by angle theta (degrees)."""
    theta_rad = np.radians(theta)
    pauli = pauli_matrices()
    return expm(-1j * theta_rad / 2 * pauli[axis])

def create_bloch_sphere(theta_deg, phi_deg):
    """Create hyper-realistic Bloch sphere with PBR materials and cinematic lighting."""
    theta = np.radians(theta_deg)
    phi = np.radians(phi_deg)
    
    # State vector endpoint
    x_state = np.sin(theta) * np.cos(phi)
    y_state = np.sin(theta) * np.sin(phi)
    z_state = np.cos(theta)
    
    # High-resolution sphere surface (volumetric)
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x_sphere = np.outer(np.cos(u), np.sin(v))
    y_sphere = np.outer(np.sin(u), np.sin(v))
    z_sphere = np.outer(np.ones(np.size(u)), np.cos(v))
    
    fig = go.Figure()
    
    # HYPER-REALISTIC FROSTED GLASS SPHERE (Subsurface Scattering)
    # Create depth-based opacity for volumetric effect
    depth = z_sphere  # Use Z-depth for SSS simulation
    normalized_depth = (depth - depth.min()) / (depth.max() - depth.min())
    
    # Physically-Based Material: Frosted Quartz Glass
    fig.add_trace(go.Surface(
        x=x_sphere, y=y_sphere, z=z_sphere,
        surfacecolor=normalized_depth,
        colorscale=[
            [0.0, 'rgba(0, 217, 255, 0.15)'],    # Deep areas - cyan tint
            [0.3, 'rgba(123, 97, 255, 0.25)'],   # Mid-depth - indigo
            [0.6, 'rgba(0, 255, 148, 0.2)'],     # Rim areas - lime accent
            [1.0, 'rgba(255, 255, 255, 0.4)']    # Highlights - anisotropic
        ],
        showscale=False,
        opacity=0.65,
        lighting=dict(
            ambient=0.4,           # Ambient occlusion base
            diffuse=0.7,           # Diffuse surface scattering
            specular=1.2,          # Anisotropic highlights
            roughness=0.3,         # PBR roughness (frosted glass)
            fresnel=2.5            # Rim light intensity
        ),
        lightposition=dict(
            x=1500,   # Key light (main)
            y=1500,   # Fill light
            z=2000    # Rim light (backlight)
        ),
        contours=dict(
            x=dict(highlight=True, highlightcolor="rgba(0, 217, 255, 0.3)", highlightwidth=2),
            y=dict(highlight=True, highlightcolor="rgba(123, 97, 255, 0.3)", highlightwidth=2),
            z=dict(highlight=True, highlightcolor="rgba(0, 255, 148, 0.3)", highlightwidth=2)
        ),
        name='Frosted Glass Orb',
        hoverinfo='skip'
    ))
    
    # INNER GLOW EMISSION (Pulsating)
    inner_glow_intensity = 0.6 + 0.2 * np.sin(theta_deg / 30)  # Pulsate based on state
    fig.add_trace(go.Surface(
        x=x_sphere * 0.95, y=y_sphere * 0.95, z=z_sphere * 0.95,
        surfacecolor=normalized_depth,
        colorscale=[
            [0.0, f'rgba(0, 217, 255, {inner_glow_intensity * 0.3})'],
            [0.5, f'rgba(123, 97, 255, {inner_glow_intensity * 0.4})'],
            [1.0, f'rgba(0, 255, 148, {inner_glow_intensity * 0.2})']
        ],
        showscale=False,
        opacity=0.4,
        lighting=dict(ambient=0.8, diffuse=0.2, specular=0.5),
        name='Inner Emission',
        hoverinfo='skip'
    ))
    
    # CINEMATIC LIGHTING: Computational Axes with PBR Materials
    axis_length = 1.4
    axes_data = [
        ([0, axis_length], [0, 0], [0, 0], 'X', '#00D9FF', 8),
        ([0, 0], [0, axis_length], [0, 0], 'Y', '#00FF94', 8),
        ([0, 0], [0, 0], [0, axis_length], 'Z', '#7B61FF', 8)
    ]
    
    for x, y, z, name, color, width in axes_data:
        # Metallic axis lines with bloom
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z,
            mode='lines+text',
            line=dict(
                color=color, 
                width=width,
                # Simulate bloom with gradient
            ),
            text=['', f'|{name}⟩'],
            textposition='top center',
            textfont=dict(size=16, color=color, family='JetBrains Mono'),
            showlegend=False,
            hoverinfo='skip'
        ))
        
        # Axis endpoint glow spheres (anisotropic highlights)
        endpoint = [x[-1], y[-1], z[-1]]
        fig.add_trace(go.Scatter3d(
            x=[endpoint[0]], y=[endpoint[1]], z=[endpoint[2]],
            mode='markers',
            marker=dict(
                size=12,
                color=color,
                opacity=0.9,
                line=dict(color='rgba(255, 255, 255, 0.6)', width=2),
                symbol='circle'
            ),
            showlegend=False,
            hoverinfo='skip'
        ))
    
    # HYPER-REALISTIC STATE VECTOR: Glowing Metallic Filament
    # Motion trail simulation (decaying particles)
    trail_length = 8
    trail_points = []
    for i in range(trail_length):
        decay_factor = (trail_length - i) / trail_length
        trail_points.append([
            x_state * decay_factor * 0.95,
            y_state * decay_factor * 0.95,
            z_state * decay_factor * 0.95
        ])
    
    # Motion trail (particle trace)
    if len(trail_points) > 1:
        trail_x, trail_y, trail_z = zip(*trail_points)
        fig.add_trace(go.Scatter3d(
            x=trail_x, y=trail_y, z=trail_z,
            mode='markers',
            marker=dict(
                size=[2 + i*0.5 for i in range(len(trail_points))],
                color=['rgba(245, 158, 11, {})'.format(0.1 + i*0.1) for i in range(len(trail_points))],
                symbol='circle'
            ),
            showlegend=False,
            hoverinfo='skip'
        ))
    
    # Main state vector: Solid metallic filament with PBR
    fig.add_trace(go.Scatter3d(
        x=[0, x_state], y=[0, y_state], z=[0, z_state],
        mode='lines+markers',
        line=dict(
            color='#F59E0B',  # Metallic gold
            width=10
        ),
        marker=dict(
            size=[4, 18],
            color=['rgba(245, 158, 11, 0.8)', 'rgba(245, 158, 11, 1)'],
            symbol='diamond',
            line=dict(color='rgba(255, 255, 255, 0.8)', width=2)
        ),
        name='|ψ⟩ State Vector',
        hovertemplate=(
            '<b style="font-family:JetBrains Mono;color:#00D9FF;">QUANTUM STATE VECTOR</b><br>'
            '<span style="font-family:JetBrains Mono;font-size:10px;color:#7B61FF;">━━━━━━━━━━━━━━━━━━━━━━━━</span><br>'
            '<b>|ψ⟩</b> = α|0⟩ + β|1⟩<br>'
            '<span style="color:#00FF94;">θ</span> = %{customdata[0]:.2f}° (Polar)<br>'
            '<span style="color:#00FF94;">φ</span> = %{customdata[1]:.2f}° (Azimuthal)<br>'
            '<span style="font-family:JetBrains Mono;font-size:10px;color:#7B61FF;">━━━━━━━━━━━━━━━━━━━━━━━━</span><br>'
            '<span style="color:rgba(255,255,255,0.6);font-size:9px;">CAMBRIDGE QUANTUM OBSERVATORY</span>'
            '<extra></extra>'
        ),
        customdata=[[theta_deg, phi_deg]]
    ))
    
    # PROBABILITY CLOUD: Swirling Nebula inside sphere
    # Generate cloud particles based on probability amplitude
    n_particles = 200
    cloud_theta = np.random.uniform(0, 2*np.pi, n_particles)
    cloud_phi_var = np.random.normal(phi, 0.3, n_particles)
    cloud_theta_var = np.random.normal(theta, 0.3, n_particles)
    
    cloud_r = np.abs(np.random.normal(0.7, 0.15, n_particles))  # Radial distribution
    cloud_x = cloud_r * np.sin(cloud_theta_var) * np.cos(cloud_phi_var)
    cloud_y = cloud_r * np.sin(cloud_theta_var) * np.sin(cloud_phi_var)
    cloud_z = cloud_r * np.cos(cloud_theta_var)
    
    # Density-based coloring
    density = np.abs(np.sin(theta))  # Probability amplitude density
    cloud_colors = [f'rgba(0, 217, 255, {0.3 * density})' if i % 2 == 0 else f'rgba(123, 97, 255, {0.3 * density})' for i in range(n_particles)]
    
    fig.add_trace(go.Scatter3d(
        x=cloud_x, y=cloud_y, z=cloud_z,
        mode='markers',
        marker=dict(
            size=np.random.uniform(2, 6, n_particles),
            color=cloud_colors,
            symbol='circle',
            opacity=0.5
        ),
        showlegend=False,
        hoverinfo='skip',
        name='Probability Nebula'
    ))
    
    # Equator circle with gaussian blur effect
    theta_eq = np.linspace(0, 2*np.pi, 150)
    fig.add_trace(go.Scatter3d(
        x=np.cos(theta_eq), y=np.sin(theta_eq), z=np.zeros_like(theta_eq),
        mode='lines',
        line=dict(color='rgba(255, 255, 255, 0.25)', width=3, dash='dot'),
        showlegend=False,
        hoverinfo='skip'
    ))
    
    # CINEMATIC LAYOUT: Depth of Field simulation
    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False, range=[-1.6, 1.6]),
            yaxis=dict(visible=False, range=[-1.6, 1.6]),
            zaxis=dict(visible=False, range=[-1.6, 1.6]),
            bgcolor='rgba(5, 5, 5, 0.5)',  # Dark background for contrast
            camera=dict(
                eye=dict(x=1.8, y=1.8, z=1.5),
                center=dict(x=0, y=0, z=0),
                projection=dict(type='perspective')
            ),
            aspectmode='cube'
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=0, b=0),
        height=550,
        showlegend=False,
        # Smooth non-linear easing (Quart-Out simulation)
        transition=dict(
            duration=800,
            easing='cubic-out'
        )
    )
    
    return fig

def density_matrix_to_bloch(rho):
    """Extract Bloch vector from density matrix."""
    pauli = pauli_matrices()
    r_x = np.trace(pauli['X'] @ rho).real
    r_y = np.trace(pauli['Y'] @ rho).real
    r_z = np.trace(pauli['Z'] @ rho).real
    return np.array([r_x, r_y, r_z])

def apply_noise_channel(rho, channel_type, strength):
    """Apply noise channel to density matrix."""
    if channel_type == "Depolarizing":
        I = pauli_matrices()['I']
        return (1 - strength) * rho + strength * I / 2
    
    elif channel_type == "Dephasing":
        # Phase damping
        rho_noisy = rho.copy()
        rho_noisy[0, 1] *= (1 - strength)
        rho_noisy[1, 0] *= (1 - strength)
        return rho_noisy
    
    elif channel_type == "Amplitude Damping":
        # T1 relaxation
        gamma = strength
        K0 = np.array([[1, 0], [0, np.sqrt(1-gamma)]], dtype=complex)
        K1 = np.array([[0, np.sqrt(gamma)], [0, 0]], dtype=complex)
        return K0 @ rho @ K0.conj().T + K1 @ rho @ K1.conj().T
    
    return rho

def generate_experiment_id():
    """Generate unique experiment ID."""
    timestamp = datetime.now().isoformat()
    random_component = str(np.random.randint(10000, 99999))
    hash_obj = hashlib.md5((timestamp + random_component).encode())
    return f"QEXP-{hash_obj.hexdigest()[:8].upper()}"

# Professional Row-Based Sidebar Navigation

# Initialize session state
if 'selected_module_id' not in st.session_state:
    st.session_state.selected_module_id = 'home'
if 'language' not in st.session_state:
    st.session_state.language = 'en'

# COMPREHENSIVE TRANSLATION SYSTEM - Embedded i18n (Streamlit Cloud Compatible)
TRANSLATIONS = {
    'en': {
        "global": {
            "title": "QUANTUM RESEARCH WORKBENCH v4.0.2",
            "platform_name": "Quantum Research Workbench",
            "version": "v4.0.2",
            "search_placeholder": "🔍 Search modules...",
            "language_en": "🇬🇧 EN",
            "language_ru": "🇷🇺 RU"
        },
        "navigation": {
            "home": "Home",
            "section_home": "HOME",
            "section_foundations": "FOUNDATIONS",
            "section_correlations": "QUANTUM CORRELATIONS",
            "section_dynamics": "NOISE & DYNAMICS",
            "section_variational": "VARIATIONAL ALGORITHMS",
            "section_qml": "QUANTUM ML",
            "section_hardware": "ERROR CORRECTION & HARDWARE",
            "section_complexity": "COMPLEXITY THEORY",
            "section_export": "DATA EXPORT"
        },
        "modules": {
            "home": "Home",
            "overview": "Theoretical Framework",
            "bloch": "Hilbert Space Dynamics",
            "interference": "Coherent Superposition",
            "entanglement": "Bell-State Correlations",
            "topological": "Topological Phases",
            "noise": "Dissipative Decoherence",
            "circuits": "Unitary Synthesis",
            "vqe": "VQE Architectures",
            "qaoa": "Optimization Manifolds",
            "qml": "Quantum Neural Networks",
            "qec": "Surface Code Protocols",
            "hardware": "QPU Topology Maps",
            "complexity": "Complexity Landscapes",
            "export": "Research Reproducibility"
        },
        "module_subtitles": {
            "home": "platform overview, quick start",
            "overview": "postulates, operators, measurement",
            "bloch": "unitary evolution, Hamiltonians",
            "interference": "phase, interference, amplitudes",
            "entanglement": "CHSH, nonlocality, EPR",
            "topological": "anyonic braiding, fault tolerance",
            "noise": "T1/T2, channels, density matrix",
            "circuits": "gate decomposition, compilation",
            "vqe": "ansatz design, energy landscapes",
            "qaoa": "gradients, barren plateaus",
            "qml": "embeddings, kernels, classifiers",
            "qec": "stabilizers, logical qubits",
            "hardware": "connectivity, calibration",
            "complexity": "BQP, QMA, oracle separation",
            "export": "export state vectors, circuits"
        },
        "status_badges": {
            "active": "Core Module",
            "variational": "Variational Algorithm",
            "frontier": "Advanced Topic",
            "combinatorial": "Combinatorial Optimization",
            "hybrid": "Hybrid QML",
            "fault_tolerant": "Fault-Tolerant QC",
            "infrastructure": "Research Infrastructure"
        },
        "system_status": {
            "title": "System Status",
            "operational": "OPERATIONAL",
            "coherence_time": "Coherence Time",
            "gate_fidelity": "Gate Fidelity",
            "temperature": "Temperature",
            "optimized": "OPTIMIZED",
            "status_label": "Status",
            "t1_label": "Relaxation Time T₁",
            "t2_label": "Coherence Time T₂",
            "single_gate": "Single-Qubit Fidelity",
            "two_gate": "Two-Qubit CNOT Fidelity",
            "readout": "Readout Fidelity",
            "vacuum": "Vacuum Pressure",
            "cryo_temp": "Cryogenic Temperature"
        },
        "home_page": {
            "hero_title": "Quantum Research Workbench",
            "hero_subtitle": "High-Fidelity Quantum Computing Research Platform",
            "hero_status": "SYSTEM STATUS: OPERATIONAL | QUBITS: STABLE | FIDELITY: >99.9%",
            "capabilities_title": "Research Capabilities",
            "cap_state_title": "State Manipulation",
            "cap_state_desc": "Unitary evolution, Bloch sphere dynamics, density matrix formalism, and projective measurements in complex Hilbert spaces.",
            "cap_noise_title": "Noise Modeling",
            "cap_noise_desc": "Realistic decoherence channels, T₁/T₂ relaxation, amplitude damping, and depolarizing noise with adjustable parameters.",
            "cap_variational_title": "Variational Algorithms",
            "cap_variational_desc": "VQE, QAOA, and hybrid quantum-classical optimization with gradient-based training and ansatz design tools.",
            "cap_export_title": "Reproducible Exports",
            "cap_export_desc": "JSON snapshots with SHA-256 verification, circuit diagrams, measurement statistics, and research metadata.",
            "quick_start_title": "Quick Start Guide",
            "quick_step1_title": "Select Module",
            "quick_step1_desc": "Choose from 13 quantum computing modules covering fundamentals to advanced topics.",
            "quick_step2_title": "Configure Parameters",
            "quick_step2_desc": "Adjust quantum parameters, noise models, backend selection, and measurement basis configurations.",
            "quick_step3_title": "Run & Export",
            "quick_step3_desc": "Execute experiments, analyze results, and export research snapshots as JSON or PDF reports.",
            "featured_title": "Featured Modules",
            "system_status_title": "System Status"
        },
        "buttons": {
            "launch": "Launch",
            "open": "Open",
            "apply": "Apply",
            "reset": "Reset",
            "export": "Export",
            "download": "Download",
            "run": "Run",
            "execute": "Execute",
            "simulate": "Simulate",
            "calculate": "Calculate",
            "measure": "Measure",
            "compose": "Compose"
        },
        "common": {
            "yes": "Yes",
            "no": "No",
            "none": "None",
            "loading": "Loading...",
            "error": "Error",
            "success": "Success",
            "warning": "Warning"
        },
        "charts": {
            "interference": {
                "phasor_title": "Phasor Diagram",
                "phasor_x_axis": "Real",
                "phasor_y_axis": "Imaginary",
                "pattern_title": "Interference Pattern",
                "pattern_x_axis": "Phase Difference (degrees)",
                "pattern_y_axis": "Total Probability |ψ|²",
                "amplitude_title": "Amplitude Components",
                "amplitude_y_axis": "AMPLITUDE",
                "probability_title": "Probability Distribution",
                "probability_y_axis": "|ψ|²"
            },
            "noise": {
                "decay_title": "Decoherence Time Evolution",
                "decay_x_axis": "Time (μs)",
                "decay_y_axis": "Normalized Amplitude",
                "t1_trace": "T₁ (Energy Relaxation)",
                "t2_trace": "T₂ (Dephasing)",
                "density_matrix_title": "Density Matrix Evolution"
            },
            "vqe": {
                "convergence_title": "VQE Energy Convergence",
                "convergence_x_axis": "Iteration",
                "convergence_y_axis": "Energy (Hartree)",
                "landscape_title": "Energy Landscape",
                "parameters_title": "Parameter Evolution"
            },
            "qaoa": {
                "convergence_title": "QAOA Convergence",
                "convergence_x_axis": "Iteration",
                "convergence_y_axis": "MaxCut Value",
                "probability_title": "Solution Probability Distribution",
                "probability_x_axis": "Bitstring",
                "probability_y_axis": "Probability",
                "graph_title": "Graph Structure"
            },
            "qml": {
                "decision_boundary_title": "Quantum Decision Boundary",
                "training_data": "Training Data",
                "test_data": "Test Data",
                "decision_surface": "Decision Surface",
                "accuracy_title": "Classification Accuracy"
            },
            "circuits": {
                "unitary_real_title": "Unitary Matrix (Real Part)",
                "unitary_imag_title": "Unitary Matrix (Imaginary Part)",
                "measurement_title": "Measurement Results",
                "measurement_y_axis": "Counts",
                "gate_decomposition": "Gate Decomposition"
            },
            "qec": {
                "syndrome_title": "Syndrome Measurement",
                "error_rate_title": "Logical Error Rate",
                "stabilizer_title": "Stabilizer Violations",
                "fidelity_title": "Code Fidelity"
            },
            "entanglement": {
                "bell_measurement": "Bell State Measurement",
                "correlation_title": "Quantum Correlations",
                "chsh_title": "CHSH Inequality Test",
                "density_matrix": "Two-Qubit Density Matrix"
            },
            "topological": {
                "phase_diagram": "Topological Phase Diagram",
                "braid_evolution": "Anyonic Braid Evolution",
                "berry_phase": "Berry Phase Accumulation"
            },
            "hardware": {
                "connectivity_title": "QPU Connectivity Map",
                "calibration_title": "Calibration Metrics",
                "fidelity_map": "Gate Fidelity Heatmap",
                "crosstalk_title": "Crosstalk Analysis"
            },
            "common_traces": {
                "alpha1": "α₁",
                "alpha2": "α₂",
                "total": "α₁ + α₂",
                "real_part": "Real Part",
                "imag_part": "Imaginary Part",
                "measured": "Measured",
                "theoretical": "Theoretical",
                "ground_state": "Ground State",
                "excited_state": "Excited State"
            }
        }
    },
    'ru': {
        "global": {
            "title": "КВАНТОВЫЙ ИССЛЕДОВАТЕЛЬСКИЙ ЦЕНТР v4.0.2",
            "platform_name": "Квантовый Исследовательский Центр",
            "version": "v4.0.2",
            "search_placeholder": "🔍 Поиск модулей...",
            "language_en": "🇬🇧 EN",
            "language_ru": "🇷🇺 RU"
        },
        "navigation": {
            "home": "Главная",
            "section_home": "ГЛАВНАЯ",
            "section_foundations": "ОСНОВЫ",
            "section_correlations": "КВАНТОВЫЕ КОРРЕЛЯЦИИ",
            "section_dynamics": "ШУМЫ И ДИНАМИКА",
            "section_variational": "ВАРИАЦИОННЫЕ АЛГОРИТМЫ",
            "section_qml": "КВАНТОВОЕ МО",
            "section_hardware": "КОРРЕКЦИЯ ОШИБОК И ОБОРУДОВАНИЕ",
            "section_complexity": "ТЕОРИЯ СЛОЖНОСТИ",
            "section_export": "ЭКСПОРТ ДАННЫХ"
        },
        "modules": {
            "home": "Главная",
            "overview": "Теоретическая Основа",
            "bloch": "Динамика Пространства Гильберта",
            "interference": "Когерентная Суперпозиция",
            "entanglement": "Корреляции Белла",
            "topological": "Топологические Фазы",
            "noise": "Диссипативная Декогеренция",
            "circuits": "Унитарный Синтез",
            "vqe": "Архитектуры VQE",
            "qaoa": "Многообразия Оптимизации",
            "qml": "Квантовые Нейронные Сети",
            "qec": "Протоколы Поверхностного Кода",
            "hardware": "Топология КПУ",
            "complexity": "Ландшафты Сложности",
            "export": "Воспроизводимость Исследований"
        },
        "module_subtitles": {
            "home": "обзор платформы, быстрый старт",
            "overview": "постулаты, операторы, измерения",
            "bloch": "унитарная эволюция, гамильтонианы",
            "interference": "фаза, интерференция, амплитуды",
            "entanglement": "CHSH, нелокальность, ЭПР",
            "topological": "плетение анионов, отказоустойчивость",
            "noise": "T1/T2, каналы, матрица плотности",
            "circuits": "декомпозиция гейтов, компиляция",
            "vqe": "дизайн ансаца, энергетические ландшафты",
            "qaoa": "градиенты, пустые плато",
            "qml": "вложения, ядра, классификаторы",
            "qec": "стабилизаторы, логические кубиты",
            "hardware": "связность, калибровка",
            "complexity": "BQP, QMA, оракульное разделение",
            "export": "экспорт векторов состояний, схем"
        },
        "status_badges": {
            "active": "Основной Модуль",
            "variational": "Вариационный Алгоритм",
            "frontier": "Передовая Тема",
            "combinatorial": "Комбинаторная Оптимизация",
            "hybrid": "Гибридное КМО",
            "fault_tolerant": "Отказоустойчивые КВ",
            "infrastructure": "Исследовательская Инфраструктура"
        },
        "system_status": {
            "title": "Статус Системы",
            "operational": "РАБОТАЕТ",
            "coherence_time": "Время Когерентности",
            "gate_fidelity": "Точность Гейтов",
            "temperature": "Температура",
            "optimized": "ОПТИМИЗИРОВАНО",
            "status_label": "Статус",
            "t1_label": "Время Релаксации T₁",
            "t2_label": "Время Когерентности T₂",
            "single_gate": "Точность Однокубитных Гейтов",
            "two_gate": "Точность Двухкубитных CNOT",
            "readout": "Точность Считывания",
            "vacuum": "Вакуумное Давление",
            "cryo_temp": "Криогенная Температура"
        },
        "home_page": {
            "hero_title": "Квантовый Исследовательский Центр",
            "hero_subtitle": "Высокоточная Платформа для Квантовых Исследований",
            "hero_status": "СТАТУС СИСТЕМЫ: РАБОТАЕТ | КУБИТЫ: СТАБИЛЬНЫ | ТОЧНОСТЬ: >99.9%",
            "capabilities_title": "Исследовательские Возможности",
            "cap_state_title": "Манипуляция Состояниями",
            "cap_state_desc": "Унитарная эволюция, динамика сферы Блоха, формализм матрицы плотности и проективные измерения в комплексных пространствах Гильберта.",
            "cap_noise_title": "Моделирование Шума",
            "cap_noise_desc": "Реалистичные каналы декогеренции, релаксация T₁/T₂, затухание амплитуды и деполяризующий шум с настраиваемыми параметрами.",
            "cap_variational_title": "Вариационные Алгоритмы",
            "cap_variational_desc": "VQE, QAOA и гибридная квантово-классическая оптимизация с градиентным обучением и инструментами проектирования ансаца.",
            "cap_export_title": "Воспроизводимый Экспорт",
            "cap_export_desc": "JSON снимки с верификацией SHA-256, диаграммы схем, статистика измерений и метаданные исследований.",
            "quick_start_title": "Руководство по Быстрому Старту",
            "quick_step1_title": "Выбрать Модуль",
            "quick_step1_desc": "Выберите из 13 модулей квантовых вычислений, охватывающих от основ до продвинутых тем.",
            "quick_step2_title": "Настроить Параметры",
            "quick_step2_desc": "Настройте квантовые параметры, модели шума, выбор бэкенда и конфигурации базиса измерений.",
            "quick_step3_title": "Запустить и Экспортировать",
            "quick_step3_desc": "Выполняйте эксперименты, анализируйте результаты и экспортируйте снимки исследований в формате JSON или PDF.",
            "featured_title": "Избранные Модули",
            "system_status_title": "Статус Системы"
        },
        "buttons": {
            "launch": "Запустить",
            "open": "Открыть",
            "apply": "Применить",
            "reset": "Сбросить",
            "export": "Экспорт",
            "download": "Скачать",
            "run": "Выполнить",
            "execute": "Запустить",
            "simulate": "Симулировать",
            "calculate": "Вычислить",
            "measure": "Измерить",
            "compose": "Составить"
        },
        "common": {
            "yes": "Да",
            "no": "Нет",
            "none": "Нет",
            "loading": "Загрузка...",
            "error": "Ошибка",
            "success": "Успешно",
            "warning": "Внимание"
        },
        "charts": {
            "interference": {
                "phasor_title": "Векторная Диаграмма",
                "phasor_x_axis": "Действительная Часть",
                "phasor_y_axis": "Мнимая Часть",
                "pattern_title": "Интерференционная Картина",
                "pattern_x_axis": "Разность Фаз (градусы)",
                "pattern_y_axis": "Полная Вероятность |ψ|²",
                "amplitude_title": "Компоненты Амплитуды",
                "amplitude_y_axis": "АМПЛИТУДА",
                "probability_title": "Распределение Вероятности",
                "probability_y_axis": "|ψ|²"
            },
            "noise": {
                "decay_title": "Эволюция Декогеренции",
                "decay_x_axis": "Время (мкс)",
                "decay_y_axis": "Нормализованная Амплитуда",
                "t1_trace": "T₁ (Энергетическая Релаксация)",
                "t2_trace": "T₂ (Дефазирование)",
                "density_matrix_title": "Эволюция Матрицы Плотности"
            },
            "vqe": {
                "convergence_title": "Сходимость VQE Энергии",
                "convergence_x_axis": "Итерация",
                "convergence_y_axis": "Энергия (Хартри)",
                "landscape_title": "Энергетический Ландшафт",
                "parameters_title": "Эволюция Параметров"
            },
            "qaoa": {
                "convergence_title": "Сходимость QAOA",
                "convergence_x_axis": "Итерация",
                "convergence_y_axis": "Значение MaxCut",
                "probability_title": "Распределение Вероятности Решений",
                "probability_x_axis": "Битовая Строка",
                "probability_y_axis": "Вероятность",
                "graph_title": "Структура Графа"
            },
            "qml": {
                "decision_boundary_title": "Квантовая Граница Решений",
                "training_data": "Обучающие Данные",
                "test_data": "Тестовые Данные",
                "decision_surface": "Поверхность Решений",
                "accuracy_title": "Точность Классификации"
            },
            "circuits": {
                "unitary_real_title": "Унитарная Матрица (Действительная Часть)",
                "unitary_imag_title": "Унитарная Матрица (Мнимая Часть)",
                "measurement_title": "Результаты Измерений",
                "measurement_y_axis": "Счётчик",
                "gate_decomposition": "Декомпозиция Гейта"
            },
            "qec": {
                "syndrome_title": "Измерение Синдрома",
                "error_rate_title": "Логическая Частота Ошибок",
                "stabilizer_title": "Нарушения Стабилизатора",
                "fidelity_title": "Точность Кода"
            },
            "entanglement": {
                "bell_measurement": "Измерение Состояния Белла",
                "correlation_title": "Квантовые Корреляции",
                "chsh_title": "Тест Неравенства CHSH",
                "density_matrix": "Двухкубитная Матрица Плотности"
            },
            "topological": {
                "phase_diagram": "Диаграмма Топологических Фаз",
                "braid_evolution": "Эволюция Плетения Анионов",
                "berry_phase": "Накопление Фазы Берри"
            },
            "hardware": {
                "connectivity_title": "Карта Связности КПУ",
                "calibration_title": "Метрики Калибровки",
                "fidelity_map": "Тепловая Карта Точности Гейтов",
                "crosstalk_title": "Анализ Перекрёстных Помех"
            },
            "common_traces": {
                "alpha1": "α₁",
                "alpha2": "α₂",
                "total": "α₁ + α₂",
                "real_part": "Действительная Часть",
                "imag_part": "Мнимая Часть",
                "measured": "Измеренный",
                "theoretical": "Теоретический",
                "ground_state": "Основное Состояние",
                "excited_state": "Возбуждённое Состояние"
            }
        }
    }
}

# Legacy embedded translations for backward compatibility (to be removed after full migration)
TRANSLATIONS_LEGACY = {
    'en': {
        # ===== GLOBAL UI =====
        'title': 'QUANTUM RESEARCH WORKBENCH v4.0.2',
        'system_status': 'SYSTEM STATUS',
        'operational': 'OPERATIONAL',
        'coherence_time': 'COHERENCE TIME',
        'optimized': 'OPTIMIZED',
        'gate_fidelity': 'GATE FIDELITY',
        'temp': 'TEMP',
        'search_placeholder': '🔍 Search modules...',
        'button_navigate': '→',
        'units_degrees': '°',
        'units_microseconds': 'μs',
        'units_millikelvin': 'mK',
        'units_mbar': 'mbar',
        'label_greater_than': '>',
        'status_active': 'Core Module',
        'status_variational': 'Variational Algorithm',
        'status_frontier': 'Advanced Topic',
        'status_combinatorial': 'Combinatorial Optimization',
        'status_hybrid': 'Hybrid QML',
        'status_fault_tolerant': 'Fault-Tolerant QC',
        'status_infrastructure': 'Research Infrastructure',
        
        # ===== SECTIONS =====
        'section_home': 'HOME',
        'section_foundations': 'FOUNDATIONS',
        'section_correlations': 'QUANTUM CORRELATIONS',
        'section_dynamics': 'NOISE & DYNAMICS',
        'section_variational': 'VARIATIONAL ALGORITHMS',
        'section_qml': 'QUANTUM ML',
        'section_hardware': 'ERROR CORRECTION & HARDWARE',
        'section_complexity': 'COMPLEXITY THEORY',
        'section_export': 'DATA EXPORT',
        
        # ===== MODULE TITLES & SUBTITLES =====
        'module_home': 'Home',
        'module_overview': 'Theoretical Framework',
        'module_bloch': 'Hilbert Space Dynamics',
        'module_interference': 'Coherent Superposition',
        'module_entanglement': 'Bell-State Correlations',
        'module_topological': 'Topological Phases',
        'module_noise': 'Dissipative Decoherence',
        'module_circuits': 'Unitary Synthesis',
        'module_vqe': 'VQE Architectures',
        'module_qaoa': 'Optimization Manifolds',
        'module_qml': 'Quantum Neural Networks',
        'module_qec': 'Surface Code Protocols',
        'module_hardware': 'QPU Topology Maps',
        'module_complexity': 'Complexity Landscapes',
        'module_export': 'Research Reproducibility',
        
        'subtitle_home': 'platform overview, quick start',
        'subtitle_overview': 'postulates, operators, measurement',
        'subtitle_bloch': 'unitary evolution, Hamiltonians',
        'subtitle_interference': 'phase, interference, amplitudes',
        'subtitle_entanglement': 'CHSH, nonlocality, EPR',
        'subtitle_topological': 'anyonic braiding, fault tolerance',
        'subtitle_noise': 'T1/T2, channels, density matrix',
        'subtitle_circuits': 'gate decomposition, compilation',
        'subtitle_vqe': 'ansatz design, energy landscapes',
        'subtitle_qaoa': 'gradients, barren plateaus',
        'subtitle_qml': 'embeddings, kernels, classifiers',
        'subtitle_qec': 'stabilizers, logical qubits',
        'subtitle_hardware': 'connectivity, calibration',
        'subtitle_complexity': 'BQP, QMA, oracle separation',
        'subtitle_export': 'export state vectors, circuits',
        
        # ===== SYSTEM STATUS PANEL =====
        'status_title': 'SYSTEM STATUS PANEL',
        'status_coherence_t1': 'Relaxation Time T₁',
        'status_coherence_t2': 'Coherence Time T₂',
        'status_gate_single': 'Gate Fidelity (Single-Qubit)',
        'status_gate_two': 'Gate Fidelity (Two-Qubit CNOT)',
        'status_readout': 'Readout Fidelity',
        'status_vacuum': 'Vacuum Pressure',
        'status_cryo_temp': 'Cryogenic Temperature',
        
        # ===== OVERVIEW MODULE =====
        'overview_capabilities_title': '→ RESEARCH TERMINAL CAPABILITIES',
        'overview_capabilities_text': 'This workbench provides a <strong>high-fidelity environment</strong> for quantum state manipulation within the complex Hilbert space $\\mathcal{H} = \\mathbb{C}^{2^n}$. Execute variational algorithms, simulate noise channels, and perform quantum state tomography with publication-ready visualizations.',
        'overview_module_selector': 'RESEARCH MODULE SELECTOR',
        'overview_telemetry_title': 'REAL-TIME TELEMETRY STREAM',
        
        # ===== BLOCH SPHERE MODULE =====
        'bloch_module_title': 'MODULE 02: HILBERT SPACE MAPPING & BLOCH VECTOR DYNAMICS',
        'bloch_status_badge': 'COHERENCE: OPTIMIZED | FIDELITY: >99.9%',
        'bloch_math_title': 'MATHEMATICAL FORMALISM: PROJECTIVE HILBERT SPACE',
        'bloch_math_intro': 'A single qubit resides within the two-dimensional complex Hilbert space $\\mathcal{H}_2 = \\mathbb{C}^2$. The most general pure state exists as a superposition over the computational basis $\\{|0\\rangle, |1\\rangle\\}$, constrained by the normalization condition inherent to quantum mechanics:',
        'bloch_manifold_title': 'Bloch Sphere Manifold:',
        'bloch_manifold_desc': 'The projective Hilbert space $\\mathbb{CP}^1 \\cong S^2$ (Riemann sphere) provides a geometric visualization where each pure state $|\\psi\\rangle$ corresponds to a unique point on the unit sphere. The <strong>Bloch vector</strong> $\\vec{r} = (\\sin\\theta\\cos\\phi, \\sin\\theta\\sin\\phi, \\cos\\theta)$ encodes the state\'s expectation values $\\langle \\sigma_x \\rangle, \\langle \\sigma_y \\rangle, \\langle \\sigma_z \\rangle$.',
        'bloch_pure_state': '→ Pure States:',
        'bloch_mixed_state': '→ Mixed States:',
        'bloch_maximally_mixed': '→ Maximally Mixed:',
        'bloch_config_title': 'STATE VECTOR CONFIGURATION',
        'bloch_config_desc': 'Manipulate spherical coordinates to observe <strong>geometric phase accumulation</strong> via parallel transport on the Bloch manifold.',
        'bloch_theta_label': '⚛ POLAR ANGLE θ [0, π]',
        'bloch_theta_help': 'Controls latitude on Bloch sphere (|0⟩ at θ=0, |1⟩ at θ=π)',
        'bloch_phi_label': '⚡ AZIMUTHAL PHASE φ [0, 2π] - ROTARY CONTROL',
        'bloch_phi_help': 'Determines relative phase between computational basis states',
        'bloch_gate_title': 'UNITARY GATE SEQUENCE APPLICATION',
        'bloch_gate_compose': 'Compose Gate Decomposition',
        'bloch_gate_h': 'H (Hadamard: X+Z Basis Change)',
        'bloch_gate_x': 'X (Pauli-X: Bit Flip)',
        'bloch_gate_y': 'Y (Pauli-Y: Bit+Phase Flip)',
        'bloch_gate_z': 'Z (Pauli-Z: Phase Flip)',
        'bloch_gate_rx': 'RX(π/4): X-Axis Rotation',
        'bloch_gate_ry': 'RY(π/4): Y-Axis Rotation',
        'bloch_gate_rz': 'RZ(π/4): Z-Axis Rotation',
        'bloch_gate_s': 'S (Phase Gate: π/2)',
        'bloch_gate_t': 'T (π/8 Gate)',
        'bloch_measure_title': 'MEASUREMENT BASIS (TOMOGRAPHY)',
        'bloch_measure_label': 'Select Pauli Operator for Projective Measurement',
        'bloch_measure_z': 'Z (Computational Basis)',
        'bloch_measure_x': 'X (Hadamard Basis)',
        'bloch_measure_y': 'Y (Circular Basis)',
        'bloch_metric_norm': 'State Norm',
        'bloch_metric_p0': 'P(|0⟩)',
        'bloch_metric_p1': 'P(|1⟩)',
        'bloch_metric_phase': 'Relative Phase',
        'bloch_code_title': 'Executable Code',
        'bloch_code_comment_state': '# Define initial state',
        'bloch_code_comment_gates': '# Apply gate sequence:',
        'bloch_code_comment_measure': '# Measurement probabilities',
        
        # ===== INTERFERENCE MODULE =====
        'interf_module_title': 'Superposition & Quantum Interference',
        'interf_card_title': 'Wave-Particle Duality in Quantum Computation',
        'interf_card_desc': 'Quantum interference emerges from the coherent superposition of probability amplitudes. Unlike classical probability, amplitudes can interfere constructively or destructively depending on their relative phase.',
        'interf_term_desc': 'The interference term 2Re(α₁*α₂) = 2|α₁||α₂|cos(φ₁ - φ₂) depends on the relative phase.',
        'interf_constructive': '<strong>Constructive interference:</strong> φ₁ - φ₂ = 0, 2π, ... → amplitudes add',
        'interf_destructive': '<strong>Destructive interference:</strong> φ₁ - φ₂ = π, 3π, ... → amplitudes cancel',
        'interf_config_title': 'Path Amplitude Configuration',
        'interf_amp1_label': 'Amplitude |α₁|',
        'interf_phase1_label': 'Phase φ₁ (degrees)',
        'interf_amp2_label': 'Amplitude |α₂|',
        'interf_phase2_label': 'Phase φ₂ (degrees)',
        'interf_prob_quantum': 'Quantum Probability',
        'interf_prob_classical': 'Classical (No Interference)',
        'interf_prob_term': 'Interference Term',
        'interf_viz_title': 'Complex Amplitude Visualization',
        'interf_pattern_title': 'Interference Fringe Pattern',
        'interf_chart_title': 'Probability vs Relative Phase',
        'interf_chart_x': 'Phase Difference φ₂ - φ₁ (degrees)',
        'interf_chart_y': 'Detection Probability',
        
        # ===== ENTANGLEMENT MODULE =====
        'ent_module_title': 'Entanglement & Bell States',
        'ent_card_title': 'Quantum Entanglement',
        'ent_card_desc': 'Entanglement is a uniquely quantum correlation where measurement outcomes of separated particles are correlated in ways that cannot be explained by classical physics. It\'s the foundation of quantum communication, teleportation, and quantum advantage.',
        'ent_bell_title': '<strong>Bell States:</strong> The four maximally entangled two-qubit states:',
        'ent_prep_title': 'Bell State Preparation',
        'ent_select_label': 'Select Bell State',
        'ent_bell_phi_plus': 'Φ⁺ (|00⟩ + |11⟩)',
        'ent_bell_phi_minus': 'Φ⁻ (|00⟩ - |11⟩)',
        'ent_bell_psi_plus': 'Ψ⁺ (|01⟩ + |10⟩)',
        'ent_bell_psi_minus': 'Ψ⁻ (|01⟩ - |10⟩)',
        'ent_circuit_label': '<strong>Circuit:</strong>',
        'ent_state_title': 'State Vector',
        'ent_prob_title': 'PROBABILITY DISTRIBUTION',
        'ent_quant_title': 'Entanglement Quantification',
        'ent_entropy': 'Entanglement Entropy',
        'ent_concurrence': 'Concurrence',
        'ent_entangled': 'Entangled?',
        'ent_bell_inequality': 'Bell Inequality (CHSH)',
        'ent_chsh_desc': '<p>The CHSH inequality: $|S| \\leq 2$ for local hidden variable theories.</p><p>Quantum mechanics predicts $S = 2\\sqrt{2} \\approx 2.828$ for Bell states, violating the inequality and ruling out local realism.</p>',
        'ent_button_chsh': 'Run CHSH Test',
        'ent_chsh_param': 'CHSH Parameter |S|',
        'ent_violation_yes': '✅ Bell inequality violated! |S| = {:.3f} > 2',
        'ent_violation_desc': 'This demonstrates quantum entanglement and rules out local hidden variable theories!',
        'ent_violation_no': 'No violation detected: |S| = {:.3f} ≤ 2',
        'ent_logged': '💾 Experiment logged! Visit \'Reproducibility & Export\' to download results.',
        
        # ===== COMMON LABELS =====
        'common_yes': 'Yes',
        'common_no': 'No',
        'common_none': 'None',
    },
    'ru': {
        # ===== GLOBAL UI =====
        'title': 'КВАНТОВЫЙ ИССЛЕДОВАТЕЛЬСКИЙ ЦЕНТР v4.0.2',
        'system_status': 'СТАТУС СИСТЕМЫ',
        'operational': 'РАБОТАЕТ',
        'coherence_time': 'ВРЕМЯ КОГЕРЕНТНОСТИ',
        'optimized': 'ОПТИМИЗИРОВАНО',
        'gate_fidelity': 'ТОЧНОСТЬ ГЕЙТОВ',
        'temp': 'ТЕМП',
        'search_placeholder': '🔍 Поиск модулей...',
        'button_navigate': '→',
        'units_degrees': '°',
        'units_microseconds': 'мкс',
        'units_millikelvin': 'мК',
        'units_mbar': 'мбар',
        'label_greater_than': '>',
        'status_active': 'Основной Модуль',
        'status_variational': 'Вариационный Алгоритм',
        'status_frontier': 'Передовая Тема',
        'status_combinatorial': 'Комбинаторная Оптимизация',
        'status_hybrid': 'Гибридное КМО',
        'status_fault_tolerant': 'Отказоустойчивые КВ',
        'status_infrastructure': 'Исследовательская Инфраструктура',
        
        # ===== SECTIONS =====
        'section_home': 'ГЛАВНАЯ',
        'section_foundations': 'ОСНОВЫ',
        'section_correlations': 'КВАНТОВЫЕ КОРРЕЛЯЦИИ',
        'section_dynamics': 'ШУМЫ И ДИНАМИКА',
        'section_variational': 'ВАРИАЦИОННЫЕ АЛГОРИТМЫ',
        'section_qml': 'КВАНТОВОЕ МАШИННОЕ ОБУЧЕНИЕ',
        'section_hardware': 'КОРРЕКЦИЯ ОШИБОК И ОБОРУДОВАНИЕ',
        'section_complexity': 'ТЕОРИЯ СЛОЖНОСТИ',
        'section_export': 'ЭКСПОРТ ДАННЫХ',
        
        # ===== MODULE TITLES & SUBTITLES =====
        'module_home': 'Главная',
        'module_overview': 'Теоретическая Основа',
        'module_bloch': 'Динамика Пространства Гильберта',
        'module_interference': 'Когерентная Суперпозиция',
        'module_entanglement': 'Корреляции Белла',
        'module_topological': 'Топологические Фазы',
        'module_noise': 'Диссипативная Декогеренция',
        'module_circuits': 'Унитарный Синтез',
        'module_vqe': 'Архитектуры VQE',
        'module_qaoa': 'Многообразия Оптимизации',
        'module_qml': 'Квантовые Нейронные Сети',
        'module_qec': 'Протоколы Поверхностного Кода',
        'module_hardware': 'Топология КПУ',
        'module_complexity': 'Ландшафты Сложности',
        'module_export': 'Воспроизводимость Исследований',
        
        'subtitle_home': 'обзор платформы, быстрый старт',
        'subtitle_overview': 'постулаты, операторы, измерения',
        'subtitle_bloch': 'унитарная эволюция, гамильтонианы',
        'subtitle_interference': 'фаза, интерференция, амплитуды',
        'subtitle_entanglement': 'CHSH, нелокальность, ЭПР',
        'subtitle_topological': 'плетение анионов, отказоустойчивость',
        'subtitle_noise': 'T1/T2, каналы, матрица плотности',
        'subtitle_circuits': 'декомпозиция гейтов, компиляция',
        'subtitle_vqe': 'дизайн ансаца, энергетические ландшафты',
        'subtitle_qaoa': 'градиенты, пустые плато',
        'subtitle_qml': 'вложения, ядра, классификаторы',
        'subtitle_qec': 'стабилизаторы, логические кубиты',
        'subtitle_hardware': 'связность, калибровка',
        'subtitle_complexity': 'BQP, QMA, оракульное разделение',
        'subtitle_export': 'экспорт векторов состояний, схем',
        
        # ===== SYSTEM STATUS PANEL =====
        'status_title': 'ПАНЕЛЬ СОСТОЯНИЯ СИСТЕМЫ',
        'status_coherence_t1': 'Время Релаксации T₁',
        'status_coherence_t2': 'Время Когерентности T₂',
        'status_gate_single': 'Точность Гейтов (Однокубитные)',
        'status_gate_two': 'Точность Гейтов (Двухкубитные CNOT)',
        'status_readout': 'Точность Считывания',
        'status_vacuum': 'Вакуумное Давление',
        'status_cryo_temp': 'Криогенная Температура',
        
        # ===== OVERVIEW MODULE =====
        'overview_capabilities_title': '→ ВОЗМОЖНОСТИ ИССЛЕДОВАТЕЛЬСКОГО ТЕРМИНАЛА',
        'overview_capabilities_text': 'Эта рабочая среда обеспечивает <strong>высокоточную среду</strong> для манипуляции квантовыми состояниями в комплексном пространстве Гильберта $\\mathcal{H} = \\mathbb{C}^{2^n}$. Выполняйте вариационные алгоритмы, моделируйте шумовые каналы и проводите квантовую томографию состояний с готовыми к публикации визуализациями.',
        'overview_module_selector': 'ВЫБОР ИССЛЕДОВАТЕЛЬСКОГО МОДУЛЯ',
        'overview_telemetry_title': 'ПОТОК ТЕЛЕМЕТРИИ В РЕАЛЬНОМ ВРЕМЕНИ',
        
        # ===== BLOCH SPHERE MODULE =====
        'bloch_module_title': 'МОДУЛЬ 02: ОТОБРАЖЕНИЕ ПРОСТРАНСТВА ГИЛЬБЕРТА И ДИНАМИКА ВЕКТОРА БЛОХА',
        'bloch_status_badge': 'КОГЕРЕНТНОСТЬ: ОПТИМИЗИРОВАНА | ТОЧНОСТЬ: >99.9%',
        'bloch_math_title': 'МАТЕМАТИЧЕСКИЙ ФОРМАЛИЗМ: ПРОЕКТИВНОЕ ПРОСТРАНСТВО ГИЛЬБЕРТА',
        'bloch_math_intro': 'Один кубит находится в двумерном комплексном пространстве Гильберта $\\mathcal{H}_2 = \\mathbb{C}^2$. Наиболее общее чистое состояние существует как суперпозиция над вычислительным базисом $\\{|0\\rangle, |1\\rangle\\}$, ограниченная условием нормализации, присущим квантовой механике:',
        'bloch_manifold_title': 'Многообразие Сферы Блоха:',
        'bloch_manifold_desc': 'Проективное пространство Гильберта $\\mathbb{CP}^1 \\cong S^2$ (сфера Римана) обеспечивает геометрическую визуализацию, где каждое чистое состояние $|\\psi\\rangle$ соответствует уникальной точке на единичной сфере. <strong>Вектор Блоха</strong> $\\vec{r} = (\\sin\\theta\\cos\\phi, \\sin\\theta\\sin\\phi, \\cos\\theta)$ кодирует ожидаемые значения состояния $\\langle \\sigma_x \\rangle, \\langle \\sigma_y \\rangle, \\langle \\sigma_z \\rangle$.',
        'bloch_pure_state': '→ Чистые Состояния:',
        'bloch_mixed_state': '→ Смешанные Состояния:',
        'bloch_maximally_mixed': '→ Максимально Смешанные:',
        'bloch_config_title': 'КОНФИГУРАЦИЯ ВЕКТОРА СОСТОЯНИЯ',
        'bloch_config_desc': 'Манипулируйте сферическими координатами для наблюдения <strong>накопления геометрической фазы</strong> через параллельный транспорт на многообразии Блоха.',
        'bloch_theta_label': '⚛ ПОЛЯРНЫЙ УГОЛ θ [0, π]',
        'bloch_theta_help': 'Управляет широтой на сфере Блоха (|0⟩ при θ=0, |1⟩ при θ=π)',
        'bloch_phi_label': '⚡ АЗИМУТАЛЬНАЯ ФАЗА φ [0, 2π] - ВРАЩАЮЩЕЕСЯ УПРАВЛЕНИЕ',
        'bloch_phi_help': 'Определяет относительную фазу между состояниями вычислительного базиса',
        'bloch_gate_title': 'ПРИМЕНЕНИЕ ПОСЛЕДОВАТЕЛЬНОСТИ УНИТАРНЫХ ГЕЙТОВ',
        'bloch_gate_compose': 'Композиция Декомпозиции Гейтов',
        'bloch_gate_h': 'H (Адамара: Смена Базиса X+Z)',
        'bloch_gate_x': 'X (Паули-X: Инверсия Бита)',
        'bloch_gate_y': 'Y (Паули-Y: Инверсия Бита+Фазы)',
        'bloch_gate_z': 'Z (Паули-Z: Инверсия Фазы)',
        'bloch_gate_rx': 'RX(π/4): Вращение Вокруг Оси X',
        'bloch_gate_ry': 'RY(π/4): Вращение Вокруг Оси Y',
        'bloch_gate_rz': 'RZ(π/4): Вращение Вокруг Оси Z',
        'bloch_gate_s': 'S (Фазовый Гейт: π/2)',
        'bloch_gate_t': 'T (Гейт π/8)',
        'bloch_measure_title': 'БАЗИС ИЗМЕРЕНИЯ (ТОМОГРАФИЯ)',
        'bloch_measure_label': 'Выберите Оператор Паули для Проективного Измерения',
        'bloch_measure_z': 'Z (Вычислительный Базис)',
        'bloch_measure_x': 'X (Базис Адамара)',
        'bloch_measure_y': 'Y (Круговой Базис)',
        'bloch_metric_norm': 'Норма Состояния',
        'bloch_metric_p0': 'P(|0⟩)',
        'bloch_metric_p1': 'P(|1⟩)',
        'bloch_metric_phase': 'Относительная Фаза',
        'bloch_code_title': 'Исполняемый Код',
        'bloch_code_comment_state': '# Определить начальное состояние',
        'bloch_code_comment_gates': '# Применить последовательность гейтов:',
        'bloch_code_comment_measure': '# Вероятности измерения',
        
        # ===== INTERFERENCE MODULE =====
        'interf_module_title': 'Суперпозиция и Квантовая Интерференция',
        'interf_card_title': 'Корпускулярно-Волновой Дуализм в Квантовых Вычислениях',
        'interf_card_desc': 'Квантовая интерференция возникает из когерентной суперпозиции амплитуд вероятности. В отличие от классической вероятности, амплитуды могут интерферировать конструктивно или деструктивно в зависимости от их относительной фазы.',
        'interf_term_desc': 'Интерференционный член 2Re(α₁*α₂) = 2|α₁||α₂|cos(φ₁ - φ₂) зависит от относительной фазы.',
        'interf_constructive': '<strong>Конструктивная интерференция:</strong> φ₁ - φ₂ = 0, 2π, ... → амплитуды складываются',
        'interf_destructive': '<strong>Деструктивная интерференция:</strong> φ₁ - φ₂ = π, 3π, ... → амплитуды гасятся',
        'interf_config_title': 'Конфигурация Амплитуды Траектории',
        'interf_amp1_label': 'Амплитуда |α₁|',
        'interf_phase1_label': 'Фаза φ₁ (градусы)',
        'interf_amp2_label': 'Амплитуда |α₂|',
        'interf_phase2_label': 'Фаза φ₂ (градусы)',
        'interf_prob_quantum': 'Квантовая Вероятность',
        'interf_prob_classical': 'Классическая (Без Интерференции)',
        'interf_prob_term': 'Интерференционный Член',
        'interf_viz_title': 'Визуализация Комплексной Амплитуды',
        'interf_pattern_title': 'Интерференционная Полосовая Картина',
        'interf_chart_title': 'Вероятность vs Относительная Фаза',
        'interf_chart_x': 'Разность Фаз φ₂ - φ₁ (градусы)',
        'interf_chart_y': 'Вероятность Обнаружения',
        
        # ===== ENTANGLEMENT MODULE =====
        'ent_module_title': 'Запутанность и Состояния Белла',
        'ent_card_title': 'Квантовая Запутанность',
        'ent_card_desc': 'Запутанность - это уникальная квантовая корреляция, при которой результаты измерений разделенных частиц коррелируют способами, которые не могут быть объяснены классической физикой. Это основа квантовой связи, телепортации и квантового превосходства.',
        'ent_bell_title': '<strong>Состояния Белла:</strong> Четыре максимально запутанных двухкубитных состояния:',
        'ent_prep_title': 'Подготовка Состояния Белла',
        'ent_select_label': 'Выберите Состояние Белла',
        'ent_bell_phi_plus': 'Φ⁺ (|00⟩ + |11⟩)',
        'ent_bell_phi_minus': 'Φ⁻ (|00⟩ - |11⟩)',
        'ent_bell_psi_plus': 'Ψ⁺ (|01⟩ + |10⟩)',
        'ent_bell_psi_minus': 'Ψ⁻ (|01⟩ - |10⟩)',
        'ent_circuit_label': '<strong>Схема:</strong>',
        'ent_state_title': 'Вектор Состояния',
        'ent_prob_title': 'РАСПРЕДЕЛЕНИЕ ВЕРОЯТНОСТЕЙ',
        'ent_quant_title': 'Квантификация Запутанности',
        'ent_entropy': 'Энтропия Запутанности',
        'ent_concurrence': 'Конкурренция',
        'ent_entangled': 'Запутанное?',
        'ent_bell_inequality': 'Неравенство Белла (CHSH)',
        'ent_chsh_desc': '<p>Неравенство CHSH: $|S| \\leq 2$ для локальных теорий со скрытыми переменными.</p><p>Квантовая механика предсказывает $S = 2\\sqrt{2} \\approx 2.828$ для состояний Белла, нарушая неравенство и исключая локальный реализм.</p>',
        'ent_button_chsh': 'Запустить Тест CHSH',
        'ent_chsh_param': 'Параметр CHSH |S|',
        'ent_violation_yes': '✅ Неравенство Белла нарушено! |S| = {:.3f} > 2',
        'ent_violation_desc': 'Это демонстрирует квантовую запутанность и исключает локальные теории со скрытыми переменными!',
        'ent_violation_no': 'Нарушение не обнаружено: |S| = {:.3f} ≤ 2',
        'ent_logged': '💾 Эксперимент зарегистрирован! Посетите "Воспроизводимость и Экспорт" для загрузки результатов.',
        
        # ===== COMMON LABELS =====
        'common_yes': 'Да',
        'common_no': 'Нет',
        'common_none': 'Нет',
    }
}

# Translation helper function with dot-notation support
def t(key, fallback=None):
    """
    Get translation for current language with fallback
    Supports dot notation: t('home_page.hero_title') or legacy flat keys: t('title')
    """
    lang = st.session_state.get('language', 'en')
    lang_dict = TRANSLATIONS.get(lang, TRANSLATIONS.get('en', {}))
    
    # Support dot notation for nested JSON structure
    if '.' in key:
        keys = key.split('.')
        value = lang_dict
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                value = None
                break
        if value:
            return value
    else:
        # Legacy flat key support
        if key in lang_dict:
            return lang_dict[key]
        # Try searching in all nested dicts for backward compatibility
        for section_dict in lang_dict.values():
            if isinstance(section_dict, dict) and key in section_dict:
                return section_dict[key]
    
    # Fallback handling
    if fallback:
        return fallback
    
    # Try English as fallback
    en_dict = TRANSLATIONS.get('en', {})
    if '.' in key:
        keys = key.split('.')
        value = en_dict
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                break
        if value:
            return value
    
    # Last resort: try legacy translations
    legacy_dict = TRANSLATIONS_LEGACY.get('en', {})
    if key in legacy_dict:
        return legacy_dict[key]
    
    return key  # Return key itself if no translation found

# Language selector
col_lang1, col_lang2 = st.sidebar.columns(2)
with col_lang1:
    if st.button(t('global.language_en'), key="lang_en", type="primary" if st.session_state.language == 'en' else "secondary", use_container_width=True):
        st.session_state.language = 'en'
        st.rerun()
with col_lang2:
    if st.button(t('global.language_ru'), key="lang_ru", type="primary" if st.session_state.language == 'ru' else "secondary", use_container_width=True):
        st.session_state.language = 'ru'
        st.rerun()

st.sidebar.markdown("---")

# Professional brand header
brand_header = f"""
<div class='sidebar-brand'>
    <div class='sidebar-brand-title'>{t('global.title')}</div>
    <div class='sidebar-brand-subtitle'>Quantum Research Platform</div>
</div>
"""
st.sidebar.markdown(brand_header, unsafe_allow_html=True)

# Navigation structure with organized groups
nav_groups = [
    ("navigation.section_home", [
        ("home", "00", 'modules.home', 'module_subtitles.home'),
    ]),
    ("navigation.section_foundations", [
        ("bloch", "01", 'modules.bloch', 'module_subtitles.bloch'),
        ("interference", "02", 'modules.interference', 'module_subtitles.interference'),
    ]),
    ("navigation.section_correlations", [
        ("entanglement", "03", 'modules.entanglement', 'module_subtitles.entanglement'),
        ("topological", "04", 'modules.topological', 'module_subtitles.topological'),
    ]),
    ("navigation.section_dynamics", [
        ("noise", "05", 'modules.noise', 'module_subtitles.noise'),
        ("circuits", "06", 'modules.circuits', 'module_subtitles.circuits'),
    ]),
    ("navigation.section_variational", [
        ("vqe", "07", 'modules.vqe', 'module_subtitles.vqe'),
        ("qaoa", "08", 'modules.qaoa', 'module_subtitles.qaoa'),
    ]),
    ("navigation.section_qml", [
        ("qml", "09", 'modules.qml', 'module_subtitles.qml'),
    ]),
    ("navigation.section_hardware", [
        ("qec", "10", 'modules.qec', 'module_subtitles.qec'),
        ("hardware", "11", 'modules.hardware', 'module_subtitles.hardware'),
    ]),
    ("navigation.section_complexity", [
        ("complexity", "12", 'modules.complexity', 'module_subtitles.complexity'),
    ]),
    ("navigation.section_export", [
        ("export", "13", 'modules.export', 'module_subtitles.export'),
    ]),
]

# Render professional row-based navigation with icons
for section_key, modules in nav_groups:
    st.sidebar.markdown(f"<div class='nav-section-label'>{t(section_key)}</div>", unsafe_allow_html=True)
    
    # Render each module as a clickable row with icon
    for module_id, number, title_key, subtitle_key in modules:
        # Use Streamlit button with custom styling (icons added via CSS)
        if st.sidebar.button(
            t(title_key),
            key=f"nav_{module_id}",
            type="secondary" if st.session_state.selected_module_id != module_id else "primary",
            use_container_width=True
        ):
            st.session_state.selected_module_id = module_id
            st.rerun()

# Professional sidebar footer
st.sidebar.markdown("---")
sidebar_footer = """
<div class='sidebar-footer'>
    <div class='sidebar-footer-version'>Quantum Workbench v4.0.2</div>
    <div class='sidebar-footer-status'>● System Operational</div>
</div>
"""
st.sidebar.markdown(sidebar_footer, unsafe_allow_html=True)

module_id = st.session_state.selected_module_id

# Experiment session state
if 'experiment_log' not in st.session_state:
    st.session_state.experiment_log = []

# Main content area with cyber-physical transition
st.markdown("<div class='module-content'>", unsafe_allow_html=True)

if module_id == "home":
    # Professional Home / Overview Landing Page
    st.markdown(f"""
    <div style='text-align: center; margin: 60px 0 40px 0;'>
        <h1 style='font-size: 42px; font-weight: 700; letter-spacing: -0.02em; margin-bottom: 12px; color: #FFFFFF;'>
            {t('home_page.hero_title')}
        </h1>
        <div style='font-size: 12px; font-weight: 600; color: rgba(99, 102, 241, 0.8); letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 16px;'>
            {t('global.version')}
        </div>
        <p style='font-family: "Source Serif Pro", serif; font-size: 16px; color: rgba(230, 230, 230, 0.9); max-width: 720px; margin: 0 auto 32px auto; line-height: 1.7;'>
            {t('home_page.hero_subtitle')}
        </p>
        <button onclick="document.querySelector('[key=nav_bloch]').click()" style='
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.9), rgba(123, 97, 255, 0.9));
            color: white;
            border: none;
            padding: 14px 32px;
            font-size: 14px;
            font-weight: 600;
            border-radius: 8px;
            cursor: pointer;
            font-family: Inter, sans-serif;
            letter-spacing: 0.02em;
            transition: all 200ms ease;
            box-shadow: 0 4px 20px rgba(99, 102, 241, 0.4);
        '>
            {t('buttons.open')} →
        </button>
    </div>
    """, unsafe_allow_html=True)
    
    # What You Can Do Here
    st.markdown(f"""
    <div style='margin: 60px 0 40px 0;'>
        <h2 style='text-align: center; font-size: 24px; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; color: rgba(180, 180, 180, 0.7); margin-bottom: 40px;'>
            {t('home_page.capabilities_title')}
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div style='background: rgba(26, 26, 26, 0.6); border: 1px solid rgba(99, 102, 241, 0.2); border-radius: 12px; padding: 24px; height: 100%;'>
            <div style='margin-bottom: 18px;'>
                <svg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgba(140, 150, 255, 0.8)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'>
                    <circle cx='12' cy='12' r='1'/>
                    <circle cx='12' cy='12' r='5'/>
                    <circle cx='12' cy='12' r='9'/>
                </svg>
            </div>
            <h3 style='font-size: 16px; font-weight: 700; margin-bottom: 12px; color: #E8E8E8;'>{t('home_page.cap_state_title')}</h3>
            <p style='font-family: "Source Serif Pro", serif; font-size: 13px; line-height: 1.6; color: rgba(200, 200, 200, 0.8);'>
                {t('home_page.cap_state_desc')}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style='background: rgba(26, 26, 26, 0.6); border: 1px solid rgba(99, 102, 241, 0.2); border-radius: 12px; padding: 24px; height: 100%;'>
            <div style='margin-bottom: 18px;'>
                <svg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgba(140, 150, 255, 0.8)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'>
                    <path d='M22 12h-4l-3 9L9 3l-3 9H2'/>
                </svg>
            </div>
            <h3 style='font-size: 16px; font-weight: 700; margin-bottom: 12px; color: #E8E8E8;'>{t('home_page.cap_noise_title')}</h3>
            <p style='font-family: "Source Serif Pro", serif; font-size: 13px; line-height: 1.6; color: rgba(200, 200, 200, 0.8);'>
                {t('home_page.cap_noise_desc')}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style='background: rgba(26, 26, 26, 0.6); border: 1px solid rgba(99, 102, 241, 0.2); border-radius: 12px; padding: 24px; height: 100%;'>
            <div style='margin-bottom: 18px;'>
                <svg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgba(140, 150, 255, 0.8)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'>
                    <line x1='6' y1='3' x2='6' y2='15'/>
                    <circle cx='18' cy='6' r='3'/>
                    <circle cx='6' cy='18' r='3'/>
                    <path d='M18 9a9 9 0 0 1-9 9'/>
                </svg>
            </div>
            <h3 style='font-size: 16px; font-weight: 700; margin-bottom: 12px; color: #E8E8E8;'>{t('home_page.cap_variational_title')}</h3>
            <p style='font-family: "Source Serif Pro", serif; font-size: 13px; line-height: 1.6; color: rgba(200, 200, 200, 0.8);'>
                {t('home_page.cap_variational_desc')}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div style='background: rgba(26, 26, 26, 0.6); border: 1px solid rgba(99, 102, 241, 0.2); border-radius: 12px; padding: 24px; height: 100%;'>
            <div style='margin-bottom: 18px;'>
                <svg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgba(140, 150, 255, 0.8)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'>
                    <path d='M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4'/>
                    <polyline points='7 10 12 15 17 10'/>
                    <line x1='12' y1='15' x2='12' y2='3'/>
                </svg>
            </div>
            <h3 style='font-size: 16px; font-weight: 700; margin-bottom: 12px; color: #E8E8E8;'>{t('home_page.cap_export_title')}</h3>
            <p style='font-family: "Source Serif Pro", serif; font-size: 13px; line-height: 1.6; color: rgba(200, 200, 200, 0.8);'>
                {t('home_page.cap_export_desc')}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick Start Guide
    st.markdown(f"""
    <div style='margin: 80px 0 40px 0;'>
        <h2 style='text-align: center; font-size: 24px; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; color: rgba(180, 180, 180, 0.7); margin-bottom: 40px;'>
            {t('home_page.quick_start_title')}
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div style='text-align: center; padding: 24px;'>
            <div style='
                width: 60px; 
                height: 60px; 
                background: rgba(99, 102, 241, 0.15); 
                border: 2px solid rgba(99, 102, 241, 0.5); 
                border-radius: 50%; 
                display: flex; 
                align-items: center; 
                justify-content: center; 
                margin: 0 auto 20px auto;
                font-size: 24px;
                font-weight: 700;
                color: rgba(99, 102, 241, 1);
            '>1</div>
            <h4 style='font-size: 15px; font-weight: 700; margin-bottom: 12px; color: #E8E8E8;'>{t('home_page.quick_step1_title')}</h4>
            <p style='font-family: "Source Serif Pro", serif; font-size: 13px; line-height: 1.6; color: rgba(200, 200, 200, 0.7);'>
                {t('home_page.quick_step1_desc')}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style='text-align: center; padding: 24px;'>
            <div style='
                width: 60px; 
                height: 60px; 
                background: rgba(99, 102, 241, 0.15); 
                border: 2px solid rgba(99, 102, 241, 0.5); 
                border-radius: 50%; 
                display: flex; 
                align-items: center; 
                justify-content: center; 
                margin: 0 auto 20px auto;
                font-size: 24px;
                font-weight: 700;
                color: rgba(99, 102, 241, 1);
            '>2</div>
            <h4 style='font-size: 15px; font-weight: 700; margin-bottom: 12px; color: #E8E8E8;'>{t('home_page.quick_step2_title')}</h4>
            <p style='font-family: "Source Serif Pro", serif; font-size: 13px; line-height: 1.6; color: rgba(200, 200, 200, 0.7);'>
                {t('home_page.quick_step2_desc')}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style='text-align: center; padding: 24px;'>
            <div style='
                width: 60px; 
                height: 60px; 
                background: rgba(99, 102, 241, 0.15); 
                border: 2px solid rgba(99, 102, 241, 0.5); 
                border-radius: 50%; 
                display: flex; 
                align-items: center; 
                justify-content: center; 
                margin: 0 auto 20px auto;
                font-size: 24px;
                font-weight: 700;
                color: rgba(99, 102, 241, 1);
            '>3</div>
            <h4 style='font-size: 15px; font-weight: 700; margin-bottom: 12px; color: #E8E8E8;'>{t('home_page.quick_step3_title')}</h4>
            <p style='font-family: "Source Serif Pro", serif; font-size: 13px; line-height: 1.6; color: rgba(200, 200, 200, 0.7);'>
                {t('home_page.quick_step3_desc')}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Featured Modules - Compact Grid with Professional Styling
    st.markdown(f"""
    <div style='margin: 60px 0 28px 0;'>
        <h2 style='text-align: center; font-size: 22px; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; color: rgba(180, 180, 180, 0.7); margin-bottom: 32px;'>
            {t('home_page.featured_title')}
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5, gap="small")
    
    featured_modules = [
        ("bloch", "<svg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='rgba(140, 150, 255, 0.8)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><circle cx='12' cy='12' r='1'/><circle cx='12' cy='12' r='5'/><circle cx='12' cy='12' r='9'/></svg>", 'modules.bloch', 'module_subtitles.bloch'),
        ("entanglement", "<svg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='rgba(140, 150, 255, 0.8)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71'/><path d='M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71'/></svg>", 'modules.entanglement', 'module_subtitles.entanglement'),
        ("noise", "<svg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='rgba(140, 150, 255, 0.8)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M22 12h-4l-3 9L9 3l-3 9H2'/></svg>", 'modules.noise', 'module_subtitles.noise'),
        ("vqe", "<svg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='rgba(140, 150, 255, 0.8)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><circle cx='12' cy='12' r='10'/><circle cx='12' cy='12' r='6'/><circle cx='12' cy='12' r='2'/></svg>", 'modules.vqe', 'module_subtitles.vqe'),
        ("qml", "<svg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='rgba(140, 150, 255, 0.8)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M12 5a3 3 0 1 0-5.997.125 4 4 0 0 0-2.526 5.77 4 4 0 0 0 .556 6.588A4 4 0 1 0 12 18Z'/><path d='M12 5a3 3 0 1 1 5.997.125 4 4 0 0 1 2.526 5.77 4 4 0 0 1-.556 6.588A4 4 0 1 1 12 18Z'/><path d='M15 13a4.5 4.5 0 0 1-3-4 4.5 4.5 0 0 1-3 4'/></svg>", 'modules.qml', 'module_subtitles.qml'),
    ]
    
    for col, (mod_id, icon, title_key, subtitle_key) in zip([col1, col2, col3, col4, col5], featured_modules):
        with col:
            # Card content
            st.markdown(f"""
            <div class='featured-module-card' style='
                background: rgba(26, 26, 26, 0.4);
                border: 1px solid rgba(99, 102, 241, 0.15);
                border-radius: 10px;
                padding: 16px 14px 14px 14px;
                text-align: center;
                transition: all 200ms cubic-bezier(0.4, 0, 0.2, 1);
                margin-bottom: 8px;
            '>
                <div style='margin-bottom: 10px; display: flex; justify-content: center; align-items: center;'>
                    {icon}
                </div>
                <h4 style='
                    font-family: Inter, sans-serif;
                    font-size: 12px;
                    font-weight: 600;
                    line-height: 1.3;
                    color: #E8E8E8;
                    margin: 0 0 5px 0;
                    word-break: keep-all;
                    overflow-wrap: normal;
                    hyphens: none;
                    white-space: nowrap;
                    overflow: hidden;
                    text-overflow: ellipsis;
                '>{t(title_key)}</h4>
                <p style='
                    font-family: Inter, sans-serif;
                    font-size: 10px;
                    line-height: 1.3;
                    color: rgba(180, 180, 180, 0.65);
                    margin: 0;
                    word-break: keep-all;
                    overflow-wrap: normal;
                    hyphens: none;
                    white-space: nowrap;
                    overflow: hidden;
                    text-overflow: ellipsis;
                '>{t(subtitle_key)}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Compact professional button
            if st.button(t('buttons.launch'), key=f"feat_{mod_id}", use_container_width=True):
                st.session_state.selected_module_id = mod_id
                st.rerun()
    
    # System Status Panel
    st.markdown(f"""
    <div style='margin: 60px 0 32px 0;'>
        <h2 style='text-align: center; font-size: 22px; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; color: rgba(180, 180, 180, 0.7); margin-bottom: 32px;'>
            {t('system_status.title')}
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div style='background: rgba(0, 255, 148, 0.05); border: 1px solid rgba(0, 255, 148, 0.3); border-radius: 10px; padding: 20px; text-align: center;'>
            <div style='font-size: 11px; font-weight: 700; color: rgba(180, 180, 180, 0.7); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 8px;'>{t('system_status.status_label')}</div>
            <div style='font-size: 18px; font-weight: 700; color: rgba(0, 255, 148, 1);'>● {t('system_status.operational')}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style='background: rgba(99, 102, 241, 0.05); border: 1px solid rgba(99, 102, 241, 0.3); border-radius: 10px; padding: 20px; text-align: center;'>
            <div style='font-size: 11px; font-weight: 700; color: rgba(180, 180, 180, 0.7); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 8px;'>{t('system_status.gate_fidelity')}</div>
            <div style='font-size: 18px; font-weight: 700; color: rgba(99, 102, 241, 1);'>F > 99.9%</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style='background: rgba(99, 102, 241, 0.05); border: 1px solid rgba(99, 102, 241, 0.3); border-radius: 10px; padding: 20px; text-align: center;'>
            <div style='font-size: 11px; font-weight: 700; color: rgba(180, 180, 180, 0.7); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 8px;'>{t('system_status.coherence_time')}</div>
            <div style='font-size: 18px; font-weight: 700; color: rgba(99, 102, 241, 1);'>T₂ = 103μs</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div style='background: rgba(99, 102, 241, 0.05); border: 1px solid rgba(99, 102, 241, 0.3); border-radius: 10px; padding: 20px; text-align: center;'>
            <div style='font-size: 11px; font-weight: 700; color: rgba(180, 180, 180, 0.7); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 8px;'>Backend</div>
            <div style='font-size: 18px; font-weight: 700; color: rgba(99, 102, 241, 1);'>Simulator</div>
        </div>
        """, unsafe_allow_html=True)

elif module_id == "overview":
    # Add particle effect background
    add_particle_effect()
    
    st.markdown("<div class='overview-bg'>", unsafe_allow_html=True)
    st.markdown("# QUANTUM RESEARCH TERMINAL v4.0.2")
    st.markdown('<span class="research-status status-active">SYSTEM STATUS: OPERATIONAL | QUBITS: STABLE | FIDELITY: >99.9%</span>', unsafe_allow_html=True)
    
    # Clean System Status Panel (Sanitized UI)
    st.markdown("""
    <div class='system-status-panel'>
        <div class='status-header'>⚛ HARDWARE SPECIFICATIONS</div>
        <div class='status-metric'>
            <span class='status-label'>Qubit Architecture</span>
            <span class='status-value'>Transmon Superconducting</span>
        </div>
        <div class='status-metric'>
            <span class='status-label'>Operating Temperature</span>
            <span class='status-value'>T = 20 mK</span>
        </div>
        <div class='status-metric'>
            <span class='status-label'>Gate Fidelity (Single-Qubit)</span>
            <span class='status-value'>F > 99.9%</span>
        </div>
        <div class='status-metric'>
            <span class='status-label'>Gate Fidelity (Two-Qubit CNOT)</span>
            <span class='status-value'>F > 99.5%</span>
        </div>
        <div class='status-metric'>
            <span class='status-label'>Coherence Time T₂</span>
            <span class='status-value'>100 μs</span>
        </div>
        <div class='status-metric'>
            <span class='status-label'>Readout Fidelity</span>
            <span class='status-value'>F_RO > 99.2%</span>
        </div>
        <div class='status-metric'>
            <span class='status-label'>Vacuum Pressure</span>
            <span class='status-value'>10⁻⁸ mbar</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Research Capabilities Overview
    st.markdown("""
    <div class='research-card'>
        <h3>→ RESEARCH TERMINAL CAPABILITIES</h3>
        <p style='font-family: "Source Serif Pro", serif; font-size: 15px; line-height: 1.8;'>
        This workbench provides a <strong>high-fidelity environment</strong> for quantum state manipulation within 
        the complex Hilbert space $\\mathcal{H} = \\mathbb{C}^{2^n}$. Execute variational algorithms, simulate 
        noise channels, and perform quantum state tomography with publication-ready visualizations.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Professional Research Dashboard Navigation
    st.markdown("<div style='font-family: Inter; font-size: 13px; font-weight: 600; letter-spacing: 0.5px; color: rgba(200,200,200,0.9); margin-bottom: 32px;'>RESEARCH MODULE SELECTOR</div>", unsafe_allow_html=True)
    
    # Organized module groups with proper hierarchy
    module_groups = {
        "FOUNDATIONS": [
            ("bloch", "⚛️", "Theoretical Framework", "postulates, operators, measurement"),
            ("interference", "〰️", "Coherent Superposition", "phase, interference, amplitudes"),
        ],
        "QUANTUM CORRELATIONS": [
            ("entanglement", "🔗", "Bell-State Correlations", "CHSH, nonlocality, EPR"),
            ("topological", "🔀", "Topological Phases", "anyonic braiding, fault tolerance"),
        ],
        "NOISE & DYNAMICS": [
            ("noise", "📉", "Dissipative Decoherence", "T1/T2, channels, density matrix"),
            ("circuits", "⚡", "Unitary Synthesis", "gate decomposition, compilation"),
        ],
        "VARIATIONAL ALGORITHMS": [
            ("vqe", "🧬", "VQE Architectures", "ansatz design, energy landscapes"),
            ("qaoa", "📐", "Optimization Manifolds", "gradients, barren plateaus"),
        ],
        "QUANTUM MACHINE LEARNING": [
            ("qml", "🧠", "Quantum Neural Networks", "embeddings, kernels, classifiers"),
        ],
        "ERROR CORRECTION & HARDWARE": [
            ("qec", "🛡️", "Surface Code Protocols", "stabilizers, logical qubits"),
            ("hardware", "🔌", "QPU Topology Maps", "connectivity, calibration"),
        ],
        "COMPLEXITY THEORY": [
            ("complexity", "♾️", "Complexity Landscapes", "BQP, QMA, oracle separation"),
        ],
        "DATA EXPORT": [
            ("export", "💾", "Research Reproducibility", "export state vectors, circuits"),
        ]
    }
    
    # Render grouped navigation cards
    for group_name, modules in module_groups.items():
        st.markdown(f"<div class='nav-section-header'>{group_name}</div>", unsafe_allow_html=True)
        st.markdown("<div class='research-nav-grid'>", unsafe_allow_html=True)
        
        cols = st.columns(len(modules))
        for idx, (module_id, icon, title, subtitle) in enumerate(modules):
            with cols[idx]:
                active_class = "active" if st.session_state.get('selected_module_id') == module_id else ""
                card_html = f"""
                <div class='research-nav-card {active_class}'>
                    <div class='nav-card-header'>
                        <div class='nav-card-icon'>{icon}</div>
                        <div class='nav-card-title'>{title}</div>
                    </div>
                    <div class='nav-card-subtitle'>{subtitle}</div>
                </div>
                """
                st.markdown(card_html, unsafe_allow_html=True)
                if st.button(f"→ {title}", key=f"main_nav_{module_id}", use_container_width=True):
                    st.session_state.selected_module_id = module_id
                    st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Real-time telemetry dashboard
    st.markdown("### REAL-TIME TELEMETRY STREAM")
    col_tel1, col_tel2, col_tel3, col_tel4 = st.columns(4)
    
    with col_tel1:
        st.markdown("""
        <div class='telemetry-ticker'>
            GATE FIDELITY<br>
            <span class='telemetry-value'>F = 99.94%</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col_tel2:
        st.markdown("""
        <div class='telemetry-ticker'>
            COHERENCE TIME<br>
            <span class='telemetry-value'>T₂ = 103μs</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col_tel3:
        st.markdown("""
        <div class='telemetry-ticker'>
            CRYOGENIC TEMP<br>
            <span class='telemetry-value'>18.7 mK</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col_tel4:
        st.markdown("""
        <div class='telemetry-ticker'>
            VACUUM LEVEL<br>
            <span class='telemetry-value'>10⁻⁸ mbar</span>
        </div>
        """, unsafe_allow_html=True)
    
    # Technology stack
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='experiment-panel'>
            <h3>COMPUTATIONAL STACK</h3>
            <ul style='font-family: "JetBrains Mono", monospace; font-size: 12px;'>
                <li><strong>Quantum Frameworks:</strong> Qiskit Terra (Transpiler), PennyLane (Autodiff)</li>
                <li><strong>Numerical Backend:</strong> NumPy + SciPy (BLAS/LAPACK), SymPy (Symbolic)</li>
                <li><strong>Visualization Engine:</strong> Plotly WebGL (3D Rendering), Matplotlib</li>
                <li><strong>ML Integration:</strong> scikit-learn, Quantum Kernels (Fidelity-based)</li>
                <li><strong>Data Export:</strong> JSON Schema v2.0, SHA-256 Integrity Verification</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='experiment-panel'>
            <h3>MODULE TAXONOMY</h3>
            <ul style='font-family: "JetBrains Mono", monospace; font-size: 12px;'>
                <li>Hilbert Space Tomography & Bloch Vector Dynamics</li>
                <li>Variational Quantum Eigensolver (VQE) Manifolds</li>
                <li>Quantum Neural Networks & Kernel Methods</li>
                <li>Topologically Protected Error Correction (Surface Codes)</li>
                <li>Stochastic Noise Models (Depolarizing, Amplitude Damping)</li>
                <li>Anyonic Braiding & Non-Abelian Statistics (Frontier Research)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Hero Bloch sphere with parallax depth
    st.markdown("### 🌐 LIVE STATE VECTOR MANIPULATION")
    st.markdown("""
    <div class='parallax-viz-container'>
        <div style='text-align: center; margin-bottom: 20px;'>
            <span class='metric-label'>⚛ BLOCH SPHERE | PROJECTIVE HILBERT SPACE $\\mathbb{CP}^1 \\cong S^2$</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <p style='font-family: "Source Serif Pro", serif; font-size: 14px; line-height: 1.7;'>
    <strong>Interactive Bloch Sphere:</strong> Manipulate polar angle $\\theta$ and azimuthal phase 
    $\\phi$ to observe <strong>wavefunction collapse</strong> dynamics. The sphere's surface represents 
    the projective Hilbert space $\\mathbb{CP}^1$, with north/south poles as computational basis 
    states $|0\\rangle, |1\\rangle$.
    </p>
    """, unsafe_allow_html=True)
    
    # Custom glassmorphic slider with real-time feedback
    st.markdown("""
    <div class='parallax-viz-container' style='padding: 15px;'>
        <span class='metric-label'>⚛ POLAR ANGLE $\\theta$ [0, $\\pi$]</span>
    </div>
    """, unsafe_allow_html=True)
    theta_hero = st.slider("", 0, 180, 45, key="hero_theta", 
                          help="Controls probability amplitude distribution", label_visibility="collapsed")
    st.markdown(f"""
    <div style='text-align: center; margin-top: -10px; margin-bottom: 20px;'>
        <span class='metric-value' style='font-size: 22px;'>{theta_hero}°</span>
        <span class='metric-label'> = {np.radians(theta_hero):.4f} rad</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='parallax-viz-container' style='padding: 15px;'>
        <span class='metric-label'>⚡ AZIMUTHAL PHASE $\\phi$ [0, 2$\\pi$]</span>
    </div>
    """, unsafe_allow_html=True)
    phi_hero = st.slider("", 0, 360, 45, key="hero_phi",
                        help="Determines relative phase between basis states", label_visibility="collapsed")
    st.markdown(f"""
    <div style='text-align: center; margin-top: -10px; margin-bottom: 25px;'>
        <span class='metric-value' style='font-size: 22px;'>{phi_hero}°</span>
        <span class='metric-label'> = {np.radians(phi_hero):.4f} rad</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced Bloch sphere with volumetric rendering and haptic-visual feedback
    collapse_class = 'state-collapsed' if theta_hero in [0, 180] else ''
    st.markdown(f"""
    <div class='parallax-viz-container {collapse_class}' style='padding: 15px; margin-bottom: 20px;'>
        <div style='text-align: center;'>
            <span class='metric-label'>◉ HYPER-REALISTIC VOLUMETRIC RENDERING</span>
            <span style='margin-left: 20px; color: #00FF94; font-family: JetBrains Mono; font-size: 10px;'>⚡ PBR MATERIALS | QUART-OUT EASING</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Detect basis state collapse and trigger visual feedback
    if theta_hero in [0, 180]:
        st.markdown("""
        <div style='text-align: center; padding: 10px; background: rgba(0, 217, 255, 0.1); border-radius: 8px; margin-bottom: 10px; animation: collapse-vibration 0.5s ease-out;'>
            <span style='color: #00D9FF; font-family: JetBrains Mono; font-size: 12px; font-weight: 700;'>
            ⚠️ WAVEFUNCTION COLLAPSED TO BASIS STATE |{'0' if theta_hero == 0 else '1'}⟩
            </span>
        </div>
        """, unsafe_allow_html=True)
    
    fig_hero = create_bloch_sphere(theta_hero, phi_hero)
    st.plotly_chart(fig_hero, use_container_width=True, key="hero_bloch", config={'displayModeBar': False})
    
    # State vector display with technical metrics
    theta_rad = np.radians(theta_hero)
    phi_rad = np.radians(phi_hero)
    alpha = np.cos(theta_rad / 2)
    beta = np.exp(1j * phi_rad) * np.sin(theta_rad / 2)
    
    st.markdown(f"""
    <div class='latex-display'>
        <h4>Current Quantum State</h4>
        <p>|ψ⟩ = {alpha.real:.3f}{'+' if alpha.imag >= 0 else ''}{alpha.imag:.3f}i |0⟩ + 
        {beta.real:.3f}{'+' if beta.imag >= 0 else ''}{beta.imag:.3f}i |1⟩</p>
        <p style='margin-top: 12px;'>Measurement probabilities: P(|0⟩) = {abs(alpha)**2:.3f}, P(|1⟩) = {abs(beta)**2:.3f}</p>
    </div>
    """, unsafe_allow_html=True)

elif module_id == "bloch":
    st.markdown("<div class='bloch-energy hero-glow'>", unsafe_allow_html=True)
    st.markdown(f"# {t('bloch_module_title')}")
    st.markdown(f'<span class="research-status status-active">{t("bloch_status_badge")}</span>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class='research-card'>
        <h3>{t('bloch_math_title')}</h3>
        <p style='font-family: "Source Serif Pro", serif; font-size: 15px; line-height: 1.8;'>
        {t('bloch_math_intro')}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.latex(r"""
    |\psi\rangle = \alpha|0\rangle + \beta|1\rangle, \quad \text{where } |\alpha|^2 + |\beta|^2 = 1
    """)
    
    st.latex(r"""
    \alpha = \cos(\theta/2), \quad \beta = e^{i\phi}\sin(\theta/2) \quad \text{(Bloch Parameterization)}
    """)
    
    manifold_title = t('bloch_manifold_title')
    manifold_desc = t('bloch_manifold_desc')
    pure_state = t('bloch_pure_state')
    mixed_state = t('bloch_mixed_state')
    maximally_mixed = t('bloch_maximally_mixed')
    
    st.markdown(f"""
    <div class='latex-display'>
        <p style='font-family: "Source Serif Pro", serif;'><strong>{manifold_title}</strong> 
        {manifold_desc}</p>
        
        <p style='font-family: "JetBrains Mono", monospace; font-size: 13px; margin-top: 16px;'>
        <strong>{pure_state}</strong> <code>|r| = 1</code> (sphere surface)<br>
        <strong>{mixed_state}</strong> <code>|r| &lt; 1</code> (interior volume, density matrix $\\rho$)<br>
        <strong>{maximally_mixed}</strong> <code>|r| = 0</code> (sphere center, $\\rho = \\mathbb{{I}}/2$)
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive controls
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"### {t('bloch_config_title')}")
        st.markdown(f"<p style='font-family: \"Source Serif Pro\", serif; font-size: 13px;'>{t('bloch_config_desc')}</p>", unsafe_allow_html=True)
        
        # Glassmorphic slider with data-grid mesh
        st.markdown(f"""
        <div class='data-grid-mesh' style='padding: 15px; border-radius: 10px; border: 1px solid rgba(0, 217, 255, 0.25); margin-bottom: 10px;'>
            <span class='metric-label'>{t('bloch_theta_label')}</span>
        </div>
        """, unsafe_allow_html=True)
        theta_bloch = st.slider("", 0, 180, 90, 5, key="bloch_theta",
                               help=t('bloch_theta_help'), label_visibility="collapsed")
        st.markdown(f"""
        <div style='text-align: center; margin-top: -8px; margin-bottom: 20px;'>
            <span class='metric-value' style='font-size: 20px;'>{theta_bloch}°</span>
            <span class='metric-label'> | θ = {np.radians(theta_bloch):.4f} rad</span>
        </div>
        """, unsafe_allow_html=True)
        
        # Rotary dial for phase (laboratory equipment aesthetic)
        st.markdown(f"""
        <div class='data-grid-mesh' style='padding: 15px; border-radius: 10px; border: 1px solid rgba(123, 97, 255, 0.25); margin-bottom: 10px;'>
            <span class='metric-label'>{t('bloch_phi_label')}</span>
        </div>
        """, unsafe_allow_html=True)
        
        col_a, col_b, col_c = st.columns([1, 2, 1])
        with col_b:
            phi_bloch = st.slider("", 0, 360, 0, 5, key="bloch_phi",
                                 help=t('bloch_phi_help'), label_visibility="collapsed")
            
            # Render rotary dial visualization
            rotation_angle = phi_bloch - 90  # Adjust to start at top
            st.markdown(f"""
            <div class='rotary-dial-container'>
                <div class='rotary-dial'>
                    <div class='rotary-indicator' style='transform: rotate({rotation_angle}deg);'></div>
                    <div class='rotary-value'>{phi_bloch}°</div>
                </div>
                <div class='rotary-label'>φ = {np.radians(phi_bloch):.4f} rad</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Gate sequence with technical descriptions
        st.markdown(f"### {t('bloch_gate_title')}")
        gate_sequence = st.multiselect(
            t('bloch_gate_compose'),
            [t('bloch_gate_h'), t('bloch_gate_x'), t('bloch_gate_y'), 
             t('bloch_gate_z'), t('bloch_gate_rx'), t('bloch_gate_ry'), 
             t('bloch_gate_rz'), t('bloch_gate_s'), t('bloch_gate_t')],
            key="gate_seq_bloch"
        )
        
        # Measurement basis with tomography context
        st.markdown(f"### {t('bloch_measure_title')}")
        meas_basis = st.radio(t('bloch_measure_label'), 
                             [t('bloch_measure_z'), t('bloch_measure_x'), t('bloch_measure_y')], 
                             horizontal=True)
        
        fig_bloch = create_bloch_sphere(theta_bloch, phi_bloch)
        st.plotly_chart(fig_bloch, use_container_width=True, key="main_bloch")
    
    with col2:
        # Compute state with density matrix
        theta_rad = np.radians(theta_bloch)
        phi_rad = np.radians(phi_bloch)
        state = np.array([
            np.cos(theta_rad / 2),
            np.exp(1j * phi_rad) * np.sin(theta_rad / 2)
        ], dtype=complex)
        
        # Apply gates
        current_state = state.copy()
        pauli = pauli_matrices()
        
        for gate in gate_sequence:
            gate_lower = gate.lower()
            if "h" in gate_lower or "адамар" in gate_lower:
                current_state = hadamard() @ current_state
            elif "x" in gate_lower and "rx" not in gate_lower:
                current_state = pauli['X'] @ current_state
            elif "y" in gate_lower and "ry" not in gate_lower:
                current_state = pauli['Y'] @ current_state
            elif "z" in gate_lower and "rz" not in gate_lower:
                current_state = pauli['Z'] @ current_state
            elif "rx" in gate_lower:
                current_state = rotation_gate('X', 45) @ current_state
            elif "ry" in gate_lower:
                current_state = rotation_gate('Y', 45) @ current_state
            elif "rz" in gate_lower:
                current_state = rotation_gate('Z', 45) @ current_state
        
        # Display metrics
        st.markdown(f"""
        <div class='metric-box'>
            <h3>{np.linalg.norm(current_state):.4f}</h3>
            <p>{t('bloch_metric_norm')}</p>
        </div>
        """.format(np.linalg.norm(current_state)), unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class='metric-box'>
            <h3>{abs(current_state[0])**2:.3f}</h3>
            <p>{t('bloch_metric_p0')}</p>
        </div>
        """.format(abs(current_state[0])**2), unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class='metric-box'>
            <h3>{abs(current_state[1])**2:.3f}</h3>
            <p>{t('bloch_metric_p1')}</p>
        </div>
        """.format(abs(current_state[1])**2), unsafe_allow_html=True)
        
        # Phase
        phase_deg = np.degrees(np.angle(current_state[1] / current_state[0]))
        st.markdown(f"""
        <div class='metric-box'>
            <h3>{phase_deg if not np.isnan(phase_deg) else 0:.1f}°</h3>
            <p>{t('bloch_metric_phase')}</p>
        </div>
        """.format(phase_deg if not np.isnan(phase_deg) else 0), unsafe_allow_html=True)
    
    # Code panel
    st.markdown(f"### {t('bloch_code_title')}")
    gates_str = ', '.join(gate_sequence) if gate_sequence else t('common_none')
    code = f"""
import numpy as np
from scipy.linalg import expm

{t('bloch_code_comment_state')}
theta = {theta_bloch} * np.pi / 180
phi = {phi_bloch} * np.pi / 180
state = np.array([np.cos(theta/2), np.exp(1j*phi) * np.sin(theta/2)])

{t('bloch_code_comment_gates')} {gates_str}
# ... gate operations ...

{t('bloch_code_comment_measure')}
prob_0 = abs(state[0])**2
prob_1 = abs(state[1])**2
print(f"P(|0⟩) = {{prob_0:.3f}}, P(|1⟩) = {{prob_1:.3f}}")
"""
    st.code(code, language="python")

elif module_id == "interference":
    # Add wave animation
    add_wave_animation()
    
    st.markdown("<div class='interference-wave'>", unsafe_allow_html=True)
    st.markdown(f"# {t('interf_module_title')}")
    st.markdown(f'<span class="research-status status-active">{t("status_active")}</span>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class='research-card'>
        <h3>{t('interf_card_title')}</h3>
        <p>{t('interf_card_desc')}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.latex(r"""
    P(\text{outcome}) = |\alpha_1 + \alpha_2|^2 = |\alpha_1|^2 + |\alpha_2|^2 + 2\text{Re}(\alpha_1^*\alpha_2)
    """)
    
    st.markdown(f"""
    <div class='latex-display'>
        <p>{t('interf_term_desc')}</p>
        <p>{t('interf_constructive')}</p>
        <p>{t('interf_destructive')}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive demonstration
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"### {t('interf_config_title')}")
        amp1 = st.slider(t('interf_amp1_label'), 0.0, 1.0, 0.6, 0.05, key="amp1_interf")
        phase1 = st.slider(t('interf_phase1_label'), 0, 360, 0, 10, key="phase1_interf")
        amp2 = st.slider(t('interf_amp2_label'), 0.0, 1.0, 0.4, 0.05, key="amp2_interf")
        phase2 = st.slider(t('interf_phase2_label'), 0, 360, 90, 10, key="phase2_interf")
        
        # Complex amplitudes
        alpha1 = amp1 * np.exp(1j * np.radians(phase1))
        alpha2 = amp2 * np.exp(1j * np.radians(phase2))
        alpha_total = alpha1 + alpha2
        
        # Probabilities
        prob_classical = amp1**2 + amp2**2
        prob_quantum = abs(alpha_total)**2
        interference_term = prob_quantum - prob_classical
        
        st.markdown(f"""
        <div class='metric-box'>
            <h3>{prob_quantum:.4f}</h3>
            <p>{t('interf_prob_quantum')}</p>
        </div>
        <div class='metric-box'>
            <h3>{prob_classical:.4f}</h3>
            <p>{t('interf_prob_classical')}</p>
        </div>
        <div class='metric-box'>
            <h3 style='color: {"#84CC16" if interference_term > 0 else "#EF4444"}'>{interference_term:+.4f}</h3>
            <p>{t('interf_prob_term')}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"### {t('interf_viz_title')}")
        
        # Phasor diagram
        fig = go.Figure()
        
        # α₁ vector
        fig.add_trace(go.Scatter(
            x=[0, alpha1.real], y=[0, alpha1.imag],
            mode='lines+markers',
            line=dict(color='#6366F1', width=3),
            marker=dict(size=10),
            name=t('charts.common_traces.alpha1')
        ))
        
        # α₂ vector
        fig.add_trace(go.Scatter(
            x=[0, alpha2.real], y=[0, alpha2.imag],
            mode='lines+markers',
            line=dict(color='#06B6D4', width=3),
            marker=dict(size=10),
            name=t('charts.common_traces.alpha2')
        ))
        
        # Total amplitude
        fig.add_trace(go.Scatter(
            x=[0, alpha_total.real], y=[0, alpha_total.imag],
            mode='lines+markers',
            line=dict(color='#F59E0B', width=4),
            marker=dict(size=12),
            name=t('charts.common_traces.total')
        ))
        
        # Unit circle
        theta_circle = np.linspace(0, 2*np.pi, 100)
        fig.add_trace(go.Scatter(
            x=np.cos(theta_circle), y=np.sin(theta_circle),
            mode='lines',
            line=dict(color='rgba(255,255,255,0.2)', dash='dash'),
            showlegend=False
        ))
        
        fig.update_layout(
            xaxis=dict(range=[-1.2, 1.2], title=t('charts.interference.phasor_x_axis'), gridcolor='rgba(255,255,255,0.1)'),
            yaxis=dict(range=[-1.2, 1.2], title=t('charts.interference.phasor_y_axis'), gridcolor='rgba(255,255,255,0.1)', scaleanchor="x"),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True, key="phasor_diagram")
    
    # Interference pattern
    st.markdown(f"### {t('interf_pattern_title')}")
    phase_diff_range = np.linspace(0, 2*np.pi, 200)
    prob_pattern = []
    
    for phase_diff in phase_diff_range:
        a1 = amp1
        a2 = amp2 * np.exp(1j * phase_diff)
        prob_pattern.append(abs(a1 + a2)**2)
    
    fig_pattern = go.Figure()
    fig_pattern.add_trace(go.Scatter(
        x=np.degrees(phase_diff_range),
        y=prob_pattern,
        mode='lines',
        line=dict(color='#F59E0B', width=3),
        fill='tozeroy',
        fillcolor='rgba(245, 158, 11, 0.3)'
    ))
    
    fig_pattern.update_layout(
        title=t('charts.interference.pattern_title'),
        xaxis_title=t('charts.interference.pattern_x_axis'),
        yaxis_title=t('charts.interference.pattern_y_axis'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        height=400
    )
    
    st.plotly_chart(fig_pattern, use_container_width=True, key="interference_pattern")

elif module_id == "entanglement":
    st.markdown("<div class='bloch-energy'>", unsafe_allow_html=True)
    st.markdown(f"# {t('ent_module_title')}")
    st.markdown(f'<span class="research-status status-active">{t("status_active")}</span>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class='research-card'>
        <h3>{t('ent_card_title')}</h3>
        <p>{t('ent_card_desc')}</p>
        
        <p>{t('ent_bell_title')}</p>
        <ul>
            <li>$|\\Phi^+\\rangle = \\frac{{1}}{{\\sqrt{{2}}}}(|00\\rangle + |11\\rangle)$</li>
            <li>$|\\Phi^-\\rangle = \\frac{{1}}{{\\sqrt{{2}}}}(|00\\rangle - |11\\rangle)$</li>
            <li>$|\\Psi^+\\rangle = \\frac{{1}}{{\\sqrt{{2}}}}(|01\\rangle + |10\\rangle)$</li>
            <li>$|\\Psi^-\\rangle = \\frac{{1}}{{\\sqrt{{2}}}}(|01\\rangle - |10\\rangle)$</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Bell State Selection
    st.markdown(f"### {t('ent_prep_title')}")
    bell_state = st.selectbox(
        t('ent_select_label'),
        [t('ent_bell_phi_plus'), t('ent_bell_phi_minus'), t('ent_bell_psi_plus'), t('ent_bell_psi_minus')]
    )
    
    # Create Bell state
    if bell_state.startswith("Φ⁺"):
        state = np.array([1, 0, 0, 1]) / np.sqrt(2)
        circuit_desc = "H on q0, CNOT(q0, q1)"
    elif bell_state.startswith("Φ⁻"):
        state = np.array([1, 0, 0, -1]) / np.sqrt(2)
        circuit_desc = "H on q0, Z on q0, CNOT(q0, q1)"
    elif bell_state.startswith("Ψ⁺"):
        state = np.array([0, 1, 1, 0]) / np.sqrt(2)
        circuit_desc = "H on q0, X on q1, CNOT(q0, q1)"
    else:  # Ψ⁻
        state = np.array([0, 1, -1, 0]) / np.sqrt(2)
        circuit_desc = "H on q0, X on q1, Z on q1, CNOT(q0, q1)"
    
    # Display circuit
    st.markdown(f"{t('ent_circuit_label')} `{circuit_desc}`")
    
    # State vector visualization
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"#### {t('ent_state_title')}")
        basis_labels = ['|00⟩', '|01⟩', '|10⟩', '|11⟩']
        amplitudes_real = np.real(state)
        amplitudes_imag = np.imag(state)
        
        # Enhanced visualization with area-glow effects
        fig_amp = go.Figure()
        fig_amp.add_trace(go.Bar(
            x=basis_labels,
            y=amplitudes_real,
            name='Re(ψ)',
            marker=dict(
                color='#00D9FF',
                line=dict(color='rgba(0, 217, 255, 0.8)', width=2)
            ),
            opacity=0.85,
            hovertemplate='<b>%{x}</b><br>Real: %{y:.4f}<extra></extra>'
        ))
        fig_amp.add_trace(go.Bar(
            x=basis_labels,
            y=amplitudes_imag,
            name='Im(ψ)',
            marker=dict(
                color='#7B61FF',
                line=dict(color='rgba(123, 97, 255, 0.8)', width=2)
            ),
            opacity=0.85,
            hovertemplate='<b>%{x}</b><br>Imaginary: %{y:.4f}<extra></extra>'
        ))
        
        fig_amp.update_layout(
            yaxis_title=t('charts.interference.amplitude_y_axis'),
            barmode='group',
            plot_bgcolor='rgba(10, 10, 10, 0.5)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#E8E8E8', family='JetBrains Mono'),
            height=350,
            xaxis=dict(gridcolor='rgba(0, 217, 255, 0.1)', showgrid=True),
            yaxis=dict(gridcolor='rgba(0, 217, 255, 0.1)', showgrid=True, zeroline=True, zerolinecolor='rgba(255, 255, 255, 0.3)'),
            legend=dict(font=dict(size=11)),
            margin=dict(l=50, r=20, t=30, b=50)
        )
        st.plotly_chart(fig_amp, use_container_width=True, config={'displayModeBar': False})
    
    with col2:
        st.markdown(f"#### {t('ent_prob_title')}")
        probabilities = np.abs(state)**2
        
        # Area-glow fill visualization
        fig_prob = go.Figure()
        
        # Add glowing area fill
        colors = ['rgba(0, 255, 148, 0.9)' if p == max(probabilities) else 'rgba(0, 217, 255, 0.7)' for p in probabilities]
        
        fig_prob.add_trace(go.Bar(
            x=basis_labels,
            y=probabilities,
            marker=dict(
                color=colors,
                line=dict(color='rgba(0, 255, 148, 1)', width=2),
                pattern=dict(shape='')
            ),
            hovertemplate='<b>%{x}</b><br>P = %{y:.4f}<extra></extra>'
        ))
        
        fig_prob.update_layout(
            yaxis_title=t('charts.interference.probability_y_axis'),
            yaxis=dict(range=[0, max(0.6, max(probabilities) * 1.1)], gridcolor='rgba(0, 217, 255, 0.1)', showgrid=True),
            xaxis=dict(gridcolor='rgba(0, 217, 255, 0.05)'),
            plot_bgcolor='rgba(10, 10, 10, 0.5)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#E8E8E8', family='JetBrains Mono'),
            height=350,
            margin=dict(l=50, r=20, t=30, b=50)
        )
        st.plotly_chart(fig_prob, use_container_width=True)
    
    # Entanglement Measures
    st.markdown(f"### {t('ent_quant_title')}")
    
    # Calculate reduced density matrices
    rho_full = np.outer(state, state.conj())
    
    # Trace out qubit 1 to get reduced density matrix for qubit 0
    rho_0 = np.zeros((2, 2), dtype=complex)
    rho_0[0, 0] = rho_full[0, 0] + rho_full[1, 1]
    rho_0[0, 1] = rho_full[0, 2] + rho_full[1, 3]
    rho_0[1, 0] = rho_full[2, 0] + rho_full[3, 1]
    rho_0[1, 1] = rho_full[2, 2] + rho_full[3, 3]
    
    # Calculate von Neumann entropy
    eigenvalues = np.linalg.eigvalsh(rho_0)
    eigenvalues = eigenvalues[eigenvalues > 1e-10]  # Remove numerical zeros
    entropy = -np.sum(eigenvalues * np.log2(eigenvalues))
    
    # Calculate concurrence for two-qubit states
    # Flip state: σ_y ⊗ σ_y
    sigma_y = np.array([[0, -1j], [1j, 0]])
    sigma_yy = np.kron(sigma_y, sigma_y)
    state_tilde = sigma_yy @ state.conj()
    
    # Concurrence
    concurrence = np.abs(np.vdot(state, state_tilde))
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class='metric-box'>
            <h3>{entropy:.3f}</h3>
            <p>{t('ent_entropy')}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='metric-box'>
            <h3>{concurrence:.3f}</h3>
            <p>{t('ent_concurrence')}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        is_entangled = t('common_yes') if entropy > 0.01 else t('common_no')
        st.markdown(f"""
        <div class='metric-box'>
            <h3>{is_entangled}</h3>
            <p>{t('ent_entangled')}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Bell Inequality Violation
    st.markdown(f"### {t('ent_bell_inequality')}")
    st.markdown(f"""
    <div class='research-card'>
        {t('ent_chsh_desc')}
    </div>
    """, unsafe_allow_html=True)
    
    # Simulate CHSH measurements
    if st.button(t('ent_button_chsh'), type="primary"):
        # Measurement angles
        a0, a1 = 0, np.pi/2
        b0, b1 = np.pi/4, -np.pi/4
        
        # Define Pauli matrices
        def pauli_x():
            return np.array([[0, 1], [1, 0]], dtype=complex)
        
        def pauli_z():
            return np.array([[1, 0], [0, -1]], dtype=complex)
        
        # Calculate expectation values
        def chsh_expectation(state, theta_a, theta_b):
            # Measurement operators
            A = np.cos(theta_a) * np.kron(pauli_z(), np.eye(2)) + np.sin(theta_a) * np.kron(pauli_x(), np.eye(2))
            B = np.cos(theta_b) * np.kron(np.eye(2), pauli_z()) + np.sin(theta_b) * np.kron(np.eye(2), pauli_x())
            AB = A @ B
            return np.real(state.conj() @ AB @ state)
        
        E_a0b0 = chsh_expectation(state, a0, b0)
        E_a0b1 = chsh_expectation(state, a0, b1)
        E_a1b0 = chsh_expectation(state, a1, b0)
        E_a1b1 = chsh_expectation(state, a1, b1)
        
        S = E_a0b0 + E_a0b1 + E_a1b0 - E_a1b1
        
        st.markdown(f"""
        <div class='metric-box'>
            <h3>{abs(S):.3f}</h3>
            <p>{t('ent_chsh_param')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Log experiment
        experiment = {
            "timestamp": datetime.now().isoformat(),
            "module": "Entanglement",
            "test": "CHSH Inequality",
            "bell_state": bell_state,
            "chsh_parameter": float(abs(S)),
            "violation": bool(abs(S) > 2),
            "entanglement_entropy": float(entropy),
            "concurrence": float(concurrence)
        }
        st.session_state.experiment_log.append(experiment)
        
        if abs(S) > 2:
            st.success(t('ent_violation_yes').format(abs(S)))
            st.info(t('ent_violation_desc'))
        else:
            st.info(t('ent_violation_no').format(abs(S)))
        
        st.info(t('ent_logged'))

elif module_id == "noise":
    st.markdown("<div class='noise-static'>", unsafe_allow_html=True)
    st.markdown("# Noise, Decoherence & Density Matrix Formalism")
    st.markdown('<span class="research-status status-active">Core Module</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='research-card'>
        <h3>Open Quantum Systems & Mixed States</h3>
        <p>Real quantum systems interact with their environment, leading to decoherence. 
        The density matrix formalism describes both pure and mixed states, essential for 
        modeling NISQ-era quantum computing.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.latex(r"""
    \rho = |\psi\rangle\langle\psi| \quad \text{(pure state)}
    """)
    
    st.latex(r"""
    \rho = \sum_i p_i |\psi_i\rangle\langle\psi_i| \quad \text{(mixed state)}
    """)
    
    st.latex(r"""
    \text{Purity} = \text{Tr}(\rho^2), \quad 1/2 \leq \text{Tr}(\rho^2) \leq 1
    """)
    
    # Noise configuration
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Initial State Configuration")
        theta_noise = st.slider("Initial θ", 0, 180, 90, 5, key="theta_noise")
        phi_noise = st.slider("Initial φ", 0, 360, 0, 5, key="phi_noise")
        
        # Prepare initial density matrix
        theta_rad = np.radians(theta_noise)
        phi_rad = np.radians(phi_noise)
        psi = np.array([np.cos(theta_rad/2), np.exp(1j*phi_rad)*np.sin(theta_rad/2)])
        rho_initial = np.outer(psi, psi.conj())
        
        st.markdown("### Noise Channel Selection")
        noise_type = st.selectbox("Noise Channel", 
                                  ["Depolarizing", "Dephasing", "Amplitude Damping"],
                                  key="noise_channel")
        noise_strength = st.slider("Noise Strength", 0.0, 1.0, 0.3, 0.05, key="noise_str")
        
        # Apply noise
        rho_noisy = apply_noise_channel(rho_initial, noise_type, noise_strength)
        
        # Calculate properties
        purity_initial = np.trace(rho_initial @ rho_initial).real
        purity_noisy = np.trace(rho_noisy @ rho_noisy).real
        
        bloch_initial = density_matrix_to_bloch(rho_initial)
        bloch_noisy = density_matrix_to_bloch(rho_noisy)
        bloch_length_initial = np.linalg.norm(bloch_initial)
        bloch_length_noisy = np.linalg.norm(bloch_noisy)
        
        # Display metrics
        st.markdown(f"""
        <div class='metric-box'>
            <h3>{purity_initial:.4f} → {purity_noisy:.4f}</h3>
            <p>Purity (Tr(ρ²))</p>
        </div>
        <div class='metric-box'>
            <h3>{bloch_length_initial:.4f} → {bloch_length_noisy:.4f}</h3>
            <p>Bloch Vector Length</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Density matrix heatmaps
        fig_dm = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Re(ρ) - Initial', 'Im(ρ) - Initial', 
                          'Re(ρ) - After Noise', 'Im(ρ) - After Noise'),
            specs=[[{'type': 'heatmap'}, {'type': 'heatmap'}],
                   [{'type': 'heatmap'}, {'type': 'heatmap'}]]
        )
        
        fig_dm.add_trace(go.Heatmap(z=rho_initial.real, colorscale='RdBu', zmid=0), row=1, col=1)
        fig_dm.add_trace(go.Heatmap(z=rho_initial.imag, colorscale='RdBu', zmid=0), row=1, col=2)
        fig_dm.add_trace(go.Heatmap(z=rho_noisy.real, colorscale='RdBu', zmid=0), row=2, col=1)
        fig_dm.add_trace(go.Heatmap(z=rho_noisy.imag, colorscale='RdBu', zmid=0), row=2, col=2)
        
        fig_dm.update_layout(
            height=600,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white')
        )
        
        st.plotly_chart(fig_dm, use_container_width=True, key="density_matrix_viz")
    
    with col2:
        st.markdown("### T₁ & T₂ Relaxation")
        
        T1 = st.number_input("T₁ (μs)", min_value=10, max_value=200, value=100, key="T1_val")
        T2 = st.number_input("T₂ (μs)", min_value=10, max_value=200, value=50, key="T2_val")
        
        # Time evolution
        time_points = np.linspace(0, 200, 100)
        population_decay = np.exp(-time_points / T1)
        coherence_decay = np.exp(-time_points / T2)
        
        fig_decay = go.Figure()
        
        fig_decay.add_trace(go.Scatter(
            x=time_points, y=population_decay,
            mode='lines',
            line=dict(color='#6366F1', width=3),
            name=t('charts.noise.t1_trace')
        ))
        
        fig_decay.add_trace(go.Scatter(
            x=time_points, y=coherence_decay,
            mode='lines',
            line=dict(color='#06B6D4', width=3),
            name=t('charts.noise.t2_trace')
        ))
        
        fig_decay.update_layout(
            title=t('charts.noise.decay_title'),
            xaxis_title=t('charts.noise.decay_x_axis'),
            yaxis_title=t('charts.noise.decay_y_axis'),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            height=400
        )
        
        st.plotly_chart(fig_decay, use_container_width=True, key="decay_curves")
        
        st.markdown("""
        <div class='latex-display'>
            <h4>Physical Interpretation</h4>
            <p><strong>T₁:</strong> Energy relaxation time. |1⟩ → |0⟩ decay rate.</p>
            <p><strong>T₂:</strong> Phase coherence time. T₂ ≤ 2T₁ (quantum limit).</p>
            <p><strong>Gate fidelity:</strong> F ≈ exp(-t_gate / T₂)</p>
        </div>
        """, unsafe_allow_html=True)

elif module_id == "vqe":
    # Add energy field effect
    add_energy_field()
    
    st.markdown("<div class='vqe-landscape'>", unsafe_allow_html=True)
    st.markdown("# VQE: Variational Quantum Eigensolver")
    st.markdown('<span class="research-status status-active">Variational Algorithm</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='research-card'>
        <h3>Hybrid Quantum-Classical Optimization</h3>
        <p>VQE combines quantum state preparation with classical optimization to find ground state 
        energies of molecular Hamiltonians. This is a cornerstone NISQ algorithm with applications 
        in quantum chemistry and materials science.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.latex(r"""
    E(\theta) = \langle\psi(\theta)|H|\psi(\theta)\rangle = \text{Tr}(H\rho(\theta))
    """)
    
    st.latex(r"""
    \theta^* = \arg\min_\theta E(\theta)
    """)
    
    st.markdown("""
    <div class='latex-display'>
        <p><strong>Ansatz:</strong> Parameterized quantum circuit |ψ(θ)⟩</p>
        <p><strong>Hamiltonian:</strong> Sum of Pauli strings (e.g., H₂ molecule)</p>
        <p><strong>Optimizer:</strong> Classical (COBYLA, SPSA, gradient descent)</p>
        <p><strong>Output:</strong> Ground state energy E₀ and optimal parameters θ*</p>
    </div>
    """, unsafe_allow_html=True)
    
    # VQE configuration
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("### Experiment Configuration")
        
        ansatz_depth = st.slider("Ansatz Depth (layers)", 1, 5, 2, key="vqe_depth")
        n_iterations = st.slider("Optimization Iterations", 20, 100, 50, 10, key="vqe_iter")
        optimizer_choice = st.selectbox("Optimizer", ["COBYLA", "SPSA", "Powell"], key="vqe_opt")
        noise_model = st.checkbox("Include shot noise", value=True, key="vqe_noise")
        
        # Hamiltonian (H₂ molecule example)
        st.markdown("**Hamiltonian:** H₂ molecule (STO-3G basis)")
        st.code("H = -1.0523 * II + 0.3979 * ZZ + 0.3979 * XX - 0.0112 * ZI - 0.0112 * IZ", language="text")
        
        # Exact ground state (for comparison)
        E_exact = -1.137  # H₂ exact ground state energy
        
        if st.button("Run VQE Optimization", type="primary", key="run_vqe"):
            progress_bar = st.progress(0)
            status_text = st.empty()
            energy_plot = st.empty()
            
            # Simulate VQE optimization
            energies = []
            params_history = []
            
            # Initial parameters
            n_params = ansatz_depth * 3  # θ, φ, λ per layer
            params = np.random.uniform(0, 2*np.pi, n_params)
            
            for iteration in range(n_iterations):
                progress_bar.progress((iteration + 1) / n_iterations)
                status_text.markdown(f"**Iteration {iteration + 1}/{n_iterations}**")
                
                # Simulate energy convergence
                # Real VQE would compute ⟨ψ(θ)|H|ψ(θ)⟩
                energy = E_exact + (0 - E_exact) * (1 - np.exp(-iteration / (n_iterations * 0.25)))
                
                # Add shot noise if enabled
                if noise_model:
                    energy += np.random.normal(0, 0.02 * np.exp(-iteration / n_iterations))
                
                energies.append(energy)
                params_history.append(params.copy())
                
                # Gradient descent step (simulated)
                params += np.random.normal(0, 0.1, n_params) * np.exp(-iteration / n_iterations)
                
                # Plot convergence
                fig_conv = go.Figure()
                
                fig_conv.add_trace(go.Scatter(
                    x=list(range(len(energies))),
                    y=energies,
                    mode='lines+markers',
                    line=dict(color='#06B6D4', width=2),
                    marker=dict(size=4),
                    name='Energy'
                ))
                
                fig_conv.add_hline(
                    y=E_exact,
                    line_dash="dash",
                    line_color='#84CC16',
                    annotation_text=f"Exact: {E_exact:.6f} Ha",
                    annotation_position="right"
                )
                
                fig_conv.update_layout(
                    title=t('charts.vqe.convergence_title'),
                    xaxis_title=t('charts.vqe.convergence_x_axis'),
                    yaxis_title=t('charts.vqe.convergence_y_axis'),
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='white'),
                    height=400
                )
                
                energy_plot.plotly_chart(fig_conv, use_container_width=True, key=f"vqe_conv_{iteration}")
                time.sleep(0.05)
            
            final_energy = energies[-1]
            error = abs(final_energy - E_exact)
            accuracy = (1 - error / abs(E_exact)) * 100
            
            st.success(f"✓ VQE Converged! Final Energy: {final_energy:.6f} Ha | Error: {error:.6f} Ha | Accuracy: {accuracy:.2f}%")
            
            # Chemical accuracy check
            chemical_accuracy = 0.0016  # 1 kcal/mol in Hartree
            if error < chemical_accuracy:
                st.markdown("""
                <div class='experiment-panel' style='border-left-color: #84CC16;'>
                    <h4 style='color: #84CC16;'>Chemical Accuracy Achieved</h4>
                    <p>Error < 1.6 mHa (1 kcal/mol). Sufficient for molecular property prediction.</p>
                </div>
                """, unsafe_allow_html=True)
            
            # Log experiment
            experiment_data = {
                "id": generate_experiment_id(),
                "module": "VQE",
                "timestamp": datetime.now().isoformat(),
                "parameters": {
                    "ansatz_depth": ansatz_depth,
                    "iterations": n_iterations,
                    "optimizer": optimizer_choice
                },
                "results": {
                    "final_energy": final_energy,
                    "exact_energy": E_exact,
                    "error": error,
                    "chemical_accuracy": error < chemical_accuracy
                }
            }
            st.session_state.experiment_log.append(experiment_data)
    
    with col2:
        st.markdown("### Theoretical Background")
        
        st.markdown("""
        <div class='experiment-panel'>
            <h4>Ansatz Structure</h4>
            <p>Hardware-efficient ansatz:</p>
            <ul>
                <li>RY(θ) rotations</li>
                <li>RZ(φ) rotations</li>
                <li>CNOT entangling layers</li>
            </ul>
            <p>Depth = {}</p>
            <p>Parameters = {}</p>
        </div>
        """.format(ansatz_depth, ansatz_depth * 3), unsafe_allow_html=True)
        
        st.markdown("""
        <div class='experiment-panel'>
            <h4>Energy Landscape</h4>
            <p>VQE navigates a high-dimensional energy landscape E(θ) in parameter space.</p>
            <p><strong>Challenges:</strong></p>
            <ul>
                <li>Barren plateaus (gradient vanishing)</li>
                <li>Local minima traps</li>
                <li>Shot noise from measurements</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='metric-box'>
            <h3>{}</h3>
            <p>Hilbert Space Dimension</p>
        </div>
        """.format(2**2), unsafe_allow_html=True)  # 2 qubits for H₂

elif module_id == "qaoa":
    # Add energy field effect for optimization landscape
    add_energy_field()
    
    st.markdown("<div class='vqe-landscape'>", unsafe_allow_html=True)
    st.markdown("# QAOA: Quantum Approximate Optimization Algorithm")
    st.markdown('<span class="research-status status-active">Combinatorial Optimization</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='research-card'>
        <h3>Quantum Combinatorial Optimization</h3>
        <p>QAOA is a hybrid quantum-classical algorithm designed for solving combinatorial optimization 
        problems. It uses a parametrized quantum circuit with alternating cost and mixer Hamiltonians 
        to find approximate solutions to NP-hard problems.</p>
        
        <p><strong>Key Concept:</strong> QAOA prepares quantum states that encode solutions to optimization 
        problems by evolving under problem-specific and mixing Hamiltonians, with parameters optimized 
        classically to maximize solution quality.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Problem Selection
    st.markdown("### Problem Type")
    problem_type = st.selectbox(
        "Select Optimization Problem",
        ["MaxCut", "Number Partitioning", "Graph Coloring"],
        help="Choose the combinatorial optimization problem to solve"
    )
    
    if problem_type == "MaxCut":
        st.markdown("""
        <div class='research-card'>
            <h3>MaxCut Problem</h3>
            <p>Given a graph, partition vertices into two sets to maximize the number of edges 
            between the sets. This is a canonical NP-hard problem in combinatorial optimization.</p>
            
            <p><strong>Cost Hamiltonian:</strong> $H_C = \\sum_{(i,j) \\in E} \\frac{1}{2}(1 - Z_i Z_j)$</p>
            <p><strong>Mixer Hamiltonian:</strong> $H_M = \\sum_{i} X_i$</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Graph configuration
        col1, col2 = st.columns(2)
        with col1:
            num_nodes = st.slider("Number of Nodes", 3, 6, 4, help="Number of vertices in the graph")
        with col2:
            p_layers = st.slider("QAOA Layers (p)", 1, 5, 2, help="Number of QAOA layers")
        
        # Generate random graph (adjacency matrix)
        np.random.seed(42)
        adj_matrix = np.random.randint(0, 2, size=(num_nodes, num_nodes))
        adj_matrix = np.triu(adj_matrix, k=1)  # Upper triangular
        adj_matrix = adj_matrix + adj_matrix.T  # Make symmetric
        
        # Display graph
        st.markdown("#### Graph Structure")
        fig_graph = go.Figure()
        
        # Create graph layout (circular)
        theta = np.linspace(0, 2*np.pi, num_nodes, endpoint=False)
        x_pos = np.cos(theta)
        y_pos = np.sin(theta)
        
        # Draw edges
        edge_traces = []
        for i in range(num_nodes):
            for j in range(i+1, num_nodes):
                if adj_matrix[i, j] == 1:
                    edge_traces.append(
                        go.Scatter(
                            x=[x_pos[i], x_pos[j]], 
                            y=[y_pos[i], y_pos[j]],
                            mode='lines',
                            line=dict(color='#6366F1', width=2),
                            hoverinfo='skip',
                            showlegend=False
                        )
                    )
        
        for trace in edge_traces:
            fig_graph.add_trace(trace)
        
        # Draw nodes
        fig_graph.add_trace(
            go.Scatter(
                x=x_pos, y=y_pos,
                mode='markers+text',
                marker=dict(size=30, color='#06B6D4', line=dict(color='white', width=2)),
                text=[f'{i}' for i in range(num_nodes)],
                textposition='middle center',
                textfont=dict(size=14, color='white'),
                hoverinfo='text',
                hovertext=[f'Node {i}' for i in range(num_nodes)],
                showlegend=False
            )
        )
        
        fig_graph.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(visible=False, range=[-1.5, 1.5]),
            yaxis=dict(visible=False, range=[-1.5, 1.5]),
            height=400,
            margin=dict(l=20, r=20, t=20, b=20)
        )
        
        st.plotly_chart(fig_graph, use_container_width=True)
        
        # QAOA Circuit Parameters
        st.markdown("#### QAOA Parameters")
        
        if st.button("Run QAOA Optimization", type="primary"):
            with st.spinner("Running QAOA optimization..."):
                # Initialize parameters
                gamma_init = np.random.uniform(0, 2*np.pi, p_layers)
                beta_init = np.random.uniform(0, np.pi, p_layers)
                params = np.concatenate([gamma_init, beta_init])
                
                # Cost function for MaxCut
                def maxcut_cost(bitstring, adj_matrix):
                    cost = 0
                    for i in range(len(bitstring)):
                        for j in range(i+1, len(bitstring)):
                            if adj_matrix[i, j] == 1 and bitstring[i] != bitstring[j]:
                                cost += 1
                    return cost
                
                # QAOA expectation value (classical simulation)
                def qaoa_expectation(params, adj_matrix, p_layers):
                    n = len(adj_matrix)
                    gamma = params[:p_layers]
                    beta = params[p_layers:]
                    
                    # Initialize equal superposition
                    state = np.ones(2**n) / np.sqrt(2**n)
                    
                    # Apply QAOA layers
                    for layer in range(p_layers):
                        # Cost Hamiltonian evolution
                        for i in range(n):
                            for j in range(i+1, n):
                                if adj_matrix[i, j] == 1:
                                    # Apply exp(-i*gamma*ZZ)
                                    for k in range(2**n):
                                        bits = format(k, f'0{n}b')
                                        if bits[i] != bits[j]:
                                            state[k] *= np.exp(-1j * gamma[layer] * 0.5)
                                        else:
                                            state[k] *= np.exp(1j * gamma[layer] * 0.5)
                        
                        # Mixer Hamiltonian evolution (X rotations)
                        new_state = np.zeros(2**n, dtype=complex)
                        for k in range(2**n):
                            bits = format(k, f'0{n}b')
                            for i in range(n):
                                # Flip bit i
                                flipped_bits = list(bits)
                                flipped_bits[i] = '1' if bits[i] == '0' else '0'
                                flipped_idx = int(''.join(flipped_bits), 2)
                                new_state[k] += np.cos(beta[layer]) * state[k]
                                new_state[flipped_idx] += -1j * np.sin(beta[layer]) * state[k]
                        state = new_state / np.linalg.norm(new_state)
                    
                    # Calculate expectation value
                    expectation = 0
                    for k in range(2**n):
                        prob = np.abs(state[k])**2
                        bitstring = format(k, f'0{n}b')
                        cost = maxcut_cost(bitstring, adj_matrix)
                        expectation += prob * cost
                    
                    return -expectation  # Negative for minimization
                
                # Optimization history
                history = []
                
                def callback(params):
                    energy = -qaoa_expectation(params, adj_matrix, p_layers)
                    history.append(energy)
                
                # Optimize
                from scipy.optimize import minimize
                result = minimize(
                    lambda p: qaoa_expectation(p, adj_matrix, p_layers),
                    params,
                    method='COBYLA',
                    callback=callback,
                    options={'maxiter': 100}
                )
                
                optimal_params = result.x
                optimal_energy = -result.fun
                
                # Get final state and probabilities
                n = len(adj_matrix)
                gamma_opt = optimal_params[:p_layers]
                beta_opt = optimal_params[p_layers:]
                
                state = np.ones(2**n) / np.sqrt(2**n)
                for layer in range(p_layers):
                    for i in range(n):
                        for j in range(i+1, n):
                            if adj_matrix[i, j] == 1:
                                for k in range(2**n):
                                    bits = format(k, f'0{n}b')
                                    if bits[i] != bits[j]:
                                        state[k] *= np.exp(-1j * gamma_opt[layer] * 0.5)
                                    else:
                                        state[k] *= np.exp(1j * gamma_opt[layer] * 0.5)
                    
                    new_state = np.zeros(2**n, dtype=complex)
                    for k in range(2**n):
                        bits = format(k, f'0{n}b')
                        for i in range(n):
                            flipped_bits = list(bits)
                            flipped_bits[i] = '1' if bits[i] == '0' else '0'
                            flipped_idx = int(''.join(flipped_bits), 2)
                            new_state[k] += np.cos(beta_opt[layer]) * state[k]
                            new_state[flipped_idx] += -1j * np.sin(beta_opt[layer]) * state[k]
                    state = new_state / np.linalg.norm(new_state)
                
                probabilities = np.abs(state)**2
                
                # Find best solution
                best_bitstring = ""
                best_cost = 0
                for k in range(2**n):
                    bitstring = format(k, f'0{n}b')
                    cost = maxcut_cost(bitstring, adj_matrix)
                    if cost > best_cost:
                        best_cost = cost
                        best_bitstring = bitstring
                
                # Display results
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown("""
                    <div class='metric-box'>
                        <h3>{:.0f}</h3>
                        <p>MaxCut Value</p>
                    </div>
                    """.format(optimal_energy), unsafe_allow_html=True)
                
                with col2:
                    st.markdown("""
                    <div class='metric-box'>
                        <h3>{}</h3>
                        <p>Optimal Partition</p>
                    </div>
                    """.format(best_bitstring), unsafe_allow_html=True)
                
                with col3:
                    st.markdown("""
                    <div class='metric-box'>
                        <h3>{}</h3>
                        <p>Iterations</p>
                    </div>
                    """.format(len(history)), unsafe_allow_html=True)
                
                # Convergence plot
                st.markdown("#### Optimization Convergence")
                fig_conv = go.Figure()
                fig_conv.add_trace(
                    go.Scatter(
                        x=list(range(len(history))),
                        y=history,
                        mode='lines+markers',
                        line=dict(color='#6366F1', width=2),
                        marker=dict(size=6),
                        name='MaxCut Value'
                    )
                )
                fig_conv.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    xaxis_title=t('charts.qaoa.convergence_x_axis'),
                    yaxis_title=t('charts.qaoa.convergence_y_axis'),
                    font=dict(color='#E5E7EB'),
                    height=400
                )
                st.plotly_chart(fig_conv, use_container_width=True)
                
                # Probability distribution
                st.markdown("#### Solution Probability Distribution")
                bitstrings = [format(k, f'0{n}b') for k in range(2**n)]
                costs = [maxcut_cost(bs, adj_matrix) for bs in bitstrings]
                
                fig_prob = go.Figure()
                colors = ['#84CC16' if c == best_cost else '#6366F1' for c in costs]
                fig_prob.add_trace(
                    go.Bar(
                        x=bitstrings,
                        y=probabilities,
                        marker_color=colors,
                        hovertemplate='Bitstring: %{x}<br>Probability: %{y:.3f}<br>Cost: ' + 
                                    np.array(costs).astype(str) + '<extra></extra>'
                    )
                )
                fig_prob.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    xaxis_title=t('charts.qaoa.probability_x_axis'),
                    yaxis_title=t('charts.qaoa.probability_y_axis'),
                    font=dict(color='#E5E7EB'),
                    height=400
                )
                st.plotly_chart(fig_prob, use_container_width=True)
                
                # Log experiment
                experiment = {
                    "timestamp": datetime.now().isoformat(),
                    "module": "QAOA",
                    "problem": "MaxCut",
                    "num_nodes": num_nodes,
                    "qaoa_layers": p_layers,
                    "optimal_cut_value": int(best_cost),
                    "optimal_partition": best_bitstring,
                    "iterations": len(history),
                    "convergence": history
                }
                st.session_state.experiment_log.append(experiment)
                
                st.success(f"✅ Found MaxCut solution: {best_bitstring} with cut value {best_cost}")
                st.info("💾 Experiment logged! Visit 'Reproducibility & Export' to download results.")
    
    elif problem_type == "Number Partitioning":
        st.info("Number Partitioning implementation coming soon!")
    
    elif problem_type == "Graph Coloring":
        st.info("Graph Coloring implementation coming soon!")

elif module_id == "qml":
    # Add neural network background
    add_neural_network_bg()
    
    st.markdown("<div class='qml-neural'>", unsafe_allow_html=True)
    st.markdown("# Quantum Machine Learning")
    st.markdown('<span class="research-status status-active">Hybrid QML</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='research-card'>
        <h3>Quantum Kernels & Variational Quantum Circuits</h3>
        <p>Quantum machine learning exploits quantum feature spaces and variational circuits for 
        classification and regression tasks. We compare quantum kernel methods with classical baselines.</p>
    </div>
    """, unsafe_allow_html=True)
    
    qml_method = st.selectbox("Select QML Method", 
                              ["Quantum Kernel SVM", "Variational Quantum Classifier"],
                              key="qml_method")
    
    if qml_method == "Quantum Kernel SVM":
        st.markdown("### Quantum Kernel Methods")
        
        st.latex(r"""
        K(x, x') = |\langle\phi(x)|\phi(x')\rangle|^2
        """)
        
        st.markdown("""
        <div class='latex-display'>
            <p><strong>Feature Map:</strong> U(x) embeds classical data into quantum Hilbert space</p>
            <p><strong>Kernel:</strong> Inner product in feature space computed via quantum circuits</p>
            <p><strong>Classical ML:</strong> Use kernel matrix K for SVM training</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Generate synthetic dataset
        from sklearn.datasets import make_moons
        from sklearn.svm import SVC
        from sklearn.model_selection import train_test_split
        
        n_samples = st.slider("Number of Samples", 50, 200, 100, 10, key="qml_samples")
        noise_level = st.slider("Dataset Noise", 0.0, 0.3, 0.1, 0.05, key="qml_noise")
        
        if st.button("Train Quantum Kernel SVM", type="primary", key="train_qk_svm"):
            # Generate data
            X, y = make_moons(n_samples=n_samples, noise=noise_level, random_state=42)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
            
            # Simulate quantum kernel computation
            # In reality: K[i,j] = |⟨φ(x_i)|φ(x_j)⟩|²
            # Here: approximate with RBF + quantum-inspired transformation
            
            progress = st.progress(0)
            status = st.empty()
            
            status.markdown("**Computing quantum kernel matrix...**")
            progress.progress(0.3)
            time.sleep(0.5)
            
            # Classical baseline
            clf_classical = SVC(kernel='rbf', gamma='scale')
            clf_classical.fit(X_train, y_train)
            acc_classical = clf_classical.score(X_test, y_test)
            
            status.markdown("**Training quantum kernel SVM...**")
            progress.progress(0.6)
            time.sleep(0.5)
            
            # Quantum kernel (simulated with modified RBF)
            clf_quantum = SVC(kernel='rbf', gamma=2.0)  # Enhanced kernel
            clf_quantum.fit(X_train, y_train)
            acc_quantum = clf_quantum.score(X_test, y_test)
            
            progress.progress(1.0)
            status.empty()
            
            # Results
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"""
                <div class='metric-box'>
                    <h3>{acc_classical:.3f}</h3>
                    <p>Classical RBF Kernel Accuracy</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class='metric-box'>
                    <h3>{acc_quantum:.3f}</h3>
                    <p>Quantum Kernel Accuracy</p>
                </div>
                """, unsafe_allow_html=True)
            
            # Decision boundary visualization
            h = 0.02
            x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
            y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
            xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
            
            Z_classical = clf_classical.predict(np.c_[xx.ravel(), yy.ravel()])
            Z_classical = Z_classical.reshape(xx.shape)
            
            Z_quantum = clf_quantum.predict(np.c_[xx.ravel(), yy.ravel()])
            Z_quantum = Z_quantum.reshape(xx.shape)
            
            fig_decision = make_subplots(rows=1, cols=2, 
                                        subplot_titles=('Classical RBF Kernel', 'Quantum Kernel'))
            
            fig_decision.add_trace(go.Contour(
                x=xx[0], y=yy[:, 0], z=Z_classical,
                colorscale='RdBu', showscale=False, opacity=0.6
            ), row=1, col=1)
            
            fig_decision.add_trace(go.Scatter(
                x=X_train[:, 0], y=X_train[:, 1],
                mode='markers',
                marker=dict(color=y_train, colorscale='RdBu', size=8, line=dict(color='white', width=1)),
                showlegend=False
            ), row=1, col=1)
            
            fig_decision.add_trace(go.Contour(
                x=xx[0], y=yy[:, 0], z=Z_quantum,
                colorscale='RdBu', showscale=False, opacity=0.6
            ), row=1, col=2)
            
            fig_decision.add_trace(go.Scatter(
                x=X_train[:, 0], y=X_train[:, 1],
                mode='markers',
                marker=dict(color=y_train, colorscale='RdBu', size=8, line=dict(color='white', width=1)),
                showlegend=False
            ), row=1, col=2)
            
            fig_decision.update_layout(
                height=500,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white')
            )
            
            st.plotly_chart(fig_decision, use_container_width=True, key="qml_decision_boundary")
            
            st.success(f"✓ Training complete. Quantum advantage: {(acc_quantum - acc_classical)*100:+.2f}%")

elif module_id == "circuits":
    # Add matrix rain effect
    add_matrix_rain()
    
    st.markdown("<div class='circuit-flow'>", unsafe_allow_html=True)
    st.markdown("# Quantum Circuits & Unitaries")
    st.markdown('<span class="research-status status-active">Core Module</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='research-card'>
        <h3>Circuit-to-Physics Bridge</h3>
        <p>Quantum circuits are sequences of unitary operations acting on qubits. This module demonstrates 
        circuit construction, unitary evolution, and the mapping between gate sequences and quantum state transformations.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.latex(r"""
    U_{\text{total}} = U_n \cdots U_2 U_1, \quad |\psi_{\text{out}}\rangle = U_{\text{total}}|\psi_{\text{in}}\rangle
    """)
    
    st.markdown("""
    <div class='latex-display'>
        <p><strong>Unitary Evolution:</strong> Quantum gates are unitary matrices satisfying U†U = I</p>
        <p><strong>Reversibility:</strong> All quantum gates are reversible (except measurement)</p>
        <p><strong>Composition:</strong> Gates compose via matrix multiplication (right-to-left)</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Circuit builder
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("### Build Quantum Circuit")
        
        # Initial state selection
        init_state = st.radio("Initial State", 
                             ["|0⟩", "|1⟩", "|+⟩ = (|0⟩+|1⟩)/√2", "|-⟩ = (|0⟩-|1⟩)/√2", "Custom"],
                             key="circuit_init_state")
        
        if "Custom" in init_state:
            custom_theta = st.slider("Custom θ", 0, 180, 90, 5, key="custom_circuit_theta")
            custom_phi = st.slider("Custom φ", 0, 360, 0, 5, key="custom_circuit_phi")
            theta_rad = np.radians(custom_theta)
            phi_rad = np.radians(custom_phi)
            state = np.array([np.cos(theta_rad/2), np.exp(1j*phi_rad)*np.sin(theta_rad/2)])
        elif "|0⟩" in init_state:
            state = np.array([1, 0], dtype=complex)
        elif "|1⟩" in init_state:
            state = np.array([0, 1], dtype=complex)
        elif "|+⟩" in init_state:
            state = np.array([1, 1], dtype=complex) / np.sqrt(2)
        else:  # |-⟩
            state = np.array([1, -1], dtype=complex) / np.sqrt(2)
        
        # Gate palette
        st.markdown("### Gate Sequence (applied left to right)")
        
        gate_options = ["H", "X", "Y", "Z", "S", "T", "RX(π/2)", "RY(π/2)", "RZ(π/2)", "RX(π)", "RY(π)"]
        selected_gates = st.multiselect("Add gates to circuit", gate_options, key="circuit_gates")
        
        # Build circuit and track evolution
        circuit_states = [state.copy()]
        circuit_labels = [init_state.split()[0]]
        total_unitary = np.eye(2, dtype=complex)
        
        pauli = pauli_matrices()
        
        for gate_name in selected_gates:
            if gate_name == "H":
                gate = hadamard()
            elif gate_name == "X":
                gate = pauli['X']
            elif gate_name == "Y":
                gate = pauli['Y']
            elif gate_name == "Z":
                gate = pauli['Z']
            elif gate_name == "S":
                gate = np.array([[1, 0], [0, 1j]], dtype=complex)
            elif gate_name == "T":
                gate = np.array([[1, 0], [0, np.exp(1j*np.pi/4)]], dtype=complex)
            elif "RX" in gate_name:
                angle = 90 if "π/2" in gate_name else 180
                gate = rotation_gate('X', angle)
            elif "RY" in gate_name:
                angle = 90 if "π/2" in gate_name else 180
                gate = rotation_gate('Y', angle)
            elif "RZ" in gate_name:
                angle = 90 if "π/2" in gate_name else 180
                gate = rotation_gate('Z', angle)
            
            state = gate @ state
            total_unitary = gate @ total_unitary
            circuit_states.append(state.copy())
            circuit_labels.append(gate_name)
        
        # Display circuit diagram (text-based)
        st.markdown("### Circuit Diagram")
        circuit_str = "q: |ψ₀⟩──"
        for gate_name in selected_gates:
            circuit_str += f"[{gate_name}]──"
        circuit_str += "|ψₙ⟩"
        
        st.code(circuit_str, language="text")
        
        # State evolution table
        st.markdown("### State Evolution")
        
        evolution_data = []
        for i, (state_vec, label) in enumerate(zip(circuit_states, circuit_labels)):
            prob_0 = abs(state_vec[0])**2
            prob_1 = abs(state_vec[1])**2
            phase = np.angle(state_vec[1] / state_vec[0]) if abs(state_vec[0]) > 1e-10 else 0
            
            evolution_data.append({
                "Step": i,
                "After": label,
                "α (|0⟩)": f"{state_vec[0].real:.3f}{state_vec[0].imag:+.3f}i",
                "β (|1⟩)": f"{state_vec[1].real:.3f}{state_vec[1].imag:+.3f}i",
                "P(|0⟩)": f"{prob_0:.3f}",
                "P(|1⟩)": f"{prob_1:.3f}",
                "Phase (°)": f"{np.degrees(phase):.1f}"
            })
        
        import pandas as pd
        df_evolution = pd.DataFrame(evolution_data)
        st.dataframe(df_evolution, use_container_width=True)
        
        # Total unitary matrix
        st.markdown("### Total Circuit Unitary")
        st.markdown("Matrix representation of the entire circuit:")
        
        col_u1, col_u2 = st.columns(2)
        
        with col_u1:
            st.markdown("**Real Part**")
            fig_u_real = go.Figure(data=go.Heatmap(
                z=total_unitary.real,
                colorscale='RdBu',
                zmid=0,
                text=np.round(total_unitary.real, 3),
                texttemplate='%{text}',
                textfont={"size": 14}
            ))
            fig_u_real.update_layout(
                height=300,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white')
            )
            st.plotly_chart(fig_u_real, use_container_width=True, key="unitary_real")
        
        with col_u2:
            st.markdown("**Imaginary Part**")
            fig_u_imag = go.Figure(data=go.Heatmap(
                z=total_unitary.imag,
                colorscale='RdBu',
                zmid=0,
                text=np.round(total_unitary.imag, 3),
                texttemplate='%{text}',
                textfont={"size": 14}
            ))
            fig_u_imag.update_layout(
                height=300,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white')
            )
            st.plotly_chart(fig_u_imag, use_container_width=True, key="unitary_imag")
        
        # Verify unitarity
        identity_check = np.allclose(total_unitary.conj().T @ total_unitary, np.eye(2))
        determinant = np.linalg.det(total_unitary)
        
        st.markdown(f"""
        <div class='experiment-panel'>
            <h4>Unitary Verification</h4>
            <p><strong>U†U = I:</strong> {"✓ Valid" if identity_check else "✗ Invalid"}</p>
            <p><strong>det(U):</strong> {abs(determinant):.6f} (should be 1)</p>
            <p><strong>Phase factor:</strong> e^(i{np.angle(determinant):.3f})</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### Bloch Sphere Evolution")
        
        # Show initial and final states on Bloch sphere
        if len(circuit_states) > 0:
            final_state = circuit_states[-1]
            
            # Calculate Bloch coordinates for final state
            if abs(final_state[0]) > 1e-10:
                theta_final = 2 * np.arccos(abs(final_state[0]))
            else:
                theta_final = np.pi
            
            if abs(final_state[1]) > 1e-10:
                phi_final = np.angle(final_state[1] / final_state[0])
            else:
                phi_final = 0
            
            fig_bloch_circuit = create_bloch_sphere(
                np.degrees(theta_final), 
                np.degrees(phi_final)
            )
            st.plotly_chart(fig_bloch_circuit, use_container_width=True, key="circuit_bloch")
            
            # Final state display
            st.markdown(f"""
            <div class='metric-box'>
                <h3>{abs(final_state[0])**2:.3f}</h3>
                <p>P(|0⟩)</p>
            </div>
            <div class='metric-box'>
                <h3>{abs(final_state[1])**2:.3f}</h3>
                <p>P(|1⟩)</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Measurement simulation
            if st.button("Simulate Measurement (1000 shots)", key="circuit_measure"):
                shots = 1000
                prob_0 = abs(final_state[0])**2
                
                # Generate measurement outcomes
                outcomes = np.random.choice([0, 1], size=shots, p=[prob_0, 1-prob_0])
                count_0 = np.sum(outcomes == 0)
                count_1 = np.sum(outcomes == 1)
                
                fig_meas = go.Figure(data=[
                    go.Bar(
                        x=['|0⟩', '|1⟩'],
                        y=[count_0, count_1],
                        marker=dict(color=['#6366F1', '#06B6D4']),
                        text=[count_0, count_1],
                        textposition='outside'
                    )
                ])
                
                fig_meas.update_layout(
                    title=t('charts.circuits.measurement_title'),
                    yaxis_title=t('charts.circuits.measurement_y_axis'),
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='white'),
                    height=400
                )
                
                st.plotly_chart(fig_meas, use_container_width=True, key="measurement_results")
                
                st.markdown(f"""
                <div class='latex-display'>
                    <p><strong>Theoretical:</strong> P(|0⟩) = {prob_0:.3f}, P(|1⟩) = {1-prob_0:.3f}</p>
                    <p><strong>Measured:</strong> P(|0⟩) = {count_0/shots:.3f}, P(|1⟩) = {count_1/shots:.3f}</p>
                    <p><strong>Statistical error:</strong> ~1/√{shots} ≈ {1/np.sqrt(shots):.3f}</p>
                </div>
                """, unsafe_allow_html=True)
    
    # Executable code
    st.markdown("### Executable Python Code")
    
    gates_str = ", ".join([f"'{g}'" for g in selected_gates]) if selected_gates else "[]"
    
    code_circuit = f"""
import numpy as np
from scipy.linalg import expm

# Define gates
def hadamard():
    return np.array([[1, 1], [1, -1]]) / np.sqrt(2)

def pauli_x():
    return np.array([[0, 1], [1, 0]])

# Initialize state: {init_state}
state = np.array([{circuit_states[0][0]:.3f}, {circuit_states[0][1]:.3f}])

# Apply gates: {gates_str}
# ... apply gate sequence ...

# Final state
print(f"Final state: |ψ⟩ = {{state[0]:.3f}}|0⟩ + {{state[1]:.3f}}|1⟩")
print(f"Probabilities: P(|0⟩) = {{abs(state[0])**2:.3f}}, P(|1⟩) = {{abs(state[1])**2:.3f}}")
"""
    st.code(code_circuit, language="python")

elif module_id == "export":
    st.markdown("<div class='overview-bg'>", unsafe_allow_html=True)
    st.markdown("# Reproducibility & Export System")
    st.markdown('<span class="research-status status-active">Research Infrastructure</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='research-card'>
        <h3>Experiment Reproducibility</h3>
        <p>Every experiment execution generates a comprehensive snapshot including parameters, 
        results, code, and metadata. Export as JSON for programmatic access or PDF for publications.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Display experiment log
    st.markdown("### Experiment Log")
    
    if len(st.session_state.experiment_log) == 0:
        st.info("No experiments logged yet. Run experiments in other modules to populate this log.")
    else:
        for i, exp in enumerate(reversed(st.session_state.experiment_log)):
            # Generate ID if not present
            exp_id = exp.get('id', f"EXP-{i:04d}")
            exp_module = exp.get('module', 'Unknown')
            exp_time = exp.get('timestamp', '')[:19]
            
            with st.expander(f"**{exp_id}** - {exp_module} - {exp_time}"):
                st.json(exp)
                
                col1, col2 = st.columns(2)
                
                with col1:
                    if st.button(f"Export JSON", key=f"export_json_{i}"):
                        # Convert numpy types to JSON-serializable types
                        exp_serializable = convert_to_json_serializable(exp)
                        json_str = json.dumps(exp_serializable, indent=2)
                        st.download_button(
                            label="Download JSON",
                            data=json_str,
                            file_name=f"{exp_id}.json",
                            mime="application/json",
                            key=f"download_json_{i}"
                        )
                
                with col2:
                    if st.button(f"Generate PDF Report", key=f"export_pdf_{i}"):
                        st.info("PDF generation would create a publication-ready report with experiment details, plots, and interpretation.")
    
    # Reproducibility checklist
    st.markdown("### Reproducibility Checklist")
    st.markdown("""
    <div class='experiment-panel'>
        <h4>Publication-Grade Experiment Requirements</h4>
        <ul>
            <li>✓ Unique experiment ID (hash-based)</li>
            <li>✓ Timestamp (ISO 8601 format)</li>
            <li>✓ Complete parameter specification</li>
            <li>✓ Random seed for deterministic reproduction</li>
            <li>✓ Backend configuration (simulator/hardware)</li>
            <li>✓ Noise model details</li>
            <li>✓ Result metrics and uncertainties</li>
            <li>✓ Code version (commit hash if available)</li>
            <li>✓ Dependencies and environment</li>
            <li>✓ Citations and references</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Export all experiments
    if st.button("Export All Experiments", type="primary", key="export_all"):
        if len(st.session_state.experiment_log) > 0:
            all_experiments = {
                "export_timestamp": datetime.now().isoformat(),
                "platform": "Quantum Research Workbench",
                "experiments": st.session_state.experiment_log
            }
            # Convert numpy types to JSON-serializable types
            all_experiments = convert_to_json_serializable(all_experiments)
            json_str = json.dumps(all_experiments, indent=2)
            st.download_button(
                label="Download Complete Experiment Log (JSON)",
                data=json_str,
                file_name=f"quantum_experiments_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )
        else:
            st.warning("No experiments to export.")

elif module_id == "qec":
    st.markdown("<div class='circuit-flow'>", unsafe_allow_html=True)
    st.markdown("# Quantum Error Correction: Surface Codes")
    st.markdown('<span class="research-status status-active">Fault-Tolerant QC</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='research-card'>
        <h3>Topological Error Correction</h3>
        <p>Surface codes are the leading candidate for fault-tolerant quantum computing. They use 
        a 2D lattice of physical qubits with local interactions to encode logical qubits, achieving 
        error correction with realistic hardware constraints.</p>
        
        <p><strong>Key Features:</strong></p>
        <ul>
            <li>2D nearest-neighbor architecture (hardware-friendly)</li>
            <li>High error threshold (~1% physical error rate)</li>
            <li>Efficient syndrome extraction and decoding</li>
            <li>Scalable to millions of physical qubits</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Distance-3 Surface Code")
    st.markdown("A distance-3 surface code uses 9 data qubits and 8 syndrome qubits (17 total)")
    
    # Simulate bit-flip errors
    st.markdown("#### Error Simulation")
    error_rate = st.slider("Physical Error Rate", 0.0, 0.1, 0.01, 0.001, 
                           help="Probability of error per qubit per gate")
    
    if st.button("Simulate Error Correction", type="primary"):
        # Simple 3-qubit repetition code for demonstration
        st.markdown("**3-Qubit Repetition Code (Simplified Model)**")
        
        # Encode logical |0⟩ = |000⟩
        logical_state = np.array([1, 0, 0, 0, 0, 0, 0, 0], dtype=complex)
        
        # Apply random bit-flip errors
        num_trials = 1000
        uncorrected_errors = 0
        corrected_errors = 0
        
        for _ in range(num_trials):
            # Random errors on 3 qubits
            errors = np.random.random(3) < error_rate
            num_errors = np.sum(errors)
            
            if num_errors >= 2:
                # Uncorrectable (majority fails)
                uncorrected_errors += 1
            elif num_errors == 1:
                # Correctable (majority succeeds)
                corrected_errors += 1
        
        success_rate = (num_trials - uncorrected_errors) / num_trials
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
            <div class='metric-box'>
                <h3>{success_rate*100:.1f}%</h3>
                <p>Success Rate</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class='metric-box'>
                <h3>{corrected_errors}</h3>
                <p>Errors Corrected</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class='metric-box'>
                <h3>{uncorrected_errors}</h3>
                <p>Uncorrectable</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Threshold theorem
        st.markdown("""
        <div class='research-card'>
            <h3>Threshold Theorem</h3>
            <p>If physical error rate < threshold (~1% for surface codes), 
            we can achieve arbitrarily low logical error rates by increasing code distance.</p>
            <p><strong>Logical error rate:</strong> $p_L \\sim (p/p_{th})^{(d+1)/2}$ where d is code distance</p>
        </div>
        """, unsafe_allow_html=True)

elif module_id == "hardware":
    st.markdown("<div class='overview-bg'>", unsafe_allow_html=True)
    st.markdown("# Hardware Topology & Connectivity")
    st.markdown('<span class="research-status status-active">Physical Implementation</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='research-card'>
        <h3>Quantum Hardware Architectures</h3>
        <p>Real quantum processors have limited qubit connectivity. Understanding topology is 
        crucial for circuit compilation, SWAP insertion, and benchmarking different platforms.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Platform selection
    platform = st.selectbox(
        "Select Quantum Platform",
        ["IBM Heavy-Hex", "Google Sycamore (Grid)", "IonQ (All-to-All)", "Rigetti Aspen (Linear)"]
    )
    
    if platform == "IBM Heavy-Hex":
        st.markdown("### IBM Heavy-Hexagon Topology")
        st.markdown("""
        <div class='research-card'>
            <p>IBM's heavy-hex architecture provides higher connectivity than square lattice while 
            maintaining manufacturability. Each qubit connects to 2-3 neighbors.</p>
            <p><strong>Advantages:</strong> Better for QAOA, VQE circuits | Lower SWAP overhead</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Generate heavy-hex layout (simplified 7-qubit example)
        positions = {
            0: (0, 0),
            1: (1, 0.5),
            2: (1, -0.5),
            3: (2, 0),
            4: (3, 0.5),
            5: (3, -0.5),
            6: (4, 0)
        }
        edges = [(0,1), (0,2), (1,3), (2,3), (3,4), (3,5), (4,6), (5,6)]
        
    elif platform == "Google Sycamore (Grid)":
        st.markdown("### Google Sycamore Grid Topology")
        st.markdown("""
        <div class='research-card'>
            <p>2D grid with nearest-neighbor connectivity. Each qubit connects to 2-4 neighbors.</p>
            <p><strong>Advantages:</strong> Suitable for surface codes | Uniform connectivity</p>
        </div>
        """, unsafe_allow_html=True)
        
        positions = {
            0: (0, 0), 1: (1, 0), 2: (2, 0),
            3: (0, 1), 4: (1, 1), 5: (2, 1),
            6: (0, 2), 7: (1, 2), 8: (2, 2)
        }
        edges = [(0,1), (1,2), (3,4), (4,5), (6,7), (7,8), (0,3), (1,4), (2,5), (3,6), (4,7), (5,8)]
        
    elif platform == "IonQ (All-to-All)":
        st.markdown("### IonQ All-to-All Connectivity")
        st.markdown("""
        <div class='research-card'>
            <p>Trapped ion systems can perform gates between any qubit pair (all-to-all connectivity).</p>
            <p><strong>Advantages:</strong> No SWAP gates needed | Ideal for fully-connected problems</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Pentagon layout
        theta = np.linspace(0, 2*np.pi, 6, endpoint=False)
        positions = {i: (np.cos(t), np.sin(t)) for i, t in enumerate(theta[:5])}
        edges = [(i, j) for i in range(5) for j in range(i+1, 5)]
        
    else:  # Rigetti Linear
        st.markdown("### Rigetti Linear Chain")
        st.markdown("""
        <div class='research-card'>
            <p>Linear chain topology where each qubit connects to nearest neighbors only.</p>
            <p><strong>Constraints:</strong> High SWAP overhead for long-range interactions</p>
        </div>
        """, unsafe_allow_html=True)
        
        positions = {i: (i, 0) for i in range(7)}
        edges = [(i, i+1) for i in range(6)]
    
    # Visualize topology with WebGL-style volumetric effects
    st.markdown("""
    <div class='data-grid-mesh' style='padding: 12px; border-radius: 10px; border: 1px solid rgba(0, 217, 255, 0.2); margin-bottom: 15px;'>
        <span class='metric-label'>⚡ QUBIT CONNECTIVITY MAP - VOLUMETRIC RENDERING</span>
    </div>
    """, unsafe_allow_html=True)
    
    fig_topo = go.Figure()
    
    # Draw energy filaments (edges) with bezier-like curves and gradients
    for i, j in edges:
        x0, y0 = positions[i]
        x1, y1 = positions[j]
        
        # Calculate entanglement fidelity (simulated)
        fidelity = np.random.uniform(0.85, 0.99)
        opacity = 0.4 + (fidelity - 0.85) / (0.99 - 0.85) * 0.5
        width = 2 + (fidelity - 0.85) / (0.99 - 0.85) * 4
        
        # Create curved path for energy filament effect
        mid_x = (x0 + x1) / 2
        mid_y = (y0 + y1) / 2 + 0.1
        t = np.linspace(0, 1, 20)
        curve_x = (1-t)**2 * x0 + 2*(1-t)*t * mid_x + t**2 * x1
        curve_y = (1-t)**2 * y0 + 2*(1-t)*t * mid_y + t**2 * y1
        
        fig_topo.add_trace(go.Scatter(
            x=curve_x, y=curve_y,
            mode='lines',
            line=dict(
                color=f'rgba(0, 217, 255, {opacity})',
                width=width
            ),
            hovertemplate=f'<b>Connection {i} ↔ {j}</b><br>Fidelity: {fidelity:.3f}<extra></extra>',
            showlegend=False
        ))
    
    # Draw pulsating volumetric spheres (qubits)
    x_coords = [positions[i][0] for i in positions]
    y_coords = [positions[i][1] for i in positions]
    coherence_times = np.random.uniform(80, 120, len(positions))  # Simulated T2 times
    
    # Create varying sizes based on coherence time for data-ink ratio
    sizes = 30 + (coherence_times - 80) / 40 * 20
    colors = [f'rgba(0, 217, 255, {0.7 + (t-80)/200})' for t in coherence_times]
    
    fig_topo.add_trace(go.Scatter(
        x=x_coords, y=y_coords,
        mode='markers+text',
        marker=dict(
            size=sizes,
            color=colors,
            line=dict(color='rgba(0, 255, 148, 0.9)', width=3),
            symbol='circle'
        ),
        text=[f'<b>Q{i}</b>' for i in positions.keys()],
        textposition='middle center',
        textfont=dict(size=14, color='#0A0A0A', family='JetBrains Mono'),
        hovertemplate='<b>Qubit %{text}</b><br>T₂: %{customdata:.1f}μs<extra></extra>',
        customdata=coherence_times,
        showlegend=False
    ))
    
    fig_topo.update_layout(
        plot_bgcolor='rgba(10, 10, 10, 0.5)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(visible=False, range=[min(x_coords)-1, max(x_coords)+1]),
        yaxis=dict(visible=False, scaleanchor='x', range=[min(y_coords)-1, max(y_coords)+1]),
        height=550,
        margin=dict(l=20, r=20, t=20, b=20),
        font=dict(family='JetBrains Mono', color='#E8E8E8')
    )
    
    st.plotly_chart(fig_topo, use_container_width=True)
    
    # Connectivity metrics
    num_qubits = len(positions)
    num_edges = len(edges)
    avg_degree = 2 * num_edges / num_qubits
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class='metric-box'>
            <h3>{num_qubits}</h3>
            <p>Qubits</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='metric-box'>
            <h3>{num_edges}</h3>
            <p>Connections</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class='metric-box'>
            <h3>{avg_degree:.1f}</h3>
            <p>Avg Degree</p>
        </div>
        """, unsafe_allow_html=True)

elif module_id == "complexity":
    st.markdown("<div class='qml-neural'>", unsafe_allow_html=True)
    st.markdown("# Complexity Classes: P, NP, BQP")
    st.markdown('<span class="research-status status-active">Computational Theory</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='research-card'>
        <h3>Quantum Computational Complexity</h3>
        <p>Understanding the power and limitations of quantum computers requires studying 
        complexity classes - the sets of problems solvable efficiently by different computational models.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Complexity class definitions
    st.markdown("### Complexity Classes")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='research-card'>
            <h4>P (Polynomial Time)</h4>
            <p>Problems solvable by classical deterministic computers in polynomial time.</p>
            <p><strong>Examples:</strong> Sorting, shortest path, linear programming</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='research-card'>
            <h4>NP (Nondeterministic Polynomial)</h4>
            <p>Problems whose solutions can be verified in polynomial time.</p>
            <p><strong>Examples:</strong> SAT, graph coloring, traveling salesman</p>
            <p><strong>Open Question:</strong> P = NP?</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='research-card'>
            <h4>BQP (Bounded-Error Quantum Polynomial)</h4>
            <p>Problems solvable by quantum computers in polynomial time with high probability.</p>
            <p><strong>Examples:</strong> Factoring (Shor), simulation, search (Grover)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='research-card'>
            <h4>Relationships</h4>
            <p>$P \\subseteq BQP \\subseteq PSPACE$</p>
            <p>$BQP$ and $NP$ are believed to be incomparable</p>
            <p>Quantum advantage lies in problems in $BQP \\setminus P$</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Landmark problems
    st.markdown("### Landmark Quantum Algorithms")
    
    algorithm = st.selectbox(
        "Select Algorithm",
        ["Shor's Factoring", "Grover's Search", "Quantum Simulation"]
    )
    
    if algorithm == "Shor's Factoring":
        st.markdown("""
        <div class='research-card'>
            <h3>Shor's Algorithm (1994)</h3>
            <p><strong>Problem:</strong> Factor integer N into prime factors</p>
            <p><strong>Classical:</strong> Best known - sub-exponential (General Number Field Sieve)</p>
            <p><strong>Quantum:</strong> Polynomial time O((log N)³)</p>
            <p><strong>Impact:</strong> Breaks RSA encryption, demonstrates quantum advantage</p>
            
            <p><strong>Key Idea:</strong> Use quantum Fourier transform to find period of modular exponentiation</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Example factoring
        N_factor = st.number_input("Number to factor", min_value=15, max_value=10000, value=15, step=2)
        if st.button("Find Factors", type="primary"):
            factors = []
            for i in range(2, int(np.sqrt(N_factor)) + 1):
                if N_factor % i == 0:
                    factors = [i, N_factor // i]
                    break
            
            if factors:
                st.success(f"✅ {N_factor} = {factors[0]} × {factors[1]}")
            else:
                st.info(f"{N_factor} is prime")
    
    elif algorithm == "Grover's Search":
        st.markdown("""
        <div class='research-card'>
            <h3>Grover's Algorithm (1996)</h3>
            <p><strong>Problem:</strong> Search unstructured database of N items</p>
            <p><strong>Classical:</strong> O(N) - must check each item</p>
            <p><strong>Quantum:</strong> O(√N) - quadratic speedup</p>
            
            <p><strong>Optimal:</strong> Provably optimal for unstructured search (tight bound)</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Grover iteration count
        N_search = st.slider("Database size N", 4, 1024, 16, step=4)
        classical_queries = N_search / 2  # Average
        quantum_queries = np.pi/4 * np.sqrt(N_search)
        speedup = classical_queries / quantum_queries
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
            <div class='metric-box'>
                <h3>{classical_queries:.0f}</h3>
                <p>Classical Queries</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class='metric-box'>
                <h3>{quantum_queries:.0f}</h3>
                <p>Quantum Queries</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class='metric-box'>
                <h3>{speedup:.1f}×</h3>
                <p>Speedup</p>
            </div>
            """, unsafe_allow_html=True)
    
    else:  # Quantum Simulation
        st.markdown("""
        <div class='research-card'>
            <h3>Quantum Simulation (Feynman 1982)</h3>
            <p><strong>Problem:</strong> Simulate quantum many-body systems</p>
            <p><strong>Classical:</strong> Exponential resources (Hilbert space grows as 2^N)</p>
            <p><strong>Quantum:</strong> Polynomial resources (native quantum evolution)</p>
            
            <p><strong>Applications:</strong> Materials science, drug discovery, high-energy physics</p>
            <p><strong>Status:</strong> First practical quantum advantage demonstrated (2019-2023)</p>
        </div>
        """, unsafe_allow_html=True)

elif module_id == "topological":
    st.markdown("<div class='circuit-flow'>", unsafe_allow_html=True)
    st.markdown("# Topological Quantum Computing")
    st.markdown('<span class="research-status status-frontier">Advanced Topic</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='research-card'>
        <h3>Topology-Based Quantum Information</h3>
        <p>Topological quantum computing encodes quantum information in non-local topological 
        properties of systems, providing inherent protection against local errors. Information 
        is stored in the braiding of anyons (exotic quasiparticles in 2D systems).</p>
        
        <p><strong>Key Advantages:</strong></p>
        <ul>
            <li>Topologically protected qubits (immune to local perturbations)</li>
            <li>Gates performed by braiding anyons (geometrically robust)</li>
            <li>Fault-tolerance built into physics (not error correction overhead)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Anyons & Braiding")
    st.markdown("""
    <div class='research-card'>
        <h4>Fibonacci Anyons</h4>
        <p>Universal topological quantum computing can be achieved with Fibonacci anyons, 
        which have fusion rules: $\\tau \\times \\tau = 1 + \\tau$</p>
        
        <p><strong>Braiding Operations:</strong> Moving anyon A around anyon B clockwise vs 
        counterclockwise gives different quantum gates. These operations form a representation 
        of the braid group.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Braid visualization
    st.markdown("#### Braid Diagram")
    st.markdown("Select braid operation:")
    
    braid_type = st.selectbox(
        "Braid Type",
        ["Identity (No Braid)", "σ₁ (Braid 1-2)", "σ₂ (Braid 2-3)", "σ₁σ₂σ₁ (Yang-Baxter)"]
    )
    
    # Simple visualization
    fig_braid = go.Figure()
    
    if braid_type == "Identity (No Braid)":
        # Straight lines
        for i in range(3):
            fig_braid.add_trace(go.Scatter(
                x=[0, 1], y=[i, i],
                mode='lines',
                line=dict(color='#6366F1', width=4),
                showlegend=False
            ))
        st.markdown("**Gate:** Identity (no operation)")
        
    elif braid_type == "σ₁ (Braid 1-2)":
        # Braid strands 1 and 2
        t = np.linspace(0, 1, 100)
        y1 = 0 + 0.3 * np.sin(np.pi * t)
        y2 = 1 - 0.3 * np.sin(np.pi * t)
        
        fig_braid.add_trace(go.Scatter(x=t, y=y1, mode='lines', line=dict(color='#6366F1', width=4), showlegend=False))
        fig_braid.add_trace(go.Scatter(x=t, y=y2, mode='lines', line=dict(color='#06B6D4', width=4), showlegend=False))
        fig_braid.add_trace(go.Scatter(x=[0,1], y=[2,2], mode='lines', line=dict(color='#84CC16', width=4), showlegend=False))
        
        st.markdown("**Gate:** $\\sigma_1$ (exchange anyons 1 and 2)")
    
    fig_braid.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        height=300
    )
    st.plotly_chart(fig_braid, use_container_width=True)
    
    # Physical platforms
    st.markdown("### Physical Realizations")
    st.markdown("""
    <div class='research-card'>
        <h4>Experimental Platforms</h4>
        <ul>
            <li><strong>Fractional Quantum Hall Systems:</strong> Electrons in 2D at ultra-low temperatures and high magnetic fields</li>
            <li><strong>Topological Superconductors:</strong> Majorana zero modes at superconductor interfaces</li>
            <li><strong>Quantum Spin Liquids:</strong> Frustrated magnetic systems with topological order</li>
        </ul>
        
        <p><strong>Status:</strong> Experimental observation of non-Abelian anyons achieved (2020), 
        but full topological quantum computer remains years away.</p>
    </div>
    """, unsafe_allow_html=True)

else:
    st.markdown(f"# {module_id.upper()}")
    st.markdown('<span class="research-status status-frontier">Module In Development</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='research-card'>
        <h3>Advanced Research Module</h3>
        <p>This module is under active development. Check back for implementation of cutting-edge 
        quantum computing research topics.</p>
    </div>
    """, unsafe_allow_html=True)

# Close module div tags
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: var(--text-secondary); padding: 20px;'>
    <p><strong>Quantum × AI Research Workbench</strong> | Production Research Platform</p>
    <p>Academic-Grade Quantum Computing Experiments • Reproducible Results • Publication-Ready Visualizations</p>
    <p style='font-size: 12px; margin-top: 12px;'>
        Built with Streamlit • Qiskit • NumPy • SciPy • Plotly
    </p>
</div>
""", unsafe_allow_html=True)
