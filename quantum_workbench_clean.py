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

# Custom CSS for styling
st.markdown("""
<style>
.nav-section-label {
    font-weight: bold;
    font-size: 0.9em;
    color: #666;
    margin-top: 1rem;
    margin-bottom: 0.5rem;
    padding: 0.25rem 0;
    border-bottom: 1px solid #eee;
}

.sidebar-brand {
    text-align: center;
    padding: 1rem 0;
    margin-bottom: 1rem;
}

.sidebar-brand-title {
    font-size: 1.1em;
    font-weight: bold;
    color: #2c3e50;
}

.sidebar-brand-subtitle {
    font-size: 0.85em;
    color: #7f8c8d;
    margin-top: 0.25rem;
}

.sidebar-footer {
    text-align: center;
    padding-top: 1rem;
    margin-top: 1rem;
    border-top: 1px solid #eee;
}

.sidebar-footer-text {
    font-size: 0.8em;
    color: #666;
}

.sidebar-footer-version {
    color: #999;
    font-size: 0.75em;
}
</style>
""", unsafe_allow_html=True)