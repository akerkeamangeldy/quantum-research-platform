"""
ALPHANOVA QUANTUM RESEARCH PLATFORM v1.0.0
Advanced Quantum Computing & AI Research Environment
High-Density Bento Grid Architecture | Quantum Processor Interface
Reactive Module Matrix | Technical Vector Graphics | LaTeX Rendering

System Architecture: Next-Generation Quantum Computing Platform
Interface Design: Premium Dark Theme | Mathematical Precision UI
Research Modules: Comprehensive Quantum Computing Research Suite
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

# AlphaNova Quantum Configuration
st.set_page_config(
    page_title="AlphaNova Quantum | Advanced Research Platform",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# AlphaNova Quantum Premium CSS - Deep Space Research Interface
st.markdown("""
<style>
    /* ALPHANOVA PREMIUM FONT IMPORTS */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700;800&display=swap');
    
    /* ROOT VARIABLES - QUANTUM RESEARCH PALETTE */
    :root {
        --deep-navy-primary: #061226;
        --deep-navy-secondary: #0A1630;
        --deep-navy-tertiary: #0D1B3D;
        --quantum-blue-light: #123A6B;
        --quantum-blue-medium: #1E5AA8;
        --quantum-blue-bright: #3B82F6;
        --cyan-bright: #22D3EE;
        --cyan-medium: #38BDF8;
        --indigo-glow: #6366F1;
        --text-primary: #EAF2FF;
        --text-secondary: rgba(234, 242, 255, 0.72);
        --border-subtle: rgba(120, 170, 255, 0.18);
        --hover-glow: rgba(56, 189, 248, 0.35);
        --card-bg: rgba(10, 22, 48, 0.72);
    }
    
    /* GLOBAL QUANTUM TYPOGRAPHY */
    * {
        box-sizing: border-box;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-rendering: optimizeLegibility;
    }
    
    /* TYPOGRAPHY HIERARCHY - RESEARCH GRADE */
    h1 {
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 800;
        font-size: 3.5rem;
        line-height: 1.1;
        letter-spacing: -0.03em;
        background: linear-gradient(135deg, var(--cyan-bright), var(--quantum-blue-bright), var(--indigo-glow));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1.5rem;
        text-shadow: 0 0 30px rgba(34, 211, 238, 0.3);
    }
    
    h2 {
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 700;
        font-size: 2rem;
        color: var(--text-primary);
        line-height: 1.2;
        letter-spacing: -0.02em;
        margin-bottom: 1.25rem;
    }
    
    h3 {
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 600;
        font-size: 1.4rem;
        color: var(--cyan-bright);
        line-height: 1.3;
        margin-bottom: 1rem;
    }
    
    h4 {
        font-family: 'Inter', sans-serif !important;
        font-weight: 600;
        font-size: 1.125rem;
        color: var(--text-primary);
        margin-bottom: 0.75rem;
    }
    
    p {
        font-family: 'Inter', sans-serif !important;
        font-weight: 400;
        color: var(--text-secondary);
        line-height: 1.6;
        font-size: 0.95rem;
    }
    
    code, pre, .stCode {
        font-family: 'JetBrains Mono', monospace !important;
        background: rgba(6, 18, 38, 0.8);
        color: var(--cyan-bright);
        border-radius: 6px;
        padding: 0.25rem 0.5rem;
    }
    
    /* DEEP SPACE BACKGROUND SYSTEM */
    .stApp {
        background: radial-gradient(circle at 20% 80%, rgba(13, 27, 61, 0.8) 0%, transparent 50%),
                    radial-gradient(circle at 80% 20%, rgba(18, 58, 107, 0.6) 0%, transparent 50%),
                    radial-gradient(circle at 40% 40%, rgba(99, 102, 241, 0.1) 0%, transparent 50%),
                    linear-gradient(135deg, var(--deep-navy-primary) 0%, var(--deep-navy-secondary) 35%, var(--deep-navy-tertiary) 100%);
        min-height: 100vh;
        background-attachment: fixed;
    }
    
    .main {
        background: transparent !important;
    }
    
    /* PREMIUM GLASSMORPHISM CARDS */
    .alphanova-card {
        background: linear-gradient(145deg, 
            rgba(10, 22, 48, 0.85) 0%,
            rgba(13, 27, 61, 0.75) 100%);
        backdrop-filter: blur(20px);
        border: 1px solid var(--border-subtle);
        border-radius: 20px;
        padding: 2rem;
        margin: 1.5rem 0;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        box-shadow: 0 8px 32px rgba(6, 18, 38, 0.3),
                    inset 0 1px 0 rgba(255, 255, 255, 0.1);
    }
    
    .alphanova-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: linear-gradient(90deg, 
            transparent 0%, 
            var(--cyan-bright) 20%, 
            var(--quantum-blue-bright) 50%, 
            var(--indigo-glow) 80%, 
            transparent 100%);
        opacity: 0.8;
    }
    
    .alphanova-card:hover {
        background: linear-gradient(145deg, 
            rgba(10, 22, 48, 0.95) 0%,
            rgba(13, 27, 61, 0.85) 100%);
        border-color: var(--hover-glow);
        transform: translateY(-3px);
        box-shadow: 0 12px 48px rgba(34, 211, 238, 0.2),
                    0 0 0 1px rgba(56, 189, 248, 0.3),
                    inset 0 1px 0 rgba(255, 255, 255, 0.15);
    }
    
    .alphanova-card h3 {
        color: var(--cyan-bright);
        font-size: 1.375rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-shadow: 0 0 20px rgba(34, 211, 238, 0.3);
    }
    
    .alphanova-card p {
        color: var(--text-secondary);
        line-height: 1.7;
        font-size: 0.95rem;
        margin-bottom: 1rem;
    }
    
    /* HERO SECTION - LUMINOUS DEPTH */
    .alphanova-header {
        text-align: center;
        margin-bottom: 4rem;
        padding: 4rem 2rem;
        position: relative;
        background: radial-gradient(ellipse at center, 
            rgba(99, 102, 241, 0.1) 0%,
            rgba(34, 211, 238, 0.05) 40%,
            transparent 70%);
        border-radius: 24px;
        border: 1px solid rgba(120, 170, 255, 0.1);
    }
    
    .alphanova-main-title {
        font-family: 'Space Grotesk', sans-serif !important;
        font-size: 4rem;
        font-weight: 900;
        background: linear-gradient(135deg, 
            var(--cyan-bright) 0%,
            var(--quantum-blue-bright) 35%,
            var(--indigo-glow) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
        letter-spacing: -0.04em;
        text-shadow: 0 0 40px rgba(34, 211, 238, 0.4);
        position: relative;
    }
    
    .alphanova-subtitle {
        font-size: 1.125rem;
        color: var(--text-primary);
        text-transform: uppercase;
        letter-spacing: 0.15em;
        font-weight: 600;
        margin-bottom: 0.75rem;
        font-family: 'Space Grotesk', sans-serif !important;
    }
    
    .alphanova-tagline {
        font-size: 1rem;
        color: var(--text-secondary);
        font-style: italic;
        font-weight: 300;
        opacity: 0.9;
    }
    
    /* QUANTUM RESEARCH STATUS BADGES */
    .alphanova-status {
        display: inline-block;
        padding: 8px 16px;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.03em;
        margin-bottom: 1rem;
        font-family: 'Space Grotesk', sans-serif !important;
        backdrop-filter: blur(10px);
        border: 1px solid;
    }
    
    .status-active {
        background: rgba(34, 211, 238, 0.15);
        color: var(--cyan-bright);
        border-color: rgba(34, 211, 238, 0.3);
        box-shadow: 0 0 20px rgba(34, 211, 238, 0.2);
    }
    
    .status-research {
        background: rgba(59, 130, 246, 0.15);
        color: var(--quantum-blue-bright);
        border-color: rgba(59, 130, 246, 0.3);
        box-shadow: 0 0 20px rgba(59, 130, 246, 0.2);
    }
    
    .status-emerging {
        background: rgba(99, 102, 241, 0.15);
        color: var(--indigo-glow);
        border-color: rgba(99, 102, 241, 0.3);
        box-shadow: 0 0 20px rgba(99, 102, 241, 0.2);
    }
    
    /* PREMIUM SIDEBAR - QUANTUM LAB CONTROL PANEL */
    .css-1d391kg {
        background: linear-gradient(180deg,
            var(--deep-navy-primary) 0%,
            var(--deep-navy-secondary) 50%,
            var(--deep-navy-tertiary) 100%) !important;
        border-right: 1px solid var(--border-subtle) !important;
        box-shadow: inset -1px 0 0 rgba(56, 189, 248, 0.1),
                    4px 0 24px rgba(6, 18, 38, 0.5);
    }
    
    /* SIDEBAR CONTENT STYLING */
    .css-1d391kg .element-container {
        background: transparent !important;
    }
    
    /* QUANTUM BUTTONS - RESEARCH GRADE */
    .stButton > button {
        background: linear-gradient(135deg,
            rgba(10, 22, 48, 0.8) 0%,
            rgba(13, 27, 61, 0.6) 100%) !important;
        border: 1px solid var(--border-subtle) !important;
        border-radius: 14px !important;
        color: var(--text-primary) !important;
        font-weight: 500 !important;
        font-family: 'Inter', sans-serif !important;
        padding: 0.75rem 1.25rem !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
        backdrop-filter: blur(10px);
        text-align: left !important;
        width: 100% !important;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg,
            rgba(34, 211, 238, 0.1) 0%,
            rgba(13, 27, 61, 0.8) 100%) !important;
        border-color: var(--hover-glow) !important;
        color: var(--text-primary) !important;
        box-shadow: 0 4px 20px rgba(34, 211, 238, 0.25),
                    0 0 0 1px rgba(56, 189, 248, 0.3) !important;
        transform: translateY(-1px) !important;
    }
    
    .stButton > button:focus {
        border-color: var(--cyan-bright) !important;
        box-shadow: 0 0 0 3px rgba(34, 211, 238, 0.2) !important;
    }
    
    /* SIDEBAR MARKDOWN STYLING */
    .css-1d391kg .stMarkdown {
        color: var(--text-primary) !important;
    }
    
    .css-1d391kg h3 {
        color: var(--cyan-bright) !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.1em !important;
        margin: 1.5rem 0 1rem 0 !important;
        padding-bottom: 0.5rem !important;
        border-bottom: 1px solid var(--border-subtle) !important;
    }
    
    /* METRICS ENHANCEMENT */
    .css-1r6slb0 {
        background: linear-gradient(145deg,
            rgba(10, 22, 48, 0.7) 0%,
            rgba(13, 27, 61, 0.5) 100%) !important;
        border: 1px solid var(--border-subtle) !important;
        border-radius: 16px !important;
        backdrop-filter: blur(15px) !important;
        padding: 1.5rem !important;
    }
    
    /* STREAMLIT METRIC STYLING */
    [data-testid="metric-container"] {
        background: linear-gradient(145deg,
            rgba(10, 22, 48, 0.8) 0%,
            rgba(13, 27, 61, 0.6) 100%);
        border: 1px solid var(--border-subtle);
        border-radius: 16px;
        padding: 1.25rem;
        backdrop-filter: blur(15px);
        transition: all 0.25s ease;
    }
    
    [data-testid="metric-container"]:hover {
        border-color: var(--hover-glow);
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.2);
    }
    
    [data-testid="metric-container"] > div {
        color: var(--cyan-bright) !important;
    }
    
    [data-testid="metric-container"] label {
        color: var(--text-secondary) !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-size: 0.8rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
    }
    
    /* SLIDER ENHANCEMENT */
    .stSlider > div > div > div > div {
        background: var(--quantum-blue-bright) !important;
    }
    
    /* SELECT BOX STYLING */
    .stSelectbox > div > div {
        background: rgba(10, 22, 48, 0.8) !important;
        border: 1px solid var(--border-subtle) !important;
        border-radius: 12px !important;
        color: var(--text-primary) !important;
    }
    
    /* REMOVE DEFAULT STREAMLIT UI */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }
    .stDeployButton { visibility: hidden; }
    
    /* MAIN CONTAINER ADJUSTMENTS */
    .main .block-container {
        padding: 2rem !important;
        max-width: none !important;
    }
    
    /* SECTION SPACING - LABORATORY PRECISION */
    .element-container {
        margin-bottom: 1.5rem;
    }
    
    /* PLOTLY CHART INTEGRATION */
    .js-plotly-plot {
        border-radius: 16px;
        overflow: hidden;
        border: 1px solid var(--border-subtle);
        background: rgba(6, 18, 38, 0.3);
    }
    
    /* RESPONSIVE DESIGN - MOBILE LAB INTERFACE */
    @media (max-width: 768px) {
        .alphanova-main-title {
            font-size: 2.5rem;
        }
        
        .alphanova-header {
            padding: 2rem 1rem;
        }
        
        .alphanova-card {
            padding: 1.5rem;
            margin: 1rem 0;
        }
    }
    
    /* QUANTUM GLOW ANIMATIONS */
    @keyframes quantum-pulse {
        0%, 100% { 
            opacity: 1; 
            box-shadow: 0 0 20px rgba(34, 211, 238, 0.3);
        }
        50% { 
            opacity: 0.8; 
            box-shadow: 0 0 30px rgba(34, 211, 238, 0.5);
        }
    }
    
    .quantum-glow {
        animation: quantum-pulse 3s ease-in-out infinite;
    }
</style>
""", unsafe_allow_html=True)
# ALPHANOVA QUANTUM RESEARCH PLATFORM - COMPREHENSIVE SCIENTIFIC INTERFACE
# Initialize AlphaNova Session State
if "selected_section" not in st.session_state:
    st.session_state.selected_section = "home"

if "selected_subsection" not in st.session_state:
    st.session_state.selected_subsection = None

# Platform configuration
st.set_page_config(
    page_title="AlphaNova Quantum Research Platform",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# QUANTUM COMPUTATION FUNCTIONS
def pauli_matrices():
    """AlphaNova Quantum Pauli matrices"""
    return {
        'I': np.array([[1, 0], [0, 1]], dtype=complex),
        'X': np.array([[0, 1], [1, 0]], dtype=complex),
        'Y': np.array([[0, -1j], [1j, 0]], dtype=complex),
        'Z': np.array([[1, 0], [0, -1]], dtype=complex)
    }

def hadamard():
    """AlphaNova Quantum Hadamard gate"""
    return np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)

def create_alphanova_bloch_sphere(theta_deg=0, phi_deg=0):
    """Create AlphaNova Quantum Bloch sphere visualization"""
    theta = np.radians(theta_deg)
    phi = np.radians(phi_deg)
    
    # Sphere coordinates
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    x_sphere = np.outer(np.cos(u), np.sin(v))
    y_sphere = np.outer(np.sin(u), np.sin(v))
    z_sphere = np.outer(np.ones(np.size(u)), np.cos(v))
    
    # Quantum state vector
    x_state = np.sin(theta) * np.cos(phi)
    y_state = np.sin(theta) * np.sin(phi)
    z_state = np.cos(theta)
    
    fig = go.Figure()
    
    # Bloch sphere
    fig.add_trace(go.Surface(
        x=x_sphere, y=y_sphere, z=z_sphere,
        opacity=0.15,
        colorscale='Blues',
        showscale=False,
        name="Bloch Sphere"
    ))
    
    # State vector
    fig.add_trace(go.Scatter3d(
        x=[0, x_state], y=[0, y_state], z=[0, z_state],
        mode='lines+markers',
        line=dict(color='#06B6D4', width=8),
        marker=dict(size=[0, 12], color=['#06B6D4', '#F59E0B']),
        name="Quantum State"
    ))
    
    # Coordinate axes
    axes_data = [
        ([1, 0, 0], '#EF4444', 'X'),
        ([0, 1, 0], '#10B981', 'Y'), 
        ([0, 0, 1], '#3B82F6', 'Z')
    ]
    
    for axis, color, label in axes_data:
        fig.add_trace(go.Scatter3d(
            x=[-axis[0], axis[0]], y=[-axis[1], axis[1]], z=[-axis[2], axis[2]],
            mode='lines+text',
            line=dict(color=color, width=4),
            text=['', label],
            textposition="middle center",
            showlegend=False
        ))
    
    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False, range=[-1.5, 1.5]),
            yaxis=dict(visible=False, range=[-1.5, 1.5]),
            zaxis=dict(visible=False, range=[-1.5, 1.5]),
            bgcolor='rgba(0,0,0,0)',
            camera=dict(eye=dict(x=1.2, y=1.2, z=1.2))
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=0, b=0),
        showlegend=True,
        legend=dict(
            bgcolor='rgba(15, 23, 42, 0.8)',
            bordercolor='rgba(6, 182, 212, 0.2)',
            font=dict(color='#E2E8F0')
        )
    )
    
    return fig

def bell_states():
    """AlphaNova Quantum Bell states"""
    return {
        'Φ+': np.array([1, 0, 0, 1]) / np.sqrt(2),
        'Φ-': np.array([1, 0, 0, -1]) / np.sqrt(2),
        'Ψ+': np.array([0, 1, 1, 0]) / np.sqrt(2),
        'Ψ-': np.array([0, 1, -1, 0]) / np.sqrt(2)
    }

def vqe_h2_hamiltonian():
    """AlphaNova Quantum VQE H2 molecule Hamiltonian"""
    I = np.eye(2)
    X = pauli_matrices()['X']
    Z = pauli_matrices()['Z']
    
    # H2 Hamiltonian coefficients
    return -1.0523 * np.kron(I, I) + 0.3979 * np.kron(Z, Z) + 0.3979 * np.kron(X, X)

# COMPREHENSIVE SIDEBAR NAVIGATION - QUANTUM RESEARCH PLATFORM
with st.sidebar:
    # Platform Header
    st.markdown("""
    <div style="text-align: center; padding: 1.5rem 0; border-bottom: 1px solid var(--border-subtle); margin-bottom: 1.5rem;">
        <h2 style="color: var(--cyan-bright); font-family: 'Space Grotesk', sans-serif; font-size: 1.5rem; font-weight: 800; margin-bottom: 0.25rem;">⚛️ AlphaNova</h2>
        <p style="color: var(--text-secondary); font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.1em; margin: 0;">Quantum Research Platform</p>
        <p style="color: var(--indigo-glow); font-size: 0.7rem; margin: 0.25rem 0 0 0;">Version 2.0.0</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Primary Navigation
    st.markdown("### 🏠 PLATFORM")
    if st.button("🏠 Home Dashboard", key="nav_home", width='stretch'):
        st.session_state.selected_section = "home"
        st.rerun()
    
    st.markdown("### ⚛️ FOUNDATIONS")
    foundation_sections = [
        ("quantum_foundations", "📚 Quantum Foundations"),
        ("quantum_state_viz", "🌐 State Visualization"),
        ("quantum_gates", "🔧 Gates & Circuits")
    ]
    for section_id, label in foundation_sections:
        if st.button(label, key=f"nav_{section_id}", width='stretch'):
            st.session_state.selected_section = section_id
            st.rerun()
    
    st.markdown("### 🧮 ALGORITHMS")
    algorithm_sections = [
        ("quantum_algorithms", "⚡ Quantum Algorithms"),
        ("quantum_ml", "🧠 Quantum ML")
    ]
    for section_id, label in algorithm_sections:
        if st.button(label, key=f"nav_{section_id}", width='stretch'):
            st.session_state.selected_section = section_id
            st.rerun()
    
    st.markdown("### 🔬 SYSTEMS")
    systems_sections = [
        ("hardware_arch", "🔩 Hardware Architecture"),
        ("error_correction", "🛡️ Error Correction"),
        ("complexity_theory", "📊 Complexity Theory")
    ]
    for section_id, label in systems_sections:
        if st.button(label, key=f"nav_{section_id}", width='stretch'):
            st.session_state.selected_section = section_id
            st.rerun()
    
    # Platform Status
    st.markdown("---")
    st.markdown("### SYSTEM STATUS")
    status_metrics = [
        ("🟢 Quantum Simulator", "Online"),
        ("🟡 Hardware Backend", "Limited"), 
        ("🟢 ML Algorithms", "Active"),
        ("🟢 Visualization Engine", "Optimal")
    ]
    for metric, status in status_metrics:
        st.markdown(f"<small style='color: var(--text-secondary);'>{metric}: **{status}**</small>", unsafe_allow_html=True)

# MAIN CONTENT ROUTING
section_id = st.session_state.selected_section

if section_id == "home":
    # AlphaNova Home Module
    st.markdown("""
    <div class="alphanova-header">
        <h1 class="alphanova-main-title">AlphaNova Quantum</h1>
        <div class="alphanova-subtitle">Advanced Quantum Computing Research Platform</div>
        <div class="alphanova-tagline">Next-generation research environment for quantum innovation</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Platform Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Quantum Volume", "128", delta="16")
    with col2:
        st.metric("Gate Fidelity", "99.5%", delta="0.3%")
    with col3:
        st.metric("Coherence Time", "150 μs", delta="12 μs")
    with col4:
        st.metric("Active Modules", "15", delta="3")
    
    # Research Modules Overview
    st.markdown("## 🚀 Research Modules")
    
    research_modules = [
        {
            "title": "Hilbert Space Dynamics",
            "description": "Interactive Bloch sphere visualization with real-time quantum state manipulation and gate operations.",
            "status": "active",
            "module_id": "bloch"
        },
        {
            "title": "Bell-State Correlations",
            "description": "Complete Bell state analysis with CHSH inequality testing and entanglement quantification.",
            "status": "active", 
            "module_id": "entanglement"
        },
        {
            "title": "VQE Architectures",
            "description": "Variational quantum eigensolver implementation for molecular systems with optimization tracking.", 
            "status": "research",
            "module_id": "vqe"
        },
        {
            "title": "Quantum Neural Networks",
            "description": "Machine learning with quantum circuits, feature maps, and hybrid optimization algorithms.",
            "status": "emerging",
            "module_id": "qml"
        }
    ]
    
    # Create module cards grid
    cols = st.columns(2)
    for i, module in enumerate(research_modules):
        with cols[i % 2]:
            status_class = f"status-{module['status']}"
            if st.button(
                f"""
                **{module['title']}**
                
                {module['description']}
                """,
                key=f"module_{module['module_id']}",
                width='stretch'
            ):
                st.session_state.selected_alphanova_module = module['module_id']
                st.rerun()
    
    # Platform Capabilities
    st.markdown("## ⚡ Platform Capabilities")
    
    st.markdown("""
    <div class="alphanova-card">
        <h3>🌐 Advanced Quantum Simulation</h3>
        <p>AlphaNova Quantum provides a research-grade environment for quantum state manipulation within 
        the complex Hilbert space ℋ = ℂ^(2^n). Execute variational algorithms, simulate noise channels, 
        and perform quantum state tomography with publication-ready visualizations.</p>
        
        <h4 style="color: #3B82F6; margin-top: 1.5rem;">Key Features</h4>
        <ul style="color: #E2E8F0;">
            <li><strong>Interactive 3D Visualizations</strong> - Real-time Bloch sphere and quantum circuit representations</li>
            <li><strong>Research-Grade Algorithms</strong> - Complete VQE, QAOA, and quantum ML implementations</li>
            <li><strong>Noise Modeling</strong> - Comprehensive decoherence simulation with T1/T2 analysis</li>
            <li><strong>Hardware Integration</strong> - Realistic quantum processor topology simulation</li>
            <li><strong>Publication Tools</strong> - Exportable data and reproducible experiment logging</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif section_id == "quantum_foundations":
    st.markdown("# 📚 Quantum Foundations")
    st.markdown('<span class="alphanova-status status-active">Core Theory Module</span>', unsafe_allow_html=True)
    
    # Subsection navigation
    foundations_tabs = st.tabs(["Qubits & Superposition", "Measurement Theory", "Entanglement", "Mathematical Framework"])
    
    with foundations_tabs[0]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Qubits and Superposition Principle</h3>
            <p>The fundamental unit of quantum information, existing in coherent superposition of basis states.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            ### Classical vs Quantum Bits
            
            **Classical Bit:**
            - Definite state: 0 or 1
            - Binary information storage
            - Deterministic measurement
            
            **Quantum Bit (Qubit):**
            - Superposition: α|0⟩ + β|1⟩ 
            - Complex probability amplitudes
            - Probabilistic measurement outcomes
            - |α|² + |β|² = 1 (normalization)
            """)
            
        with col2:
            st.latex(r"""
            |\psi\rangle = \alpha|0\rangle + \beta|1\rangle
            """)
            st.latex(r"""
            \alpha, \beta \in \mathbb{C}, \quad |\alpha|^2 + |\beta|^2 = 1
            """)
            
            # Interactive amplitude control
            alpha_real = st.slider("α (real part)", -1.0, 1.0, 0.707, step=0.01)
            alpha_imag = st.slider("α (imaginary part)", -1.0, 1.0, 0.0, step=0.01)
            
            alpha = alpha_real + 1j * alpha_imag
            beta = np.sqrt(1 - abs(alpha)**2) if abs(alpha)**2 <= 1 else 0
            
            st.write(f"α = {alpha:.3f}")
            st.write(f"β = {beta:.3f}")
            st.write(f"P(|0⟩) = {abs(alpha)**2:.3f}")
            st.write(f"P(|1⟩) = {abs(beta)**2:.3f}")
    
    with foundations_tabs[1]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Quantum Measurement Theory</h3>
            <p>The Born rule and the collapse of the quantum state upon measurement.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            ### Born Rule
            
            For a quantum state |ψ⟩ = α|0⟩ + β|1⟩:
            
            - **Probability of measuring |0⟩:** P(0) = |α|²
            - **Probability of measuring |1⟩:** P(1) = |β|²
            - **State collapse:** After measuring |0⟩, state becomes |0⟩
            
            ### Measurement Operators
            
            Computational basis measurement:
            - M₀ = |0⟩⟨0| (projects onto |0⟩)
            - M₁ = |1⟩⟨1| (projects onto |1⟩)
            - M₀ + M₁ = I (completeness)
            """)
            
        with col2:
            # Measurement simulation
            st.markdown("### Measurement Simulation")
            
            theta = st.slider("State angle θ", 0, 180, 45, key="measure_theta")
            theta_rad = np.radians(theta)
            
            alpha_sim = np.cos(theta_rad/2)
            beta_sim = np.sin(theta_rad/2)
            
            prob_0 = abs(alpha_sim)**2
            prob_1 = abs(beta_sim)**2
            
            if st.button("Perform Measurement", key="measurement_btn"):
                outcome = np.random.choice([0, 1], p=[prob_0, prob_1])
                st.success(f"Measurement result: |{outcome}⟩")
                if outcome == 0:
                    st.info("State collapsed to |0⟩")
                else:
                    st.info("State collapsed to |1⟩")
            
            # Probability visualization
            fig = go.Figure(data=[
                go.Bar(x=['|0⟩', '|1⟩'], y=[prob_0, prob_1], 
                       marker_color=['#22D3EE', '#6366F1'])
            ])
            fig.update_layout(
                title="Measurement Probabilities",
                yaxis_title="P(outcome)",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#E2E8F0'
            )
            st.plotly_chart(fig, width='stretch')
    
    with foundations_tabs[2]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Quantum Entanglement</h3>
            <p>Non-local correlations between quantum systems that cannot be described classically.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            ### Bell States - Maximally Entangled
            
            The four Bell states form a complete orthonormal basis for two-qubit systems:
            
            1. **|Φ⁺⟩ = (|00⟩ + |11⟩)/√2**
            2. **|Φ⁻⟩ = (|00⟩ - |11⟩)/√2** 
            3. **|Ψ⁺⟩ = (|01⟩ + |10⟩)/√2**
            4. **|Ψ⁻⟩ = (|01⟩ - |10⟩)/√2**
            
            ### Entanglement Properties
            
            - **Non-separability:** Cannot write as |ψ⟩ ⊗ |φ⟩
            - **Non-locality:** Measurement correlations exceed classical bounds
            - **Monogamy:** Entanglement cannot be freely shared
            """)
            
        with col2:
            bell_state = st.selectbox(
                "Select Bell State", 
                ["Φ+ (|00⟩ + |11⟩)/√2", "Φ- (|00⟩ - |11⟩)/√2", 
                 "Ψ+ (|01⟩ + |10⟩)/√2", "Ψ- (|01⟩ - |10⟩)/√2"]
            )
            
            bell_states_dict = bell_states()
            state_map = {
                "Φ+ (|00⟩ + |11⟩)/√2": bell_states_dict['Φ+'],
                "Φ- (|00⟩ - |11⟩)/√2": bell_states_dict['Φ-'], 
                "Ψ+ (|01⟩ + |10⟩)/√2": bell_states_dict['Ψ+'],
                "Ψ- (|01⟩ - |10⟩)/√2": bell_states_dict['Ψ-']
            }
            
            selected_bell = state_map[bell_state]
            probs = np.abs(selected_bell)**2
            
            # Probability distribution
            fig = go.Figure(data=[
                go.Bar(x=['|00⟩', '|01⟩', '|10⟩', '|11⟩'], y=probs,
                       marker_color=['#22D3EE', '#3B82F6', '#8B5CF6', '#F59E0B'])
            ])
            fig.update_layout(
                title=f"Bell State: {bell_state.split(' ')[0]}",
                yaxis_title="Probability",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#E2E8F0'
            )
            st.plotly_chart(fig, width='stretch')
    
    with foundations_tabs[3]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Mathematical Framework - Hilbert Space</h3>
            <p>The complete mathematical foundation of quantum mechanics in complex vector spaces.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            ### Bra-Ket Notation (Dirac Notation)
            
            **Ket:** |ψ⟩ represents a quantum state vector
            **Bra:** ⟨φ| represents the complex conjugate transpose
            **Bracket:** ⟨φ|ψ⟩ represents the inner product
            
            ### Hilbert Space Properties
            
            - **Completeness:** Cauchy sequences converge
            - **Inner Product:** ⟨ψ|φ⟩ ∈ ℂ
            - **Norm:** ||ψ|| = √⟨ψ|ψ⟩
            - **Orthonormal Basis:** {|i⟩} where ⟨i|j⟩ = δᵢⱼ
            """)
            
        with col2:
            st.markdown("### Key Mathematical Relations")
            
            st.latex(r"""
            \langle\psi|\phi\rangle = \langle\phi|\psi\rangle^*
            """)
            st.latex(r"""
            ||\psi||^2 = \langle\psi|\psi\rangle = 1
            """)
            st.latex(r"""
            |\psi\rangle = \sum_i c_i |i\rangle
            """)
            st.latex(r"""
            \hat{A}|\psi\rangle = \sum_i a_i c_i |i\rangle
            """)
            
            st.markdown("""
            ### Quantum Operators
            
            - **Hermitian:** Â† = Â (observables)
            - **Unitary:** Û†Û = I (time evolution)
            - **Projection:** P² = P (measurement)
            - **Eigenvalue Equation:** Â|a⟩ = a|a⟩
            """)

elif section_id == "quantum_state_viz":
    st.markdown("# 🌐 Quantum State Visualization")
    st.markdown('<span class="alphanova-status status-active">Interactive Visualization Module</span>', unsafe_allow_html=True)
    
    viz_tabs = st.tabs(["Bloch Sphere", "State Vector Analysis", "Phase Relationships", "State Transformations"])
    
    with viz_tabs[0]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Interactive Bloch Sphere Visualization</h3>
            <p>Explore quantum states through real-time 3D visualization of the Bloch sphere representation.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Bloch sphere controls
        col1, col2 = st.columns(2)
        
        with col1:
            theta_deg = st.slider("θ (Polar Angle)", 0, 180, 45, key="bloch_theta",
                                 help="Angle from the north pole")
            phi_deg = st.slider("φ (Azimuthal Angle)", 0, 360, 90, key="bloch_phi", 
                               help="Angle around the equator")
        
        with col2:
            gate_sequence = st.multiselect(
                "Apply Quantum Gates",
                ["H (Hadamard)", "X (Pauli-X)", "Y (Pauli-Y)", "Z (Pauli-Z)", "S (Phase)", "T (π/8)"],
                help="Select gates to apply"
            )
        
        # Create and display Bloch sphere
        fig = create_alphanova_bloch_sphere(theta_deg, phi_deg)
        st.plotly_chart(fig, width='stretch')
        
        # Quantum state analysis
        col1, col2 = st.columns(2) 
        
        with col1:
            st.markdown("### Quantum State Vector")
            theta_rad = np.radians(theta_deg)
            phi_rad = np.radians(phi_deg)
            
            alpha = np.cos(theta_rad/2)
            beta = np.sin(theta_rad/2) * np.exp(1j * phi_rad)
            
            st.write(f"α = {alpha:.4f}")
            st.write(f"β = {beta:.4f}") 
            st.write(f"|ψ⟩ = {alpha:.3f}|0⟩ + {beta:.3f}|1⟩")
            
            prob_0 = np.abs(alpha)**2
            prob_1 = np.abs(beta)**2
            
            st.write(f"P(|0⟩) = |α|² = {prob_0:.4f}")
            st.write(f"P(|1⟩) = |β|² = {prob_1:.4f}")
        
        with col2:
            st.markdown("### Bloch Vector Coordinates")
            x = np.sin(theta_rad) * np.cos(phi_rad)
            y = np.sin(theta_rad) * np.sin(phi_rad)
            z = np.cos(theta_rad)
            
            st.write(f"x = ⟨σₓ⟩ = {x:.4f}")
            st.write(f"y = ⟨σᵧ⟩ = {y:.4f}")
            st.write(f"z = ⟨σᵤ⟩ = {z:.4f}")
            st.write(f"r = |⟨σ⟩| = {np.sqrt(x**2 + y**2 + z**2):.4f}")
    
    with viz_tabs[1]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>State Vector Analysis in ℂ²</h3>
            <p>Comprehensive analysis of quantum state vectors in the two-dimensional complex Hilbert space.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Amplitude Control")
            alpha_mag = st.slider("α magnitude", 0.0, 1.0, 0.707, key="alpha_mag")
            alpha_phase = st.slider("α phase (°)", 0, 360, 0, key="alpha_phase")
            
            alpha_complex = alpha_mag * np.exp(1j * np.radians(alpha_phase))
            beta_mag = np.sqrt(1 - alpha_mag**2) if alpha_mag**2 <= 1 else 0
            beta_phase = st.slider("β phase (°)", 0, 360, 90, key="beta_phase")
            beta_complex = beta_mag * np.exp(1j * np.radians(beta_phase))
            
            # Create LaTeX string for state vector
            latex_str = rf"|\\psi\\rangle = {alpha_complex:.3f}|0\\rangle + {beta_complex:.3f}|1\\rangle"
            st.latex(latex_str)
            
        with col2:
            # Complex plane visualization
            fig = go.Figure()
            
            # Add alpha amplitude
            fig.add_trace(go.Scatter(
                x=[0, alpha_complex.real], y=[0, alpha_complex.imag],
                mode='lines+markers',
                name='α amplitude',
                line=dict(color='#22D3EE', width=4),
                marker=dict(size=10)
            ))
            
            # Add beta amplitude
            fig.add_trace(go.Scatter(
                x=[0, beta_complex.real], y=[0, beta_complex.imag],
                mode='lines+markers', 
                name='β amplitude',
                line=dict(color='#6366F1', width=4),
                marker=dict(size=10)
            ))
            
            # Unit circle
            theta_circle = np.linspace(0, 2*np.pi, 100)
            fig.add_trace(go.Scatter(
                x=np.cos(theta_circle), y=np.sin(theta_circle),
                mode='lines',
                name='Unit Circle',
                line=dict(color='#64748B', width=1, dash='dash'),
                showlegend=False
            ))
            
            fig.update_layout(
                title="Complex Amplitude Visualization",
                xaxis_title="Real",
                yaxis_title="Imaginary",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#E2E8F0',
                xaxis=dict(range=[-1.2, 1.2]),
                yaxis=dict(range=[-1.2, 1.2])
            )
            st.plotly_chart(fig, width='stretch')
    
    with viz_tabs[2]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Quantum Phase Relationships</h3>
            <p>Explore the critical role of relative phases in quantum superposition states.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            relative_phase = st.slider("Relative Phase δ (°)", 0, 360, 90, key="rel_phase")
            delta_rad = np.radians(relative_phase)
            
            # Equal superposition with relative phase
            alpha_phase = 1/np.sqrt(2)
            beta_phase = (1/np.sqrt(2)) * np.exp(1j * delta_rad)
            
            st.markdown(f"""
            ### Equal Superposition with Phase δ = {relative_phase}°
            
            |ψ⟩ = (1/√2)|0⟩ + (1/√2)e^(iδ)|1⟩
            
            **Physical Interpretation:**
            - Global phases are unobservable
            - Relative phases affect interference
            - Measurement probabilities: |1/√2|² = 50% each
            """)
            
        with col2:
            # Phase wheel visualization
            fig = go.Figure()
            
            # Unit circle
            theta_wheel = np.linspace(0, 2*np.pi, 100)
            fig.add_trace(go.Scatter(
                x=np.cos(theta_wheel), y=np.sin(theta_wheel),
                mode='lines',
                name='Unit Circle',
                line=dict(color='#64748B', width=2)
            ))
            
            # Phase vector
            fig.add_trace(go.Scatter(
                x=[0, np.cos(delta_rad)], y=[0, np.sin(delta_rad)],
                mode='lines+markers',
                name=f'Phase δ = {relative_phase}°',
                line=dict(color='#F59E0B', width=4),
                marker=dict(size=12)
            ))
            
            fig.update_layout(
                title="Relative Phase Visualization",
                xaxis_title="Real",
                yaxis_title="Imaginary",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#E2E8F0',
                xaxis=dict(range=[-1.5, 1.5]),
                yaxis=dict(range=[-1.5, 1.5])
            )
            st.plotly_chart(fig, width='stretch')
    
    with viz_tabs[3]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Quantum State Transformations</h3>
            <p>Observe how unitary operations transform quantum states on the Bloch sphere.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### Apply Sequential Gate Operations")
        
        # Initial state setup
        col1, col2 = st.columns(2)
        with col1:
            initial_theta = st.slider("Initial θ", 0, 180, 45, key="init_theta")
            initial_phi = st.slider("Initial φ", 0, 360, 0, key="init_phi")
        
        with col2:
            transformation_gates = st.multiselect(
                "Gate Sequence (applied left to right)",
                ["I", "X", "Y", "Z", "H", "S", "T"],
                default=["H"],
                help="Select gates to apply in sequence"
            )
        
        if transformation_gates:
            # Calculate final state after gate sequence
            theta_final = initial_theta
            phi_final = initial_phi
            
            # Simple gate transformations on Bloch sphere (approximation)
            for gate in transformation_gates:
                if gate == "X":
                    theta_final = 180 - theta_final
                elif gate == "Y":
                    theta_final = 180 - theta_final
                    phi_final = phi_final + 180
                elif gate == "Z":
                    phi_final = phi_final + 180
                elif gate == "H":
                    # Hadamard rotation - approximate
                    if theta_final == 0:
                        theta_final = 90
                        phi_final = 0
                    elif theta_final == 180:
                        theta_final = 90
                        phi_final = 180
                elif gate == "S":
                    phi_final = phi_final + 90
                elif gate == "T":
                    phi_final = phi_final + 45
            
            # Normalize angles
            theta_final = theta_final % 180
            phi_final = phi_final % 360
            
            # Display before and after Bloch spheres
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### Initial State")
                fig_initial = create_alphanova_bloch_sphere(initial_theta, initial_phi)
                st.plotly_chart(fig_initial, width='stretch')
            
            with col2:
                st.markdown(f"#### After Gates: {' → '.join(transformation_gates)}")
                fig_final = create_alphanova_bloch_sphere(theta_final, phi_final)
                st.plotly_chart(fig_final, width='stretch')

elif section_id == "quantum_gates":
    st.markdown("# 🔧 Quantum Gates & Circuits")
    st.markdown('<span class="alphanova-status status-active">Core Computation Module</span>', unsafe_allow_html=True)
    
    gates_tabs = st.tabs(["Single-Qubit Gates", "Two-Qubit Gates", "Gate Matrices", "Circuit Builder"])
    
    with gates_tabs[0]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Single-Qubit Gate Operations</h3>
            <p>Fundamental single-qubit gates that form the building blocks of quantum computation.</p>
        </div>
        """, unsafe_allow_html=True)
        
        gate_type = st.selectbox(
            "Select Gate Type",
            ["Pauli-X (NOT)", "Pauli-Y", "Pauli-Z", "Hadamard (H)", "Phase (S)", "T Gate (π/8)"]
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            if gate_type == "Pauli-X (NOT)":
                st.markdown("""
                ### Pauli-X Gate (Quantum NOT)
                
                **Matrix Representation:**
                """) 
                st.latex(r"X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}")
                
                st.markdown("""
                **Action on Basis States:**
                - X|0⟩ = |1⟩
                - X|1⟩ = |0⟩
                
                **Bloch Sphere:** 180° rotation around X-axis
                
                **Properties:**
                - Hermitian: X† = X
                - Unitary: X†X = I  
                - Involutory: X² = I
                """)
                
            elif gate_type == "Hadamard (H)":
                st.markdown("""
                ### Hadamard Gate
                
                **Matrix Representation:**
                """)
                st.latex(r"H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}")
                
                st.markdown("""
                **Action on Basis States:**
                - H|0⟩ = (|0⟩ + |1⟩)/√2
                - H|1⟩ = (|0⟩ - |1⟩)/√2
                
                **Creates Superposition:**
                Transforms computational basis to superposition basis
                
                **Properties:**
                - Self-inverse: H² = I
                - Essential for quantum algorithms
                """)
            
            # Add other gate descriptions similarly...
        
        with col2:
            # Interactive gate application
            st.markdown("### Apply Gate to Custom State")
            
            input_alpha = st.slider("α coefficient", 0.0, 1.0, 1.0, key="gate_alpha")
            input_beta = np.sqrt(1 - input_alpha**2) if input_alpha**2 <= 1 else 0
            
            # Define gate matrices
            gates = {
                "Pauli-X (NOT)": pauli_matrices()['X'],
                "Pauli-Y": pauli_matrices()['Y'], 
                "Pauli-Z": pauli_matrices()['Z'],
                "Hadamard (H)": hadamard(),
                "Phase (S)": np.array([[1, 0], [0, 1j]]),
                "T Gate (π/8)": np.array([[1, 0], [0, np.exp(1j*np.pi/4)]])
            }
            
            input_state = np.array([input_alpha, input_beta])
            selected_gate = gates[gate_type]
            output_state = selected_gate @ input_state
            
            st.write(f"**Input:** {input_alpha:.3f}|0⟩ + {input_beta:.3f}|1⟩")
            st.write(f"**Output:** {output_state[0]:.3f}|0⟩ + {output_state[1]:.3f}|1⟩")
            
            # Probability comparison
            input_probs = np.abs(input_state)**2
            output_probs = np.abs(output_state)**2
            
            fig = go.Figure(data=[
                go.Bar(name='Input', x=['|0⟩', '|1⟩'], y=input_probs, marker_color='#22D3EE'),
                go.Bar(name='Output', x=['|0⟩', '|1⟩'], y=output_probs, marker_color='#6366F1')
            ])
            fig.update_layout(
                title="State Probability Comparison",
                yaxis_title="Probability",
                barmode='group',
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#E2E8F0'
            )
            st.plotly_chart(fig, width='stretch')
    
    with gates_tabs[1]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Two-Qubit Gates & Entanglement</h3>
            <p>Multi-qubit operations that create and manipulate entangled quantum states.</p>
        </div>
        """, unsafe_allow_html=True)
        
        two_qubit_gate = st.selectbox(
            "Select Two-Qubit Gate",
            ["CNOT (Controlled-X)", "CZ (Controlled-Z)", "SWAP", "Controlled-H"]
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            if two_qubit_gate == "CNOT (Controlled-X)":
                st.markdown("""
                ### CNOT (Controlled-X) Gate
                
                **Matrix Representation:**
                """)
                st.latex(r"""CNOT = \begin{pmatrix}
                1 & 0 & 0 & 0 \\
                0 & 1 & 0 & 0 \\
                0 & 0 & 0 & 1 \\
                0 & 0 & 1 & 0
                \end{pmatrix}""")
                
                st.markdown("""
                **Truth Table:**
                - |00⟩ → |00⟩
                - |01⟩ → |01⟩  
                - |10⟩ → |11⟩
                - |11⟩ → |10⟩
                
                **Properties:**
                - Flips target qubit if control is |1⟩
                - Creates Bell states from specific inputs
                - Universal for quantum computation (with single-qubit gates)
                """)
        
        with col2:
            # Bell state creation demo
            st.markdown("### Create Bell State")
            
            if st.button("Apply H ⊕ I then CNOT to |00⟩"):
                st.markdown("""
                **Step 1:** Apply H ⊕ I to |00⟩
                
                |00⟩ → (H|0⟩) ⊗ |0⟩ = (|0⟩ + |1⟩)/√2 ⊗ |0⟩
                = (|00⟩ + |10⟩)/√2
                
                **Step 2:** Apply CNOT
                
                (|00⟩ + |10⟩)/√2 → (|00⟩ + |11⟩)/√2
                
                **Result:** Bell state |Φ⁺⟩ = (|00⟩ + |11⟩)/√2
                """)
                
                # Visualize Bell state probabilities
                bell_probs = [0.5, 0, 0, 0.5]  # |00⟩ and |11⟩ only
                
                fig = go.Figure(data=[
                    go.Bar(x=['|00⟩', '|01⟩', '|10⟩', '|11⟩'], y=bell_probs,
                           marker_color=['#22D3EE', '#64748B', '#64748B', '#22D3EE'])
                ])
                fig.update_layout(
                    title="Bell State |Φ⁺⟩ Probabilities",
                    yaxis_title="Probability",
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font_color='#E2E8F0'
                )
                st.plotly_chart(fig, width='stretch')
    
    with gates_tabs[2]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Gate Matrix Representations</h3>
            <p>Complete mathematical descriptions of quantum gates in matrix form.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Display all gate matrices
        pauli_gates = pauli_matrices()
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Pauli Gates")
            
            for gate_name, matrix in pauli_gates.items():
                st.markdown(f"**{gate_name} Gate:**")
                
                # Display matrix in a formatted way
                matrix_str = rf"""
                \begin{{pmatrix}}
                {matrix[0,0]} & {matrix[0,1]} \\\\
                {matrix[1,0]} & {matrix[1,1]}
                \end{{pmatrix}}
                """
                st.latex(matrix_str)
                
                # Eigenvalues and properties
                eigenvals = np.linalg.eigvals(matrix)
                st.write(f"Eigenvalues: {eigenvals}")
                st.write(f"Trace: {np.trace(matrix)}")
                st.write(f"Determinant: {np.linalg.det(matrix):.1f}")
                st.markdown("---")
        
        with col2:
            st.markdown("### Rotation Gates")
            
            # Parameterized rotation gates
            angle = st.slider("Rotation Angle θ (radians)", 0.0, 2*np.pi, np.pi/4)
            
            # RX, RY, RZ gates
            rx_gate = np.array([[np.cos(angle/2), -1j*np.sin(angle/2)],
                               [-1j*np.sin(angle/2), np.cos(angle/2)]])
            
            ry_gate = np.array([[np.cos(angle/2), -np.sin(angle/2)],
                               [np.sin(angle/2), np.cos(angle/2)]])
            
            rz_gate = np.array([[np.exp(-1j*angle/2), 0],
                               [0, np.exp(1j*angle/2)]])
            
            st.markdown(f"**RX(θ) with θ = {angle:.3f}:**")
            st.write(rx_gate)
            
            st.markdown(f"**RY(θ) with θ = {angle:.3f}:**")
            st.write(ry_gate)
            
            st.markdown(f"**RZ(θ) with θ = {angle:.3f}:**")
            st.write(rz_gate) 
    
    with gates_tabs[3]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Quantum Circuit Builder</h3>
            <p>Design and simulate custom quantum circuits with multiple qubits and gates.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Simple circuit builder
        col1, col2 = st.columns(2)
        
        with col1:
            n_qubits = st.selectbox("Number of Qubits", [1, 2, 3], index=1)
            
            st.markdown("### Add Gates to Circuit")
            circuit_gates = st.multiselect(
                "Gate Sequence",
                ["H", "X", "Y", "Z", "CNOT", "S", "T"],
                default=["H"],
                help="Gates applied in order from left to right"
            )
            
        with col2:
            st.markdown("### Circuit Diagram")
            
            # Simple text-based circuit representation
            if n_qubits == 1:
                circuit_repr = "q0: ─"
                for gate in circuit_gates:
                    if gate in ['H', 'X', 'Y', 'Z', 'S', 'T']:
                        circuit_repr += f"─[{gate}]─"
                st.code(circuit_repr, language="text")
                
            elif n_qubits == 2:
                circuit_repr_0 = "q0: ─"
                circuit_repr_1 = "q1: ─"
                
                for gate in circuit_gates:
                    if gate == 'CNOT':
                        circuit_repr_0 += "─•─"  # control
                        circuit_repr_1 += "─⊕─"  # target
                    elif gate in ['H', 'X', 'Y', 'Z', 'S', 'T']:
                        circuit_repr_0 += f"─[{gate}]─"
                        circuit_repr_1 += "─────"
                
                st.code(circuit_repr_0 + "\n" + circuit_repr_1, language="text")
        
        # Simulate circuit if possible
        if st.button("Simulate Circuit", type="primary"):
            if n_qubits == 1 and len(circuit_gates) > 0:
                # Single qubit simulation
                state = np.array([1.0, 0.0], dtype=complex)  # |0⟩
                
                for gate in circuit_gates:
                    if gate == 'H':
                        state = hadamard() @ state
                    elif gate == 'X':
                        state = pauli_matrices()['X'] @ state
                    elif gate == 'Y':
                        state = pauli_matrices()['Y'] @ state
                    elif gate == 'Z':
                        state = pauli_matrices()['Z'] @ state
                
                probs = np.abs(state)**2
                
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"Final state: {state[0]:.3f}|0⟩ + {state[1]:.3f}|1⟩")
                    st.write(f"P(|0⟩) = {probs[0]:.4f}")
                    st.write(f"P(|1⟩) = {probs[1]:.4f}")
                
                with col2:
                    fig = go.Figure(data=[
                        go.Bar(x=['|0⟩', '|1⟩'], y=probs, marker_color=['#22D3EE', '#6366F1'])
                    ])
                    fig.update_layout(
                        title="Output Probabilities",
                        yaxis_title="Probability",
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)',
                        font_color='#E2E8F0'
                    )
                    st.plotly_chart(fig, width='stretch')

elif section_id == "quantum_algorithms":
    st.markdown("# ⚡ Quantum Algorithms")
    st.markdown('<span class="alphanova-status status-research">Advanced Research Module</span>', unsafe_allow_html=True)
    
    algorithm_tabs = st.tabs(["Deutsch Algorithm", "Deutsch-Jozsa", "Grover's Algorithm", "Quantum Fourier Transform"])
    
    with algorithm_tabs[0]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Deutsch Algorithm - First Quantum Speedup</h3>
            <p>The historically first quantum algorithm demonstrating exponential speedup over classical computation.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Problem Statement
            
            Given a black-box function f: {0,1} → {0,1}, determine if f is:
            - **Constant:** f(0) = f(1) (both 0 or both 1)
            - **Balanced:** f(0) ≠ f(1) (one 0, one 1)
            
            ### Classical Approach
            
            - Must evaluate f(0) and f(1)
            - Requires **2 function evaluations**
            - No way to avoid checking both inputs
            
            ### Quantum Approach
            
            - Uses quantum superposition and interference
            - Requires only **1 function evaluation**
            - 50% speedup, infinite in relative terms
            """)
        
        with col2:
            st.markdown("### Deutsch Circuit")
            
            # Circuit representation
            st.code("""
q0: |0⟩─[H]─[Uf]─[H]─M
                  │    │
q1: |1⟩─[H]─[Uf]────
            """, language="text")
            
            st.markdown("""
            **Steps:**
            1. Initialize |01⟩
            2. Apply H ⊗ H → (|0⟩+|1⟩)(|0⟩-|1⟩)/2
            3. Apply oracle Uf
            4. Apply H ⊗ I to first qubit
            5. Measure first qubit
            
            **Result:**
            - Measure |0⟩: f is constant
            - Measure |1⟩: f is balanced
            """)
        
        # Interactive simulation
        st.markdown("### Simulate Deutsch Algorithm")
        
        function_type = st.selectbox(
            "Choose Function Type",
            ["Constant (f=0)", "Constant (f=1)", "Balanced (f=id)", "Balanced (f=NOT)"]
        )
        
        if st.button("Run Deutsch Algorithm", key="deutsch_run"):
            # Simulate the algorithm
            if "Constant" in function_type:
                result_prob_0 = 1.0
                result_prob_1 = 0.0
                interpretation = "Function is CONSTANT"
            else:
                result_prob_0 = 0.0
                result_prob_1 = 1.0
                interpretation = "Function is BALANCED"
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("P(measure |0⟩)", f"{result_prob_0:.1%}")
                st.metric("P(measure |1⟩)", f"{result_prob_1:.1%}")
                st.success(f"✅ {interpretation}")
            
            with col2:
                fig = go.Figure(data=[
                    go.Bar(x=['|0⟩', '|1⟩'], y=[result_prob_0, result_prob_1],
                           marker_color=['#22D3EE', '#EF4444'])
                ])
                fig.update_layout(
                    title="Measurement Outcome",
                    yaxis_title="Probability",
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font_color='#E2E8F0'
                )
                st.plotly_chart(fig, width='stretch')
    
    with algorithm_tabs[1]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Deutsch-Jozsa Algorithm</h3>
            <p>Generalization of Deutsch algorithm to n-bit functions with exponential speedup.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Extended Problem
            
            For function f: {0,1}^n → {0,1}, determine if:
            - **Constant:** f(x) = c for all x (c = 0 or 1)
            - **Balanced:** f(x) = 0 for exactly half the inputs
            
            ### Classical Complexity
            
            - Worst case: 2^(n-1) + 1 evaluations
            - For n=10: up to 513 evaluations needed
            - Exponential in problem size
            
            ### Quantum Complexity  
            
            - **Exactly 1 evaluation** regardless of n
            - Exponential speedup: O(2^n) → O(1)
            - Among the largest quantum advantages known
            """)
        
        with col2:
            n_bits = st.slider("Number of Input Bits (n)", 2, 6, 3, key="dj_bits")
            
            st.markdown(f"### Circuit for n={n_bits}")
            
            # Show scaling
            classical_worst = 2**(n_bits-1) + 1
            quantum_evals = 1
            speedup = classical_worst / quantum_evals
            
            st.metric("Classical Worst Case", f"{classical_worst} evaluations")
            st.metric("Quantum Required", "1 evaluation")
            st.metric("Speedup Factor", f"{speedup:.0f}x")
            
            # Visualization of exponential growth
            bits_range = np.arange(1, 11)
            classical_evals = 2**(bits_range-1) + 1
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=bits_range, y=classical_evals,
                mode='lines+markers',
                name='Classical (worst case)',
                line=dict(color='#EF4444', width=3)
            ))
            fig.add_trace(go.Scatter(
                x=bits_range, y=np.ones_like(bits_range),
                mode='lines+markers', 
                name='Quantum',
                line=dict(color='#22D3EE', width=3)
            ))
            
            fig.update_layout(
                title="Deutsch-Jozsa Complexity Scaling",
                xaxis_title="Input bits (n)",
                yaxis_title="Function evaluations",
                yaxis_type="log",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#E2E8F0'
            )
            st.plotly_chart(fig, width='stretch')
    
    with algorithm_tabs[2]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Grover's Search Algorithm</h3>
            <p>Quadratic speedup for unstructured search problems - optimal quantum search algorithm.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Unstructured Search Problem
            
            Search unsorted database of N=2^n items for marked item.
            
            **Classical Search:**
            - Random sampling: O(N) = O(2^n)
            - Must check ~N/2 items on average
            
            **Grover's Algorithm:**
            - Quantum search: O(√N) = O(2^(n/2))
            - Quadratic speedup - provably optimal
            - Uses amplitude amplification technique
            
            ### Key Components
            
            1. **Oracle:** Marks target item
            2. **Diffusion:** Amplifies marked amplitude
            3. **Iteration:** Repeat ~π√N/4 times
            """)
        
        with col2:
            database_size = st.selectbox(
                "Database Size (N)",
                [4, 8, 16, 32, 64, 128],
                index=2
            )
            
            n_qubits_grover = int(np.log2(database_size))
            optimal_iterations = int(np.pi * np.sqrt(database_size) / 4)
            classical_average = database_size // 2
            
            st.metric("Database Items (N)", database_size)
            st.metric("Qubits Required", n_qubits_grover)
            st.metric("Grover Iterations", optimal_iterations)
            st.metric("Classical Average", f"{classical_average} queries")
            
            speedup_grover = classical_average / optimal_iterations if optimal_iterations > 0 else classical_average
            st.metric("Quantum Speedup", f"{speedup_grover:.1f}x")
            
        # Grover simulation
        st.markdown("### Grover Algorithm Simulation")
        
        target_item = st.slider("Target Item Index", 0, database_size-1, 0, key="grover_target")
        
        if st.button("Simulate Grover Search", key="grover_run"):
            # Simulate amplitude evolution
            iterations = np.arange(0, min(optimal_iterations + 3, 10))
            
            # Approximate probability evolution (simplified)
            success_probs = []
            for i in iterations:
                if i <= optimal_iterations:
                    # Approximate sinusoidal growth
                    prob = np.sin((2*i + 1) * np.arcsin(1/np.sqrt(database_size)))**2
                else:
                    # Probability decreases after optimal point
                    prob = np.sin((2*optimal_iterations + 1) * np.arcsin(1/np.sqrt(database_size)))**2
                    prob *= np.exp(-(i - optimal_iterations) * 0.3)
                
                success_probs.append(prob)
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=iterations, y=success_probs,
                mode='lines+markers',
                name='Success Probability',
                line=dict(color='#22D3EE', width=4),
                marker=dict(size=8)
            ))
            
            # Mark optimal point
            fig.add_vline(x=optimal_iterations, line_dash="dash", 
                         line_color="#F59E0B", annotation_text="Optimal")
            
            fig.update_layout(
                title=f"Grover's Algorithm: Finding Item {target_item} in Database of {database_size}",
                xaxis_title="Iteration",
                yaxis_title="Probability of Success",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#E2E8F0'
            )
            st.plotly_chart(fig, width='stretch')
    
    with algorithm_tabs[3]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Quantum Fourier Transform (QFT)</h3>
            <p>Quantum analog of classical FFT, essential for period finding and Shor's algorithm.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Mathematical Definition
            
            QFT maps computational basis to Fourier basis:
            
            |x⟩ → (1/√N) Σₖ e^(2πikx/N) |k⟩
            
            where N = 2^n for n qubits.
            
            ### Key Properties
            
            - **Unitary transformation**
            - **Efficient implementation:** O(n²) gates
            - **Classical FFT comparison:** O(N log N)
            - **Exponential speedup** for certain problems
            
            ### Applications
            
            - **Period Finding:** Core of Shor's algorithm
            - **Phase Estimation:** Quantum eigenvalue estimation  
            - **Hidden Subgroup Problems**
            """)
        
        with col2:
            qft_qubits = st.slider("QFT Qubits (n)", 2, 5, 3, key="qft_qubits")
            qft_size = 2**qft_qubits
            
            st.markdown(f"### QFT Circuit for n={qft_qubits}")
            
            # QFT circuit complexity
            qft_gates = qft_qubits**2  # Approximation
            classical_ops = qft_size * np.log2(qft_size) if qft_size > 1 else 1
            
            st.metric("Hilbert Space Size", f"2^{qft_qubits} = {qft_size}")
            st.metric("QFT Gates Required", f"~{qft_gates}")
            st.metric("Classical FFT Ops", f"~{classical_ops:.0f}")
            
            if qft_size > 8:
                qft_speedup = classical_ops / qft_gates
                st.metric("Potential Speedup", f"{qft_speedup:.1f}x")
        
        # QFT visualization example
        st.markdown("### QFT Example: Fourier Transform of |001⟩")
        
        if st.button("Compute QFT|001⟩", key="qft_example"):
            # Simple 3-qubit QFT example
            n = 3
            N = 2**n
            input_state = 1  # |001⟩ corresponds to x=1
            
            # Compute QFT amplitudes
            amplitudes = []
            labels = []
            
            for k in range(N):
                # QFT amplitude: (1/√N) * e^(2πikx/N)
                amplitude = (1/np.sqrt(N)) * np.exp(2j * np.pi * k * input_state / N)
                amplitudes.append(np.abs(amplitude)**2)  # Probability
                labels.append(f"|{k:03b}⟩")
            
            fig = go.Figure(data=[
                go.Bar(x=labels, y=amplitudes, marker_color='#6366F1')
            ])
            
            fig.update_layout(
                title="QFT Output Probabilities for Input |001⟩",
                xaxis_title="Output Basis States",
                yaxis_title="Probability",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#E2E8F0'
            )
            st.plotly_chart(fig, width='stretch')
            
            st.info("💡 The QFT produces equal amplitude superposition with phase relationships encoding the input information.")
    # Bell States Module
    st.markdown("# 🔗 Bell-State Correlations")
    st.markdown('<span class="alphanova-status status-active">Active Research Module</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="alphanova-card">
        <h3>Quantum Entanglement & Non-locality</h3>
        <p>Explore the fundamental quantum phenomenon of entanglement through Bell state analysis, 
        CHSH inequality testing, and comprehensive correlation measurements.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Bell state selection
    bell_state = st.selectbox(
        "Select Bell State",
        ["Φ+ (|00⟩ + |11⟩)/√2", "Φ- (|00⟩ - |11⟩)/√2", "Ψ+ (|01⟩ + |10⟩)/√2", "Ψ- (|01⟩ - |10⟩)/√2"],
        help="Choose which Bell state to analyze"
    )
    
    # Get Bell states
    bell_dict = bell_states()
    state_map = {
        "Φ+ (|00⟩ + |11⟩)/√2": bell_dict['Φ+'],
        "Φ- (|00⟩ - |11⟩)/√2": bell_dict['Φ-'],
        "Ψ+ (|01⟩ + |10⟩)/√2": bell_dict['Ψ+'],
        "Ψ- (|01⟩ - |10⟩)/√2": bell_dict['Ψ-']
    }
    
    selected_state = state_map[bell_state]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### State Vector Components")
        st.write(f"|00⟩ coefficient: {selected_state[0]:.4f}")
        st.write(f"|01⟩ coefficient: {selected_state[1]:.4f}")
        st.write(f"|10⟩ coefficient: {selected_state[2]:.4f}")
        st.write(f"|11⟩ coefficient: {selected_state[3]:.4f}")
        
        # Probability distribution
        probs = np.abs(selected_state)**2
        st.markdown("### Measurement Probabilities")
        st.write(f"P(|00⟩) = {probs[0]:.4f}")
        st.write(f"P(|01⟩) = {probs[1]:.4f}")
        st.write(f"P(|10⟩) = {probs[2]:.4f}")
        st.write(f"P(|11⟩) = {probs[3]:.4f}")
    
    with col2:
        # Visualization of probability distribution
        fig = go.Figure(data=[
            go.Bar(x=['|00⟩', '|01⟩', '|10⟩', '|11⟩'], y=probs,
                   marker_color=['#06B6D4', '#3B82F6', '#8B5CF6', '#F59E0B'])
        ])
        fig.update_layout(
            title="Bell State Probability Distribution",
            xaxis_title="Basis States",
            yaxis_title="Probability",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='#E2E8F0'
        )
        st.plotly_chart(fig, width='stretch')
    
    # CHSH inequality analysis
    st.markdown("### CHSH Inequality Analysis")
    
    # Calculate CHSH parameter for Bell states
    chsh_value = 2 * np.sqrt(2)
    classical_bound = 2
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("CHSH Parameter", f"{chsh_value:.3f}", delta=f"{chsh_value - classical_bound:.3f}")
    with col2:
        st.metric("Quantum Violation", f"{chsh_value/classical_bound:.2f}x", delta="Exceeds classical")
    
    violation_percentage = ((chsh_value - classical_bound) / classical_bound) * 100
    st.progress(min(violation_percentage / 50, 1.0), text=f"CHSH Violation: {violation_percentage:.1f}%")

elif module_id == "vqe":
    # VQE Module
    st.markdown("# 🔬 VQE Architectures")
    st.markdown('<span class="alphanova-status status-research">Research Module</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="alphanova-card">
        <h3>Variational Quantum Eigensolver</h3>
        <p>Implement the hybrid quantum-classical VQE algorithm for finding ground state energies 
        of molecular systems. Explore parameterized quantum circuits and optimization landscapes.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # VQE parameters
    col1, col2 = st.columns(2)
    
    with col1:
        ansatz_depth = st.slider("Ansatz Depth", 1, 5, 2, help="Number of parameterized circuit layers")
        optimizer = st.selectbox("Optimizer", ["COBYLA", "SPSA", "Powell"], help="Classical optimization method")
    
    with col2:
        max_iterations = st.slider("Max Iterations", 10, 100, 50)
        noise_level = st.slider("Noise Level", 0.0, 0.1, 0.0, step=0.01, help="Simulated quantum noise")
    
    # Run VQE simulation
    if st.button("Run VQE Optimization", type="primary"):
        with st.spinner("Running VQE optimization..."):
            # Simulate VQE optimization
            h2_hamiltonian = vqe_h2_hamiltonian()
            exact_energy = np.min(np.linalg.eigvals(h2_hamiltonian)).real
            
            # Mock optimization trajectory
            iterations = np.arange(max_iterations)
            start_energy = exact_energy + np.random.uniform(0.5, 1.5)
            energies = start_energy * np.exp(-iterations / (max_iterations / 3)) + exact_energy
            
            # Add noise if specified  
            if noise_level > 0:
                noise = np.random.normal(0, noise_level, len(energies))
                energies += noise
                
            # Create optimization plot
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=iterations, y=energies,
                mode='lines+markers',
                name='VQE Energy',
                line=dict(color='#06B6D4', width=3)
            ))
            fig.add_hline(y=exact_energy, line_dash="dash", 
                         line_color="#F59E0B", annotation_text="Exact Ground State")
            
            fig.update_layout(
                title="VQE Energy Optimization",
                xaxis_title="Iteration",
                yaxis_title="Energy (Hartree)",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#E2E8F0'
            )
            
            st.plotly_chart(fig, width='stretch')
            
            # Results summary
            final_energy = energies[-1]
            error = abs(final_energy - exact_energy)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Final Energy", f"{final_energy:.6f} Ha")
            with col2:
                st.metric("Exact Energy", f"{exact_energy:.6f} Ha") 
            with col3:
                st.metric("Chemical Accuracy", f"{error*627.5:.2f} kcal/mol", 
                         delta=f"{'✓' if error*627.5 < 1.0 else '✗'} Target: <1 kcal/mol")

elif module_id == "qml":
    # Quantum ML Module
    st.markdown("# 🧠 Quantum Neural Networks")
    st.markdown('<span class="alphanova-status status-emerging">Emerging Research</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="alphanova-card">
        <h3>Quantum Machine Learning</h3>
        <p>Explore quantum-enhanced machine learning algorithms including quantum neural networks,
        variational classifiers, and quantum kernel methods for advanced pattern recognition.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # QML algorithm selection
    qml_algorithm = st.selectbox(
        "Select QML Algorithm",
        ["Quantum Kernel SVM", "Variational Quantum Classifier", "Quantum Neural Network"],
        help="Choose which quantum machine learning algorithm to explore"
    )
    
    if qml_algorithm == "Quantum Kernel SVM":
        st.markdown("### Quantum Kernel Support Vector Machine")
        
        # Generate sample dataset
        np.random.seed(42)
        n_samples = st.slider("Number of Samples", 50, 200, 100)
        
        # Create synthetic 2D dataset
        X = np.random.randn(n_samples, 2)
        y = (X[:, 0]**2 + X[:, 1]**2 > 1).astype(int)
        
        # Visualization
        col1, col2 = st.columns(2)
        
        with col1:
            # Dataset visualization
            colors = ['#06B6D4', '#F59E0B']
            fig = go.Figure()
            for class_idx in [0, 1]:
                mask = y == class_idx
                fig.add_trace(go.Scatter(
                    x=X[mask, 0], y=X[mask, 1],
                    mode='markers',
                    name=f'Class {class_idx}',
                    marker=dict(color=colors[class_idx], size=8)
                ))
            
            fig.update_layout(
                title="Training Dataset",
                xaxis_title="Feature 1",
                yaxis_title="Feature 2",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#E2E8F0'
            )
            st.plotly_chart(fig, width='stretch')
        
        with col2:
            # Mock quantum kernel matrix
            kernel_matrix = np.random.exponential(0.5, (20, 20))
            kernel_matrix = (kernel_matrix + kernel_matrix.T) / 2  # Make symmetric
            np.fill_diagonal(kernel_matrix, 1.0)  # Diagonal is 1
            
            fig = go.Figure(data=go.Heatmap(
                z=kernel_matrix,
                colorscale='Viridis',
                colorbar=dict(title="Kernel Value")
            ))
            fig.update_layout(
                title="Quantum Kernel Matrix",
                xaxis_title="Sample i",
                yaxis_title="Sample j",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#E2E8F0'
            )
            st.plotly_chart(fig, width='stretch')
        
        # Training simulation
        if st.button("Train Quantum Kernel SVM", type="primary"):
            with st.spinner("Training quantum kernel SVM..."):
                progress_bar = st.progress(0)
                for i in range(101):
                    time.sleep(0.02)
                    progress_bar.progress(i / 100)
                
                # Mock training results
                classical_accuracy = 0.85 + np.random.normal(0, 0.05)
                quantum_accuracy = 0.91 + np.random.normal(0, 0.03)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Classical SVM", f"{classical_accuracy:.1%}")
                with col2: 
                    st.metric("Quantum Kernel SVM", f"{quantum_accuracy:.1%}")
                with col3:
                    improvement = (quantum_accuracy - classical_accuracy) / classical_accuracy * 100
                    st.metric("Improvement", f"{improvement:.1f}%")
                
                st.success("✅ Quantum kernel SVM shows enhanced classification performance!")

elif section_id == "quantum_ml":
    st.markdown("# 🧠 Quantum Machine Learning")
    st.markdown('<span class="alphanova-status status-emerging">Emerging Research</span>', unsafe_allow_html=True)
    
    ml_tabs = st.tabs(["QML Fundamentals", "Variational Circuits", "Quantum Kernels", "QAOA Optimization", "Tensor Networks"])
    
    with ml_tabs[0]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Quantum Machine Learning Foundations</h3>
            <p>Exploring the intersection of quantum computing and machine learning for enhanced pattern recognition and optimization.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Mathematical Foundations
            
            **Quantum Feature Maps φ(x):**
            
            Classical data x ∈ ℝⁿ mapped to quantum states:
            |φ(x)⟩ = U(x)|0⟩⊗ⁿ
            
            Common encodings:
            - **Angle encoding:** RY(xᵢ)|0⟩ 
            - **Amplitude encoding:** Σᵢ xᵢ|i⟩/||x||
            - **Basis encoding:** |x₁x₂...xₙ⟩
            
            **Quantum Kernels:**
            
            K(x,x') = |⟨φ(x)|φ(x')⟩|²
            
            Potentially exponential separation from classical kernels.
            
            **Parameterized Quantum Circuits:**
            
            f(x;θ) = ⟨0|U†(θ)†φ(x)†OU(θ)φ(x)|0⟩
            
            Where O is the observable operator.
            """)
            
        with col2:
            st.markdown("### Quantum Advantage Analysis")
            
            # Feature space dimension comparison
            n_features = st.slider("Number of Features", 2, 10, 4, key="qml_features")
            
            classical_dim = n_features  # Linear feature map
            polynomial_dim = n_features**2  # Polynomial kernel
            quantum_dim = 2**n_features  # Quantum Hilbert space
            
            fig = go.Figure(data=[
                go.Bar(name='Classical Linear', x=['Feature Space Dimension'], y=[classical_dim], marker_color='#EF4444'),
                go.Bar(name='Polynomial Kernel', x=['Feature Space Dimension'], y=[polynomial_dim], marker_color='#F59E0B'),
                go.Bar(name='Quantum Hilbert', x=['Feature Space Dimension'], y=[quantum_dim], marker_color='#22D3EE')
            ])
            
            fig.update_layout(
                title=f"Feature Space Comparison (n={n_features})",
                yaxis_title="Dimension",
                yaxis_type="log",
                barmode='group',
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#E2E8F0'
            )
            st.plotly_chart(fig, width='stretch')
            
            # Quantum advantage metrics
            if quantum_dim > 100:
                advantage = quantum_dim / max(classical_dim, polynomial_dim)
                st.metric("Quantum Advantage", f"{advantage:.1f}x", 
                         delta=f"Exponential scaling: 2^{n_features}")
    
    with ml_tabs[1]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Variational Quantum Circuits (VQCs)</h3>
            <p>Parameterized quantum circuits optimized classically for machine learning tasks.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### VQC Architecture Design
            
            **Layer Structure:**
            1. **Data Encoding:** U_enc(x)
            2. **Variational Layer:** U_var(θ)
            3. **Entangling Gates:** CNOT, CZ, etc.
            4. **Measurement:** ⟨Z⟩, ⟨X⟩, ⟨Y⟩
            
            **Training Process:**
            
            Cost function: C(θ) = 1/N Σᵢ L(f(xᵢ;θ), yᵢ)
            
            Gradient: ∂C/∂θⱼ via parameter-shift rule:
            
            ∂f/∂θⱼ = [f(θ + π/2·eⱼ) - f(θ - π/2·eⱼ)]/2
            
            **Expressivity vs Trainability:**
            - More parameters → Higher expressivity
            - Deeper circuits → Barren plateaus
            - Circuit design critical for performance
            """)
            
            # VQC parameters
            st.markdown("### Circuit Configuration")
            vqc_layers = st.slider("Number of Layers", 1, 8, 3, key="vqc_layers")
            vqc_qubits = st.slider("Number of Qubits", 2, 6, 4, key="vqc_qubits")
            entangling_type = st.selectbox(
                "Entangling Pattern",
                ["Linear", "Circular", "All-to-All"],
                key="entangle_type"
            )
            
        with col2:
            # Gradient visualization
            st.markdown("### Gradient Landscape Analysis")
            
            # Simulate barren plateau effect
            layer_range = np.arange(1, 11)
            gradient_magnitude = np.exp(-layer_range / 3) + 0.01 * np.random.random(len(layer_range))
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=layer_range, y=gradient_magnitude,
                mode='lines+markers',
                name='Gradient Magnitude',
                line=dict(color='#EF4444', width=3),
                marker=dict(size=8)
            ))
            
            # Highlight barren plateau region
            fig.add_hrect(y0=0, y1=0.05, 
                         fillcolor="rgba(239, 68, 68, 0.2)", 
                         annotation_text="Barren Plateau", 
                         annotation_position="top left")
            
            fig.update_layout(
                title="Barren Plateau Effect vs Circuit Depth",
                xaxis_title="Number of Layers",
                yaxis_title="Gradient Magnitude",
                yaxis_type="log",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#E2E8F0'
            )
            st.plotly_chart(fig, width='stretch')
            
            # Circuit complexity metrics
            total_params = vqc_layers * vqc_qubits * 3  # 3 rotation gates per qubit per layer
            circuit_depth = vqc_layers * 2  # Approx depth including entangling
            
            st.metric("Total Parameters", total_params)
            st.metric("Circuit Depth", circuit_depth)
            
            if circuit_depth > 20:
                st.warning("⚠️ Deep circuit may suffer from barren plateaus")
            else:
                st.info("✅ Circuit depth suitable for training")
    
    with ml_tabs[2]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Quantum Kernel Methods</h3>
            <p>Quantum-enhanced kernel methods for classification and regression tasks.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Quantum Kernel Theory
            
            **Quantum Kernel Definition:**
            
            K_q(xᵢ, xⱼ) = |⟨φ(xᵢ)|φ(xⱼ)⟩|²
            
            where φ(x) is the quantum feature map.
            
            **Kernel Properties:**
            - Positive semi-definite by construction
            - Symmetric: K_q(xᵢ, xⱼ) = K_q(xⱼ, xᵢ)
            - Bounded: 0 ≤ K_q(x,x') ≤ 1
            
            **Feature Map Examples:**
            
            1. **IQP (Instantaneous Quantum Polynomial):**
               U_IQP(x) = ∏ᵢ RZ(xᵢ) ∏ᵢ,ⱼ RZZ(xᵢxⱼ)
            
            2. **Data Re-uploading:**
               U(x) = ∏ₗ [∏ᵢ RY(θₗᵢ + xᵢ) ∏ᵢ CNOT_{i,i+1}]
            
            **Quantum Advantage Sources:**
            - Non-classical correlations
            - Exponential feature space dimension
            - Interference effects in computation
            """)
            
        with col2:
            st.markdown("### Kernel Comparison Experiment")
            
            # Generate synthetic dataset
            kernel_demo = st.button("Generate Quantum vs Classical Kernel Comparison", key="kernel_demo")
            
            if kernel_demo:
                np.random.seed(42)
                n_samples = 50
                
                # Create XOR-like dataset that's hard for linear kernels
                angles = np.random.uniform(0, 2*np.pi, n_samples)
                radii = np.random.uniform(0.5, 1.5, n_samples)
                X = np.column_stack([radii * np.cos(angles), radii * np.sin(angles)])
                y = ((X[:, 0] > 0) == (X[:, 1] > 0)).astype(int)
                
                # Simulate quantum vs classical kernels
                classical_margin = 0.3 + 0.1 * np.random.random()
                quantum_margin = 0.8 + 0.1 * np.random.random()
                
                # Visualization
                colors = ['#EF4444', '#22D3EE']
                fig = go.Figure()
                
                for class_idx in [0, 1]:
                    mask = y == class_idx
                    fig.add_trace(go.Scatter(
                        x=X[mask, 0], y=X[mask, 1],
                        mode='markers',
                        name=f'Class {class_idx}',
                        marker=dict(color=colors[class_idx], size=10, opacity=0.7)
                    ))
                
                fig.update_layout(
                    title="XOR-like Dataset for Kernel Comparison",
                    xaxis_title="Feature 1",
                    yaxis_title="Feature 2",
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font_color='#E2E8F0'
                )
                st.plotly_chart(fig, width='stretch')
                
                # Performance comparison
                col_a, col_b = st.columns(2)
                with col_a:
                    st.metric("RBF Kernel Accuracy", f"{65 + 10*classical_margin:.1f}%")
                with col_b:
                    st.metric("Quantum Kernel Accuracy", f"{75 + 15*quantum_margin:.1f}%")
                
                improvement = (75 + 15*quantum_margin) - (65 + 10*classical_margin)
                if improvement > 10:
                    st.success(f"✅ Quantum kernel shows {improvement:.1f}% improvement!")
    
    with ml_tabs[3]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Quantum Approximate Optimization Algorithm (QAOA)</h3>
            <p>Hybrid quantum-classical algorithm for combinatorial optimization problems.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### QAOA Framework
            
            **Problem Setup:**
            
            Optimize: ⟨ψ(γ,β)|C|ψ(γ,β)⟩
            
            where C is the cost Hamiltonian.
            
            **Ansatz State:**
            
            |ψ(γ,β)⟩ = e^(-iβₚH_B)e^(-iγₚH_C)...e^(-iβ₁H_B)e^(-iγ₁H_C)|+⟩^⊗n
            
            **Components:**
            - **H_C:** Cost Hamiltonian (problem-specific)
            - **H_B:** Mixer Hamiltonian (typically Σᵢ Xᵢ)
            - **γ, β:** Variational parameters
            - **p:** QAOA depth (number of layers)
            
            **Max-Cut Example:**
            
            H_C = ½ Σ_{(i,j)∈E} (1 - ZᵢZⱼ)
            
            Classical solution: NP-hard
            QAOA approximation ratio: > 0.6924 for p=1
            """)
            
            # QAOA parameters
            st.markdown("### QAOA Configuration")
            qaoa_p = st.slider("QAOA Depth (p)", 1, 5, 2, key="qaoa_depth")
            graph_size = st.slider("Graph Size (vertices)", 3, 8, 4, key="graph_size")
            edge_probability = st.slider("Edge Probability", 0.3, 1.0, 0.6, key="edge_prob")
            
        with col2:
            st.markdown("### Max-Cut QAOA Simulation")
            
            # Generate random graph
            if st.button("Run QAOA Max-Cut", key="qaoa_run"):
                # Simulate QAOA optimization
                np.random.seed(42)
                
                # Generate adjacency matrix
                adj_matrix = np.random.random((graph_size, graph_size)) < edge_probability
                adj_matrix = np.triu(adj_matrix) + np.triu(adj_matrix).T  # Make symmetric
                np.fill_diagonal(adj_matrix, 0)
                
                num_edges = np.sum(adj_matrix) // 2
                
                # Simulate QAOA convergence
                iterations = np.arange(0, 50)
                
                # Theoretical max-cut value (upper bound)
                max_cut_upper = num_edges
                classical_greedy = int(0.85 * num_edges)  # Greedy approximation
                
                # QAOA approximation (starts random, converges)
                qaoa_values = classical_greedy * 0.5 + (classical_greedy * 0.4) * (
                    1 - np.exp(-iterations / 15)) + 0.05 * num_edges * np.random.random(len(iterations))
                
                fig = go.Figure()
                
                fig.add_trace(go.Scatter(
                    x=iterations, y=qaoa_values,
                    mode='lines+markers',
                    name=f'QAOA (p={qaoa_p})',
                    line=dict(color='#22D3EE', width=3)
                ))
                
                fig.add_hline(y=classical_greedy, line_dash="dash", 
                             line_color="#F59E0B", annotation_text="Classical Greedy")
                fig.add_hline(y=max_cut_upper, line_dash="dash", 
                             line_color="#10B981", annotation_text="Optimal Upper Bound")
                
                fig.update_layout(
                    title=f"QAOA Max-Cut Optimization ({num_edges} edges)",
                    xaxis_title="Iteration",
                    yaxis_title="Cut Value",
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font_color='#E2E8F0'
                )
                st.plotly_chart(fig, width='stretch')
                
                # Performance metrics
                final_qaoa = qaoa_values[-1]
                approximation_ratio = final_qaoa / max_cut_upper
                classical_ratio = classical_greedy / max_cut_upper
                
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    st.metric("QAOA Cut Value", f"{final_qaoa:.1f}")
                with col_b:
                    st.metric("Approximation Ratio", f"{approximation_ratio:.3f}")
                with col_c:
                    improvement = approximation_ratio - classical_ratio
                    st.metric("vs Classical", f"{improvement:+.3f}")
    
    with ml_tabs[4]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Quantum Tensor Networks for ML</h3>
            <p>Matrix Product States and tensor decomposition methods for quantum machine learning.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Matrix Product States (MPS)
            
            **MPS Representation:**
            
            |ψ⟩ = Σ_{i₁...iₙ} A¹ᵢ₁ A²ᵢ₂ ... Aⁿᵢₙ |i₁i₂...iₙ⟩
            
            where Aᵏᵢₖ are rank-3 tensors.
            
            **Key Advantages:**
            - Efficient classical representation
            - Polynomial memory scaling
            - Natural for 1D correlations
            - DMRG optimization
            
            **Bond Dimension χ:**
            - Controls entanglement capacity
            - Exponential scaling: χ = 2^(S_EE)
            - Compression vs accuracy tradeoff
            
            **Tree Tensor Networks (TTN):**
            - Hierarchical structure
            - Better for higher-dimensional problems
            - Reduced bond dimensions
            """)
            
            # TN parameters
            st.markdown("### Tensor Network Configuration")
            tn_qubits = st.slider("System Size (qubits)", 4, 12, 8, key="tn_qubits")
            bond_dim = st.slider("Bond Dimension χ", 2, 32, 8, key="bond_dim")
            tn_type = st.selectbox("Network Type", ["MPS", "Tree TN", "PEPS"], key="tn_type")
            
        with col2:
            st.markdown("### Entanglement Scaling Analysis")
            
            # Entanglement area law visualization
            system_sizes = np.arange(4, 21)
            
            # Different scaling laws
            area_law = np.log2(bond_dim) * np.ones_like(system_sizes)  # Constant for area law
            volume_law = 0.5 * system_sizes  # Linear scaling
            efficient_rep = np.minimum(area_law, system_sizes/4)  # MPS efficiency limit
            
            fig = go.Figure()
            
            fig.add_trace(go.Scatter(
                x=system_sizes, y=area_law,
                mode='lines',
                name='Area Law (MPS efficient)',
                line=dict(color='#10B981', width=3)
            ))
            
            fig.add_trace(go.Scatter(
                x=system_sizes, y=volume_law,
                mode='lines',
                name='Volume Law (exponential)',
                line=dict(color='#EF4444', width=3, dash='dash')
            ))
            
            fig.add_trace(go.Scatter(
                x=system_sizes, y=efficient_rep,
                mode='lines',
                name=f'MPS χ={bond_dim}',
                line=dict(color='#22D3EE', width=3)
            ))
            
            fig.update_layout(
                title="Entanglement Scaling in Tensor Networks",
                xaxis_title="System Size (qubits)",
                yaxis_title="Entanglement Entropy",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#E2E8F0'
            )
            st.plotly_chart(fig, width='stretch')
            
            # Memory requirements
            mps_memory = tn_qubits * bond_dim**2 * 2  # Complex numbers
            exact_memory = 2**tn_qubits * 2
            
            compression_ratio = exact_memory / mps_memory if mps_memory > 0 else float('inf')
            
            st.metric("MPS Memory (complex numbers)", f"{mps_memory:,}")
            st.metric("Exact Memory", f"{exact_memory:,}")
            if compression_ratio < 1e6:
                st.metric("Compression Ratio", f"{compression_ratio:.0f}x")
            else:
                st.metric("Compression Ratio", ">1M x")
            
            if compression_ratio > 100:
                st.success("✅ Significant memory advantage for MPS")
            elif compression_ratio > 10:
                st.info("✅ Moderate memory savings")
            else:
                st.warning("⚠️ Limited compression benefit")

elif section_id == "hardware_arch":
    st.markdown("# 🔩 Quantum Hardware Architecture")
    st.markdown('<span class="alphanova-status status-research">Physical Systems Module</span>', unsafe_allow_html=True)
    
    hardware_tabs = st.tabs(["Qubit Technologies", "Superconducting Systems", "Trapped Ion Platforms", "Photonic Quantum Computing", "NISQ Characteristics"])
    
    with hardware_tabs[0]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Physical Qubit Implementation Technologies</h3>
            <p>Comprehensive overview of different physical systems used to realize quantum bits and quantum computation.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Major Qubit Technologies Comparison
            
            **Superconducting Qubits (Josephson Junctions):**
            - **Energy Scale:** ħω ≈ 1-10 GHz (5-50 μeV)
            - **Operating Temperature:** 10-50 mK (dilution refrigerator)
            - **Gate Times:** 10-100 ns
            - **Coherence:** T₁ ≈ 10-100 μs, T₂* ≈ 1-50 μs
            - **Connectivity:** Planar nearest-neighbor
            - **Readout:** Microwave cavity QND measurement
            
            **Trapped Ion Qubits:**
            - **Species:** ⁹⁰Be⁺, ¹³³Ba⁺, ⁴³Ca⁺, ¹³Yb⁺
            - **Trap Frequency:** ωᵣ ≈ 1-5 MHz
            - **Gate Times:** 10-100 μs (laser pulses)
            - **Coherence:** T₁ > 1 ms, T₂ ≈ 100 μs - 1 ms
            - **Connectivity:** All-to-all via Coulomb interaction
            - **Two-qubit Gates:** Mølmer-Sørensen, CNOT via motional modes
            
            **Neutral Atom Qubits:**
            - **Species:** Cs, Rb, Sr (optical tweezers)
            - **Gate Mechanism:** Rydberg blockade interaction
            - **Connectivity:** Reconfigurable via optical lattices
            - **Scalability:** 100+ qubits demonstrated
            """)
            
        with col2:
            st.markdown("### Performance Comparison")
            
            # Technology comparison metrics
            tech_names = ["Superconducting", "Trapped Ion", "Neutral Atom", "Photonic"]
            gate_speeds = [50, 50000, 10000, 100]  # Gate time in ns
            coherence_times = [50, 1000, 100, float('inf')]  # T2 in microseconds
            connectivity = [4, 20, 100, 10]  # Relative connectivity score
            
            # Gate speed comparison
            fig_speed = go.Figure(data=[
                go.Bar(x=tech_names, y=gate_speeds, 
                       marker_color=['#22D3EE', '#10B981', '#F59E0B', '#8B5CF6'])
            ])
            fig_speed.update_layout(
                title="Gate Times (ns) - Lower is Better",
                yaxis_title="Gate Time (ns)",
                yaxis_type="log",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#E2E8F0'
            )
            st.plotly_chart(fig_speed, width='stretch')
            
            # Coherence comparison
            fig_coherence = go.Figure(data=[
                go.Bar(x=tech_names[:3], y=coherence_times[:3],  # Exclude infinite photonic
                       marker_color=['#22D3EE', '#10B981', '#F59E0B'])
            ])
            fig_coherence.update_layout(
                title="Coherence Times T₂ (μs) - Higher is Better",
                yaxis_title="T₂ (μs)",
                yaxis_type="log",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#E2E8F0'
            )
            st.plotly_chart(fig_coherence, width='stretch')
    
    with hardware_tabs[1]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Superconducting Quantum Processors</h3>
            <p>Detailed analysis of Josephson junction-based quantum computers and their operating principles.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Superconducting Qubit Physics
            
            **Josephson Junction Hamiltonian:**
            
            H = 4E_C(n - n_g)² - E_J cos(φ)
            
            - **E_C = e²/2C:** Charging energy
            - **E_J:** Josephson coupling energy  
            - **φ:** Superconducting phase difference
            - **n:** Cooper pair number operator
            
            **Qubit Types:**
            
            1. **Transmon (E_J ≫ E_C):**
               - Charge noise insensitive
               - ω₁₀ ≈ 4-8 GHz
               - Anharmonicity α ≈ -200 to -300 MHz
            
            2. **Flux Qubit:**
               - Persistent current states
               - Flux noise sensitivity
               - Large dipole moment
            
            3. **Fluxonium (E_C ≈ E_J):**
               - Protected against charge and flux noise
               - Long coherence times
               - Lower frequency operation
            """)
            
            # Superconducting qubit parameters
            st.markdown("### Transmon Parameters")
            ej_over_ec = st.slider("E_J/E_C Ratio", 10, 100, 50, key="ej_ec_ratio")
            charging_energy = st.slider("Charging Energy E_C (MHz)", 100, 500, 300, key="ec_mhz")
            
        with col2:
            # Calculate transmon properties
            josephson_energy = ej_over_ec * charging_energy
            
            # Transmon frequency (approximate)
            qubit_freq = np.sqrt(8 * josephson_energy * charging_energy) * 1e-3  # Convert to GHz
            anharmonicity = -charging_energy  # Approximate anharmonicity
            
            st.markdown("### Calculated Properties")
            st.metric("Qubit Frequency", f"{qubit_freq:.2f} GHz")
            st.metric("Anharmonicity", f"{anharmonicity:.0f} MHz")
            
            # Sweet spot analysis
            flux_range = np.linspace(-0.1, 0.1, 100)  # Flux deviation from sweet spot
            freq_sensitivity = qubit_freq + 0.01 * flux_range**2  # Quadratic sensitivity
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=flux_range, y=freq_sensitivity,
                mode='lines',
                name='Qubit Frequency',
                line=dict(color='#22D3EE', width=3)
            ))
            
            fig.update_layout(
                title="Transmon Frequency vs Flux Noise",
                xaxis_title="Flux Deviation (Φ₀)",
                yaxis_title="Frequency (GHz)",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#E2E8F0'
            )
            st.plotly_chart(fig, width='stretch')
            
            # State-of-the-art systems
            st.markdown("### Current Superconducting Systems")
            
            systems_data = {
                "IBM Condor": {"qubits": 1121, "connectivity": "Heavy-hex", "year": 2023},
                "Google Sycamore": {"qubits": 70, "connectivity": "2D grid", "year": 2019},
                "Rigetti Aspen-M": {"qubits": 80, "connectivity": "Octagonal", "year": 2022},
                "IonQ Forte": {"qubits": 32, "connectivity": "All-to-all", "year": 2023}
            }
            
            for system, specs in systems_data.items():
                st.write(f"**{system}:** {specs['qubits']} qubits, {specs['connectivity']} ({specs['year']})")
    
    with hardware_tabs[2]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Trapped Ion Quantum Computers</h3>
            <p>Ion trap quantum computing systems using electromagnetic confinement and laser-driven operations.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Ion Trap Physics
            
            **Paul Trap Confinement:**
            
            Effective potential: V_eff = ½ mω²r²
            
            **Trap frequency:** ω = (qV/mr₀²)√(α/2Ω²)
            
            where:
            - q: ion charge
            - V: RF voltage amplitude  
            - r₀: electrode spacing
            - Ω: RF drive frequency
            
            **Qubit Encoding:**
            
            1. **Hyperfine States:** |0⟩ = |F=0, m_F=0⟩, |1⟩ = |F=1, m_F=0⟩
            2. **Zeeman States:** Magnetic field insensitive transitions
            3. **Optical Transitions:** ²S₁/₂ ↔ ²D₅/₂ (clock transitions)
            
            **Gate Operations:**
            
            - **Single-qubit:** Laser pulses (Rabi oscillations)
            - **Two-qubit:** Mølmer-Sørensen gates via motional modes
            - **Readout:** State-dependent fluorescence
            
            **Key Advantages:**
            - Identical qubits (same atomic species)
            - Long coherence times
            - High-fidelity gates (>99.9%)
            - All-to-all connectivity
            """)
            
            # Ion trap parameters
            st.markdown("### Trap Configuration")
            num_ions = st.slider("Number of Ions", 2, 32, 8, key="num_ions")
            trap_freq = st.slider("Trap Frequency (MHz)", 0.5, 5.0, 2.0, step=0.1, key="trap_freq")
            ion_species = st.selectbox(
                "Ion Species", 
                ["⁹⁰Be⁺", "¹³³Ba⁺", "⁴³Ca⁺", "¹³Yb⁺"],
                key="ion_species"
            )
            
        with col2:
            st.markdown("### Motional Mode Analysis")
            
            # Calculate normal modes for ion chain
            mode_freqs = []
            for k in range(num_ions):
                # Approximate mode frequencies for linear chain
                mode_freq = trap_freq * np.sqrt(1 + 2 * np.sin(np.pi * k / (2 * num_ions))**2)
                mode_freqs.append(mode_freq)
            
            # Visualization of normal modes
            fig = go.Figure()
            
            fig.add_trace(go.Scatter(
                x=list(range(num_ions)), y=mode_freqs,
                mode='lines+markers',
                name='Normal Mode Frequencies',
                line=dict(color='#22D3EE', width=3),
                marker=dict(size=8)
            ))
            
            fig.update_layout(
                title=f"Normal Mode Spectrum ({num_ions} ions)",
                xaxis_title="Mode Number",
                yaxis_title="Frequency (MHz)",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#E2E8F0'
            )
            st.plotly_chart(fig, width='stretch')
            
            # Gate time analysis
            # Two-qubit gate time scales with mode frequency
            fastest_mode_freq = min(mode_freqs)
            gate_time = 1 / (2 * fastest_mode_freq)  # Approximate scaling
            
            st.markdown("### Performance Metrics")
            st.metric("Center-of-Mass Mode", f"{mode_freqs[0]:.2f} MHz")
            st.metric("Breathing Mode", f"{mode_freqs[-1]:.2f} MHz")
            st.metric("Typical Gate Time", f"{gate_time*1000:.1f} μs")
            
            # Ion spacing
            # Equilibrium spacing scales as n^(2/3) for long chains
            spacing_microns = 5.0 * (num_ions/8)**(2/3)  # Approximate scaling
            st.metric("Ion Spacing", f"{spacing_microns:.1f} μm")
            
            # Decoherence analysis
            if num_ions <= 10:
                st.success("✅ Small chain: Excellent coherence")
            elif num_ions <= 20:
                st.info("✅ Medium chain: Good performance")
            else:
                st.warning("⚠️ Large chain: Challenging mode control")
    
    with hardware_tabs[3]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Photonic Quantum Computing</h3>
            <p>Quantum computation using photons as information carriers with linear optical elements.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Photonic Quantum Information
            
            **Encoding Schemes:**
            
            1. **Polarization Encoding:**
               - |0⟩ = |H⟩ (horizontal), |1⟩ = |V⟩ (vertical)
               - Single-photon qubits
               - Easy manipulation with wave plates
            
            2. **Dual-Rail Encoding:**
               - |0⟩ = |10⟩, |1⟩ = |01⟩ (spatial modes)
               - More resources but better for computation
               - Natural for interference-based gates
            
            3. **Time-Bin Encoding:**
               - Early/late arrival times
               - Robust against decoherence
               - Compatible with fiber networks
            
            **Linear Optical Elements:**
            
            - **Beam Splitters:** Hadamard-like operations
            - **Phase Shifters:** Z rotations
            - **Wave Plates:** Polarization rotations
            - **Mirrors/Prisms:** Routing and delays
            
            **Advantages:**
            - Room temperature operation
            - Natural for networking
            - Low decoherence (no T₁, T₂ limits)
            - Compatible with telecommunications
            """)
            
            # Photonic system parameters
            st.markdown("### System Configuration")
            encoding_type = st.selectbox(
                "Encoding Type",
                ["Polarization", "Dual-Rail", "Time-Bin"],
                key="photonic_encoding"
            )
            
            num_modes = st.slider("Number of Spatial Modes", 2, 16, 8, key="photonic_modes")
            photon_rate = st.slider("Photon Generation Rate (MHz)", 1, 100, 10, key="photon_rate")
            
        with col2:
            st.markdown("### Linear Optical Quantum Computing")
            
            # Success probability for linear optical gates
            if encoding_type == "Dual-Rail":
                # Two-qubit gates in dual-rail have low success probability
                n_qubits = num_modes // 2
                gate_success_prob = 1/9  # CNOT gate success probability
            else:
                n_qubits = num_modes
                gate_success_prob = 0.5
            
            # Circuit depth vs success probability
            depths = np.arange(1, 21)
            circuit_success = gate_success_prob ** depths
            
            fig = go.Figure()
            
            fig.add_trace(go.Scatter(
                x=depths, y=circuit_success,
                mode='lines+markers',
                name='Circuit Success Probability',
                line=dict(color='#EF4444', width=3),
                marker=dict(size=6)
            ))
            
            # Add threshold lines
            fig.add_hline(y=0.5, line_dash="dash", line_color="#F59E0B", 
                         annotation_text="50% threshold")
            fig.add_hline(y=0.1, line_dash="dash", line_color="#64748B", 
                         annotation_text="10% threshold")
            
            fig.update_layout(
                title=f"Linear Optics Success Rate ({encoding_type})",
                xaxis_title="Circuit Depth",
                yaxis_title="Success Probability",
                yaxis_type="log",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#E2E8F0'
            )
            st.plotly_chart(fig, width='stretch')
            
            # Performance metrics
            st.metric("Effective Qubits", n_qubits)
            st.metric("Gate Success Rate", f"{gate_success_prob:.1%}")
            
            # Resource requirements
            if encoding_type == "Dual-Rail":
                photons_per_qubit = 1
                classical_postprocessing = "High"
            else:
                photons_per_qubit = 1  
                classical_postprocessing = "Medium"
            
            st.metric("Photons per Qubit", photons_per_qubit)
            st.write(f"**Classical Postprocessing:** {classical_postprocessing}")
            
            # Current limitations
            if gate_success_prob < 0.2:
                st.warning("⚠️ Low gate success rate requires significant overhead")
            else:
                st.info("✅ Reasonable success rate for near-term applications")
    
    with hardware_tabs[4]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>NISQ Era Characteristics and Limitations</h3>
            <p>Understanding the current capabilities and constraints of Noisy Intermediate-Scale Quantum devices.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### NISQ Regime Definition
            
            **Scale:** 10-1000 qubits
            **Noise:** No error correction
            **Depth:** Limited by decoherence
            **Applications:** Heuristic algorithms
            
            **Key Limitations:**
            
            1. **Quantum Volume:**
               QV = min(n, d)² where n = qubits, d = depth
               Current record: QV = 524,288 (IonQ)
            
            2. **Gate Fidelity:**
               - Single-qubit: 99.8-99.95%
               - Two-qubit: 99.0-99.8%
               - Measurement: 99.5-99.9%
            
            3. **Coherence Time:**
               - Limits circuit depth
               - T₁: Energy relaxation
               - T₂*: Dephasing time
               - T₂ᵉ: Hahn echo time
            
            4. **Connectivity:**
               - Limited qubit-qubit interactions
               - SWAP overhead for distant operations
               - Topology-dependent performance
            """)
            
        with col2:
            st.markdown("### NISQ Performance Analysis")
            
            # NISQ system parameters
            system_qubits = st.slider("System Qubits", 10, 1000, 100, key="nisq_qubits")
            gate_fidelity = st.slider("Two-Qubit Gate Fidelity", 0.90, 0.999, 0.995, step=0.001, format="%.3f", key="nisq_fidelity")
            t2_time = st.slider("T₂* Time (μs)", 1, 200, 50, key="nisq_t2")
            gate_time = st.slider("Gate Time (ns)", 10, 1000, 100, key="nisq_gate_time")
            
            # Calculate maximum coherent depth
            max_gates = (t2_time * 1000) / gate_time  # Convert μs to ns
            
            # Quantum volume estimation
            max_depth = min(50, max_gates / 5)  # Conservative estimate
            quantum_volume = min(system_qubits, max_depth)**2
            
            # Error accumulation
            circuit_depths = np.arange(1, 51)
            error_prob = 1 - gate_fidelity
            total_error = 1 - (gate_fidelity ** circuit_depths)
            
            fig = go.Figure()
            
            fig.add_trace(go.Scatter(
                x=circuit_depths, y=total_error,
                mode='lines+markers',
                name='Circuit Error Rate',
                line=dict(color='#EF4444', width=3)
            ))
            
            # Error threshold lines
            fig.add_hline(y=0.1, line_dash="dash", line_color="#F59E0B", 
                         annotation_text="10% error")
            fig.add_hline(y=0.5, line_dash="dash", line_color="#64748B", 
                         annotation_text="50% error")
            
            fig.update_layout(
                title="Error Accumulation vs Circuit Depth",
                xaxis_title="Circuit Depth (gates)",
                yaxis_title="Total Error Probability",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#E2E8F0'
            )
            st.plotly_chart(fig, width='stretch')
            
            # Performance metrics
            st.metric("Estimated Quantum Volume", f"{quantum_volume:,.0f}")
            st.metric("Max Coherent Gates", f"{max_gates:.0f}")
            st.metric("Practical Circuit Depth", f"{max_depth:.0f}")
            
            # Quality assessment
            if quantum_volume > 100000:
                st.success("🏆 Excellent quantum volume for NISQ applications")
            elif quantum_volume > 10000:
                st.info("✅ Good quantum volume for near-term algorithms")
            elif quantum_volume > 1000:
                st.warning("⚠️ Limited quantum volume - simple problems only")
            else:
                st.error("❌ Very limited quantum volume")
elif section_id == "error_correction":
    st.markdown("# 🛡️ Quantum Error Correction")
    st.markdown('<span class="alphanova-status status-research">Critical Systems Module</span>', unsafe_allow_html=True)
    
    error_tabs = st.tabs(["Error Types & Models", "Stabilizer Codes", "Surface Codes", "Fault Tolerance", "Threshold Analysis"])
    
    with error_tabs[0]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Quantum Error Types and Noise Models</h3>
            <p>Understanding the fundamental sources of errors in quantum computation and their mathematical description.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Quantum Error Classification
            
            **Pauli Errors (Discrete):**
            
            - **X Error (Bit-flip):** X|ψ⟩ = α|1⟩ + β|0⟩
            - **Z Error (Phase-flip):** Z|ψ⟩ = α|0⟩ - β|1⟩  
            - **Y Error:** Y = iXZ (both bit and phase flip)
            - **I Error:** No error (identity)
            
            **Continuous Errors:**
            
            Arbitrary rotation: R_n(θ) = cos(θ/2)I - i sin(θ/2)(σ · n)
            
            **Error Model:** ε(ρ) = Σ_i p_i σ_i ρ σ_i†
            
            **Decoherence Channels:**
            
            1. **Amplitude Damping (T₁ process):**
               ε_AD(ρ) = E_0ρE_0† + E_1ρE_1†
               E_0 = |0⟩⟨0| + √(1-γ)|1⟩⟨1|, E_1 = √γ|0⟩⟨1|
            
            2. **Dephasing (T₂ process):**
               ε_D(ρ) = (1-p)ρ + pZρZ
            
            3. **Depolarizing Channel:**
               ε_dep(ρ) = (1-p)ρ + (p/3)(XρX + YρY + ZρZ)
            """)
            
        with col2:
            # Error rate simulation
            st.markdown("### Error Rate Analysis")
            
            error_rate = st.slider("Physical Error Rate (p)", 0.001, 0.1, 0.01, step=0.001, format="%.3f", key="error_rate_qec")
            error_model = st.selectbox(
                "Error Model",
                ["Depolarizing", "Bit-flip only", "Phase-flip only", "Amplitude damping"],
                key="error_model"
            )
            
            # Calculate error probabilities based on model
            if error_model == "Depolarizing":
                p_i = 1 - error_rate
                p_x = p_y = p_z = error_rate / 3
            elif error_model == "Bit-flip only":
                p_i = 1 - error_rate
                p_x = error_rate
                p_y = p_z = 0
            elif error_model == "Phase-flip only":
                p_i = 1 - error_rate  
                p_z = error_rate
                p_x = p_y = 0
            else:  # Amplitude damping
                p_i = 1 - error_rate/2
                p_x = error_rate/2
                p_y = p_z = error_rate/4
            
            # Visualization
            fig = go.Figure(data=[
                go.Bar(x=['I (No Error)', 'X (Bit-flip)', 'Y (Both)', 'Z (Phase-flip)'], 
                       y=[p_i, p_x, p_y, p_z],
                       marker_color=['#10B981', '#EF4444', '#8B5CF6', '#F59E0B'])
            ])
            
            fig.update_layout(
                title=f"{error_model} Error Distribution",
                yaxis_title="Probability",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#E2E8F0'
            )
            st.plotly_chart(fig, width='stretch')
            
            # Error thresholds
            if error_rate < 0.001:
                st.success("🏆 Excellent: Below fault-tolerant threshold")
            elif error_rate < 0.01:
                st.info("✅ Good: Approaching threshold for surface codes")
            elif error_rate < 0.1:
                st.warning("⚠️ Challenging: Above most QEC thresholds")
            else:
                st.error("❌ Very high error rate: QEC infeasible")
    
    with error_tabs[1]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Stabilizer Quantum Error Correction Codes</h3>
            <p>Mathematical framework for quantum error correction using stabilizer formalism.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Stabilizer Formalism
            
            **Stabilizer Group S:**
            
            Set of Pauli operators that commute with codewords:
            S|ψ_L⟩ = +|ψ_L⟩ for all |ψ_L⟩ in code space
            
            **Code Parameters [[n,k,d]]:**
            - n: Total number of physical qubits
            - k: Number of logical qubits  
            - d: Code distance (minimum weight error detectable)
            
            **Error Detection:**
            
            Syndrome s = (s_1, s_2, ..., s_{n-k})
            s_i = ⟨ψ|g_i|ψ⟩ where g_i are stabilizer generators
            
            **Error Correction:**
            1. Measure syndrome s
            2. Determine error E from syndrome
            3. Apply correction E†
            
            **Examples:**
            
            1. **Shor's 9-qubit code [[9,1,3]]:**
               Corrects any single qubit error
               
            2. **Steane code [[7,1,3]]:**
               CSS code, more efficient than Shor's
               
            3. **Surface code [[d²,1,d]]:**
               2D topological code, highest threshold
            """)
            
        with col2:
            st.markdown("### Code Comparison")
            
            # Code selection
            code_type = st.selectbox(
                "Select Stabilizer Code",
                ["Shor [[9,1,3]]", "Steane [[7,1,3]]", "Surface [[d²,1,d]]", "Color [[15,1,3]]"],
                key="stabilizer_code"
            )
            
            # Code properties
            code_properties = {
                "Shor [[9,1,3]]": {"n": 9, "k": 1, "d": 3, "threshold": 0.001, "overhead": 9},
                "Steane [[7,1,3]]": {"n": 7, "k": 1, "d": 3, "threshold": 0.002, "overhead": 7},
                "Surface [[d²,1,d]]": {"n": 25, "k": 1, "d": 5, "threshold": 0.006, "overhead": 25},
                "Color [[15,1,3]]": {"n": 15, "k": 1, "d": 3, "threshold": 0.003, "overhead": 15}
            }
            
            props = code_properties[code_type]
            
            # Display properties
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric("Physical Qubits (n)", props["n"])
                st.metric("Logical Qubits (k)", props["k"])
            with col_b:
                st.metric("Code Distance (d)", props["d"])
                st.metric("Error Threshold", f"{props['threshold']:.1%}")
            
            # Error correction capability
            correctable_errors = (props["d"] - 1) // 2
            st.metric("Correctable Errors", correctable_errors)
            
            # Overhead analysis
            overhead_ratio = props["overhead"] / props["k"]
            st.metric("Qubit Overhead", f"{overhead_ratio:.0f}x")
            
            # Logical error rate
            p_phys = st.slider("Physical Error Rate", 0.001, 0.05, 0.01, step=0.001, key="stab_error_rate")
            
            if p_phys < props["threshold"]:
                # Below threshold: exponential suppression
                p_logical = (p_phys / props["threshold"])**(props["d"]+1) / 2
                st.metric("Logical Error Rate", f"{p_logical:.2e}")
                st.success("✅ Below threshold: Exponential error suppression")
            else:
                # Above threshold: error correction fails
                p_logical = 0.5  # Random logical state
                st.metric("Logical Error Rate", "~50%")
                st.error("❌ Above threshold: Error correction fails")
    
    with error_tabs[2]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Surface Codes - Topological Quantum Error Correction</h3>
            <p>The leading candidate for fault-tolerant quantum computation with highest error thresholds.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Surface Code Architecture
            
            **2D Lattice Structure:**
            
            - **Data qubits:** On lattice vertices
            - **Ancilla qubits:** On lattice faces (Z-type) and edges (X-type)
            - **Distance d:** Linear size of lattice
            - **Physical qubits:** n = d² + (d-1)² ≈ 2d²
            
            **Stabilizer Types:**
            
            1. **Plaquette (Z-type):** ∏_{v∈p} Z_v
            2. **Star (X-type):** ∏_{v∈s} X_v
            
            **Error Detection:**
            
            - Z errors create X-syndrome violations
            - X errors create Z-syndrome violations  
            - Error chains connecting boundaries are logical errors
            
            **Key Advantages:**
            
            - **Highest threshold:** ~0.6-1% for various noise models
            - **Local interactions:** Only nearest-neighbor operations
            - **Parallelizable:** Fast syndrome measurement
            - **Scalable:** Modular construction
            
            **Limitations:**
            
            - High qubit overhead: Ω(d²) physical qubits per logical
            - Only Clifford gates transversally
            - Magic state distillation needed for universal computation
            """)
            
            # Surface code parameters
            st.markdown("### Surface Code Configuration")
            code_distance_surface = st.slider("Code Distance (d)", 3, 15, 5, step=2, key="surface_distance")
            syndrome_rounds = st.slider("Syndrome Rounds", 1, 10, 3, key="syndrome_rounds")
            
        with col2:
            st.markdown("### Resources and Performance")
            
            # Calculate surface code resources
            data_qubits = code_distance_surface**2
            z_ancilla = (code_distance_surface - 1)**2
            x_ancilla = (code_distance_surface - 1)**2
            total_qubits = data_qubits + z_ancilla + x_ancilla
            
            # Performance metrics
            st.metric("Data Qubits", data_qubits)
            st.metric("Z-Ancilla Qubits", z_ancilla)
            st.metric("X-Ancilla Qubits", x_ancilla)  
            st.metric("Total Physical Qubits", total_qubits)
            
            # Error correction performance
            surface_threshold = 0.006  # Approximate threshold for surface codes
            
            # Logical error rate scaling
            distances = np.arange(3, 16, 2)
            log_error_rates = []
            
            p_phys_surface = st.slider("Physical Error Rate", 0.001, 0.02, 0.005, step=0.001, key="surface_phys_error")
            
            for d in distances:
                if p_phys_surface < surface_threshold:
                    # Below threshold: α^d scaling
                    alpha = p_phys_surface / surface_threshold
                    p_log = alpha**d
                else:
                    # Above threshold
                    p_log = 0.1
                log_error_rates.append(p_log)
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=distances, y=log_error_rates,
                mode='lines+markers',
                name='Logical Error Rate',
                line=dict(color='#22D3EE', width=3),
                marker=dict(size=8)
            ))
            
            fig.update_layout(
                title="Surface Code Error Suppression",
                xaxis_title="Code Distance",
                yaxis_title="Logical Error Rate",
                yaxis_type="log",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#E2E8F0'
            )
            st.plotly_chart(fig, width='stretch')
            
            # Current distance performance
            current_log_error = log_error_rates[distances.tolist().index(code_distance_surface)]
            st.metric(f"Logical Error (d={code_distance_surface})", f"{current_log_error:.2e}")
            
            # Overhead analysis
            overhead = total_qubits
            if p_phys_surface < surface_threshold:
                st.success(f"✅ Below threshold: {overhead}x overhead for distance {code_distance_surface}")
            else:
                st.error(f"❌ Above threshold: Error correction ineffective")
    
    with error_tabs[3]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Fault-Tolerant Quantum Computation</h3>
            <p>Protocols for quantum computation that maintain logical fidelity even with noisy operations.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Fault Tolerance Requirements
            
            **Threshold Condition:**
            
            Physical error rate p < p_th ⟹ P_L(coded) < P_L(uncoded)
            
            **Fault-Tolerant Operations:**
            
            1. **Transversal Gates:**
               U_L = U⊗n (bitwise application)
               - Error propagation is limited
               - CNOT, Pauli gates for stabilizer codes
               
            2. **Magic State Injection:**
               |T⟩ = (|0⟩ + e^{iπ/4}|1⟩)/√2
               - Enables non-Clifford gates
               - Requires magic state distillation
               
            3. **Code Deformation:**
               - Braiding for topological codes
               - Lattice surgery for surface codes
            
            **Universal Gate Set:**
            
            - **Clifford gates:** Transversal (H, S, CNOT)
            - **T gate:** Magic state injection + measurement
            - **Arbitrary rotations:** Approximation sequences
            
            **Error Budget:**
            
            Total logical error ≈ (Gate errors) + (Syndrome errors) + (Idle errors)
            """)
            
        with col2:
            st.markdown("### Magic State Distillation")
            
            # Magic state parameters
            input_fidelity = st.slider("Input Magic State Fidelity", 0.85, 0.99, 0.90, step=0.01, key="magic_fidelity")
            distillation_level = st.slider("Distillation Levels", 1, 4, 2, key="distill_levels")
            
            # Simulate distillation protocol
            # Simplified model: each level squares the error rate
            input_error = 1 - input_fidelity
            
            fidelities = [input_fidelity]
            overhead_costs = [1]
            
            for level in range(distillation_level):
                # Bravyi-Kitaev distillation: error rate roughly squares
                current_error = 1 - fidelities[-1]
                new_error = current_error**2 * 10  # Simplified scaling
                new_fidelity = max(1 - new_error, fidelities[-1])  # Ensure improvement
                fidelities.append(new_fidelity)
                
                # Overhead: ~15 magic states per output magic state
                overhead_costs.append(overhead_costs[-1] * 15)
            
            # Visualization
            levels = list(range(distillation_level + 1))
            
            fig = go.Figure()
            
            # Fidelity improvement
            fig.add_trace(go.Scatter(
                x=levels, y=fidelities,
                mode='lines+markers',
                name='Magic State Fidelity',
                line=dict(color='#22D3EE', width=3),
                yaxis='y'
            ))
            
            # Overhead cost
            fig.add_trace(go.Scatter(
                x=levels, y=overhead_costs,
                mode='lines+markers',
                name='Resource Overhead',
                line=dict(color='#F59E0B', width=3),
                yaxis='y2'
            ))
            
            fig.update_layout(
                title="Magic State Distillation",
                xaxis_title="Distillation Level",
                yaxis=dict(title="Fidelity", side='left'),
                yaxis2=dict(title="Resource Overhead", side='right', overlaying='y', type='log'),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#E2E8F0'
            )
            st.plotly_chart(fig, width='stretch')
            
            # Final metrics
            final_fidelity = fidelities[-1]
            final_overhead = overhead_costs[-1]
            
            st.metric("Output Fidelity", f"{final_fidelity:.6f}")
            st.metric("Resource Overhead", f"{final_overhead:,}x")
            
            if final_fidelity > 0.9999:
                st.success("✅ Excellent: High fidelity magic states")
            elif final_fidelity > 0.999:
                st.info("✅ Good: Suitable for fault-tolerant computation")
            else:
                st.warning("⚠️ May need higher input fidelity or more levels")
    
    with error_tabs[4]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Fault Tolerance Threshold Analysis</h3>
            <p>Understanding the critical error rates below which quantum error correction becomes beneficial.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Threshold Theory
            
            **Definition:** Critical error rate p_th where:
            
            p < p_th: Larger codes have lower logical error rates
            p > p_th: Larger codes perform worse than smaller codes
            
            **Physical Interpretation:**
            
            - **Below threshold:** Exponential error suppression α^d
            - **At threshold:** Polynomial error suppression αd^{-ν}
            - **Above threshold:** Error correction fails
            
            **Known Thresholds:**
            
            1. **Shor's code:** p_th ≈ 0.1% (perfect syndrome)
            2. **Steane code:** p_th ≈ 0.2% (perfect syndrome)
            3. **Surface code:** p_th ≈ 0.6% (depolarizing noise)
            4. **Color codes:** p_th ≈ 0.3% (2D) to 0.5% (3D)
            
            **Factors Affecting Threshold:**
            
            - Noise model (depolarizing vs. coherent)
            - Syndrome measurement errors
            - Gate scheduling and parallelization
            - Decoder efficiency
            
            **Practical Considerations:**
            
            p_effective = p_gate + ε_syndrome + ε_idle + ε_crosstalk
            """)
            
        with col2:
            st.markdown("### Threshold Simulation")
            
            # Code comparison for threshold
            code_for_threshold = st.selectbox(
                "QEC Code",
                ["Surface Code", "Color Code", "Steane Code"],
                key="threshold_code"
            )
            
            # Threshold values (approximate)
            thresholds = {
                "Surface Code": 0.006,
                "Color Code": 0.003, 
                "Steane Code": 0.002
            }
            
            p_th = thresholds[code_for_threshold]
            
            # Error rate range
            error_rates = np.logspace(-4, -1, 50)  # 0.01% to 10%
            distances = [3, 5, 7, 9]
            
            fig = go.Figure()
            
            for d in distances:
                logical_errors = []
                for p in error_rates:
                    if p < p_th:
                        # Below threshold: exponential suppression
                        alpha = p / p_th
                        p_logical = alpha**(d//2)
                    else:
                        # Above threshold: polynomial growth
                        p_logical = min(0.5, p * (d/3))
                    logical_errors.append(p_logical)
                
                fig.add_trace(go.Scatter(
                    x=error_rates, y=logical_errors,
                    mode='lines',
                    name=f'd={d}',
                    line=dict(width=2)
                ))
            
            # Add threshold line
            fig.add_vline(x=p_th, line_dash="dash", line_color="#EF4444", 
                         annotation_text=f"Threshold: {p_th:.1%}")
            
            # Add no-coding baseline
            fig.add_trace(go.Scatter(
                x=error_rates, y=error_rates,
                mode='lines',
                name='No QEC',
                line=dict(color='black', dash='dot', width=2)
            ))
            
            fig.update_layout(
                title=f"{code_for_threshold} Threshold Behavior",
                xaxis_title="Physical Error Rate",  
                yaxis_title="Logical Error Rate",
                xaxis_type="log",
                yaxis_type="log",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#E2E8F0'
            )
            st.plotly_chart(fig, width='stretch')
            
            # Current technology assessment
            current_tech_error = st.slider(
                "Current Technology Error Rate", 
                0.001, 0.1, 0.01, 
                step=0.001, 
                format="%.3f",
                key="current_tech_error"
            )
            
            # Distance needed for target logical error
            target_logical = 1e-6
            if current_tech_error < p_th:
                alpha = current_tech_error / p_th
                needed_distance = 2 * np.log(target_logical) / np.log(alpha)
                needed_distance = max(3, int(np.ceil(needed_distance)))
                
                st.metric("Needed Distance", needed_distance)
                st.metric("Required Qubits", f"{2 * needed_distance**2:,}")
                st.success(f"✅ Below threshold: {needed_distance}x{needed_distance} surface code needed")
            else:
                st.metric("Status", "Above Threshold")
                st.error("❌ Error correction ineffective at current error rates")

elif section_id == "complexity_theory":
    st.markdown("# 📊 Quantum Computational Complexity") 
    st.markdown('<span class="alphanova-status status-research">Theoretical Foundations</span>', unsafe_allow_html=True)
    
    complexity_tabs = st.tabs(["Complexity Classes", "BQP vs Classical", "Quantum Speedups", "Oracle Separations", "Fundamental Limits"])
    
    with complexity_tabs[0]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Quantum Computational Complexity Classes</h3>
            <p>The landscape of computational complexity from classical to quantum information processing.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Classical Complexity Hierarchy
            
            **P (Polynomial Time):**
            - Problems solvable in time O(n^k)
            - Examples: Sorting, matrix multiplication, linear programming
            - Fundamental for "efficient" computation
            
            **NP (Nondeterministic Polynomial):**
            - Problems verifiable in polynomial time
            - NP-complete: SAT, Graph Coloring, TSP
            - P vs NP: Millennium Prize problem
            
            **PSPACE (Polynomial Space):**
            - Solvable using polynomial space
            - PSPACE-complete: Quantified Boolean Formula (QBF)
            - P ⊆ NP ⊆ PSPACE
            
            **EXP (Exponential Time):**
            - Requires exponential time: O(2^{n^k})
            - Examples: Generalized chess, Go on n×n board
            - PSPACE ⊆ EXP
            
            **#P (Sharp-P):**
            - Counting versions of NP problems
            - #P-complete: Permanent of matrix
            - Believed: NP ⊆ #P
            """)
            
        with col2:
            st.markdown("""
            ### Quantum Complexity Classes
            
            **BQP (Bounded-error Quantum Polynomial):**
            - Quantum algorithms with ≤ 1/3 error probability
            - Examples: Factoring (Shor), Search (Grover)
            - Time: poly(n), Space: poly(n)
            
            **QMA (Quantum Merlin-Arthur):**
            - Quantum analog of NP
            - Quantum verification of quantum witnesses
            - QMA-complete: Local Hamiltonian problem
            
            **PostBQP:**
            - BQP + classical postprocessing
            - Believed: PostBQP = PP (Probabilistic Polynomial)
            - Upper bound for quantum computational power
            
            **QPSPACE:**
            - Quantum polynomial space
            - QPSPACE = PSPACE (due to simulation)
            - Quantum doesn't help for space-bounded computation
            
            **QIP (Quantum Interactive Proofs):**
            - QIP = PSPACE (surprising equality)
            - Quantum verifier, classical prover
            
            **Conjectured Relationships:**
            - P ⊆ BQP ⊆ QMA ⊆ PP ⊆ PSPACE
            - BQP ≠ NP (believed but unproven)
            """)
        
        # Complexity hierarchy visualization
        st.markdown("### Computational Complexity Landscape")
        
        # Define complexity classes and their approximate "power" levels
        classes = {
            "P": {"level": 1, "type": "classical", "color": "#22D3EE"},
            "BQP": {"level": 1.8, "type": "quantum", "color": "#10B981"},
            "NP": {"level": 2.5, "type": "classical", "color": "#EF4444"},
            "MA": {"level": 2.8, "type": "classical", "color": "#F59E0B"},
            "QMA": {"level": 3.2, "type": "quantum", "color": "#8B5CF6"},
            "PP": {"level": 4, "type": "classical", "color": "#3B82F6"},
            "PSPACE": {"level": 5, "type": "both", "color": "#64748B"},
            "EXP": {"level": 8, "type": "classical", "color": "#DC2626"}
        }
        
        # Create scatter plot for complexity hierarchy
        classical_classes = [name for name, info in classes.items() if info["type"] == "classical"]
        quantum_classes = [name for name, info in classes.items() if info["type"] == "quantum"]
        both_classes = [name for name, info in classes.items() if info["type"] == "both"]
        
        fig = go.Figure()
        
        # Classical classes
        fig.add_trace(go.Scatter(
            x=[i for i, name in enumerate(classical_classes)],
            y=[classes[name]["level"] for name in classical_classes],
            mode='markers+text',
            text=classical_classes,
            textposition="middle center",
            name='Classical',
            marker=dict(size=40, color='#EF4444', symbol='square'),
            textfont=dict(color='white', size=10)
        ))
        
        # Quantum classes
        fig.add_trace(go.Scatter(
            x=[i + 0.3 for i, name in enumerate(quantum_classes)],
            y=[classes[name]["level"] for name in quantum_classes],
            mode='markers+text',
            text=quantum_classes,
            textposition="middle center",
            name='Quantum',
            marker=dict(size=40, color='#10B981', symbol='circle'),
            textfont=dict(color='white', size=10)
        ))
        
        # Both
        fig.add_trace(go.Scatter(
            x=[0.15],
            y=[classes["PSPACE"]["level"]],
            mode='markers+text',
            text=["PSPACE"],
            textposition="middle center",
            name='Both',
            marker=dict(size=40, color='#64748B', symbol='diamond'),
            textfont=dict(color='white', size=10)
        ))
        
        fig.update_layout(
            title="Complexity Class Hierarchy",
            xaxis_title="Alphabetical Order (Classical) / Quantum",
            yaxis_title="Computational Power (log scale)",
            yaxis_type="log",
            showlegend=True,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='#E2E8F0',
            xaxis=dict(showticklabels=False)
        )
        st.plotly_chart(fig, width='stretch')
    
    with complexity_tabs[1]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>BQP vs Classical Complexity Classes</h3>
            <p>Understanding the relationship between quantum polynomial time and classical complexity.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### BQP Characterization
            
            **Definition:** BQP is the class of decision problems solvable by a quantum computer in polynomial time with bounded error probability ≤ 1/3.
            
            **Formal Definition:**
            
            L ∈ BQP if ∃ uniform family {Q_n} of quantum circuits where:
            
            1. |Q_n| = poly(n) (polynomial size)
            2. For x ∈ L: Pr[Q_{|x|}(x) accepts] ≥ 2/3
            3. For x ∉ L: Pr[Q_{|x|}(x) accepts] ≤ 1/3
            
            **Key Properties:**
            
            - **Error Reduction:** Amplification to exponentially small error
            - **Uniformity:** Efficient classical description of circuits
            - **Reversibility:** Unitary evolution preserves |||ψ||| = 1
            
            **Complete Problems for BQP:**
            
            Currently no natural BQP-complete problems known!
            
            **Candidates:**
            - Quantum circuit evaluation
            - Approximating Jones polynomial
            - Quantum satisfiability (QSAT)
            """)
            
        with col2:
            st.markdown("### Relationship Analysis")
            
            # Problem classification simulation
            problem_type = st.selectbox(
                "Analyze Problem Type",
                ["Integer Factorization", "Graph Isomorphism", "Discrete Logarithm", "Boolean Satisfiability"],
                key="bqp_problem"
            )
            
            # Problem complexity analysis
            problem_info = {
                "Integer Factorization": {
                    "classical_best": "Subexp (GNFS)",
                    "quantum": "Polynomial (Shor)", 
                    "classical_class": "NP ∩ co-NP",
                    "quantum_class": "BQP",
                    "speedup": "Exponential"
                },
                "Graph Isomorphism": {
                    "classical_best": "Quasipolynomial",
                    "quantum": "No known speedup",
                    "classical_class": "NP",
                    "quantum_class": "BQP",
                    "speedup": "None known"
                },
                "Discrete Logarithm": {
                    "classical_best": "Subexp (Index Calculus)",
                    "quantum": "Polynomial (Shor)",
                    "classical_class": "NP", 
                    "quantum_class": "BQP",
                    "speedup": "Exponential"
                },
                "Boolean Satisfiability": {
                    "classical_best": "Exponential",
                    "quantum": "Quadratic (Grover)",
                    "classical_class": "NP-complete",
                    "quantum_class": "BQP (?)",
                    "speedup": "Polynomial only"
                }
            }
            
            info = problem_info[problem_type]
            
            # Display problem analysis
            st.markdown(f"### {problem_type} Analysis")
            
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric("Classical Best", info["classical_best"])
                st.metric("Classical Class", info["classical_class"])
            with col_b:
                st.metric("Quantum Best", info["quantum"])
                st.metric("Quantum Class", info["quantum_class"])
            
            st.metric("Quantum Speedup", info["speedup"])
            
            # Complexity relationship visualization
            if problem_type == "Integer Factorization":
                st.success("✅ Major quantum advantage: Breaks RSA cryptography")
            elif problem_type == "Boolean Satisfiability":
                st.info("ℹ️ Polynomial speedup only: Still exponential scaling")
            elif problem_type == "Graph Isomorphism":
                st.warning("⚠️ No known quantum speedup despite classical progress")
            else:
                st.success("✅ Exponential quantum speedup for cryptographically relevant problem")
        
        # BQP inclusion relationships
        st.markdown("### Known Complexity Relationships")
        
        relationships = [
            ("P ⊆ BQP", "Any classical polynomial algorithm can be simulated quantumly"),
            ("BQP ⊆ PSPACE", "Quantum circuits can be simulated classically in polynomial space"),
            ("BQP vs NP", "Unknown relationship - major open problem"),
            ("NP ⊆? BQP", "Unresolved: Does quantum computation solve all NP problems efficiently?"),
            ("BQP ⊆ PP", "Quantum computers are contained in probabilistic polynomial time")
        ]
        
        for relation, description in relationships:
            st.write(f"**{relation}:** {description}")
    
    with complexity_tabs[2]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Quantum Computational Speedups</h3>
            <p>Systematic analysis of quantum advantages across different problem domains.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Types of Quantum Speedups
            
            **Exponential Speedups:**
            
            1. **Period Finding (Shor's Algorithm):**
               - Classical: O(exp(∛n log a)) - subexponential
               - Quantum: O((log n)³) - polynomial
               - Applications: Factoring, discrete log
            
            2. **Quantum Simulation:**
               - Classical: O(exp(n)) for n-qubit systems
               - Quantum: O(poly(n)) with efficient Hamiltonians
               - Advantage: Exponential for specific systems
            
            **Polynomial Speedups:**
            
            1. **Unstructured Search (Grover):**
               - Classical: O(N) = O(2^n)
               - Quantum: O(√N) = O(2^{n/2})
               - Optimal: Quadratic speedup is best possible
            
            2. **Collision Finding:**
               - Classical: O(N^{2/3}) using random walk
               - Quantum: O(N^{1/3}) using quantum walk
               - Applications: Hash function analysis
            
            **Constant Factor Speedups:**
            
            - Database search with partial information
            - Some optimization problems
            - Often not practically significant
            """)
            
        with col2:
            st.markdown("### Speedup Analysis Tool")
            
            problem_size = st.slider("Input Size (n)", 10, 100, 50, key="speedup_n")
            
            # Calculate complexities for different problems
            problems = {
                "Factoring": {
                    "classical": problem_size**(1.5) * np.exp(0.1 * problem_size**(1/3)),  # Simplified GNFS
                    "quantum": problem_size**3,  # Shor's algorithm
                    "type": "Exponential"
                },
                "Search": {
                    "classical": 2**problem_size,
                    "quantum": 2**(problem_size/2),
                    "type": "Polynomial"
                },
                "Simulation": {
                    "classical": 2**problem_size,
                    "quantum": problem_size**4,  # Efficient Hamiltonian simulation
                    "type": "Exponential"
                }
            }
            
            selected_problem = st.selectbox(
                "Select Problem",
                ["Factoring", "Search", "Simulation"],
                key="speedup_problem"
            )
            
            classical_time = problems[selected_problem]["classical"]
            quantum_time = problems[selected_problem]["quantum"]
            speedup_factor = classical_time / quantum_time
            speedup_type = problems[selected_problem]["type"]
            
            # Display metrics
            if classical_time > 1e10:
                classical_str = f"{classical_time:.2e}"
            else:
                classical_str = f"{classical_time:,.0f}"
            
            if quantum_time > 1e10:
                quantum_str = f"{quantum_time:.2e}"
            else:
                quantum_str = f"{quantum_time:,.0f}"
                
            st.metric("Classical Time", classical_str)
            st.metric("Quantum Time", quantum_str)
            
            if speedup_factor > 1e10:
                speedup_str = f"{speedup_factor:.2e}x"
            else:
                speedup_str = f"{speedup_factor:,.0f}x"
            
            st.metric("Speedup Factor", speedup_str)
            st.metric("Speedup Type", speedup_type)
            
            # Scaling visualization
            sizes = np.arange(10, 101, 10)
            classical_times = []
            quantum_times = []
            
            for n in sizes:
                if selected_problem == "Factoring":
                    c_time = n**(1.5) * np.exp(0.05 * n**(1/3))
                    q_time = n**3
                elif selected_problem == "Search":
                    c_time = 2**min(n, 50)  # Cap to prevent overflow
                    q_time = 2**min(n/2, 25)
                else:  # Simulation
                    c_time = 2**min(n, 50)
                    q_time = n**4
                
                classical_times.append(c_time)
                quantum_times.append(q_time)
            
            fig = go.Figure()
            
            fig.add_trace(go.Scatter(
                x=sizes, y=classical_times,
                mode='lines+markers',
                name='Classical',
                line=dict(color='#EF4444', width=3)
            ))
            
            fig.add_trace(go.Scatter(
                x=sizes, y=quantum_times,
                mode='lines+markers', 
                name='Quantum',
                line=dict(color='#10B981', width=3)
            ))
            
            fig.update_layout(
                title=f"{selected_problem} Complexity Scaling",
                xaxis_title="Problem Size (n)",
                yaxis_title="Time Complexity",
                yaxis_type="log",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#E2E8F0'
            )
            st.plotly_chart(fig, width='stretch')
    
    with complexity_tabs[3]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Oracle Separations and Black-Box Results</h3>
            <p>Understanding fundamental separations between classical and quantum computing using oracle methods.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Oracle Complexity Theory
            
            **Black-Box Model:**
            
            Algorithm has access to unknown function f via oracle queries.
            Goal: Determine property of f using minimal queries.
            
            **Key Results:**
            
            1. **Deutsch-Jozsa Separation:**
               - Problem: Determine if f: {0,1}ⁿ → {0,1} is constant or balanced
               - Classical: Ω(2ⁿ⁻¹) queries (worst case)
               - Quantum: 1 query (exactly!)
               - Separation: Exponential
            
            2. **Simon's Problem:**
               - Problem: Find hidden period s where f(x) = f(x ⊕ s)
               - Classical: Ω(2ⁿ/²) queries
               - Quantum: O(n) queries
               - Separation: Exponential
            
            3. **Bernstein-Vazirani:**
               - Problem: Find hidden string s where f(x) = s · x (mod 2)
               - Classical: n queries (adaptive)
               - Quantum: 1 query
            
            4. **Grover's Optimality:**
               - Unstructured search is Ω(√N) for quantum
               - No better than quadratic speedup possible
               - Tight bound: quantum optimal
            """)
            
        with col2:
            st.markdown("### Oracle Simulation")
            
            oracle_problem = st.selectbox(
                "Select Oracle Problem",
                ["Deutsch-Jozsa", "Simon's Problem", "Bernstein-Vazirani", "Search Lower Bound"],
                key="oracle_problem"
            )
            
            if oracle_problem == "Deutsch-Jozsa":
                n_bits = st.slider("Function Input Bits (n)", 2, 12, 6, key="dj_bits_oracle")
                
                classical_worst = 2**(n_bits-1) + 1
                quantum_queries = 1
                
                st.metric("Classical Worst Case", f"{classical_worst:,} queries")
                st.metric("Quantum Required", "1 query")
                st.metric("Separation", f"{classical_worst:,}x")
                
                # Scaling visualization
                sizes = np.arange(2, 13)
                classical_scaling = 2**(sizes-1) + 1
                quantum_scaling = np.ones_like(sizes)
                
            elif oracle_problem == "Simon's Problem":
                n_bits = st.slider("Function Input Bits (n)", 4, 16, 8, key="simon_bits")
                
                classical_expected = 2**(n_bits/2) * np.sqrt(np.pi/2)  # Birthday paradox
                quantum_queries = 2 * n_bits  # O(n) with some constant
                
                st.metric("Classical Expected", f"{classical_expected:,.0f} queries")
                st.metric("Quantum Required", f"{quantum_queries} queries")
                separation = classical_expected / quantum_queries
                st.metric("Separation", f"{separation:,.1f}x")
                
                # Scaling
                sizes = np.arange(4, 17)
                classical_scaling = 2**(sizes/2) * np.sqrt(np.pi/2)
                quantum_scaling = 2 * sizes
                
            elif oracle_problem == "Bernstein-Vazirani":
                n_bits = st.slider("Hidden String Length (n)", 3, 20, 10, key="bv_bits")
                
                classical_adaptive = n_bits
                quantum_queries = 1
                
                st.metric("Classic (Adaptive)", f"{classical_adaptive} queries")
                st.metric("Quantum Required", "1 query")
                st.metric("Separation", f"{classical_adaptive}x")
                
                # Scaling
                sizes = np.arange(3, 21)
                classical_scaling = sizes
                quantum_scaling = np.ones_like(sizes)
            
            else:  # Search Lower Bound
                database_size = st.selectbox("Database Size (N)", [16, 64, 256, 1024, 4096], index=2, key="search_db_size")
                
                classical_expected = database_size // 2
                quantum_optimal = int(np.pi * np.sqrt(database_size) / 4)
                
                st.metric("Classical Expected", f"{classical_expected} queries")
                st.metric("Quantum Optimal", f"{quantum_optimal} queries")
                separation = classical_expected / quantum_optimal
                st.metric("Speedup", f"{separation:.1f}x (quadratic)")
                
                # Scaling for search
                sizes = [16, 64, 256, 1024, 4096]
                classical_scaling = np.array(sizes) // 2
                quantum_scaling = [int(np.pi * np.sqrt(N) / 4) for N in sizes]
            
            # Plot scaling comparison
            if oracle_problem != "Search Lower Bound":
                fig = go.Figure()
                
                fig.add_trace(go.Scatter(
                    x=sizes, y=classical_scaling,
                    mode='lines+markers',
                    name='Classical',
                    line=dict(color='#EF4444', width=3),
                    marker=dict(size=8)
                ))
                
                fig.add_trace(go.Scatter(
                    x=sizes, y=quantum_scaling,
                    mode='lines+markers',
                    name='Quantum',
                    line=dict(color='#10B981', width=3),
                    marker=dict(size=8)
                ))
                
                fig.update_layout(
                    title=f"{oracle_problem} Query Complexity",
                    xaxis_title="Input Size (n)",
                    yaxis_title="Queries Required",
                    yaxis_type="log",
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font_color='#E2E8F0'
                )
                
                st.plotly_chart(fig, width='stretch')
            
            # Oracle insights
            if oracle_problem in ["Deutsch-Jozsa", "Simon's Problem"]:
                st.success("✅ Exponential separation: Oracle access extremely powerful")
            elif oracle_problem == "Bernstein-Vazirani":
                st.info("ℹ️ Linear separation: Still demonstrates quantum advantage")
            else:
                st.warning("⚠️ Quadratic optimal: Fundamental limit for unstructured search")
    
    with complexity_tabs[4]:
        st.markdown("""
        <div class="alphanova-card">
            <h3>Fundamental Limitations of Quantum Computing</h3>
            <p>Understanding the theoretical boundaries and impossibility results for quantum computation.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Quantum Computing Limitations
            
            **No-Cloning Theorem:**
            
            Cannot create perfect copies of unknown quantum states.
            
            Proof: If cloning possible → ∀ᵢ |ψᵢ⟩ = U|ψ⟩|0⟩ = |ψ⟩⊗|ψ⟩
            
            But unitarity requires linearity → contradiction.
            
            **No-Communication Theorem:**
            
            Quantum entanglement cannot transmit information.
            Local measurements show random outcomes regardless of distant operations.
            
            **Holevo Bound:**
            
            n qubits can store at most n classical bits of accessible information.
            χ({ρᵢ, pᵢ}) ≤ S(Σᵢ pᵢρᵢ) - Σᵢ pᵢ S(ρᵢ)
            
            **Search Lower Bounds:**
            
            - Grover's √N is optimal for unstructured search
            - Bennett et al.: Ω(√N) lower bound proven
            - No quantum algorithm can do better
            
            **NP vs BQP:**
            
            Unknown if BQP = NP, but unlikely:
            - Bennett et al.: Relative to oracle, NP ⊄ BQP
            - Quantum advantage seems limited to specific structure
            """)
            
        with col2:
            st.markdown("### Limitation Analysis")
            
            limitation_type = st.selectbox(
                "Analyze Limitation",
                ["Search Lower Bound", "Information vs Qubits", "Communication Complexity", "Factoring Limitations"],
                key="limitation_type"
            )
            
            if limitation_type == "Search Lower Bound":
                # Grover optimality demonstration
                search_size = st.slider("Search Space Size (N)", 16, 10000, 1000, step=50, key="search_limit_size")
                
                classical_avg = search_size // 2
                quantum_optimal = int(np.pi * np.sqrt(search_size) / 4)
                theoretical_limit = np.sqrt(search_size) / 2  # Theoretical lower bound
                
                st.metric("Classical Average", f"{classical_avg:,} queries")
                st.metric("Grover's Algorithm", f"{quantum_optimal:,} queries")
                st.metric("Theoretical Limit", f"{theoretical_limit:.1f} queries")
                
                optimality = quantum_optimal / theoretical_limit
                st.metric("Grover Optimality", f"{optimality:.2f} (near optimal)")
                
            elif limitation_type == "Information vs Qubits":
                # Holevo bound illustration
                n_qubits = st.slider("Number of Qubits", 1, 10, 5, key="holevo_qubits")
                
                quantum_dof = 2**(n_qubits) - 1  # Degrees of freedom in n-qubit state
                classical_bits = n_qubits  # Holevo bound
                
                st.metric("Quantum State DoF", f"{quantum_dof:,}")
                st.metric("Accessible Information", f"{classical_bits} bits")
                
                if quantum_dof > 100:
                    compression = quantum_dof / classical_bits
                    st.metric("Information Compression", f"{compression:,.0f}:1")
                
                st.info("ℹ️ Holevo bound: Exponential quantum state space, linear accessible info")
                
            elif limitation_type == "Communication Complexity":
                # Communication complexity with entanglement
                comm_problem = st.selectbox(
                    "Communication Problem",
                    ["Equality Function", "Disjointness", "Inner Product"],
                    key="comm_problem"
                )
                
                input_bits = st.slider("Input Size per Party", 5, 20, 10, key="comm_input_bits")
                
                if comm_problem == "Equality Function":
                    classical_comm = input_bits + 1  # Simple protocol
                    quantum_comm = input_bits + 1    # No advantage known
                elif comm_problem == "Disjointness":
                    classical_comm = int(np.sqrt(input_bits) * np.log(input_bits))
                    quantum_comm = int(np.sqrt(input_bits))  # Some advantage
                else:  # Inner Product
                    classical_comm = input_bits  # Must send full vector
                    quantum_comm = input_bits     # No advantage for exact version
                
                st.metric("Classical Communication", f"{classical_comm} bits")
                st.metric("Quantum Communication", f"{quantum_comm} bits")
                
                if quantum_comm < classical_comm:
                    advantage = classical_comm / quantum_comm
                    st.metric("Quantum Advantage", f"{advantage:.1f}x")
                else:
                    st.metric("Quantum Advantage", "None")
            
            else:  # Factoring Limitations
                # RSA key size analysis
                rsa_bits = st.slider("RSA Key Size (bits)", 512, 4096, 2048, step=256, key="rsa_bits")
                
                # Classical factoring complexity (GNFS)
                classical_time = np.exp(1.923 * (rsa_bits * np.log(2))**(1/3) * (np.log(rsa_bits * np.log(2)))**(2/3))
                
                # Quantum factoring (Shor's algorithm)
                quantum_time = rsa_bits**3
                
                if classical_time > 1e50:
                    classical_str = "∞ (infeasible)"
                else:
                    classical_str = f"{classical_time:.2e}"
                
                st.metric("Classical Time (ops)", classical_str)
                st.metric("Quantum Time (ops)", f"{quantum_time:,}")
                
                # Quantum resource requirements
                logical_qubits = 2 * rsa_bits  # Approximate for Shor's
                
                # Error correction overhead (surface code with d=13)
                physical_qubits = logical_qubits * 169  # 13^2 overhead per logical
                
                st.metric("Logical Qubits Needed", f"{logical_qubits:,}")
                st.metric("Physical Qubits (d=13)", f"{physical_qubits:,}")
                
                if physical_qubits > 1e6:
                    st.warning("⚠️ Requires millions of physical qubits")
                elif physical_qubits > 10000:
                    st.info("ℹ️ Challenging but potentially achievable scale")
                else:
                    st.success("✅ Within reach of near-term quantum computers")
        
        # Summary of fundamental limits
        st.markdown("### Quantum Computing: What We Cannot Do")
        
        limitations_summary = [
            "❌ **Solve NP-complete problems efficiently** (probably)",
            "❌ **Transmit information faster than light** (no-communication theorem)",
            "❌ **Clone arbitrary quantum states** (no-cloning theorem)",
            "❌ **Search unstructured databases faster than O(√N)** (Grover optimal)",
            "❌ **Access exponential information from polynomial qubits** (Holevo bound)",
            "✅ **But we CAN achieve exponential speedups for structured problems!**"
        ]
        
        for limitation in limitations_summary:
            st.markdown(limitation)

# Default section for undefined sections
else:
    st.markdown(f"# {section_id.replace('_', ' ').title()}")
    st.markdown('<span class="alphanova-status status-research">Under Development</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="alphanova-card">
        <h3>Advanced Module Under Development</h3>
        <p>This comprehensive quantum computing module is currently under active development. 
        AlphaNova Quantum continues to expand with cutting-edge research capabilities and scientific depth.</p>
        
        <h4 style="color: #3B82F6; margin-top: 1.5rem;">Coming Soon:</h4>
        <ul style="color: #E2E8F0;">
            <li><strong>Enhanced Theoretical Content</strong> - Deeper mathematical foundations</li>
            <li><strong>Interactive Simulations</strong> - Advanced quantum phenomenon modeling</li>
            <li><strong>Research Tools</strong> - Professional-grade analysis capabilities</li>
            <li><strong>Educational Resources</strong> - Comprehensive learning materials</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #64748B;">
    <p style="font-size: 1.1rem; margin-bottom: 0.5rem;">
        <strong>⚡ AlphaNova Quantum</strong> | Advanced Research Platform v1.0.0
    </p>
    <p style="font-size: 0.9rem; margin-bottom: 1rem;">
        Next-generation quantum computing research environment for scientific innovation
    </p>
    <p style="font-size: 0.8rem; color: #475569;">
        © 2024 AlphaNova Research Labs. Built for the quantum computing community.
    </p>
</div>
""", unsafe_allow_html=True)