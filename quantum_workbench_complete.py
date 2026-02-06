import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Ellipse, FancyBboxPatch, Circle, Wedge
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import json
import os
from datetime import datetime
import base64

# Page configuration
st.set_page_config(
    page_title="Quantum Research Workbench v4.0.2",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/akerkeamangeldy/quantum-research-platform',
        'Report a bug': 'https://github.com/akerkeamangeldy/quantum-research-platform/issues',
        'About': """
        # Quantum Research Workbench v4.0.2
        Advanced quantum computing simulation and research platform.
        Built with Streamlit and scientific Python libraries.
        """
    }
)

# Initialize session state
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
            st.error(f"Error loading {lang} translations: {e}")
            translations[lang] = {}
    
    return translations

# Load translations
TRANSLATIONS = load_translations()

# Translation helper function with dot-notation support
def t(key, fallback=None):
    """
    Get translation for current language with fallback
    Supports dot notation: t('global.title') or direct access: t('title')
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
                break
        if value:
            return value
    
    # Try direct key lookup
    if key in lang_dict:
        return lang_dict[key]
    
    return fallback if fallback else key

# Language selector in sidebar
col_lang1, col_lang2 = st.sidebar.columns(2)
with col_lang1:
    if st.button(t("global.language_en"), key="lang_en"):
        st.session_state.language = 'en'
        st.rerun()

with col_lang2:
    if st.button(t("global.language_ru"), key="lang_ru"):
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

st.sidebar.markdown("---")

# Sidebar footer
sidebar_footer = f"""
<div class='sidebar-footer'>
    <div class='sidebar-footer-text'>
        {t('global.platform_name')}<br>
        <span class='sidebar-footer-version'>{t('global.version')}</span>
    </div>
</div>
"""
st.sidebar.markdown(sidebar_footer, unsafe_allow_html=True)

# Modern Soft Minimalist CSS Styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* Global Variables for Consistent Design */
:root {
    --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    --surface-gradient: linear-gradient(145deg, #ffffff 0%, #f8fafc 100%);
    --glass-bg: rgba(255, 255, 255, 0.25);
    --glass-border: rgba(255, 255, 255, 0.18);
    --shadow-light: rgba(255, 255, 255, 0.8);
    --shadow-dark: rgba(148, 163, 184, 0.4);
    --border-radius-lg: 32px;
    --border-radius-md: 24px;
    --border-radius-sm: 16px;
    --spacing-xs: 0.5rem;
    --spacing-sm: 1rem;
    --spacing-md: 1.5rem;
    --spacing-lg: 2rem;
    --spacing-xl: 3rem;
    --transition-smooth: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    --font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* Global Typography Enhancement */
* {
    font-family: var(--font-family) !important;
    letter-spacing: -0.025em;
}

/* Main Container Neumorphic Styling */
.main .block-container {
    padding-top: var(--spacing-xl);
    padding-bottom: var(--spacing-xl);
    max-width: 1400px;
    background: linear-gradient(145deg, #f8fafc 0%, #ffffff 100%);
    border-radius: var(--border-radius-lg);
    box-shadow: 
        20px 20px 60px var(--shadow-dark),
        -20px -20px 60px var(--shadow-light),
        inset 0 0 0 1px rgba(255, 255, 255, 0.5);
    margin: var(--spacing-md) auto;
    backdrop-filter: blur(20px);
    transition: var(--transition-smooth);
}

/* Sidebar Neumorphic Design */
.css-1d391kg {
    background: linear-gradient(145deg, #f1f5f9 0%, #ffffff 100%) !important;
    border-radius: 0 var(--border-radius-lg) var(--border-radius-lg) 0 !important;
    box-shadow: 
        15px 15px 30px var(--shadow-dark),
        -15px -15px 30px var(--shadow-light);
    padding: var(--spacing-lg) !important;
    backdrop-filter: blur(10px);
}

.nav-section-label {
    font-weight: 600;
    font-size: 0.875rem;
    color: #64748b;
    margin: var(--spacing-md) 0 var(--spacing-sm) 0;
    padding: var(--spacing-xs) var(--spacing-sm);
    background: var(--surface-gradient);
    border-radius: var(--border-radius-sm);
    box-shadow: 
        inset 3px 3px 6px rgba(148, 163, 184, 0.2),
        inset -3px -3px 6px rgba(255, 255, 255, 0.8);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    transition: var(--transition-smooth);
}

.sidebar-brand {
    text-align: center;
    padding: var(--spacing-lg) var(--spacing-md);
    margin-bottom: var(--spacing-lg);
    background: var(--surface-gradient);
    border-radius: var(--border-radius-md);
    box-shadow: 
        12px 12px 24px var(--shadow-dark),
        -12px -12px 24px var(--shadow-light);
    transition: var(--transition-smooth);
}

.sidebar-brand:hover {
    transform: translateY(-2px);
    box-shadow: 
        16px 16px 32px var(--shadow-dark),
        -16px -16px 32px var(--shadow-light);
}

.sidebar-brand-title {
    font-size: 1.25rem;
    font-weight: 700;
    background: var(--primary-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: var(--spacing-xs);
}

.sidebar-brand-subtitle {
    font-size: 0.875rem;
    color: #64748b;
    font-weight: 500;
    margin-top: var(--spacing-xs);
    opacity: 0.8;
}

.sidebar-footer {
    text-align: center;
    padding: var(--spacing-lg) var(--spacing-sm);
    margin-top: var(--spacing-lg);
    background: var(--surface-gradient);
    border-radius: var(--border-radius-md);
    box-shadow: 
        inset 8px 8px 16px rgba(148, 163, 184, 0.15),
        inset -8px -8px 16px rgba(255, 255, 255, 0.9);
}

.sidebar-footer-text {
    font-size: 0.8rem;
    color: #64748b;
    font-weight: 500;
}

.sidebar-footer-version {
    color: #94a3b8;
    font-size: 0.75rem;
    font-weight: 400;
}

/* Research Cards with Neumorphic Design */
.research-card {
    background: var(--surface-gradient);
    border-radius: var(--border-radius-lg);
    padding: var(--spacing-xl) var(--spacing-lg);
    margin: var(--spacing-lg) 0;
    box-shadow: 
        20px 20px 60px var(--shadow-dark),
        -20px -20px 60px var(--shadow-light),
        inset 0 0 0 1px rgba(255, 255, 255, 0.3);
    transition: var(--transition-smooth);
    backdrop-filter: blur(10px);
    position: relative;
    overflow: hidden;
}

.research-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.6), transparent);
}

.research-card:hover {
    transform: translateY(-8px);
    box-shadow: 
        25px 25px 75px var(--shadow-dark),
        -25px -25px 75px var(--shadow-light),
        inset 0 0 0 1px rgba(255, 255, 255, 0.4);
}

.research-card h3 {
    background: var(--primary-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-weight: 600;
    margin-bottom: var(--spacing-md);
    font-size: 1.5rem;
}

.research-card p {
    color: #475569;
    line-height: 1.7;
    font-weight: 400;
    margin-bottom: var(--spacing-sm);
}

/* Metric Boxes with Soft Design */
.metric-box {
    background: var(--surface-gradient);
    border-radius: var(--border-radius-lg);
    padding: var(--spacing-lg);
    text-align: center;
    box-shadow: 
        15px 15px 30px var(--shadow-dark),
        -15px -15px 30px var(--shadow-light);
    transition: var(--transition-smooth);
    margin: var(--spacing-md) 0;
    backdrop-filter: blur(5px);
}

.metric-box:hover {
    transform: translateY(-4px) scale(1.02);
    box-shadow: 
        20px 20px 40px var(--shadow-dark),
        -20px -20px 40px var(--shadow-light);
}

.metric-box h3 {
    background: var(--secondary-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: var(--spacing-xs);
}

.metric-box p {
    color: #64748b;
    font-size: 0.875rem;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.1em;
}

/* Status Badges with Glassmorphism */
.research-status {
    display: inline-block;
    padding: var(--spacing-xs) var(--spacing-md);
    border-radius: 50px;
    font-size: 0.875rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    backdrop-filter: blur(20px);
    transition: var(--transition-smooth);
    margin: var(--spacing-md) 0;
}

.status-active {
    background: rgba(34, 197, 94, 0.15);
    color: #059669;
    border: 1px solid rgba(34, 197, 94, 0.3);
    box-shadow: 0 8px 32px rgba(34, 197, 94, 0.2);
}

.status-frontier {
    background: rgba(168, 85, 247, 0.15);
    color: #7c3aed;
    border: 1px solid rgba(168, 85, 247, 0.3);
    box-shadow: 0 8px 32px rgba(168, 85, 247, 0.2);
}

.status-variational {
    background: rgba(59, 130, 246, 0.15);
    color: #2563eb;
    border: 1px solid rgba(59, 130, 246, 0.3);
    box-shadow: 0 8px 32px rgba(59, 130, 246, 0.2);
}

.status-combinatorial {
    background: rgba(245, 158, 11, 0.15);
    color: #d97706;
    border: 1px solid rgba(245, 158, 11, 0.3);
    box-shadow: 0 8px 32px rgba(245, 158, 11, 0.2);
}

/* Data Grid Mesh with Modern Design */
.data-grid-mesh {
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    border-radius: var(--border-radius-lg);
    padding: var(--spacing-lg);
    backdrop-filter: blur(20px);
    box-shadow: 
        0 8px 32px rgba(148, 163, 184, 0.15);
    transition: var(--transition-smooth);
    margin: var(--spacing-md) 0;
}

.data-grid-mesh:hover {
    background: rgba(255, 255, 255, 0.35);
    border: 1px solid rgba(255, 255, 255, 0.25);
    transform: translateY(-2px);
    box-shadow: 0 12px 40px rgba(148, 163, 184, 0.2);
}

/* LaTeX Display Enhancement */
.latex-display {
    background: var(--surface-gradient);
    border-radius: var(--border-radius-lg);
    padding: var(--spacing-xl);
    margin: var(--spacing-lg) 0;
    box-shadow: 
        inset 10px 10px 20px rgba(148, 163, 184, 0.1),
        inset -10px -10px 20px rgba(255, 255, 255, 0.8),
        0 4px 20px rgba(148, 163, 184, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.5);
}

.latex-display h4 {
    background: var(--primary-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-weight: 600;
    margin-bottom: var(--spacing-md);
}

.latex-display p {
    color: #475569;
    line-height: 1.6;
    margin-bottom: var(--spacing-sm);
}

/* Experiment Panel with Glassmorphism */
.experiment-panel {
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    border-left: 4px solid #6366f1;
    border-radius: var(--border-radius-md);
    padding: var(--spacing-lg);
    margin: var(--spacing-md) 0;
    backdrop-filter: blur(15px);
    transition: var(--transition-smooth);
}

.experiment-panel:hover {
    background: rgba(255, 255, 255, 0.35);
    border-left-color: #4f46e5;
    transform: translateX(4px);
}

/* Button Enhancement */
.stButton > button {
    background: var(--surface-gradient) !important;
    border: 1px solid rgba(255, 255, 255, 0.3) !important;
    border-radius: var(--border-radius-md) !important;
    padding: var(--spacing-sm) var(--spacing-lg) !important;
    font-weight: 600 !important;
    box-shadow: 
        8px 8px 16px var(--shadow-dark),
        -8px -8px 16px var(--shadow-light) !important;
    transition: var(--transition-smooth) !important;
    color: #475569 !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 
        12px 12px 24px var(--shadow-dark),
        -12px -12px 24px var(--shadow-light) !important;
    background: linear-gradient(145deg, #ffffff 0%, #f1f5f9 100%) !important;
}

.stButton > button:active {
    transform: translateY(0px) !important;
    box-shadow: 
        inset 4px 4px 8px var(--shadow-dark),
        inset -4px -4px 8px var(--shadow-light) !important;
}

/* Primary Button Styling */
.stButton > button[data-baseweb="button"][aria-label*="primary"] {
    background: var(--primary-gradient) !important;
    color: white !important;
    border: none !important;
}

/* Module Container Styling */
.bloch-energy, .vqe-landscape, .circuit-flow {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
    border-radius: var(--border-radius-lg);
    padding: var(--spacing-xl);
    margin: var(--spacing-lg) 0;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.hero-glow {
    position: relative;
}

.hero-glow::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(99, 102, 241, 0.03) 0%, transparent 70%);
    pointer-events: none;
    z-index: -1;
}

/* Enhanced Input Styling */
.stSlider > div > div > div > div {
    background: var(--surface-gradient) !important;
    border-radius: var(--border-radius-lg) !important;
    box-shadow: 
        inset 4px 4px 8px var(--shadow-dark),
        inset -4px -4px 8px var(--shadow-light) !important;
}

.stSelectbox > div > div {
    background: var(--surface-gradient) !important;
    border-radius: var(--border-radius-md) !important;
    border: 1px solid rgba(255, 255, 255, 0.3) !important;
    box-shadow: 
        6px 6px 12px var(--shadow-dark),
        -6px -6px 12px var(--shadow-light) !important;
}

/* Responsive Design */
@media (max-width: 768px) {
    :root {
        --border-radius-lg: 24px;
        --border-radius-md: 18px;
        --border-radius-sm: 12px;
        --spacing-xl: 2rem;
        --spacing-lg: 1.5rem;
    }
    
    .main .block-container {
        padding: var(--spacing-lg);
        margin: var(--spacing-sm);
    }
    
    .research-card {
        padding: var(--spacing-lg);
    }
}

/* Animation Keyframes */
@keyframes softPulse {
    0%, 100% {
        opacity: 0.8;
        transform: scale(1);
    }
    50% {
        opacity: 1;
        transform: scale(1.02);
    }
}

@keyframes gentleFloat {
    0%, 100% {
        transform: translateY(0px);
    }
    50% {
        transform: translateY(-10px);
    }
}

/* Accessibility Enhancements */
@media (prefers-reduced-motion: reduce) {
    * {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}

/* Focus States */
*:focus {
    outline: 2px solid #6366f1;
    outline-offset: 2px;
    border-radius: var(--border-radius-sm);
}

</style>
""", unsafe_allow_html=True)

# Main content area
if st.session_state.selected_module_id == 'home':
    st.title(t('modules.home'))
    st.markdown("Welcome to the Quantum Research Workbench")
    st.info("Please select a module from the sidebar to begin your quantum research journey.")

elif st.session_state.selected_module_id == 'bloch':
    st.title(t('modules.bloch'))
    st.markdown("Single qubit dynamics visualization")

elif st.session_state.selected_module_id == 'interference':
    st.title(t('modules.interference'))
    st.markdown("Quantum interference phenomena")

elif st.session_state.selected_module_id == 'entanglement':
    st.title(t('modules.entanglement'))
    st.markdown("Bell state correlations analysis")

elif st.session_state.selected_module_id == 'topological':
    st.title(t('modules.topological'))
    st.markdown("Topological quantum phases")

elif st.session_state.selected_module_id == 'noise':
    st.title(t('modules.noise'))
    st.markdown("Quantum decoherence models")

elif st.session_state.selected_module_id == 'circuits':
    st.title(t('modules.circuits'))
    st.markdown("Quantum circuit synthesis")

elif st.session_state.selected_module_id == 'vqe':
    st.title(t('modules.vqe'))
    st.markdown("Variational quantum eigensolvers")

elif st.session_state.selected_module_id == 'qaoa':
    st.title(t('modules.qaoa'))
    st.markdown("Quantum approximate optimization")

elif st.session_state.selected_module_id == 'qml':
    st.title(t('modules.qml'))
    st.markdown("Quantum machine learning")

elif st.session_state.selected_module_id == 'qec':
    st.title(t('modules.qec'))
    st.markdown("Quantum error correction")

elif st.session_state.selected_module_id == 'hardware':
    st.title(t('modules.hardware'))
    st.markdown("Quantum hardware topology")

elif st.session_state.selected_module_id == 'complexity':
    st.title(t('modules.complexity'))
    st.markdown("Quantum complexity theory")

elif st.session_state.selected_module_id == 'export':
    st.title(t('modules.export'))
    st.markdown("Research data export and analysis")

else:
    st.error(f"Module '{st.session_state.selected_module_id}' not found.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #64748b; padding: 20px;'>
    <p><strong>Quantum x AI Research Workbench</strong> | Production Research Platform</p>
    <p>Academic-Grade Quantum Computing Experiments • Reproducible Results • Publication-Ready Visualizations</p>
    <p style='font-size: 12px; margin-top: 12px;'>
        Built with Streamlit • Qiskit • NumPy • SciPy • Plotly
    </p>
</div>
""", unsafe_allow_html=True)

