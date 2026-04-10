import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import json
import os
from datetime import datetime

# Page configuration - AlphaNova Quantum Branding
st.set_page_config(
    page_title="AlphaNova Quantum | Next-Generation Quantum Research Platform",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/alphanovalabs/quantum-platform',
        'Report a bug': 'https://github.com/alphanovalabs/quantum-platform/issues',
        'About': """
        # AlphaNova Quantum
        Interactive Quantum Computing and AI Visualization Platform
        Next-generation research environment for quantum innovation.
        """
    }
)

# Initialize session state for the platform
if 'language' not in st.session_state:
    st.session_state.language = 'en'
if 'selected_module_id' not in st.session_state:
    st.session_state.selected_module_id = 'home'

# Load translations from JSON files
def load_translations():
    """Load translations from JSON files"""
    translations = {}
    translations_dir = os.path.join(os.path.dirname(__file__), 'translations')
    
    for lang in ['en', 'ru']:
        try:
            with open(os.path.join(translations_dir, f'{lang}.json'), 'r', encoding='utf-8') as f:
                translations[lang] = json.load(f)
        except Exception as e:
            translations[lang] = {}
    
    return translations

# Load translations
TRANSLATIONS = load_translations()

# Translation helper function with dot-notation support
def t(key, fallback=None):
    """Get translation for current language with fallback"""
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
                break
        if value:
            return value
    
    # Try direct key lookup
    if key in lang_dict:
        return lang_dict[key]
    
    return fallback if fallback else key

# Premium Dark Futuristic CSS with Glassmorphism
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@300;400;500;600&display=swap');

/* ==================== GLOBAL DARK FOUNDATION ==================== */
* {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    letter-spacing: -0.01em;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

.stApp {
    background: linear-gradient(135deg, #0a0e1a 0%, #111827 40%, #1e293b 100%) !important;
    color: #f8fafc !important;
    min-height: 100vh;
}

/* Remove Streamlit default elements for immersive experience */
#MainMenu { visibility: hidden !important; }
footer { visibility: hidden !important; }
header { visibility: hidden !important; }
.stDeployButton { display: none !important; }

/* ==================== MAIN CONTAINER ==================== */
.main .block-container {
    padding: 1.5rem 2rem 3rem !important;
    max-width: 1600px !important;
    margin: 0 auto !important;
    background: transparent !important;
}

/* ==================== SIDEBAR - PREMIUM GLASSMORPHISM ==================== */
[data-testid="stSidebar"] {
    background: rgba(15, 23, 42, 0.4) !important;
    backdrop-filter: blur(20px) !important;
    border-right: 1px solid rgba(148, 163, 184, 0.1) !important;
    box-shadow: 4px 0 24px rgba(0, 0, 0, 0.2) !important;
}

[data-testid="stSidebar"] > div:first-child {
    background: transparent !important;
    padding: 1.5rem 1rem !important;
}

/* ==================== SIDEBAR BRAND HEADER ==================== */
.sidebar-brand {
    text-align: center;
    padding: 2rem 1.5rem;
    margin-bottom: 2rem;
    background: rgba(30, 41, 59, 0.3);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    border: 1px solid rgba(148, 163, 184, 0.1);
    box-shadow: 
        0 8px 32px rgba(0, 0, 0, 0.2),
        inset 0 1px 0 rgba(255, 255, 255, 0.1);
}

.brand-icon {
    font-size: 2rem;
    margin-bottom: 0.75rem;
    background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 50%, #f472b6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.sidebar-brand-title {
    font-size: 1.125rem;
    font-weight: 800;
    color: #f8fafc;
    margin-bottom: 0.5rem;
    letter-spacing: -0.025em;
    background: linear-gradient(135deg, #f8fafc 0%, #cbd5e1 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.sidebar-brand-subtitle {
    font-size: 0.75rem;
    color: #94a3b8;
    font-weight: 500;
    letter-spacing: 0.025em;
    text-transform: uppercase;
    opacity: 0.8;
}

/* ==================== NAVIGATION SECTIONS ==================== */
.nav-section-label {
    font-weight: 600;
    font-size: 0.75rem;
    color: #64748b;
    margin: 2rem 0 1rem 0;
    padding: 0.5rem 1rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    border-bottom: 1px solid rgba(148, 163, 184, 0.1);
}

/* ==================== NAVIGATION BUTTONS GLASSMORPHISM ==================== */
.stButton > button {
    background: rgba(30, 41, 59, 0.3) !important;
    backdrop-filter: blur(15px) !important;
    border: 1px solid rgba(148, 163, 184, 0.1) !important;
    border-radius: 16px !important;
    padding: 0.875rem 1.25rem !important;
    color: #e2e8f0 !important;
    font-weight: 500 !important;
    font-size: 0.875rem !important;
    width: 100% !important;
    margin: 0.25rem 0 !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    box-shadow: 
        0 4px 16px rgba(0, 0, 0, 0.1),
        inset 0 1px 0 rgba(255, 255, 255, 0.05) !important;
}

.stButton > button:hover {
    background: rgba(59, 130, 246, 0.2) !important;
    border-color: rgba(59, 130, 246, 0.3) !important;
    transform: translateY(-2px) !important;
    color: #93c5fd !important;
    box-shadow: 
        0 8px 25px rgba(0, 0, 0, 0.15),
        0 0 20px rgba(59, 130, 246, 0.1),
        inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
}

.stButton > button:focus {
    background: rgba(59, 130, 246, 0.3) !important;
    border-color: rgba(59, 130, 246, 0.5) !important;
    color: #dbeafe !important;
    box-shadow: 
        0 0 0 3px rgba(59, 130, 246, 0.2),
        0 8px 25px rgba(0, 0, 0, 0.15),
        inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
}

/* ==================== SIDEBAR FOOTER ==================== */
.sidebar-footer {
    text-align: center;
    padding: 1.5rem 1rem;
    margin-top: 2rem;
    background: rgba(30, 41, 59, 0.2);
    backdrop-filter: blur(10px);
    border-radius: 16px;
    border: 1px solid rgba(148, 163, 184, 0.05);
}

.sidebar-footer-text {
    font-size: 0.75rem;
    color: #64748b;
    font-weight: 500;
}

.sidebar-footer-version {
    color: #475569;
    font-size: 0.7rem;
    font-weight: 400;
}

/* ==================== HERO SECTION - PREMIUM DESIGN ==================== */
.hero-container {
    text-align: center;
    padding: 4rem 2rem 3rem;
    margin-bottom: 3rem;
    background: rgba(30, 41, 59, 0.3);
    backdrop-filter: blur(20px);
    border-radius: 32px;
    border: 1px solid rgba(148, 163, 184, 0.1);
    box-shadow: 
        0 25px 50px rgba(0, 0, 0, 0.15),
        0 0 40px rgba(59, 130, 246, 0.05),
        inset 0 1px 0 rgba(255, 255, 255, 0.1);
    position: relative;
    overflow: hidden;
}

.hero-container::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.03) 0%, rgba(168, 85, 247, 0.03) 50%, rgba(236, 72, 153, 0.03) 100%);
    border-radius: 32px;
    z-index: 1;
}

.hero-content {
    position: relative;
    z-index: 2;
}

.hero-icon {
    font-size: 3.5rem;
    margin-bottom: 1.5rem;
    background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 50%, #f472b6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    filter: drop-shadow(0 4px 8px rgba(59, 130, 246, 0.2));
}

.hero-title {
    font-size: 3rem;
    font-weight: 800;
    color: #f8fafc;
    margin-bottom: 1rem;
    letter-spacing: -0.03em;
    background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 40%, #94a3b8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

.hero-subtitle {
    font-size: 1.25rem;
    color: #60a5fa;
    font-weight: 600;
    margin-bottom: 1rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
}

.hero-description {
    font-size: 1.1rem;
    color: #cbd5e1;
    line-height: 1.7;
    max-width: 800px;
    margin: 0 auto 2rem;
    font-weight: 400;
}

/* ==================== FEATURE HIGHLIGHTS ==================== */
.features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
}

.feature-card {
    background: rgba(30, 41, 59, 0.4);
    backdrop-filter: blur(15px);
    border: 1px solid rgba(148, 163, 184, 0.1);
    border-radius: 20px;
    padding: 1.5rem;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 
        0 8px 25px rgba(0, 0, 0, 0.1),
        inset 0 1px 0 rgba(255, 255, 255, 0.05);
}

.feature-card:hover {
    transform: translateY(-4px);
    border-color: rgba(59, 130, 246, 0.3);
    box-shadow: 
        0 20px 40px rgba(0, 0, 0, 0.15),
        0 0 30px rgba(59, 130, 246, 0.1),
        inset 0 1px 0 rgba(255, 255, 255, 0.1);
}

.feature-icon {
    font-size: 1.5rem;
    margin-bottom: 0.75rem;
    color: #60a5fa;
}

.feature-title {
    font-size: 0.875rem;
    font-weight: 600;
    color: #f1f5f9;
    margin-bottom: 0.5rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

/* ==================== PREMIUM CARDS ==================== */
.premium-card {
    background: rgba(30, 41, 59, 0.4);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(148, 163, 184, 0.1);
    border-radius: 24px;
    padding: 2.5rem;
    margin: 2rem 0;
    box-shadow: 
        0 25px 50px rgba(0, 0, 0, 0.15),
        0 0 40px rgba(59, 130, 246, 0.03),
        inset 0 1px 0 rgba(255, 255, 255, 0.1);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}

.premium-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.02) 0%, rgba(168, 85, 247, 0.02) 100%);
    border-radius: 24px;
    opacity: 0;
    transition: opacity 0.4s ease;
}

.premium-card:hover::before {
    opacity: 1;
}

.premium-card:hover {
    transform: translateY(-6px);
    border-color: rgba(59, 130, 246, 0.2);
    box-shadow: 
        0 32px 64px rgba(0, 0, 0, 0.2),
        0 0 50px rgba(59, 130, 246, 0.1),
        inset 0 1px 0 rgba(255, 255, 255, 0.15);
}

.card-content {
    position: relative;
    z-index: 2;
}

.premium-card h3 {
    color: #60a5fa !important;
    font-size: 1.5rem !important;
    font-weight: 700 !important;
    margin-bottom: 1rem !important;
    letter-spacing: -0.025em !important;
}

.premium-card h4 {
    color: #e2e8f0 !important;
    font-size: 1.25rem !important;
    margin-bottom: 0.75rem !important;
    font-weight: 600 !important;
}

.premium-card p {
    color: #cbd5e1 !important;
    line-height: 1.8 !important;
    font-size: 1rem !important;
    font-weight: 400 !important;
    margin-bottom: 0.75rem !important;
}

/* ==================== STATUS INDICATORS ==================== */
.status-badge {
    display: inline-block;
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin: 0.5rem 0;
    backdrop-filter: blur(10px);
}

.status-active {
    background: rgba(16, 185, 129, 0.2);
    color: #6ee7b7;
    border: 1px solid rgba(16, 185, 129, 0.3);
    box-shadow: 0 0 20px rgba(16, 185, 129, 0.1);
}

.status-emerging {
    background: rgba(245, 158, 11, 0.2);
    color: #fbbf24;
    border: 1px solid rgba(245, 158, 11, 0.3);
    box-shadow: 0 0 20px rgba(245, 158, 11, 0.1);
}

.status-frontier {
    background: rgba(139, 92, 246, 0.2);
    color: #c4b5fd;
    border: 1px solid rgba(139, 92, 246, 0.3);
    box-shadow: 0 0 20px rgba(139, 92, 246, 0.1);
}

/* ==================== QUANTUM TYPOGRAPHY ==================== */
h1, h2, h3, h4, h5, h6 {
    color: #f8fafc !important;
    font-family: 'Inter', sans-serif !important;
    letter-spacing: -0.025em !important;
    font-weight: 700 !important;
}

.quantum-title {
    font-size: 2.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 50%, #f472b6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1rem;
    text-align: center;
}

/* ==================== ENHANCED 3D VISUALIZATIONS ==================== */
.plotly-container {
    background: rgba(30, 41, 59, 0.3) !important;
    backdrop-filter: blur(15px) !important;
    border-radius: 20px !important;
    border: 1px solid rgba(148, 163, 184, 0.1) !important;
    box-shadow: 
        0 20px 40px rgba(0, 0, 0, 0.15),
        inset 0 1px 0 rgba(255, 255, 255, 0.05) !important;
    overflow: hidden !important;
}

/* ==================== INTERACTIVE CONTROLS ==================== */
.stSlider > div > div > div {
    background: rgba(30, 41, 59, 0.4) !important;
    backdrop-filter: blur(15px) !important;
    border-radius: 16px !important;
    border: 1px solid rgba(148, 163, 184, 0.1) !important;
}

.stSelectbox > div > div {
    background: rgba(30, 41, 59, 0.4) !important;
    backdrop-filter: blur(15px) !important;
    border: 1px solid rgba(148, 163, 184, 0.1) !important;
    border-radius: 16px !important;
    color: #e2e8f0 !important;
}

/* ==================== RESPONSIVE DESIGN ==================== */
@media (max-width: 768px) {
    .hero-title {
        font-size: 2rem;
    }
    
    .hero-subtitle {
        font-size: 1rem;
    }
    
    .features-grid {
        grid-template-columns: 1fr;
    }
    
    .main .block-container {
        padding: 1rem !important;
    }
    
    .premium-card {
        padding: 1.5rem;
    }
}

/* ==================== SMOOTH SCROLLBAR ==================== */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: rgba(30, 41, 59, 0.3);
    border-radius: 4px;
}

::-webkit-scrollbar-thumb {
    background: rgba(148, 163, 184, 0.3);
    border-radius: 4px;
    transition: background 0.3s ease;
}

::-webkit-scrollbar-thumb:hover {
    background: rgba(148, 163, 184, 0.5);
}

/* ==================== ANIMATIONS ==================== */
@keyframes quantum-pulse {
    0%, 100% {
        box-shadow: 0 0 20px rgba(59, 130, 246, 0.1);
    }
    50% {
        box-shadow: 0 0 40px rgba(59, 130, 246, 0.2);
    }
}

.quantum-glow {
    animation: quantum-pulse 3s ease-in-out infinite;
}

@keyframes float-gentle {
    0%, 100% {
        transform: translateY(0px);
    }
    50% {
        transform: translateY(-10px);
    }
}

.floating {
    animation: float-gentle 6s ease-in-out infinite;
}

/* ==================== LANGUAGE SELECTOR ==================== */
.language-selector {
    display: flex;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
    padding: 0 1rem;
}

.lang-button {
    flex: 1;
    background: rgba(30, 41, 59, 0.3) !important;
    backdrop-filter: blur(15px) !important;
    border: 1px solid rgba(148, 163, 184, 0.1) !important;
    border-radius: 12px !important;
    padding: 0.5rem !important;
    color: #e2e8f0 !important;
    font-size: 0.75rem !important;
    font-weight: 500 !important;
    text-align: center !important;
    transition: all 0.3s ease !important;
}

.lang-button:hover {
    background: rgba(59, 130, 246, 0.2) !important;
    border-color: rgba(59, 130, 246, 0.3) !important;
    color: #dbeafe !important;
    transform: translateY(-1px) !important;
}
</style>
""", unsafe_allow_html=True)

# Language selector in sidebar
st.sidebar.markdown('<div class="language-selector">', unsafe_allow_html=True)
col_lang1, col_lang2 = st.sidebar.columns(2)
with col_lang1:
    if st.button(t("global.language_en", "English"), key="lang_en", help="Switch to English"):
        st.session_state.language = 'en'
        st.rerun()

with col_lang2:
    if st.button(t("global.language_ru", "Русский"), key="lang_ru", help="Переключить на русский"):
        st.session_state.language = 'ru'
        st.rerun()
st.sidebar.markdown('</div>', unsafe_allow_html=True)

st.sidebar.markdown("---")

# AlphaNova Quantum brand header
brand_header = f"""
<div class='sidebar-brand quantum-glow'>
    <div class='brand-icon'>⚡</div>
    <div class='sidebar-brand-title'>AlphaNova Quantum</div>
    <div class='sidebar-brand-subtitle'>Quantum Computing + AI Research Platform</div>
</div>
"""
st.sidebar.markdown(brand_header, unsafe_allow_html=True)

# Enhanced navigation structure with professional organization
nav_groups = [
    ("Home", [
        ("home", "🏠", "Platform Overview", "Interactive quantum research dashboard"),
    ]),
    ("Quantum Foundations", [
        ("bloch", "⚛️", "Bloch Sphere", "Single qubit state visualization"),
        ("interference", "〰️", "Quantum Interference", "Wave-particle duality exploration"),
        ("gates_circuits", "🔗", "Gates & Circuits", "Quantum gate operations and design"),
    ]),
    ("Quantum Correlations", [
        ("entanglement", "🔗", "Quantum Entanglement", "Bell states and non-local correlations"),
        ("algorithms", "⚡", "Quantum Algorithms", "Advanced quantum computation methods"),
    ]),
    ("Machine Learning", [
        ("qml", "🧠", "Quantum Machine Learning", "Quantum neural networks and classifiers"),
        ("vqe", "🔬", "Variational Algorithms", "VQE and QAOA optimization"),
    ]),
    ("Hardware & Systems", [
        ("hardware", "⚙️", "Quantum Hardware", "Physical quantum computing systems"),
        ("qec", "🛡️", "Error Correction", "Quantum error correction protocols"),
    ]),
    ("Advanced Theory", [
        ("complexity", "🧮", "Complexity Theory", "Computational complexity analysis"),
    ]),
]

# Render enhanced navigation with premium styling
for section_name, modules in nav_groups:
    st.sidebar.markdown(f"<div class='nav-section-label'>{section_name}</div>", unsafe_allow_html=True)
    
    for module_id, icon, title, subtitle in modules:
        button_type = "primary" if st.session_state.selected_module_id == module_id else "secondary"
        
        if st.sidebar.button(
            f"{icon} {title}",
            key=f"nav_{module_id}",
            type=button_type,
            use_container_width=True,
            help=subtitle
        ):
            st.session_state.selected_module_id = module_id
            st.rerun()

st.sidebar.markdown("---")

# Enhanced sidebar footer
sidebar_footer = f"""
<div class='sidebar-footer'>
    <div class='sidebar-footer-text'>
        AlphaNova Quantum Platform<br>
        <span class='sidebar-footer-version'>Research Edition v5.0</span>
    </div>
</div>
"""
st.sidebar.markdown(sidebar_footer, unsafe_allow_html=True)

# Enhanced Bloch Sphere Visualization with Premium Effects
def create_enhanced_bloch_sphere(theta, phi, show_trajectory=False):
    """Create a premium 3D Bloch sphere with advanced visual effects"""
    
    # High-resolution sphere coordinates
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x_sphere = np.outer(np.cos(u), np.sin(v))
    y_sphere = np.outer(np.sin(u), np.sin(v))
    z_sphere = np.outer(np.ones(np.size(u)), np.cos(v))
    
    # State vector calculations
    theta_rad = np.radians(theta)
    phi_rad = np.radians(phi)
    x_state = np.sin(theta_rad) * np.cos(phi_rad)
    y_state = np.sin(theta_rad) * np.sin(phi_rad)
    z_state = np.cos(theta_rad)
    
    fig = go.Figure()
    
    # Enhanced sphere surface with gradient and transparency
    fig.add_trace(go.Surface(
        x=x_sphere, y=y_sphere, z=z_sphere,
        opacity=0.15,
        colorscale=[
            [0, 'rgba(59, 130, 246, 0.1)'],
            [0.5, 'rgba(168, 85, 247, 0.15)'],
            [1, 'rgba(236, 72, 153, 0.1)']
        ],
        showscale=False,
        hoverinfo='skip',
        lighting=dict(
            ambient=0.3,
            diffuse=0.8,
            specular=1.0,
            roughness=0.1,
            fresnel=0.2
        ),
        name="Bloch Sphere"
    ))
    
    # Coordinate system - enhanced axes with glow effect
    axis_length = 1.3
    axes_data = [
        ([0, axis_length], [0, 0], [0, 0], '#ef4444', 'X-axis', 4),
        ([0, 0], [0, axis_length], [0, 0], '#10b981', 'Y-axis', 4),
        ([0, 0], [0, 0], [0, axis_length], '#8b5cf6', 'Z-axis', 4)
    ]
    
    for x, y, z, color, name, width in axes_data:
        # Main axis
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z,
            mode='lines',
            line=dict(color=color, width=width),
            showlegend=False,
            hoverinfo='skip'
        ))
        
        # Glowing effect
        for i, alpha in enumerate([0.3, 0.2, 0.1]):
            fig.add_trace(go.Scatter3d(
                x=x, y=y, z=z,
                mode='lines',
                line=dict(color=color, width=width + i*2),
                opacity=alpha,
                showlegend=False,
                hoverinfo='skip'
            ))
    
    # Enhanced state vector with multiple visual layers
    state_colors = ['#60a5fa', '#3b82f6', '#1d4ed8']
    state_widths = [8, 6, 4]
    state_opacities = [1.0, 0.6, 0.3]
    
    for color, width, opacity in zip(state_colors, state_widths, state_opacities):
        fig.add_trace(go.Scatter3d(
            x=[0, x_state], y=[0, y_state], z=[0, z_state],
            mode='lines+markers',
            line=dict(color=color, width=width),
            marker=dict(
                size=[0, 15],
                color=['rgba(0,0,0,0)', '#f59e0b'],
                symbol=['circle', 'circle'],
                line=dict(width=2, color='#fbbf24')
            ),
            opacity=opacity,
            showlegend=False,
            hovertemplate=f"<b>Quantum State</b><br>" +
                         f"θ: {theta:.1f}°<br>" +
                         f"φ: {phi:.1f}°<br>" +
                         f"<extra></extra>"
        ))
    
    # Trajectory path if enabled
    if show_trajectory:
        traj_points = 50
        traj_theta = np.linspace(0, theta_rad, traj_points)
        traj_x = np.sin(traj_theta) * np.cos(phi_rad)
        traj_y = np.sin(traj_theta) * np.sin(phi_rad)
        traj_z = np.cos(traj_theta)
        
        fig.add_trace(go.Scatter3d(
            x=traj_x, y=traj_y, z=traj_z,
            mode='lines',
            line=dict(color='#fbbf24', width=3, dash='dash'),
            opacity=0.7,
            showlegend=False,
            hoverinfo='skip'
        ))
    
    # Axis labels with enhanced positioning
    labels = [
        (axis_length + 0.1, 0, 0, '|+⟩'),
        (-axis_length - 0.1, 0, 0, '|-⟩'),
        (0, axis_length + 0.1, 0, '|+i⟩'),
        (0, -axis_length - 0.1, 0, '|-i⟩'),
        (0, 0, axis_length + 0.1, '|0⟩'),
        (0, 0, -axis_length - 0.1, '|1⟩')
    ]
    
    for x, y, z, text in labels:
        fig.add_trace(go.Scatter3d(
            x=[x], y=[y], z=[z],
            mode='text',
            text=[text],
            textfont=dict(size=14, color='#e2e8f0', family='Inter'),
            showlegend=False,
            hoverinfo='skip'
        ))
    
    # Enhanced layout with cinematic camera and lighting
    fig.update_layout(
        scene=dict(
            camera=dict(
                eye=dict(x=1.8, y=1.8, z=1.5),
                center=dict(x=0, y=0, z=0),
                up=dict(x=0, y=0, z=1)
            ),
            xaxis=dict(
                range=[-1.5, 1.5],
                showgrid=False,
                showticklabels=False,
                showline=False,
                zeroline=False,
                backgroundcolor='rgba(0,0,0,0)'
            ),
            yaxis=dict(
                range=[-1.5, 1.5],
                showgrid=False,
                showticklabels=False,
                showline=False,
                zeroline=False,
                backgroundcolor='rgba(0,0,0,0)'
            ),
            zaxis=dict(
                range=[-1.5, 1.5],
                showgrid=False,
                showticklabels=False,
                showline=False,
                zeroline=False,
                backgroundcolor='rgba(0,0,0,0)'
            ),
            bgcolor='rgba(0,0,0,0)',
            aspectmode='cube'
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        height=600,
        margin=dict(l=0, r=0, t=0, b=0),
        font=dict(color='#e2e8f0')
    )
    
    return fig

# Enhanced Quantum Circuit Visualization
def create_enhanced_quantum_circuit(gates_config=None):
    """Create premium quantum circuit visualization with advanced gate styling"""
    
    if gates_config is None:
        gates_config = [
            {'pos': 1, 'qubit': 0, 'type': 'H', 'color': '#60a5fa'},
            {'pos': 2, 'qubit': 1, 'type': 'X', 'color': '#ef4444'},
            {'pos': 3, 'qubit': 2, 'type': 'Y', 'color': '#10b981'},
            {'pos': 4, 'qubit': 0, 'type': 'RZ', 'color': '#8b5cf6'},
            {'pos': 5, 'qubit': [0, 1], 'type': 'CNOT', 'color': '#f59e0b'},
            {'pos': 6, 'qubit': 2, 'type': 'T', 'color': '#ec4899'},
        ]
    
    num_qubits = 3
    circuit_length = 8
    
    fig = go.Figure()
    
    # Enhanced qubit lines with glow effect
    for i in range(num_qubits):
        y_pos = num_qubits - 1 - i
        
        # Main line
        fig.add_trace(go.Scatter(
            x=[0, circuit_length - 1],
            y=[y_pos, y_pos],
            mode='lines',
            line=dict(color='#64748b', width=3),
            showlegend=False,
            hoverinfo='skip'
        ))
        
        # Glow effect
        for width, opacity in [(5, 0.3), (7, 0.1)]:
            fig.add_trace(go.Scatter(
                x=[0, circuit_length - 1],
                y=[y_pos, y_pos],
                mode='lines',
                line=dict(color='#60a5fa', width=width),
                opacity=opacity,
                showlegend=False,
                hoverinfo='skip'
            ))
        
        # Qubit label
        fig.add_trace(go.Scatter(
            x=[-0.3],
            y=[y_pos],
            mode='text',
            text=[f'q[{i}]'],
            textfont=dict(size=12, color='#e2e8f0', family='JetBrains Mono'),
            showlegend=False,
            hoverinfo='skip'
        ))
    
    # Enhanced quantum gates
    for gate in gates_config:
        pos_x = gate['pos']
        gate_type = gate['type']
        color = gate['color']
        
        if gate_type == 'CNOT':
            # Enhanced CNOT gate
            control_qubit = num_qubits - 1 - gate['qubit'][0]
            target_qubit = num_qubits - 1 - gate['qubit'][1]
            
            # Control line with glow
            fig.add_trace(go.Scatter(
                x=[pos_x, pos_x],
                y=[control_qubit, target_qubit],
                mode='lines',
                line=dict(color=color, width=4),
                showlegend=False,
                hoverinfo='skip'
            ))
            
            # Control dot
            fig.add_trace(go.Scatter(
                x=[pos_x],
                y=[control_qubit],
                mode='markers',
                marker=dict(size=12, color=color, line=dict(width=2, color='#1e293b')),
                showlegend=False,
                hovertemplate=f"<b>Control Qubit</b><br>Position: {pos_x}<extra></extra>"
            ))
            
            # Target gate
            fig.add_trace(go.Scatter(
                x=[pos_x],
                y=[target_qubit],
                mode='markers+text',
                marker=dict(size=25, color='rgba(0,0,0,0)', line=dict(width=3, color=color)),
                text=['⊕'],
                textfont=dict(size=16, color=color),
                showlegend=False,
                hovertemplate=f"<b>Target Qubit</b><br>Position: {pos_x}<extra></extra>"
            ))
            
        else:
            # Single qubit gates with enhanced styling
            qubit_y = num_qubits - 1 - gate['qubit']
            
            # Gate background with glow
            for size, opacity in [(35, 1.0), (40, 0.5), (45, 0.2)]:
                fig.add_trace(go.Scatter(
                    x=[pos_x],
                    y=[qubit_y],
                    mode='markers',
                    marker=dict(
                        size=size,
                        color=color,
                        opacity=opacity,
                        symbol='square',
                        line=dict(width=2, color='#1e293b')
                    ),
                    showlegend=False,
                    hoverinfo='skip' if opacity != 1.0 else None,
                    hovertemplate=f"<b>{gate_type} Gate</b><br>Qubit: {gate['qubit']}<br>Position: {pos_x}<extra></extra>" if opacity == 1.0 else None
                ))
            
            # Gate label
            fig.add_trace(go.Scatter(
                x=[pos_x],
                y=[qubit_y],
                mode='text',
                text=[gate_type],
                textfont=dict(size=12, color='#ffffff', family='Inter', weight='bold'),
                showlegend=False,
                hoverinfo='skip'
            ))
    
    # Enhanced layout
    fig.update_layout(
        xaxis=dict(
            range=[-0.8, circuit_length - 0.2],
            showgrid=False,
            showticklabels=False,
            zeroline=False,
            title='Time →',
            titlefont=dict(color='#94a3b8', size=12)
        ),
        yaxis=dict(
            range=[-0.5, num_qubits - 0.5],
            showgrid=False,
            showticklabels=False,
            zeroline=False
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=300,
        showlegend=False,
        margin=dict(l=60, r=20, t=20, b=40),
        font=dict(color='#e2e8f0')
    )
    
    return fig

# Main content area with enhanced routing
if st.session_state.selected_module_id == 'home':
    # Premium Hero Section
    st.markdown("""
    <div class='hero-container floating'>
        <div class='hero-content'>
            <div class='hero-icon'>⚡</div>
            <h1 class='hero-title'>AlphaNova Quantum</h1>
            <div class='hero-subtitle'>Next-Generation Quantum Research Environment</div>
            <p class='hero-description'>
                Advanced quantum computing research platform combining state-of-the-art 
                algorithms, immersive visualizations, and machine learning integration. 
                Explore quantum phenomena through interactive tools designed for the future of computing.
            </p>
            
            <div class='features-grid'>
                <div class='feature-card'>
                    <div class='feature-icon'>🎯</div>
                    <div class='feature-title'>Interactive Quantum Visualizations</div>
                </div>
                <div class='feature-card'>
                    <div class='feature-icon'>⚛️</div>
                    <div class='feature-title'>Quantum Gates and Circuits</div>
                </div>
                <div class='feature-card'>
                    <div class='feature-icon'>🧠</div>
                    <div class='feature-title'>Quantum Machine Learning</div>
                </div>
                <div class='feature-card'>
                    <div class='feature-icon'>🔬</div>
                    <div class='feature-title'>Real-Time State Exploration</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Platform Capabilities
    st.markdown("""
    <div class='premium-card quantum-glow'>
        <div class='card-content'>
            <h3>Platform Capabilities</h3>
            <p>
                AlphaNova Quantum provides comprehensive tools for quantum state manipulation, 
                algorithm development, and machine learning research. Experience quantum 
                phenomena through advanced computational methods and interactive visualizations.
            </p>
            <p>
                <strong>Research-Grade Simulations:</strong> High-fidelity quantum mechanical 
                simulations with publication-ready visualizations and analysis tools.
            </p>
            <p>
                <strong>Educational Excellence:</strong> Learn quantum computing concepts through 
                hands-on experimentation and guided exploration modules.
            </p>
            <p>
                <strong>Real-Time Interaction:</strong> Manipulate quantum systems and observe 
                results instantly with our advanced rendering engine.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick Access Grid
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='premium-card'>
            <div class='card-content'>
                <h4>Quantum Foundations</h4>
                <p>Explore fundamental quantum mechanics through Bloch sphere visualization, 
                quantum interference, and state superposition analysis.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='premium-card'>
            <div class='card-content'>
                <h4>Machine Learning</h4>
                <p>Implement variational quantum algorithms, quantum neural networks, and 
                hybrid optimization methods for next-generation AI.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='premium-card'>
            <div class='card-content'>
                <h4>Advanced Systems</h4>
                <p>Study quantum hardware architectures, error correction protocols, and 
                computational complexity theory for practical quantum computing.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Platform Status
    current_time = datetime.now().strftime("%H:%M UTC")
    st.info(f"🚀 **AlphaNova Quantum Platform Status:** All systems operational | Current time: {current_time}")

elif st.session_state.selected_module_id == 'bloch':
    st.markdown('<h1 class="quantum-title">Bloch Sphere Visualization</h1>', unsafe_allow_html=True)
    st.markdown('<span class="status-badge status-active">Single Qubit Dynamics</span>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class='premium-card'>
            <div class='card-content'>
                <h3>Interactive Quantum State Control</h3>
                <p>Manipulate the quantum state vector on the Bloch sphere and observe 
                real-time changes in state representation.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Enhanced controls
        theta = st.slider("Polar angle θ (degrees)", 0, 180, 45, help="Controls the superposition between |0⟩ and |1⟩")
        phi = st.slider("Azimuthal angle φ (degrees)", 0, 360, 0, help="Controls the relative phase")
        show_trajectory = st.checkbox("Show trajectory path", help="Display the path of state evolution")
        
        # Premium Bloch sphere visualization
        fig = create_enhanced_bloch_sphere(theta, phi, show_trajectory)
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    
    with col2:
        # Quantum state information
        theta_rad = np.radians(theta)
        phi_rad = np.radians(phi)
        alpha = np.cos(theta_rad/2)
        beta = np.sin(theta_rad/2) * np.exp(1j * phi_rad)
        
        st.markdown(f"""
        <div class='premium-card'>
            <div class='card-content'>
                <h3>Quantum State Analysis</h3>
                <p><strong>State Vector:</strong><br>|ψ⟩ = α|0⟩ + β|1⟩</p>
                <br>
                <p><strong>Amplitudes:</strong></p>
                <p>• |α|² = {abs(alpha)**2:.4f}</p>
                <p>• |β|² = {abs(beta)**2:.4f}</p>
                <br>
                <p><strong>Measurement Probabilities:</strong></p>
                <p>• P(|0⟩) = {abs(alpha)**2:.1%}</p>
                <p>• P(|1⟩) = {abs(beta)**2:.1%}</p>
                <br>
                <p><strong>Phase Information:</strong></p>
                <p>• Relative phase: {np.angle(beta):.3f} rad</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

elif st.session_state.selected_module_id == 'gates_circuits':
    st.markdown('<h1 class="quantum-title">Quantum Gates & Circuits</h1>', unsafe_allow_html=True)
    st.markdown('<span class="status-badge status-active">Gate Operations</span>', unsafe_allow_html=True)
    
    # Gate selection interface
    st.markdown("""
    <div class='premium-card'>
        <div class='card-content'>
            <h3>Interactive Quantum Circuit Builder</h3>
            <p>Design and analyze quantum circuits using fundamental quantum gates. 
            Explore gate properties, matrix representations, and their effects on quantum states.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Enhanced circuit visualization
        fig_circuit = create_enhanced_quantum_circuit()
        st.plotly_chart(fig_circuit, use_container_width=True, config={'displayModeBar': False})
    
    with col2:
        # Gate selector
        selected_gate = st.selectbox(
            "Select Quantum Gate",
            ["Hadamard (H)", "Pauli-X", "Pauli-Y", "Pauli-Z", "Phase (S)", "T-Gate", "CNOT"],
            help="Choose a gate to see its properties and matrix representation"
        )
        
        # Gate information
        gate_info = {
            "Hadamard (H)": {
                "description": "Creates superposition of |0⟩ and |1⟩ states",
                "matrix": "1/√2 [[1, 1], [1, -1]]",
                "use_case": "Quantum parallelism and interference"
            },
            "Pauli-X": {
                "description": "Quantum NOT gate, flips |0⟩ ↔ |1⟩",
                "matrix": "[[0, 1], [1, 0]]",
                "use_case": "Bit flip operations"
            },
            "CNOT": {
                "description": "Controlled-X gate for entanglement",
                "matrix": "[[1,0,0,0], [0,1,0,0], [0,0,0,1], [0,0,1,0]]",
                "use_case": "Creating entangled states"
            }
        }
        
        if selected_gate in gate_info:
            info = gate_info[selected_gate]
            st.markdown(f"""
            <div class='premium-card'>
                <div class='card-content'>
                    <h4>{selected_gate}</h4>
                    <p><strong>Function:</strong><br>{info['description']}</p>
                    <p><strong>Matrix:</strong><br>{info['matrix']}</p>
                    <p><strong>Application:</strong><br>{info['use_case']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

elif st.session_state.selected_module_id == 'entanglement':
    st.markdown('<h1 class="quantum-title">Quantum Entanglement</h1>', unsafe_allow_html=True)
    st.markdown('<span class="status-badge status-active">Non-Local Correlations</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='premium-card quantum-glow'>
        <div class='card-content'>
            <h3>Bell States & Non-Local Correlations</h3>
            <p>Explore the fundamental phenomenon of quantum entanglement through Bell state 
            analysis and violation of classical inequalities. Understand the non-local 
            correlations that enable quantum computing and quantum communication protocols.</p>
            <p><strong>Research Focus:</strong> Bell inequality violations, CHSH tests, and 
            quantum teleportation protocols demonstrate the power of entangled quantum states.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.selected_module_id == 'qml':
    st.markdown('<h1 class="quantum-title">Quantum Machine Learning</h1>', unsafe_allow_html=True)
    st.markdown('<span class="status-badge status-emerging">Emerging Technology</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='premium-card quantum-glow'>
        <div class='card-content'>
            <h3>Quantum Neural Networks</h3>
            <p>Explore the intersection of quantum computing and machine learning through 
            variational quantum circuits, quantum feature maps, and hybrid classical-quantum 
            optimization strategies.</p>
            <p><strong>Advanced Capabilities:</strong> Quantum support vector machines, 
            variational quantum classifiers, and quantum generative adversarial networks 
            for enhanced pattern recognition and data analysis.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.selected_module_id == 'vqe':
    st.markdown('<h1 class="quantum-title">Variational Quantum Algorithms</h1>', unsafe_allow_html=True)
    st.markdown('<span class="status-badge status-active">Hybrid Algorithms</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='premium-card'>
        <div class='card-content'>
            <h3>Variational Quantum Eigensolver (VQE)</h3>
            <p>Implement hybrid quantum-classical optimization algorithms for finding ground 
            state energies of molecular Hamiltonians and solving combinatorial optimization problems.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # VQE Energy Landscape Visualization
    x = np.linspace(0, 4*np.pi, 200)
    energy = np.cos(x) + 0.5*np.cos(2*x) + 0.3*np.cos(3*x) + 0.1*np.random.normal(0, 0.1, 200)
    
    fig = go.Figure()
    
    # Energy landscape with gradient fill
    fig.add_trace(go.Scatter(
        x=x, y=energy,
        mode='lines',
        line=dict(color='#60a5fa', width=3),
        fill='tonexty',
        fillcolor='rgba(96, 165, 250, 0.2)',
        name='Energy Landscape',
        hovertemplate="Parameter θ: %{x:.2f}<br>Energy: %{y:.3f}<extra></extra>"
    ))
    
    # Minimum point
    min_idx = np.argmin(energy)
    fig.add_trace(go.Scatter(
        x=[x[min_idx]], y=[energy[min_idx]],
        mode='markers',
        marker=dict(size=15, color='#f59e0b', line=dict(width=3, color='#fbbf24')),
        name='Ground State',
        hovertemplate="Ground State<br>θ: %{x:.2f}<br>Energy: %{y:.3f}<extra></extra>"
    ))
    
    fig.update_layout(
        title=dict(
            text="VQE Energy Optimization Landscape",
            font=dict(color='#f8fafc', size=16),
            x=0.5
        ),
        xaxis=dict(
            title="Parameter θ (radians)",
            color='#cbd5e1',
            gridcolor='rgba(203, 213, 225, 0.1)'
        ),
        yaxis=dict(
            title="Energy (a.u.)",
            color='#cbd5e1',
            gridcolor='rgba(203, 213, 225, 0.1)'
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e2e8f0'),
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

else:
    # Generic module template
    module_name = st.session_state.selected_module_id.replace('_', ' ').title()
    st.markdown(f'<h1 class="quantum-title">{module_name}</h1>', unsafe_allow_html=True)
    st.markdown('<span class="status-badge status-frontier">Advanced Research</span>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class='premium-card quantum-glow'>
        <div class='card-content'>
            <h3>{module_name} Research Module</h3>
            <p>Advanced quantum computing research tools and visualizations for {module_name.lower()} 
            analysis. This module provides state-of-the-art computational methods and 
            interactive exploration capabilities.</p>
            <p><strong>Features:</strong> High-performance simulations, publication-ready 
            visualizations, and comprehensive analysis tools for cutting-edge research.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Premium Footer
st.markdown("""
<div style='text-align: center; color: #64748b; padding: 3rem 2rem; margin-top: 4rem;'>
    <div style='width: 80px; height: 1px; 
        background: linear-gradient(90deg, transparent, rgba(96,165,250,0.5), transparent); 
        margin: 0 auto 2rem;'></div>
    <p style='font-size: 1rem; font-weight: 600; margin-bottom: 0.5rem; color: #94a3b8;'>
        AlphaNova Quantum
    </p>
    <p style='font-size: 0.875rem; color: #6b7280; font-weight: 400;'>
        Next-Generation Quantum Research Environment
    </p>
    <p style='font-size: 0.75rem; color: #4b5563; font-weight: 400; margin-top: 1rem;'>
        Powered by advanced quantum computing algorithms and AI-driven visualizations
    </p>
</div>
""", unsafe_allow_html=True)