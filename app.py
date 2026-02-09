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
    page_title="Quantum Raccoon Research Platform",
    page_icon="🦝",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/akerkeamangeldy/quantum-raccoon-platform',
        'Report a bug': 'https://github.com/akerkeamangeldy/quantum-raccoon-platform/issues',
        'About': """
        # Quantum Raccoon Research Platform
        Advanced QML research environment for variational circuit analysis.
        Built for quantum neural network benchmarking and optimization.
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
    if st.button(t("global.language_en", "English"), key="lang_en"):
        st.session_state.language = 'en'
        st.rerun()

with col_lang2:
    if st.button(t("global.language_ru", "Русский"), key="lang_ru"):
        st.session_state.language = 'ru'
        st.rerun()

st.sidebar.markdown("---")

# Professional brand header  
brand_header = f"""
<div class='sidebar-brand'>
    <div class='sidebar-brand-title'>🦝 {t('global.title', 'Quantum Raccoon')}</div>
    <div class='sidebar-brand-subtitle'>QML Research Platform</div>
</div>
"""
st.sidebar.markdown(brand_header, unsafe_allow_html=True)

# Navigation structure with organized groups and professional icons
nav_groups = [
    ("navigation.section_home", [
        ("home", "00", 'modules.home', 'module_subtitles.home', '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9,22 9,12 15,12 15,22"/></svg>'),
    ]),
    ("navigation.section_foundations", [
        ("bloch", "01", 'modules.bloch', 'module_subtitles.bloch', '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="m4.93 4.93 4.24 4.24"/><path d="m14.83 9.17 4.24-4.24"/><path d="m14.83 14.83 4.24 4.24"/><path d="m9.17 14.83-4.24 4.24"/></svg>'),
        ("interference", "02", 'modules.interference', 'module_subtitles.interference', '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m21 21-3-6h-5l-3 6"/><path d="m21 21-6-9-9 9"/><path d="m21 21-9-12-9 12"/></svg>'),
    ]),
    ("navigation.section_correlations", [
        ("entanglement", "03", 'modules.entanglement', 'module_subtitles.entanglement', '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 3.1c1.9-0.7 4.1-0.7 6 0"/><path d="M8 20.9c1.9 0.7 4.1 0.7 6 0"/><path d="M3.1 8c-0.7 1.9-0.7 4.1 0 6"/><path d="M20.9 8c0.7 1.9 0.7 4.1 0 6"/></svg>'),
        ("topological", "04", 'modules.topological', 'module_subtitles.topological', '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12,2 22,8.5 22,15.5 12,22 2,15.5 2,8.5"/><path d="m2,8.5 10,7 10,-7"/><path d="m12,22 0,-7"/></svg>'),
    ]),
    ("navigation.section_dynamics", [
        ("noise", "05", 'modules.noise', 'module_subtitles.noise', '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 10v3"/><path d="M6 6v11"/><path d="M10 3v18"/><path d="M14 8v7"/><path d="M18 5v13"/><path d="M22 10v3"/></svg>'),
        ("circuits", "06", 'modules.circuits', 'module_subtitles.circuits', '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M9 9h6v6h-6V9Z"/><path d="M9 1v6"/><path d="M15 1v6"/><path d="M9 15v6"/><path d="M15 15v6"/></svg>'),
    ]),
    ("navigation.section_variational", [
        ("vqe", "07", 'modules.vqe', 'module_subtitles.vqe', '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20"/><path d="m15 5 3 3-3 3"/><path d="m9 9 3 3-3 3"/><path d="m21 12-8-8-8 8"/></svg>'),
        ("qaoa", "08", 'modules.qaoa', 'module_subtitles.qaoa', '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13,2 3,14 12,14 11,22 21,10 12,10"/></svg>'),
    ]),
    ("navigation.section_qml", [
        ("qml", "09", 'modules.qml', 'module_subtitles.qml', '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.086-3.086a2 2 0 0 0-1.414-.586H13"/><path d="M13 13h3.5a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5H13"/></svg>'),
    ]),
    ("navigation.section_hardware", [
        ("qec", "10", 'modules.qec', 'module_subtitles.qec', '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6 9 17l-5-5"/><path d="M12 2a10 10 0 1 0 10 10"/></svg>'),
        ("hardware", "11", 'modules.hardware', 'module_subtitles.hardware', '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="20" height="8" x="2" y="2" rx="2" ry="2"/><rect width="20" height="8" x="2" y="14" rx="2" ry="2"/><line x1="6" x2="6" y1="6" y2="6.01"/><line x1="6" x2="6" y1="18" y2="18.01"/></svg>'),
    ]),
    ("navigation.section_complexity", [
        ("complexity", "12", 'modules.complexity', 'module_subtitles.complexity', '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m9 12 2 2 4-4"/><path d="M21 12c.552 0 1-.448 1-1V5a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v6c0 .552.448 1 1 1"/></svg>'),
    ]),
    ("navigation.section_export", [
        ("export", "13", 'modules.export', 'module_subtitles.export', '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7,10 12,15 17,10"/><line x1="12" x2="12" y1="15" y2="3"/></svg>'),
    ]),
]

# Render professional row-based navigation with desktop-style icons
for section_key, modules in nav_groups:
    st.sidebar.markdown(f"<div class='nav-section-label'>{t(section_key, section_key.split('.')[-1])}</div>", unsafe_allow_html=True)
    
    # Render each module as a clickable row with professional icon
    for module_id, number, title_key, subtitle_key, icon_svg in modules:
        active_class = "active" if st.session_state.selected_module_id == module_id else ""
        
        if st.sidebar.button(
            " ",  # Empty button text, we'll use custom HTML
            key=f"nav_{module_id}",
            type="secondary" if st.session_state.selected_module_id != module_id else "primary",
            use_container_width=True
        ):
            st.session_state.selected_module_id = module_id
            st.rerun()
        
        # Custom navigation row with icon
        st.sidebar.markdown(f"""
        <div class='nav-row {active_class}' onclick="document.querySelector('[data-testid=\'baseButton-secondary\'][key=\'nav_{module_id}\']').click()">
            <div class='nav-icon'>{icon_svg}</div>
            <div class='nav-text'>{t(title_key, title_key.split('.')[-1])}</div>
        </div>
        """, unsafe_allow_html=True)

st.sidebar.markdown("---")

# Sidebar footer
sidebar_footer = f"""
<div class='sidebar-footer'>
    <div class='sidebar-footer-text'>
        {t('global.platform_name', 'Quantum Raccoon Platform')}<br>
        <span class='sidebar-footer-version'>{t('global.version', 'Research v1.0')}</span>
    </div>
</div>
"""
st.sidebar.markdown(sidebar_footer, unsafe_allow_html=True)

# QUANTUM RACCOON DARK RESEARCH MODE CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

/* Global Dark Research Mode */
* {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    letter-spacing: -0.05em !important;
}

/* True Dark Background - Deep Matte */
.stApp {
    background: #0E1117 !important;
    color: #F1F5F9 !important;
}

/* Main Container Dark Mode */
.main .block-container {
    padding: 3rem 2rem;
    max-width: 1400px;
    background: rgba(30, 41, 59, 0.3) !important;
    border-radius: 24px;
    backdrop-filter: blur(20px);
    margin: 1.5rem auto;
    border: 1px solid rgba(71, 85, 105, 0.2);
}

/* Dark Sidebar */
[data-testid="stSidebar"] > div:first-child {
    background: rgba(30, 41, 59, 0.8) !important;
    border-radius: 0 24px 24px 0 !important;
    padding: 2rem !important;
    backdrop-filter: blur(20px);
    border-right: 1px solid rgba(71, 85, 105, 0.2);
}

/* Translucent Dark Containers */
.soft-container {
    background: rgba(30, 41, 59, 0.7) !important;
    border-radius: 20px;
    padding: 2rem;
    margin: 1.5rem 0;
    backdrop-filter: blur(15px);
    border: 1px solid rgba(71, 85, 105, 0.3);
    transition: all 0.3s ease;
}

.soft-container:hover {
    background: rgba(30, 41, 59, 0.9) !important;
    transform: translateY(-2px);
    border-color: rgba(71, 85, 105, 0.5);
}

/* Research Row Style (No Heavy Boxes) */
.research-row {
    padding: 1.5rem 2rem;
    margin: 0.5rem 0;
    background: transparent;
    border-bottom: 1px solid rgba(71, 85, 105, 0.2);
    border-radius: 12px;
    transition: all 0.3s ease;
    cursor: pointer;
}

.research-row:hover {
    background: rgba(30, 41, 59, 0.4);
    border-bottom-color: rgba(96, 165, 250, 0.4);
    transform: translateX(8px);
}

/* Typography - Apple Research Style */
h1, h2, h3, h4, h5, h6 {
    color: #F1F5F9 !important;
    font-family: 'Inter', sans-serif !important;
    letter-spacing: -0.05em !important;
    font-weight: 600 !important;
}

.soft-container h3 {
    color: #F1F5F9 !important;
    font-size: 1.5rem;
    margin-bottom: 1rem;
    letter-spacing: -0.05em;
}

.soft-container h4 {
    color: #E2E8F0 !important;
    font-size: 1.25rem;
    margin-bottom: 0.75rem;
    letter-spacing: -0.05em;
}

.soft-container p {
    color: #94A3B8 !important;
    line-height: 1.7;
    font-weight: 400;
    font-size: 0.95rem;
    margin-bottom: 0.75rem;
}

/* Professional Desktop Navigation Icons */
.nav-row {
    display: flex;
    align-items: center;
    padding: 0.75rem 1rem;
    margin: 0.25rem 0;
    border-radius: 8px;
    transition: all 0.2s ease;
    cursor: pointer;
    background: transparent;
}

.nav-row:hover {
    background: rgba(71, 85, 105, 0.3);
    transform: translateX(4px);
}

.nav-row.active {
    background: rgba(96, 165, 250, 0.2);
    border-left: 3px solid #60A5FA;
}

.nav-icon {
    margin-right: 0.75rem;
    color: #94A3B8;
    display: flex;
    align-items: center;
}

.nav-row:hover .nav-icon {
    color: #60A5FA;
}

.nav-text {
    color: #E2E8F0;
    font-size: 0.875rem;
    font-weight: 500;
    font-family: 'Inter', sans-serif;
}

/* Navigation Section Labels */
.nav-section-label {
    font-weight: 600;
    font-size: 0.75rem;
    color: #64748B;
    margin: 1.5rem 0 0.75rem 0;
    padding: 0.5rem 0;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-family: 'Inter', sans-serif;
    border-bottom: 1px solid rgba(71, 85, 105, 0.2);
}

/* Sidebar Brand */
.sidebar-brand {
    text-align: center;
    padding: 1.5rem 1rem;
    margin-bottom: 2rem;
    background: rgba(30, 41, 59, 0.6);
    border-radius: 16px;
    border: 1px solid rgba(71, 85, 105, 0.2);
}

.sidebar-brand-title {
    font-size: 1.125rem;
    font-weight: 700;
    color: #F1F5F9;
    margin-bottom: 0.25rem;
    letter-spacing: -0.05em;
}

.sidebar-brand-subtitle {
    font-size: 0.75rem;
    color: #94A3B8;
    font-weight: 500;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}

/* Sidebar Footer */
.sidebar-footer {
    text-align: center;
    padding: 1.5rem 1rem;
    margin-top: 2rem;
    background: rgba(30, 41, 59, 0.4);
    border-radius: 12px;
    border-top: 1px solid rgba(71, 85, 105, 0.2);
}

.sidebar-footer-text {
    font-size: 0.75rem;
    color: #64748B;
    font-weight: 500;
}

.sidebar-footer-version {
    color: #475569;
    font-size: 0.7rem;
    font-weight: 400;
}

/* Status Pills - Dark Mode */
.soft-status {
    display: inline-block;
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin: 1rem 0;
}

.status-active {
    background: rgba(34, 197, 94, 0.2);
    color: #4ADE80;
    border: 1px solid rgba(34, 197, 94, 0.3);
}

.status-frontier {
    background: rgba(168, 85, 247, 0.2);
    color: #C084FC;
    border: 1px solid rgba(168, 85, 247, 0.3);
}

.status-emerging {
    background: rgba(59, 130, 246, 0.2);
    color: #60A5FA;
    border: 1px solid rgba(59, 130, 246, 0.3);
}

/* Dark Mode Buttons */
.stButton > button {
    background: rgba(30, 41, 59, 0.6) !important;
    border: 1px solid rgba(71, 85, 105, 0.3) !important;
    border-radius: 12px !important;
    color: #E2E8F0 !important;
    font-weight: 500 !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    background: rgba(30, 41, 59, 0.8) !important;
    border-color: rgba(96, 165, 250, 0.5) !important;
    transform: translateY(-1px);
}

/* Info Alerts Dark Mode */
.stInfo {
    background: rgba(59, 130, 246, 0.15) !important;
    border: 1px solid rgba(59, 130, 246, 0.3) !important;
    border-radius: 12px !important;
    color: #93C5FD !important;
}

/* Hide Default Buttons */
.stButton > button {
    visibility: hidden;
    height: 0;
    margin: 0;
    padding: 0;
}

/* Responsive Design */
@media (max-width: 768px) {
    .main .block-container {
        padding: 2rem 1rem;
        margin: 1rem;
    }
    
    .soft-container {
        padding: 1.5rem;
        margin: 1rem 0;
    }
}

</style>
""", unsafe_allow_html=True)

# Main content area
if st.session_state.selected_module_id == 'home':
    st.title("Quantum Machine Learning Research Platform")
    
    # QML-Focused Hero Section
    st.markdown("""
    <div class='soft-container'>
        <h3>🦝 Quantum Raccoon Research Environment</h3>
        <p>Advanced research platform dedicated to Quantum Machine Learning (QML) exploration, 
        variational circuit analysis, and quantum neural network benchmarking. Built for researchers 
        pushing the boundaries of quantum-enhanced machine learning algorithms.</p>
        
        <p><strong>Variational Circuit Analysis</strong><br>
        Comprehensive tools for analyzing parameterized quantum circuits, optimization landscapes, 
        and gradient-based training dynamics in quantum neural networks.</p>
        
        <p><strong>Quantum Neural Network Benchmarking</strong><br>
        Performance evaluation suite for QNNs across different architectures, comparing classical 
        and quantum approaches on machine learning tasks with standardized metrics.</p>
        
        <p><strong>Hybrid Algorithm Development</strong><br>
        Research environment for developing and testing hybrid quantum-classical algorithms, 
        with focus on variational quantum eigensolvers and quantum approximate optimization.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Research Areas - Horizontal Rows Instead of Cards
    st.markdown("""
    <div style='margin: 2rem 0;'>
        <h4 style='color: #F1F5F9; margin-bottom: 1.5rem; letter-spacing: -0.05em;'>Core Research Areas</h4>
        
        <div class='research-row'>
            <h4 style='color: #60A5FA; margin-bottom: 0.5rem; font-size: 1.1rem;'>Variational Quantum Circuits</h4>
            <p style='color: #94A3B8; margin: 0;'>Design and optimization of parameterized quantum circuits for machine learning tasks, including ansatz selection and barren plateau mitigation strategies.</p>
        </div>
        
        <div class='research-row'>
            <h4 style='color: #60A5FA; margin-bottom: 0.5rem; font-size: 1.1rem;'>Quantum Feature Mapping</h4>
            <p style='color: #94A3B8; margin: 0;'>Advanced encoding techniques for classical data into quantum states, exploring kernel methods and feature map expressivity in quantum machine learning.</p>
        </div>
        
        <div class='research-row'>
            <h4 style='color: #60A5FA; margin-bottom: 0.5rem; font-size: 1.1rem;'>Noise-Aware QML</h4>
            <p style='color: #94A3B8; margin: 0;'>Developing quantum machine learning algorithms robust to NISQ device limitations, including error mitigation and noise characterization techniques.</p>
        </div>
        
        <div class='research-row'>
            <h4 style='color: #60A5FA; margin-bottom: 0.5rem; font-size: 1.1rem;'>Quantum Advantage Analysis</h4>
            <p style='color: #94A3B8; margin: 0;'>Theoretical and empirical studies of quantum computational advantage in machine learning, identifying problem domains where quantum methods excel.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("🔬 Select a QML research module from the sidebar to begin your quantum machine learning analysis.")

elif st.session_state.selected_module_id == 'bloch':
    st.title(t('modules.bloch', 'Bloch Sphere Visualization'))
    st.markdown('<span class="soft-status status-active">Single Qubit Dynamics</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='soft-container'>
        <h3>Quantum State Representation</h3>
        <p>The Bloch sphere provides a geometric representation of single-qubit quantum states, 
        essential for understanding quantum neural network building blocks. Explore pure and mixed 
        state dynamics relevant to variational quantum circuit optimization.</p>
        <p><em>Interactive Bloch sphere visualization - Research module under development</em></p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.selected_module_id == 'interference':
    st.title(t('modules.interference', 'Quantum Interference'))
    st.markdown('<span class="soft-status status-active">Coherence Analysis</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='soft-container'>
        <h3>Quantum Coherence in ML Circuits</h3>
        <p>Investigate quantum interference phenomena crucial for quantum machine learning advantage. 
        Analyze how superposition and interference contribute to computational expressivity in 
        variational quantum algorithms and quantum neural networks.</p>
        <p><em>Quantum interference analysis tools - Research module under development</em></p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.selected_module_id == 'entanglement':
    st.title(t('modules.entanglement', 'Quantum Entanglement'))
    st.markdown('<span class="soft-status status-frontier">Correlation Analysis</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='soft-container'>
        <h3>Entanglement in Quantum ML</h3>
        <p>Study entanglement generation and utilization in quantum machine learning algorithms. 
        Explore how quantum correlations enhance learning capacity and provide computational 
        advantages in variational quantum circuits and optimization problems.</p>
        <p><em>Entanglement analysis for QML - Research module under development</em></p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.selected_module_id == 'topological':
    st.title(t('modules.topological', 'Topological Quantum Computing'))
    st.markdown('<span class="soft-status status-frontier">Advanced Research</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='soft-container'>
        <h3>Topological Quantum Machine Learning</h3>
        <p>Explore topological quantum computing approaches to machine learning, including 
        anyonic quantum neural networks and topologically protected quantum algorithms 
        for robust quantum machine learning applications.</p>
        <p><em>Topological QML research - Experimental module under development</em></p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.selected_module_id == 'noise':
    st.title(t('modules.noise', 'Quantum Noise Analysis'))
    st.markdown('<span class="soft-status status-active">NISQ Characterization</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='soft-container'>
        <h3>Noise-Aware QML Development</h3>
        <p>Characterize and mitigate quantum noise effects in machine learning applications. 
        Develop noise-resilient quantum neural network architectures and error mitigation 
        strategies for practical NISQ-era quantum machine learning implementations.</p>
        <p><em>Noise characterization suite - Research module under development</em></p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.selected_module_id == 'circuits':
    st.title(t('modules.circuits', 'Variational Quantum Circuits'))
    st.markdown('<span class="soft-status status-active">Circuit Design</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='soft-container'>
        <h3>QML Circuit Architecture</h3>
        <p>Design and analyze variational quantum circuits for machine learning applications. 
        Explore ansatz design principles, circuit depth optimization, and gradient computation 
        methods for efficient quantum neural network training.</p>
        <p><em>Variational circuit designer - Research module under development</em></p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.selected_module_id == 'vqe':
    st.title(t('modules.vqe', 'Variational Quantum Eigensolver'))
    st.markdown('<span class="soft-status status-active">Hybrid Optimization</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='soft-container'>
        <h3>VQE for Machine Learning</h3>
        <p>Implement and analyze Variational Quantum Eigensolver algorithms adapted for 
        machine learning tasks. Explore hybrid optimization landscapes, parameter initialization 
        strategies, and convergence analysis for quantum-enhanced optimization problems.</p>
        <p><em>VQE optimization suite - Research module under development</em></p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.selected_module_id == 'qaoa':
    st.title(t('modules.qaoa', 'Quantum Approximate Optimization'))
    st.markdown('<span class="soft-status status-active">Combinatorial ML</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='soft-container'>
        <h3>QAOA for ML Optimization</h3>
        <p>Apply Quantum Approximate Optimization Algorithm to machine learning problems 
        including feature selection, clustering, and neural network architecture optimization. 
        Benchmark quantum approaches against classical optimization methods.</p>
        <p><em>QAOA ML applications - Research module under development</em></p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.selected_module_id == 'qml':
    st.title(t('modules.qml', 'Quantum Machine Learning'))
    st.markdown('<span class="soft-status status-emerging">Core Research Area</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='soft-container'>
        <h3>Quantum Neural Network Research</h3>
        <p>Comprehensive quantum machine learning research environment featuring quantum 
        neural networks, variational classifiers, quantum kernel methods, and quantum 
        feature maps. Advanced benchmarking suite for QML algorithm performance evaluation.</p>
        <p><em>Quantum ML research suite - Primary research module under active development</em></p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.selected_module_id == 'qec':
    st.title(t('modules.qec', 'Quantum Error Correction'))
    st.markdown('<span class="soft-status status-frontier">Fault-Tolerant QML</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='soft-container'>
        <h3>Error-Corrected Quantum ML</h3>
        <p>Research quantum error correction protocols for fault-tolerant quantum machine 
        learning. Investigate logical qubit encodings, syndrome extraction methods, and 
        error-corrected variational quantum algorithm implementations.</p>
        <p><em>Quantum error correction for ML - Research module under development</em></p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.selected_module_id == 'hardware':
    st.title(t('modules.hardware', 'Quantum Hardware Analysis'))
    st.markdown('<span class="soft-status status-active">Device Characterization</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='soft-container'>
        <h3>QML Hardware Optimization</h3>
        <p>Analyze quantum computing hardware platforms for machine learning applications. 
        Study connectivity graphs, gate fidelities, and coherence times to optimize 
        quantum neural network implementations across different quantum devices.</p>
        <p><em>Hardware analysis suite - Research module under development</em></p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.selected_module_id == 'complexity':
    st.title(t('modules.complexity', 'Quantum Complexity Theory'))
    st.markdown('<span class="soft-status status-frontier">Theoretical Foundations</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='soft-container'>
        <h3>QML Computational Complexity</h3>
        <p>Theoretical analysis of quantum machine learning computational complexity, 
        quantum advantage proofs, and complexity class separations. Study the theoretical 
        foundations underlying quantum machine learning algorithms and their classical limits.</p>
        <p><em>Complexity analysis framework - Research module under development</em></p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.selected_module_id == 'export':
    st.title(t('modules.export', 'Research Data Export'))
    st.markdown('<span class="soft-status status-active">Publication Suite</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='soft-container'>
        <h3>QML Research Publication Tools</h3>
        <p>Export quantum machine learning research results, visualizations, and benchmarking 
        data in publication-ready formats. Generate LaTeX tables, high-resolution plots, 
        and standardized performance metrics for academic publication submission.</p>
        <p><em>Publication export suite - Research module under development</em></p>
    </div>
    """, unsafe_allow_html=True)

else:
    st.error(f"Research module '{st.session_state.selected_module_id}' not found.")

# Minimalist Dark Footer
st.markdown("""
<div style='text-align: center; color: #64748B; padding: 2rem; margin-top: 3rem; border-top: 1px solid rgba(71, 85, 105, 0.2);'>
    <div style='width: 80px; height: 1px; background: linear-gradient(90deg, transparent, #475569, transparent); margin: 0 auto 1.5rem;'></div>
    <p style='font-family: "Inter", sans-serif; font-size: 0.875rem; font-weight: 500; margin-bottom: 0.5rem; color: #94A3B8; letter-spacing: -0.05em;'>Quantum Raccoon Research Platform</p>
    <p style='font-family: "Inter", sans-serif; font-size: 0.75rem; color: #64748B; font-weight: 400;'>Advanced QML research environment • Variational circuit analysis • Quantum neural network benchmarking</p>
</div>
""", unsafe_allow_html=True)

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
    if st.button(t("global.language_en", "English"), key="lang_en"):
        st.session_state.language = 'en'
        st.rerun()

with col_lang2:
    if st.button(t("global.language_ru", "Русский"), key="lang_ru"):
        st.session_state.language = 'ru'
        st.rerun()

st.sidebar.markdown("---")

# Professional brand header  
brand_header = f"""
<div class='sidebar-brand'>
    <div class='sidebar-brand-title'>{t('global.title', 'Quantum Research Workbench')}</div>
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
    st.sidebar.markdown(f"<div class='nav-section-label'>{t(section_key, section_key.split('.')[-1])}</div>", unsafe_allow_html=True)
    
    # Render each module as a clickable row with icon
    for module_id, number, title_key, subtitle_key in modules:
        # Use Streamlit button with custom styling (icons added via CSS)
        if st.sidebar.button(
            t(title_key, title_key.split('.')[-1]),
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
        {t('global.platform_name', 'Quantum Research Platform')}<br>
        <span class='sidebar-footer-version'>{t('global.version', 'v4.0.2')}</span>
    </div>
</div>
"""
st.sidebar.markdown(sidebar_footer, unsafe_allow_html=True)

# Modern Soft Minimalist CSS Styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

/* Global Variables for Consistent Design */
:root {
    --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    --accent-gradient: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%);
    --surface-gradient: linear-gradient(145deg, #ffffff 0%, #f8fafc 100%);
    --glass-bg: rgba(255, 255, 255, 0.25);
    --glass-border: rgba(255, 255, 255, 0.18);
    --shadow-light: rgba(255, 255, 255, 0.8);
    --shadow-dark: rgba(148, 163, 184, 0.4);
    --border-radius-xl: 32px;
    --border-radius-lg: 24px;
    --border-radius-md: 16px;
    --border-radius-sm: 12px;
    --spacing-xs: 0.5rem;
    --spacing-sm: 1rem;
    --spacing-md: 1.5rem;
    --spacing-lg: 2rem;
    --spacing-xl: 3rem;
    --transition-smooth: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    --font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    --font-mono: 'JetBrains Mono', Monaco, 'Cascadia Code', monospace;
}

/* Global Typography Enhancement */
* {
    font-family: var(--font-family) !important;
    letter-spacing: -0.025em;
}

/* Page Background */
.stApp {
    background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
}

/* Main Container Neumorphic Styling */
.main .block-container {
    padding: var(--spacing-xl) var(--spacing-lg);
    max-width: 1400px;
    background: var(--surface-gradient);
    border-radius: var(--border-radius-xl);
    box-shadow: 
        20px 20px 60px var(--shadow-dark),
        -20px -20px 60px var(--shadow-light),
        inset 0 0 0 1px rgba(255, 255, 255, 0.5);
    margin: var(--spacing-md) auto;
    backdrop-filter: blur(20px);
    transition: var(--transition-smooth);
    border: 1px solid rgba(255, 255, 255, 0.3);
}

/* Sidebar Neumorphic Design */
.css-1d391kg, .css-1cypcdb, [data-testid="stSidebar"] > div:first-child {
    background: linear-gradient(145deg, #f1f5f9 0%, #ffffff 100%) !important;
    border-radius: 0 var(--border-radius-xl) var(--border-radius-xl) 0 !important;
    box-shadow: 
        15px 15px 30px var(--shadow-dark),
        -15px -15px 30px var(--shadow-light);
    padding: var(--spacing-lg) !important;
    backdrop-filter: blur(10px);
}

/* Navigation Section Labels */
.nav-section-label {
    font-weight: 600;
    font-size: 0.875rem;
    color: #64748b;
    margin: var(--spacing-md) 0 var(--spacing-sm) 0;
    padding: var(--spacing-xs) var(--spacing-sm);
    background: var(--surface-gradient);
    border-radius: var(--border-radius-lg);
    box-shadow: 
        inset 3px 3px 6px rgba(148, 163, 184, 0.2),
        inset -3px -3px 6px rgba(255, 255, 255, 0.8);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    transition: var(--transition-smooth);
}

/* Sidebar Brand */
.sidebar-brand {
    text-align: center;
    padding: var(--spacing-lg) var(--spacing-md);
    margin-bottom: var(--spacing-lg);
    background: var(--surface-gradient);
    border-radius: var(--border-radius-lg);
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

/* Sidebar Footer */
.sidebar-footer {
    text-align: center;
    padding: var(--spacing-lg) var(--spacing-sm);
    margin-top: var(--spacing-lg);
    background: var(--surface-gradient);
    border-radius: var(--border-radius-lg);
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

/* Enhanced Button Styling */
.stButton > button {
    background: var(--surface-gradient) !important;
    border: 1px solid rgba(255, 255, 255, 0.3) !important;
    border-radius: var(--border-radius-lg) !important;
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
.stButton > button[kind="primary"] {
    background: var(--primary-gradient) !important;
    color: white !important;
    border: none !important;
    box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3) !important;
}

.stButton > button[kind="primary"]:hover {
    box-shadow: 0 12px 40px rgba(102, 126, 234, 0.4) !important;
}

/* Info/Alert Styling */
.stInfo, .stSuccess, .stWarning, .stError {
    border-radius: var(--border-radius-lg) !important;
    border: none !important;
    backdrop-filter: blur(10px);
}

.stInfo {
    background: rgba(59, 130, 246, 0.1) !important;
    border-left: 4px solid #3b82f6 !important;
}

.stSuccess {
    background: rgba(34, 197, 94, 0.1) !important;
    border-left: 4px solid #22c55e !important;
}

/* Metrics and Cards */
[data-testid="metric-container"] {
    background: var(--surface-gradient) !important;
    border-radius: var(--border-radius-lg) !important;
    padding: var(--spacing-lg) !important;
    box-shadow: 
        15px 15px 30px var(--shadow-dark),
        -15px -15px 30px var(--shadow-light) !important;
    transition: var(--transition-smooth) !important;
    border: 1px solid rgba(255, 255, 255, 0.3) !important;
}

[data-testid="metric-container"]:hover {
    transform: translateY(-4px) scale(1.02) !important;
    box-shadow: 
        20px 20px 40px var(--shadow-dark),
        -20px -20px 40px var(--shadow-light) !important;
}

/* Input Fields */
.stTextInput > div > div > input,
.stNumberInput > div > div > input,
.stSelectbox > div > div > div {
    background: var(--surface-gradient) !important;
    border-radius: var(--border-radius-lg) !important;
    border: 1px solid rgba(255, 255, 255, 0.3) !important;
    box-shadow: 
        inset 4px 4px 8px var(--shadow-dark),
        inset -4px -4px 8px var(--shadow-light) !important;
    transition: var(--transition-smooth) !important;
}

.stTextInput > div > div > input:focus,
.stNumberInput > div > div > input:focus {
    border-color: #6366f1 !important;
    box-shadow: 
        inset 4px 4px 8px var(--shadow-dark),
        inset -4px -4px 8px var(--shadow-light),
        0 0 0 2px rgba(99, 102, 241, 0.2) !important;
}

/* Sliders */
.stSlider > div > div > div {
    background: var(--surface-gradient) !important;
    border-radius: var(--border-radius-xl) !important;
    box-shadow: 
        inset 4px 4px 8px var(--shadow-dark),
        inset -4px -4px 8px var(--shadow-light) !important;
}

.stSlider > div > div > div > div {
    background: var(--primary-gradient) !important;
    border-radius: var(--border-radius-xl) !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    background: var(--surface-gradient) !important;
    border-radius: var(--border-radius-lg) !important;
    padding: var(--spacing-xs) !important;
    box-shadow: 
        inset 4px 4px 8px rgba(148, 163, 184, 0.2),
        inset -4px -4px 8px rgba(255, 255, 255, 0.8) !important;
}

.stTabs [data-baseweb="tab"] {
    border-radius: var(--border-radius-md) !important;
    margin: var(--spacing-xs) !important;
    transition: var(--transition-smooth) !important;
}

.stTabs [aria-selected="true"] {
    background: var(--primary-gradient) !important;
    color: white !important;
    box-shadow: 0 4px 16px rgba(99, 102, 241, 0.3) !important;
}

/* Soft UI Container Class */
.soft-container {
    background: rgba(248, 250, 252, 0.6);
    border-radius: 30px;
    padding: 2.5rem 2rem;
    margin: 2rem 0;
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.3);
    transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    box-shadow: 0 8px 32px rgba(148, 163, 184, 0.12);
}

.soft-container:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 40px rgba(148, 163, 184, 0.18);
    background: rgba(248, 250, 252, 0.8);
}

.soft-container h3 {
    color: #1e293b;
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-size: 1.375rem;
    margin-bottom: 1rem;
    letter-spacing: -0.025em;
}

.soft-container h4 {
    color: #334155;
    font-family: 'Inter', sans-serif;
    font-weight: 500;
    font-size: 1.125rem;
    margin-bottom: 0.75rem;
    letter-spacing: -0.02em;
}

.soft-container p {
    color: #64748b;
    font-family: 'Inter', sans-serif;
    line-height: 1.7;
    font-weight: 400;
    font-size: 0.95rem;
    margin-bottom: 0.75rem;
}

/* Soft Status Pills */
.soft-status {
    display: inline-block;
    padding: 0.5rem 1.25rem;
    border-radius: 30px;
    font-size: 0.8rem;
    font-weight: 500;
    font-family: 'Inter', sans-serif;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin: 1.5rem 0;
    transition: all 0.3s ease;
}

.status-active {
    background: rgba(16, 185, 129, 0.12);
    color: #047857;
    border: 1px solid rgba(16, 185, 129, 0.2);
}

.status-frontier {
    background: rgba(139, 92, 246, 0.12);
    color: #6d28d9;
    border: 1px solid rgba(139, 92, 246, 0.2);
}

.status-emerging {
    background: rgba(59, 130, 246, 0.12);
    color: #1d4ed8;
    border: 1px solid rgba(59, 130, 246, 0.2);
}

/* Plotly Charts */
.js-plotly-plot .plotly .modebar {
    background: var(--glass-bg) !important;
    border-radius: var(--border-radius-md) !important;
    backdrop-filter: blur(10px) !important;
}

/* Code Blocks */
.stCodeBlock {
    border-radius: var(--border-radius-lg) !important;
    font-family: var(--font-mono) !important;
}

/* Data Frames */
.stDataFrame {
    border-radius: var(--border-radius-lg) !important;
    overflow: hidden !important;
    box-shadow: 
        8px 8px 16px var(--shadow-dark),
        -8px -8px 16px var(--shadow-light) !important;
}

/* Progress Bars */
.stProgress > div > div > div {
    background: var(--primary-gradient) !important;
    border-radius: var(--border-radius-xl) !important;
}

.stProgress > div > div {
    background: var(--surface-gradient) !important;
    border-radius: var(--border-radius-xl) !important;
    box-shadow: 
        inset 4px 4px 8px var(--shadow-dark),
        inset -4px -4px 8px var(--shadow-light) !important;
}

/* Responsive Design */
@media (max-width: 768px) {
    :root {
        --border-radius-xl: 24px;
        --border-radius-lg: 18px;
        --border-radius-md: 12px;
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
    outline: 2px solid #6366f1 !important;
    outline-offset: 2px !important;
    border-radius: var(--border-radius-sm) !important;
}

/* Scrollbar Styling */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-track {
    background: var(--surface-gradient);
    border-radius: var(--border-radius-md);
}

::-webkit-scrollbar-thumb {
    background: var(--primary-gradient);
    border-radius: var(--border-radius-md);
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(135deg, #5a6acf 0%, #6b5b95 100%);
}

</style>
""", unsafe_allow_html=True)

# Main content area
if st.session_state.selected_module_id == 'home':
    st.title(t('modules.home', 'Home'))
    
    # Hero Section
    st.markdown("""
    <div class='soft-container'>
        <h3>Welcome to Quantum Research Workbench</h3>
        <p>Advanced quantum computing simulation and research platform designed for researchers, 
        students, and quantum computing enthusiasts. Explore fundamental quantum phenomena, 
        run cutting-edge algorithms, and visualize quantum systems with interactive tools.</p>
        
        <p><strong>Research-Grade Simulations</strong><br>
        Accurate quantum mechanical simulations with publication-ready visualizations.</p>
        
        <p><strong>Educational Content</strong><br>
        Learn quantum computing concepts through hands-on experimentation.</p>
        
        <p><strong>Real-Time Interaction</strong><br>
        Manipulate quantum systems and see results instantly.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick Start Cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='soft-container'>
            <h4>Quantum States</h4>
            <p>Explore single-qubit dynamics on the Bloch sphere. Visualize superposition, 
            entanglement, and quantum measurements.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='soft-container'>
            <h4>Entanglement</h4>
            <p>Study Bell states and quantum correlations. Test Bell inequalities and 
            explore non-local quantum phenomena.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='soft-container'>
            <h4>Algorithms</h4>
            <p>Implement variational quantum algorithms like VQE and QAOA for optimization 
            and quantum chemistry problems.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.info("👈 Please select a module from the sidebar to begin your quantum research journey.")

elif st.session_state.selected_module_id == 'bloch':
    st.title(t('modules.bloch', 'Bloch Sphere'))
    st.markdown('<span class="soft-status status-active">Single Qubit Dynamics</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='soft-container'>
        <h3>Single Qubit State Visualization</h3>
        <p>The Bloch sphere provides a geometric representation of pure single-qubit quantum states. 
        Any pure state can be represented as a point on the unit sphere surface, while mixed states 
        lie within the sphere interior.</p>
        <p><em>Interactive Bloch sphere simulation - Module under development</em></p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.selected_module_id == 'interference':
    st.title(t('modules.interference', 'Quantum Interference'))
    st.markdown('<span class="soft-status status-active">Wave-Particle Duality</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='soft-container'>
        <h3>Mach-Zehnder Interferometer</h3>
        <p>Explore quantum interference phenomena through the iconic Mach-Zehnder setup. 
        Observe how quantum superposition leads to interference patterns and understand 
        the wave-particle duality of quantum objects.</p>
        <p><em>Quantum interference simulation - Module under development</em></p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.selected_module_id == 'entanglement':
    st.title(t('modules.entanglement', 'Quantum Entanglement'))
    st.markdown('<span class="soft-status status-active">Non-Local Correlations</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='soft-container'>
        <h3>Bell States & CHSH Inequality</h3>
        <p>Investigate quantum entanglement through Bell state analysis and violation of 
        classical inequalities. Explore the foundational concepts that enable quantum 
        computing and quantum communication protocols.</p>
        <p><em>Entanglement analysis tools - Module under development</em></p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.selected_module_id == 'topological':
    st.title(t('modules.topological', 'Topological Quantum Computing'))
    st.markdown('<span class="soft-status status-frontier">Frontier Research</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='soft-container'>
        <h3>Anyons & Braiding</h3>
        <p>Explore topological quantum computing concepts including anyonic braiding, 
        topological protection, and fault-tolerant quantum computation through 
        geometric operations.</p>
        <p><em>Topological quantum simulation - Module under development</em></p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.selected_module_id == 'noise':
    st.title(t('modules.noise', 'Quantum Decoherence'))
    st.markdown('<span class="soft-status status-active">Environmental Effects</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='soft-container'>
        <h3>Noise Channels & Decoherence</h3>
        <p>Study how quantum systems interact with their environment leading to 
        decoherence and loss of quantum properties. Explore different noise models 
        and their effects on quantum computation.</p>
        <p><em>Noise simulation tools - Module under development</em></p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.selected_module_id == 'circuits':
    st.title(t('modules.circuits', 'Quantum Circuits'))
    st.markdown('<span class="soft-status status-active">Gate Operations</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='soft-container'>
        <h3>Quantum Circuit Design</h3>
        <p>Build and analyze quantum circuits using fundamental quantum gates. 
        Understand circuit depth, gate decomposition, and quantum algorithm 
        implementation through visual circuit construction.</p>
        <p><em>Circuit builder interface - Module under development</em></p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.selected_module_id == 'vqe':
    st.title(t('modules.vqe', 'Variational Quantum Eigensolver'))
    st.markdown('<span class="soft-status status-active">Hybrid Algorithms</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='soft-container'>
        <h3>Ground State Optimization</h3>
        <p>Implement the Variational Quantum Eigensolver (VQE) algorithm for finding 
        ground state energies of molecular systems. Explore quantum chemistry 
        applications and hybrid quantum-classical optimization.</p>
        <p><em>VQE optimization interface - Module under development</em></p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.selected_module_id == 'qaoa':
    st.title(t('modules.qaoa', 'Quantum Approximate Optimization'))
    st.markdown('<span class="soft-status status-active">Combinatorial Problems</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='soft-container'>
        <h3>QAOA Algorithm</h3>
        <p>Solve combinatorial optimization problems using the Quantum Approximate 
        Optimization Algorithm (QAOA). Tackle MaxCut, graph coloring, and other 
        NP-hard problems with quantum advantage.</p>
        <p><em>QAOA problem solver - Module under development</em></p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.selected_module_id == 'qml':
    st.title(t('modules.qml', 'Quantum Machine Learning'))
    st.markdown('<span class="soft-status status-emerging">Emerging Field</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='soft-container'>
        <h3>Quantum Neural Networks</h3>
        <p>Explore the intersection of quantum computing and machine learning. 
        Implement quantum neural networks, variational classifiers, and quantum 
        feature maps for enhanced pattern recognition.</p>
        <p><em>Quantum ML tools - Module under development</em></p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.selected_module_id == 'qec':
    st.title(t('modules.qec', 'Quantum Error Correction'))
    st.markdown('<span class="soft-status status-active">Fault Tolerance</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='soft-container'>
        <h3>Error Correction Codes</h3>
        <p>Study quantum error correction protocols including surface codes, 
        stabilizer codes, and logical qubit encoding. Essential for building 
        fault-tolerant quantum computers.</p>
        <p><em>Error correction simulator - Module under development</em></p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.selected_module_id == 'hardware':
    st.title(t('modules.hardware', 'Quantum Hardware'))
    st.markdown('<span class="soft-status status-active">Physical Implementation</span>', unsafe_allow_html=True)
    
    
    st.markdown("""
    <div class='soft-container'>
        <h3>Hardware Architectures</h3>
        <p>Explore different quantum computing hardware platforms including 
        superconducting qubits, trapped ions, photonic systems, and their 
        connectivity graphs and performance characteristics.</p>
        <p><em>Hardware topology analyzer - Module under development</em></p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.selected_module_id == 'complexity':
    st.title(t('modules.complexity', 'Quantum Complexity Theory'))
    st.markdown('<span class="soft-status status-frontier">Theoretical Foundations</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='soft-container'>
        <h3>Computational Complexity</h3>
        <p>Investigate quantum complexity classes, quantum speedups, and the 
        theoretical foundations of quantum computing advantage. Compare classical 
        and quantum algorithm complexities.</p>
        <p><em>Complexity analysis tools - Module under development</em></p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.selected_module_id == 'export':
    st.title(t('modules.export', 'Research Data Export'))
    st.markdown('<span class="soft-status status-active">Data Management</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='soft-container'>
        <h3>Publication-Ready Export</h3>
        <p>Export your simulation results, visualizations, and analysis data 
        in formats suitable for research publications, presentations, and 
        further analysis in external tools.</p>
        <p><em>Export functionality - Module under development</em></p>
    </div>
    """, unsafe_allow_html=True)

else:
    st.error(f"Module '{st.session_state.selected_module_id}' not found.")

# Minimalist Footer
st.markdown("""
<div style='text-align: center; color: #94a3b8; padding: 2rem; margin-top: 3rem;'>
    <div style='width: 60px; height: 1px; background: linear-gradient(90deg, transparent, #cbd5e1, transparent); margin: 0 auto 1.5rem;'></div>
    <p style='font-family: "Inter", sans-serif; font-size: 0.875rem; font-weight: 500; margin-bottom: 0.5rem;'>Quantum Research Workbench</p>
    <p style='font-family: "Inter", sans-serif; font-size: 0.75rem; color: #cbd5e1; font-weight: 400;'>Advanced quantum computing simulation platform</p>
</div>
""", unsafe_allow_html=True)

# Complete Soft UI CSS Override
st.markdown("""
<style>
    /* SOFT UI FONT IMPORTS */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Public+Sans:wght@300;400;500;600;700&display=swap');
    
    /* GLOBAL SOFT UI RESET */
    * {
        box-sizing: border-box;
        font-family: 'Inter', 'Public Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }
    
    /* DARK THEME FOUNDATION */
    .main, .stApp, [data-testid="stAppViewContainer"] {
        background-color: #0E1117 !important;
        color: #FAFAFA !important;
    }
    
    .block-container {
        padding: 2rem 1rem !important;
        background-color: #0E1117 !important;
        max-width: none !important;
    }
    
    /* SOFT SIDEBAR */
    [data-testid="stSidebar"] {
        background: linear-gradient(145deg, #1a1f2e 0%, #16202a 100%) !important;
        border-radius: 0 30px 30px 0 !important;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2) !important;
        border: none !important;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background: transparent !important;
        border-radius: 0 30px 30px 0 !important;
        padding: 2rem 1rem !important;
    }
    
    /* SOFT NAVIGATION SECTIONS */
    .nav-section {
        margin-bottom: 2rem;
    }
    
    .nav-title {
        font-size: 18px;
        font-weight: 600;
        color: #FAFAFA;
        margin-bottom: 1rem;
        padding: 0 1rem;
        letter-spacing: -0.01em;
    }
    
    .nav-subtitle {
        font-size: 12px;
        font-weight: 500;
        color: #8B8B8B;
        margin-bottom: 1.5rem;
        padding: 0 1rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* SOFT MODULE ROWS */
    .module-row {
        display: flex;
        align-items: center;
        padding: 1rem 1.5rem;
        margin: 0.5rem 1rem;
        background: rgba(255, 255, 255, 0.03);
        border-radius: 30px;
        cursor: pointer;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        border: 1px solid rgba(255, 255, 255, 0.05);
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    }
    
    .module-row:hover {
        background: rgba(255, 255, 255, 0.08);
        transform: translateY(-2px);
        box-shadow: 0 8px 40px rgba(0, 0, 0, 0.15);
        border-color: rgba(255, 255, 255, 0.1);
    }
    
    .module-row.active {
        background: rgba(96, 165, 250, 0.1);
        border-color: rgba(96, 165, 250, 0.3);
        box-shadow: 0 8px 40px rgba(96, 165, 250, 0.1);
    }
    
    .module-icon {
        width: 20px;
        height: 20px;
        margin-right: 1rem;
        color: #8B8B8B;
        transition: color 0.3s ease;
    }
    
    .module-row:hover .module-icon {
        color: #60A5FA;
    }
    
    .module-name {
        font-size: 14px;
        font-weight: 500;
        color: #FAFAFA;
        flex-grow: 1;
        letter-spacing: -0.01em;
    }
    
    /* MAIN CONTENT AREA */
    .main-header {
        text-align: center;
        margin-bottom: 3rem;
        padding: 3rem 2rem;
        background: rgba(255, 255, 255, 0.03);
        border-radius: 30px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    .main-title {
        font-size: 36px;
        font-weight: 700;
        color: #FAFAFA;
        margin-bottom: 1rem;
        letter-spacing: -0.02em;
        background: linear-gradient(135deg, #FAFAFA 0%, #8B8B8B 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .main-subtitle {
        font-size: 16px;
        color: #8B8B8B;
        font-weight: 400;
        line-height: 1.6;
        max-width: 600px;
        margin: 0 auto;
    }
    
    /* SOFT CARDS */
    .soft-card {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 30px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
    }
    
    .soft-card h3 {
        font-size: 20px;
        font-weight: 600;
        color: #60A5FA;
        margin-bottom: 1rem;
        letter-spacing: -0.01em;
    }
    
    .soft-card p {
        color: #D1D5DB;
        line-height: 1.7;
        font-size: 15px;
        font-weight: 400;
    }
    
    /* SOFT BUTTONS */
    .stButton > button {
        background: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        border-radius: 30px !important;
        padding: 0.75rem 1.5rem !important;
        color: #FAFAFA !important;
        font-weight: 500 !important;
        font-size: 14px !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1) !important;
        backdrop-filter: blur(10px) !important;
        width: 100% !important;
        height: auto !important;
    }
    
    .stButton > button:hover {
        background: rgba(255, 255, 255, 0.08) !important;
        border-color: rgba(255, 255, 255, 0.1) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 40px rgba(0, 0, 0, 0.15) !important;
    }
    
    .stButton > button:active {
        transform: translateY(0px) !important;
    }
    
    /* SOFT INPUTS */
    .stSlider > div > div > div {
        background: rgba(255, 255, 255, 0.03) !important;
        border-radius: 30px !important;
    }
    
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.03) !important;
        border-radius: 30px !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
    }
    
    /* STATUS METRICS */
    .status-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin: 2rem 0;
    }
    
    .status-metric {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 30px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    .metric-label {
        font-size: 12px;
        color: #8B8B8B;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.5rem;
    }
    
    .metric-value {
        font-size: 24px;
        font-weight: 600;
        color: #10B981;
    }
    
    /* REMOVE STREAMLIT DEFAULT STYLING */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }
    .stDeployButton { display: none; }
    
    /* HIDE SCROLLBARS */
    ::-webkit-scrollbar {
        width: 6px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.02);
        border-radius: 3px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 3px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(255, 255, 255, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'selected_module' not in st.session_state:
    st.session_state.selected_module = 'home'

# Professional SVG Icons
def get_icon(name):
    icons = {
        "home": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9,22 9,12 15,12 15,22"/></svg>',
        "overview": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1 1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>',
        "bloch": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2v20"/><path d="M2 12h20"/></svg>',
        "interference": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 12h5l3-8 6 16 3-8h5"/></svg>',
        "entanglement": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><circle cx="6" cy="6" r="2"/><circle cx="18" cy="6" r="2"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="18" r="2"/></svg>',
        "circuits": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="8" width="6" height="8"/><rect x="15" y="8" width="6" height="8"/><path d="M9 12h6"/></svg>',
        "vqe": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 6l4-4 4 4"/><path d="M12 2v20"/></svg>',
        "qml": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7v10c0 5.5 4.5 10 10 10s10-4.5 10-10V7l-10-5z"/></svg>',
        "noise": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>',
        "export": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7,10 12,15 17,10"/></svg>'
    }
    return icons.get(name, "")

# Soft Sidebar Navigation
def create_sidebar():
    with st.sidebar:
        # Home Section
        st.markdown("""
        <div class="nav-section">
            <div class="nav-title">Quantum Workbench</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Home button
        home_active = "active" if st.session_state.selected_module == 'home' else ""
        if st.button(
            f'''
            <div class="module-row {home_active}">
                <div class="module-icon">{get_icon("home")}</div>
                <div class="module-name">Research Overview</div>
            </div>
            ''',
            key="nav_home",
            unsafe_allow_html=True
        ):
            st.session_state.selected_module = 'home'
            st.rerun()
        
        # QML Modules Section
        st.markdown("""
        <div class="nav-section">
            <div class="nav-subtitle">QML Modules</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Module list
        modules = [
            ("bloch", "Bloch Sphere"),
            ("interference", "Quantum Interference"),
            ("entanglement", "Entanglement"),
            ("circuits", "Quantum Circuits"),
            ("vqe", "VQE Algorithm"),
            ("qml", "Quantum ML"),
            ("noise", "Noise Analysis"),
            ("export", "Data Export")
        ]
        
        for module_id, module_name in modules:
            active_class = "active" if st.session_state.selected_module == module_id else ""
            if st.button(
                f'''
                <div class="module-row {active_class}">
                    <div class="module-icon">{get_icon(module_id)}</div>
                    <div class="module-name">{module_name}</div>
                </div>
                ''',
                key=f"nav_{module_id}",
                unsafe_allow_html=True
            ):
                st.session_state.selected_module = module_id
                st.rerun()

# Bloch Sphere Visualization
def create_bloch_sphere(theta, phi):
    """Create interactive 3D Bloch sphere"""
    
    # Sphere coordinates
    u = np.linspace(0, 2 * np.pi, 30)
    v = np.linspace(0, np.pi, 30)
    x_sphere = np.outer(np.cos(u), np.sin(v))
    y_sphere = np.outer(np.sin(u), np.sin(v))
    z_sphere = np.outer(np.ones(np.size(u)), np.cos(v))
    
    # State vector
    theta_rad = np.radians(theta)
    phi_rad = np.radians(phi)
    x_state = np.sin(theta_rad) * np.cos(phi_rad)
    y_state = np.sin(theta_rad) * np.sin(phi_rad)
    z_state = np.cos(theta_rad)
    
    fig = go.Figure()
    
    # Bloch sphere surface
    fig.add_trace(go.Surface(
        x=x_sphere, y=y_sphere, z=z_sphere,
        opacity=0.2,
        colorscale=[[0, 'rgba(96,165,250,0.1)'], [1, 'rgba(96,165,250,0.3)']],
        showscale=False
    ))
    
    # State vector
    fig.add_trace(go.Scatter3d(
        x=[0, x_state], y=[0, y_state], z=[0, z_state],
        mode='lines+markers',
        line=dict(color='#60A5FA', width=6),
        marker=dict(size=[0, 10], color=['#60A5FA', '#F59E0B'])
    ))
    
    # Coordinate axes
    axes = [
        ([0, 1.2], [0, 0], [0, 0], '#EF4444'),
        ([0, 0], [0, 1.2], [0, 0], '#10B981'),
        ([0, 0], [0, 0], [0, 1.2], '#8B5CF6')
    ]
    
    for x, y, z, color in axes:
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z,
            mode='lines',
            line=dict(color=color, width=3),
            showlegend=False
        ))
    
    fig.update_layout(
        scene=dict(
            bgcolor='#0E1117',
            xaxis=dict(range=[-1.5, 1.5], showgrid=False, showticklabels=False),
            yaxis=dict(range=[-1.5, 1.5], showgrid=False, showticklabels=False),
            zaxis=dict(range=[-1.5, 1.5], showgrid=False, showticklabels=False),
            camera=dict(eye=dict(x=1.3, y=1.3, z=1.3))
        ),
        paper_bgcolor='#0E1117',
        plot_bgcolor='#0E1117',
        showlegend=False,
        height=500,
        margin=dict(l=0, r=0, t=0, b=0)
    )
    
    return fig

# Main Application
def main():
    # Create sidebar navigation
    create_sidebar()
    
    # Main content based on selection
    module_id = st.session_state.get('selected_module', 'home')
    
    if module_id == 'home':
        # Research Overview Page
        st.markdown("""
        <div class="main-header">
            <div class="main-title">Quantum Research Workbench</div>
            <div class="main-subtitle">
                Advanced quantum computing research platform with state-of-the-art 
                algorithms, visualizations, and machine learning integration.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # System Status
        current_time = datetime.now().strftime("%H:%M UTC")
        st.markdown(f"""
        <div class="status-grid">
            <div class="status-metric">
                <div class="metric-label">System Status</div>
                <div class="metric-value">ACTIVE</div>
            </div>
            <div class="status-metric">
                <div class="metric-label">Qubits</div>
                <div class="metric-value">127</div>
            </div>
            <div class="status-metric">
                <div class="metric-label">Fidelity</div>
                <div class="metric-value">99.87%</div>
            </div>
            <div class="status-metric">
                <div class="metric-label">Time</div>
                <div class="metric-value">{current_time}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Research Capabilities
        st.markdown("""
        <div class="soft-card">
            <h3>Research Capabilities</h3>
            <p>
                This platform provides comprehensive tools for quantum state manipulation, 
                algorithm development, and machine learning research. Explore quantum 
                phenomena through interactive visualizations and advanced computational methods.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    elif module_id == 'bloch':
        # Bloch Sphere Module
        st.markdown("""
        <div class="main-header">
            <div class="main-title">Bloch Sphere</div>
            <div class="main-subtitle">Interactive single qubit state visualization</div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            theta = st.slider("Polar angle θ (degrees)", 0, 180, 45)
            phi = st.slider("Azimuthal angle φ (degrees)", 0, 360, 0)
            
            fig = create_bloch_sphere(theta, phi)
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
        
        with col2:
            # State calculations
            theta_rad = np.radians(theta)
            phi_rad = np.radians(phi)
            alpha = np.cos(theta_rad/2)
            beta = np.sin(theta_rad/2) * np.exp(1j * phi_rad)
            
            st.markdown(f"""
            <div class="soft-card">
                <h3>Quantum State</h3>
                <p>|ψ⟩ = α|0⟩ + β|1⟩</p>
                <br>
                <div class="metric-label">|α|² (|0⟩ probability)</div>
                <div class="metric-value">{abs(alpha)**2:.3f}</div>
                <br>
                <div class="metric-label">|β|² (|1⟩ probability)</div>
                <div class="metric-value">{abs(beta)**2:.3f}</div>
            </div>
            """, unsafe_allow_html=True)
    
    elif module_id == 'vqe':
        # VQE Algorithm Module
        st.markdown("""
        <div class="main-header">
            <div class="main-title">Variational Quantum Eigensolver</div>
            <div class="main-subtitle">Hybrid quantum-classical optimization algorithm</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Energy landscape plot
        x = np.linspace(0, 2*np.pi, 100)
        y = np.cos(x) + 0.3 * np.cos(3*x) + 0.1 * np.random.normal(0, 1, 100)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=x, y=y,
            mode='lines',
            line=dict(color='#60A5FA', width=3),
            fill='tonexty',
            fillcolor='rgba(96, 165, 250, 0.1)'
        ))
        
        fig.update_layout(
            title=dict(text="Energy Landscape", font=dict(color='#FAFAFA')),
            xaxis=dict(title="Parameter θ", color='#8B8B8B', gridcolor='rgba(255,255,255,0.1)'),
            yaxis=dict(title="Energy", color='#8B8B8B', gridcolor='rgba(255,255,255,0.1)'),
            paper_bgcolor='#0E1117',
            plot_bgcolor='#0E1117',
            font=dict(color='#FAFAFA')
        )
        
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
        
        st.markdown("""
        <div class="soft-card">
            <h3>VQE Algorithm</h3>
            <p>
                The Variational Quantum Eigensolver uses a parameterized quantum circuit 
                to find the ground state energy of molecular Hamiltonians. The algorithm 
                iteratively optimizes circuit parameters using classical optimization methods.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    else:
        # Generic module page
        st.markdown(f"""
        <div class="main-header">
            <div class="main-title">{module_id.replace('_', ' ').title()}</div>
            <div class="main-subtitle">Quantum research module</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="soft-card">
            <h3>{module_id.replace('_', ' ').title()} Research</h3>
            <p>
                This module provides specialized tools and visualizations for {module_id} research. 
                Advanced quantum computing algorithms and analysis capabilities are available.
            </p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

# Soft UI CSS - Elegant Dark Theme with Rounded Corners
st.markdown("""
<style>
    /* SOFT UI FONT IMPORTS */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@300;400;500;600&display=swap');
    
    /* GLOBAL SOFT UI TYPOGRAPHY */
    * {
        box-sizing: border-box;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif !important;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }
    
    /* SOFT DARK FOUNDATION */
    .main {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%) !important;
        min-height: 100vh;
    }
    
    .block-container {
        padding: 2rem !important;
        max-width: none !important;
    }
    
    /* SOFT UI WORKBENCH CONTAINER */
    .workbench-container {
        padding: 2rem;
        min-height: 100vh;
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    }
    
    /* SOFT UI BENTO GRID */
    .workbench-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 1.5rem;
        max-width: 1400px;
        margin: 2rem auto;
    }
    
    /* SOFT UI MODULE TILES */
    .module-tile {
        background: rgba(15, 23, 42, 0.8);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(148, 163, 184, 0.1);
        border-radius: 20px;
        padding: 2rem;
        cursor: pointer;
        position: relative;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 
            0 4px 6px -1px rgba(0, 0, 0, 0.1),
            0 2px 4px -1px rgba(0, 0, 0, 0.06),
            inset 0 1px 0 rgba(255, 255, 255, 0.05);
        min-height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
    }
    
    .module-tile:hover {
        transform: translateY(-4px);
        border-color: rgba(6, 182, 212, 0.3);
        box-shadow: 
            0 20px 25px -5px rgba(0, 0, 0, 0.1),
            0 10px 10px -5px rgba(0, 0, 0, 0.04),
            0 0 30px rgba(6, 182, 212, 0.1),
            inset 0 1px 0 rgba(255, 255, 255, 0.1);
    }
    
    .module-tile.active {
        border-color: rgba(6, 182, 212, 0.6);
        background: rgba(6, 182, 212, 0.05);
        box-shadow: 
            0 20px 25px -5px rgba(0, 0, 0, 0.1),
            0 10px 10px -5px rgba(0, 0, 0, 0.04),
            0 0 40px rgba(6, 182, 212, 0.2),
            inset 0 1px 0 rgba(6, 182, 212, 0.2);
    }
    
    /* SOFT UI MODULE CONTENT */
    .module-icon {
        width: 40px;
        height: 40px;
        color: #94a3b8;
        margin-bottom: 1rem;
        transition: color 0.3s ease;
        filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.1));
    }
    
    .module-tile:hover .module-icon {
        color: #06b6d4;
    }
    
    .module-title {
        font-size: 16px;
        font-weight: 600;
        color: #e2e8f0;
        margin-bottom: 0.5rem;
        letter-spacing: -0.01em;
    }
    
    .module-desc {
        font-size: 12px;
        color: #94a3b8;
        line-height: 1.5;
        opacity: 0.8;
    }
    
    /* SOFT UI HEADER */
    .workbench-header {
        text-align: center;
        margin-bottom: 3rem;
        padding: 3rem 0;
        background: rgba(15, 23, 42, 0.6);
        backdrop-filter: blur(20px);
        border-radius: 24px;
        border: 1px solid rgba(148, 163, 184, 0.1);
        box-shadow: 
            0 10px 15px -3px rgba(0, 0, 0, 0.1),
            0 4px 6px -2px rgba(0, 0, 0, 0.05),
            inset 0 1px 0 rgba(255, 255, 255, 0.05);
    }
    
    .workbench-title {
        font-size: 32px;
        font-weight: 700;
        color: #e2e8f0;
        margin-bottom: 0.75rem;
        letter-spacing: -0.02em;
        background: linear-gradient(135deg, #e2e8f0 0%, #94a3b8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .workbench-subtitle {
        font-size: 14px;
        color: #64748b;
        font-weight: 500;
        letter-spacing: 0.02em;
        opacity: 0.9;
    }
    
    /* SOFT UI CARDS */
    .research-card {
        background: rgba(15, 23, 42, 0.8);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(148, 163, 184, 0.1);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 
            0 4px 6px -1px rgba(0, 0, 0, 0.1),
            0 2px 4px -1px rgba(0, 0, 0, 0.06),
            inset 0 1px 0 rgba(255, 255, 255, 0.05);
    }
    
    .research-card h3 {
        color: #06b6d4;
        font-size: 18px;
        font-weight: 600;
        margin-bottom: 1rem;
        letter-spacing: -0.01em;
    }
    
    .research-card p {
        color: #cbd5e1;
        line-height: 1.7;
        font-size: 14px;
        opacity: 0.9;
    }
    
    /* SOFT UI BUTTONS */
    .stButton > button {
        background: rgba(15, 23, 42, 0.8) !important;
        backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(148, 163, 184, 0.1) !important;
        border-radius: 16px !important;
        padding: 0 !important;
        width: 100% !important;
        height: 100% !important;
        color: inherit !important;
        font: inherit !important;
        box-shadow: 
            0 2px 4px -1px rgba(0, 0, 0, 0.1),
            0 1px 2px -1px rgba(0, 0, 0, 0.06) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        border-color: rgba(6, 182, 212, 0.3) !important;
        box-shadow: 
            0 10px 15px -3px rgba(0, 0, 0, 0.1),
            0 4px 6px -2px rgba(0, 0, 0, 0.05),
            0 0 20px rgba(6, 182, 212, 0.1) !important;
    }
    
    /* SOFT UI STATUS PANEL */
    .status-panel {
        background: rgba(15, 23, 42, 0.8);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(148, 163, 184, 0.1);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 
            0 4px 6px -1px rgba(0, 0, 0, 0.1),
            0 2px 4px -1px rgba(0, 0, 0, 0.06),
            inset 0 1px 0 rgba(255, 255, 255, 0.05);
    }
    
    .status-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
    }
    
    .status-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem;
        background: rgba(30, 41, 59, 0.4);
        border-radius: 12px;
        border: 1px solid rgba(148, 163, 184, 0.05);
    }
    
    .status-label {
        font-size: 12px;
        color: #94a3b8;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .status-value {
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
        color: #10b981;
        font-weight: 600;
    }
    
    /* REMOVE STREAMLIT UI */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }
    [data-testid="stSidebar"] { display: none !important; }
    
    /* SOFT UI SCROLLBAR */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(15, 23, 42, 0.8);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: rgba(148, 163, 184, 0.3);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(148, 163, 184, 0.5);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'selected_module' not in st.session_state:
    st.session_state.selected_module = 'home'

# Quantum Research Workbench - Soft UI Grid System
def create_soft_workbench_grid():
    """Generate the soft UI Bento Grid navigation system"""
    
    # SVG Vector Icons - Clean and Professional
    svg_icons = {
        "home": '<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9,22 9,12 15,12 15,22"/></svg>',
        "bloch": '<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><path d="M12 2v20"/><path d="M2 12h20"/><circle cx="12" cy="12" r="3" fill="currentColor"/></svg>',
        "interference": '<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M2 12h5l3-8 6 16 3-8h5"/></svg>',
        "entanglement": '<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="8" cy="12" r="4"/><circle cx="16" cy="12" r="4"/><path d="M12 8v8"/></svg>',
        "circuits": '<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="8" width="6" height="8"/><rect x="15" y="8" width="6" height="8"/><path d="M9 12h6"/></svg>',
        "vqe": '<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M8 6l4-4 4 4"/><path d="M12 2v20"/></svg>',
        "qml": '<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="3"/><circle cx="6" cy="6" r="2"/><circle cx="18" cy="6" r="2"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="18" r="2"/></svg>',
        "export": '<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7,10 12,15 17,10"/></svg>'
    }
    
    # Research modules
    modules = [
        {"id": "home", "title": "Platform Overview", "desc": "Research dashboard and system status"},
        {"id": "bloch", "title": "Bloch Sphere", "desc": "Single qubit state visualization"},
        {"id": "interference", "title": "Quantum Interference", "desc": "Superposition and phase analysis"},
        {"id": "entanglement", "title": "Entanglement", "desc": "Bell states and correlations"},
        {"id": "circuits", "title": "Quantum Circuits", "desc": "Gate operations and synthesis"},
        {"id": "vqe", "title": "VQE Algorithm", "desc": "Variational quantum eigensolver"},
        {"id": "qml", "title": "Quantum ML", "desc": "Machine learning on quantum computers"},
        {"id": "export", "title": "Data Export", "desc": "Analysis results and visualization"}
    ]
    
    # Soft UI Header
    st.markdown('''
    <div class="workbench-header">
        <div class="workbench-title">Quantum Research Workbench</div>
        <div class="workbench-subtitle">Professional quantum computing research platform</div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Status Panel
    current_time = datetime.now().strftime("%H:%M UTC")
    st.markdown(f'''
    <div class="status-panel">
        <div class="status-grid">
            <div class="status-item">
                <span class="status-label">System Status</span>
                <span class="status-value">ACTIVE</span>
            </div>
            <div class="status-item">
                <span class="status-label">Qubits</span>
                <span class="status-value">127</span>
            </div>
            <div class="status-item">
                <span class="status-label">Fidelity</span>
                <span class="status-value">99.87%</span>
            </div>
            <div class="status-item">
                <span class="status-label">Time</span>
                <span class="status-value">{current_time}</span>
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Container and grid
    st.markdown('<div class="workbench-container">', unsafe_allow_html=True)
    st.markdown('<div class="workbench-grid">', unsafe_allow_html=True)
    
    # Generate soft UI module tiles
    for module in modules:
        active_class = "active" if st.session_state.get("selected_module", "home") == module["id"] else ""
        
        if st.button(
            f'''
            <div class="module-tile {active_class}">
                <div class="module-icon">{svg_icons.get(module["id"], "")}</div>
                <div class="module-title">{module["title"]}</div>
                <div class="module-desc">{module["desc"]}</div>
            </div>
            ''',
            key=f"module_{module['id']}",
            unsafe_allow_html=True
        ):
            st.session_state.selected_module = module["id"]
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close workbench-grid
    st.markdown('</div>', unsafe_allow_html=True)  # Close workbench-container

# Bloch Sphere Visualization
def create_bloch_sphere(theta, phi):
    """Create an interactive 3D Bloch sphere visualization"""
    
    # Sphere coordinates
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    x_sphere = np.outer(np.cos(u), np.sin(v))
    y_sphere = np.outer(np.sin(u), np.sin(v))
    z_sphere = np.outer(np.ones(np.size(u)), np.cos(v))
    
    # State vector
    theta_rad = np.radians(theta)
    phi_rad = np.radians(phi)
    x_state = np.sin(theta_rad) * np.cos(phi_rad)
    y_state = np.sin(theta_rad) * np.sin(phi_rad)
    z_state = np.cos(theta_rad)
    
    fig = go.Figure()
    
    # Bloch sphere
    fig.add_trace(go.Surface(
        x=x_sphere, y=y_sphere, z=z_sphere,
        opacity=0.3,
        colorscale=[[0, 'rgba(6,182,212,0.1)'], [1, 'rgba(6,182,212,0.3)']],
        showscale=False,
        name='Bloch Sphere'
    ))
    
    # State vector
    fig.add_trace(go.Scatter3d(
        x=[0, x_state], y=[0, y_state], z=[0, z_state],
        mode='lines+markers',
        line=dict(color='#06b6d4', width=8),
        marker=dict(size=[0, 12], color=['#06b6d4', '#f59e0b']),
        name='Quantum State'
    ))
    
    # Axes
    axes_traces = [
        ([0, 1.2], [0, 0], [0, 0], 'X', '#ef4444'),
        ([0, 0], [0, 1.2], [0, 0], 'Y', '#10b981'),
        ([0, 0], [0, 0], [0, 1.2], 'Z', '#8b5cf6')
    ]
    
    for x, y, z, name, color in axes_traces:
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z,
            mode='lines',
            line=dict(color=color, width=4),
            name=f'{name} axis',
            showlegend=False
        ))
    
    fig.update_layout(
        scene=dict(
            xaxis_title="X", yaxis_title="Y", zaxis_title="Z",
            bgcolor='rgba(15,23,42,0.8)',
            xaxis=dict(range=[-1.5, 1.5], backgroundcolor='rgba(15,23,42,0.8)'),
            yaxis=dict(range=[-1.5, 1.5], backgroundcolor='rgba(15,23,42,0.8)'),
            zaxis=dict(range=[-1.5, 1.5], backgroundcolor='rgba(15,23,42,0.8)'),
            camera=dict(eye=dict(x=1.5, y=1.5, z=1.5))
        ),
        paper_bgcolor='rgba(15,23,42,0.8)',
        plot_bgcolor='rgba(15,23,42,0.8)',
        font=dict(color='#e2e8f0'),
        height=600
    )
    
    return fig

# Quantum Circuit Visualization
def create_quantum_circuit():
    """Create a sample quantum circuit visualization"""
    
    fig = go.Figure()
    
    # Circuit lines (qubits)
    for i in range(3):
        fig.add_trace(go.Scatter(
            x=[0, 10], y=[i, i],
            mode='lines',
            line=dict(color='#64748b', width=2),
            showlegend=False
        ))
    
    # Quantum gates
    gates = [
        (1, 0, 'H', '#06b6d4'),  # Hadamard on qubit 0
        (3, 1, 'X', '#ef4444'),  # Pauli-X on qubit 1
        (5, 2, 'Z', '#8b5cf6'),  # Pauli-Z on qubit 2
        (7, 0, 'RY', '#10b981'), # RY rotation on qubit 0
    ]
    
    for x, y, gate, color in gates:
        fig.add_trace(go.Scatter(
            x=[x], y=[y],
            mode='markers+text',
            marker=dict(size=40, color=color, symbol='square'),
            text=[gate],
            textposition='middle center',
            textfont=dict(color='white', size=12),
            showlegend=False
        ))
    
    # CNOT gate
    fig.add_trace(go.Scatter(
        x=[6, 6], y=[0, 1],
        mode='lines+markers',
        line=dict(color='#f59e0b', width=4),
        marker=dict(size=[8, 20], color='#f59e0b', symbol=['circle', 'x']),
        showlegend=False
    ))
    
    fig.update_layout(
        xaxis=dict(range=[-0.5, 10.5], showgrid=False, zeroline=False, visible=False),
        yaxis=dict(range=[-0.5, 2.5], showgrid=False, zeroline=False, visible=False),
        paper_bgcolor='rgba(15,23,42,0.8)',
        plot_bgcolor='rgba(15,23,42,0.8)',
        height=300,
        showlegend=False
    )
    
    return fig

# Main application logic
def main():
    module_id = st.session_state.get('selected_module', 'home')
    
    if module_id == "home":
        # Generate Soft UI Workbench Grid
        create_soft_workbench_grid()
        
    elif module_id == "bloch":
        st.markdown('''
        <div class="workbench-header">
            <div class="workbench-title">Bloch Sphere Visualization</div>
            <div class="workbench-subtitle">Single qubit state representation</div>
        </div>
        ''', unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            theta = st.slider("Polar angle θ (degrees)", 0, 180, 45, key="theta")
            phi = st.slider("Azimuthal angle φ (degrees)", 0, 360, 0, key="phi")
            
            fig = create_bloch_sphere(theta, phi)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown('''
            <div class="research-card">
                <h3>Quantum State</h3>
                <p>The Bloch sphere represents the pure states of a two-level quantum system.</p>
            </div>
            ''', unsafe_allow_html=True)
            
            # State vector calculation
            theta_rad = np.radians(theta)
            phi_rad = np.radians(phi)
            
            alpha = np.cos(theta_rad/2)
            beta = np.sin(theta_rad/2) * np.exp(1j * phi_rad)
            
            st.markdown(f'''
            <div class="status-panel">
                <div class="status-item">
                    <span class="status-label">|α|²</span>
                    <span class="status-value">{abs(alpha)**2:.3f}</span>
                </div>
                <div class="status-item">
                    <span class="status-label">|β|²</span>
                    <span class="status-value">{abs(beta)**2:.3f}</span>
                </div>
            </div>
            ''', unsafe_allow_html=True)
    
    elif module_id == "circuits":
        st.markdown('''
        <div class="workbench-header">
            <div class="workbench-title">Quantum Circuits</div>
            <div class="workbench-subtitle">Gate operations and quantum algorithms</div>
        </div>
        ''', unsafe_allow_html=True)
        
        fig = create_quantum_circuit()
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown('''
        <div class="research-card">
            <h3>Circuit Description</h3>
            <p>This quantum circuit demonstrates common quantum gates including Hadamard, Pauli gates, 
            rotation gates, and controlled operations. The circuit operates on 3 qubits and shows 
            the fundamental building blocks of quantum algorithms.</p>
        </div>
        ''', unsafe_allow_html=True)
    
    elif module_id == "vqe":
        st.markdown('''
        <div class="workbench-header">
            <div class="workbench-title">Variational Quantum Eigensolver</div>
            <div class="workbench-subtitle">Quantum optimization algorithm</div>
        </div>
        ''', unsafe_allow_html=True)
        
        st.markdown('''
        <div class="research-card">
            <h3>VQE Algorithm</h3>
            <p>The Variational Quantum Eigensolver (VQE) is a hybrid quantum-classical algorithm 
            designed to find the ground state energy of molecular Hamiltonians. It uses a 
            parameterized quantum circuit (ansatz) and classical optimization to minimize 
            the expectation value of the Hamiltonian.</p>
        </div>
        ''', unsafe_allow_html=True)
        
        # Simple VQE energy landscape
        x = np.linspace(0, 2*np.pi, 100)
        y = np.cos(x) + 0.5 * np.cos(2*x) + 0.1 * np.random.normal(0, 1, 100)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=x, y=y,
            mode='lines',
            line=dict(color='#06b6d4', width=3),
            name='Energy Landscape'
        ))
        
        fig.update_layout(
            title="VQE Energy Optimization",
            xaxis_title="Parameter θ",
            yaxis_title="Energy",
            paper_bgcolor='rgba(15,23,42,0.8)',
            plot_bgcolor='rgba(15,23,42,0.8)',
            font=dict(color='#e2e8f0')
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    else:
        st.markdown(f'''
        <div class="workbench-header">
            <div class="workbench-title">{module_id.upper()} Module</div>
            <div class="workbench-subtitle">Quantum research module</div>
        </div>
        ''', unsafe_allow_html=True)
        
        st.markdown(f'''
        <div class="research-card">
            <h3>{module_id.title()} Research Module</h3>
            <p>This module provides specialized tools and visualizations for {module_id} research. 
            Advanced quantum computing algorithms and analysis tools are available here.</p>
        </div>
        ''', unsafe_allow_html=True)

if __name__ == "__main__":
    main()