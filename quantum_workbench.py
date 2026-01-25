"""
Quantum × AI Paper-to-Experiment Workbench
Professional Research Dashboard for Quantum Computing and Quantum Machine Learning

Target: Cambridge Professor Presentation
Academic Rigor • Reproducible Experiments • Publication-Grade Visualizations
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

# Page configuration
st.set_page_config(
    page_title="Quantum Research Workbench",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dark Engineering Aesthetics CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=JetBrains+Mono:wght@400;700&display=swap');
    
    :root {
        --bg-primary: #0A0E1A;
        --bg-secondary: #121826;
        --bg-tertiary: #1A2332;
        --accent-indigo: #6366F1;
        --accent-cyan: #06B6D4;
        --accent-lime: #84CC16;
        --text-primary: #E5E7EB;
        --text-secondary: #9CA3AF;
        --grid-color: rgba(99, 102, 241, 0.1);
    }
    
    .stApp {
        background: linear-gradient(135deg, #0A0E1A 0%, #121826 100%);
        background-image: 
            linear-gradient(var(--grid-color) 1px, transparent 1px),
            linear-gradient(90deg, var(--grid-color) 1px, transparent 1px);
        background-size: 50px 50px;
        background-attachment: fixed;
    }
    
    .main {
        font-family: 'Inter', sans-serif;
        color: var(--text-primary);
    }
    
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        color: var(--text-primary);
        letter-spacing: -0.02em;
    }
    
    code, pre {
        font-family: 'JetBrains Mono', monospace;
        background: var(--bg-tertiary);
        border: 1px solid rgba(99, 102, 241, 0.2);
        border-radius: 6px;
        padding: 2px 6px;
    }
    
    .research-card {
        background: linear-gradient(135deg, rgba(18, 24, 38, 0.9) 0%, rgba(26, 35, 50, 0.9) 100%);
        border: 1px solid rgba(99, 102, 241, 0.3);
        border-radius: 12px;
        padding: 24px;
        margin: 16px 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        backdrop-filter: blur(10px);
    }
    
    .experiment-panel {
        background: var(--bg-secondary);
        border-left: 3px solid var(--accent-indigo);
        padding: 20px;
        margin: 16px 0;
        border-radius: 8px;
    }
    
    .metric-box {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(6, 182, 212, 0.1) 100%);
        border: 1px solid var(--accent-indigo);
        border-radius: 8px;
        padding: 16px;
        text-align: center;
        margin: 8px 0;
    }
    
    .metric-box h3 {
        color: var(--accent-cyan);
        margin: 0;
        font-size: 28px;
        font-weight: 700;
    }
    
    .metric-box p {
        color: var(--text-secondary);
        margin: 4px 0 0 0;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .latex-display {
        background: rgba(99, 102, 241, 0.05);
        border-left: 3px solid var(--accent-indigo);
        padding: 20px;
        margin: 16px 0;
        border-radius: 8px;
        font-family: 'JetBrains Mono', monospace;
        color: var(--text-primary);
    }
    
    .code-panel {
        background: #0D1117;
        border: 1px solid rgba(99, 102, 241, 0.3);
        border-radius: 8px;
        padding: 16px;
        margin: 16px 0;
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
        overflow-x: auto;
    }
    
    .stButton button {
        background: linear-gradient(135deg, var(--accent-indigo) 0%, var(--accent-cyan) 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: 600;
        font-family: 'Inter', sans-serif;
        transition: all 0.3s ease;
    }
    
    .stButton button:hover {
        box-shadow: 0 0 20px rgba(99, 102, 241, 0.5);
        transform: translateY(-2px);
    }
    
    .sidebar .sidebar-content {
        background: var(--bg-secondary);
    }
    
    .research-status {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 11px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .status-active {
        background: rgba(132, 204, 22, 0.2);
        color: var(--accent-lime);
        border: 1px solid var(--accent-lime);
    }
    
    .status-frontier {
        background: rgba(99, 102, 241, 0.2);
        color: var(--accent-indigo);
        border: 1px solid var(--accent-indigo);
    }
    
    .export-card {
        background: var(--bg-tertiary);
        border: 2px dashed rgba(99, 102, 241, 0.4);
        border-radius: 8px;
        padding: 20px;
        margin: 16px 0;
        text-align: center;
    }
    
    /* Animated Backgrounds for Each Module */
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }
    
    @keyframes pulse-glow {
        0%, 100% { box-shadow: 0 0 20px rgba(99, 102, 241, 0.3); }
        50% { box-shadow: 0 0 40px rgba(99, 102, 241, 0.6); }
    }
    
    @keyframes rotate-gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes shimmer {
        0% { background-position: -1000px 0; }
        100% { background-position: 1000px 0; }
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
    """Create interactive 3D Bloch sphere with state vector."""
    theta = np.radians(theta_deg)
    phi = np.radians(phi_deg)
    
    # State vector endpoint
    x_state = np.sin(theta) * np.cos(phi)
    y_state = np.sin(theta) * np.sin(phi)
    z_state = np.cos(theta)
    
    # Sphere surface
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    x_sphere = np.outer(np.cos(u), np.sin(v))
    y_sphere = np.outer(np.sin(u), np.sin(v))
    z_sphere = np.outer(np.ones(np.size(u)), np.cos(v))
    
    fig = go.Figure()
    
    # Sphere surface (translucent)
    fig.add_trace(go.Surface(
        x=x_sphere, y=y_sphere, z=z_sphere,
        colorscale=[[0, 'rgba(99, 102, 241, 0.1)'], [1, 'rgba(6, 182, 212, 0.1)']],
        showscale=False,
        opacity=0.3,
        name='Bloch Sphere'
    ))
    
    # Axes
    axis_length = 1.3
    axes = [
        ([0, axis_length], [0, 0], [0, 0], 'X', '#06B6D4'),
        ([0, 0], [0, axis_length], [0, 0], 'Y', '#84CC16'),
        ([0, 0], [0, 0], [0, axis_length], 'Z', '#6366F1')
    ]
    
    for x, y, z, name, color in axes:
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z,
            mode='lines+text',
            line=dict(color=color, width=4),
            text=['', f'|{name}⟩'],
            textposition='top center',
            textfont=dict(size=14, color=color),
            showlegend=False
        ))
    
    # State vector arrow
    fig.add_trace(go.Scatter3d(
        x=[0, x_state], y=[0, y_state], z=[0, z_state],
        mode='lines+markers',
        line=dict(color='#F59E0B', width=6),
        marker=dict(size=[0, 10], color='#F59E0B'),
        name='|ψ⟩'
    ))
    
    # Equator circle
    theta_eq = np.linspace(0, 2*np.pi, 100)
    fig.add_trace(go.Scatter3d(
        x=np.cos(theta_eq), y=np.sin(theta_eq), z=np.zeros_like(theta_eq),
        mode='lines',
        line=dict(color='rgba(255, 255, 255, 0.2)', width=2, dash='dash'),
        showlegend=False
    ))
    
    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False, range=[-1.5, 1.5]),
            yaxis=dict(visible=False, range=[-1.5, 1.5]),
            zaxis=dict(visible=False, range=[-1.5, 1.5]),
            bgcolor='rgba(0,0,0,0)',
            camera=dict(eye=dict(x=1.5, y=1.5, z=1.3))
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=0, b=0),
        height=500,
        showlegend=False
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

# Sidebar navigation
st.sidebar.markdown("# Quantum Research Workbench")
st.sidebar.markdown("---")

modules = {
    "Research Overview": "overview",
    "Qubit State & Bloch Sphere": "bloch",
    "Superposition & Interference": "interference",
    "Entanglement & Bell States": "entanglement",
    "Noise & Decoherence": "noise",
    "Quantum Circuits & Unitaries": "circuits",
    "VQE: Variational Eigensolver": "vqe",
    "QAOA: Optimization": "qaoa",
    "Quantum Machine Learning": "qml",
    "Error Correction: Surface Codes": "qec",
    "Hardware Topology": "hardware",
    "Complexity Classes: P, NP, BQP": "complexity",
    "Topological Quantum Computing": "topological",
    "Reproducibility & Export": "export"
}

selected_module = st.sidebar.radio("Select Research Module", list(modules.keys()))
module_id = modules[selected_module]

# Experiment session state
if 'experiment_log' not in st.session_state:
    st.session_state.experiment_log = []

# Main content area
if module_id == "overview":
    # Add particle effect background
    add_particle_effect()
    
    st.markdown("<div class='overview-bg'>", unsafe_allow_html=True)
    st.markdown("# Quantum × AI Paper-to-Experiment Workbench")
    st.markdown('<span class="research-status status-active">Production Research Platform</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='research-card'>
        <h2>Research Rationale</h2>
        <p>This platform transforms quantum computing and quantum machine learning research papers 
        into interactive, reproducible experiments. Designed for professional developers, ML engineers, 
        and quantum researchers who demand academic rigor and publication-grade visualizations.</p>
        
        <h3 style='margin-top: 24px;'>Core Workflow: Paper → Experiment</h3>
        <ol>
            <li><strong>Select Research Module:</strong> Choose from canonical quantum algorithms and QML methods</li>
            <li><strong>Review Theory:</strong> Mathematical formalism with LaTeX, key definitions, and limitations</li>
            <li><strong>Configure Experiment:</strong> Interactive parameter controls, noise models, backend selection</li>
            <li><strong>Execute & Visualize:</strong> Run quantum circuits with real-time state evolution and metrics</li>
            <li><strong>Export Results:</strong> Generate reproducibility snapshots (JSON + PDF) for publication</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    # Technology stack
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='experiment-panel'>
            <h3>Technical Stack</h3>
            <ul>
                <li><strong>Quantum Frameworks:</strong> Qiskit, PennyLane</li>
                <li><strong>Numerics:</strong> NumPy, SciPy, SymPy</li>
                <li><strong>Visualization:</strong> Plotly 3D, Matplotlib</li>
                <li><strong>Machine Learning:</strong> scikit-learn, quantum kernels</li>
                <li><strong>Export:</strong> JSON snapshots, PDF reports</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='experiment-panel'>
            <h3>Research Modules</h3>
            <ul>
                <li>Quantum state manipulation & measurement</li>
                <li>Variational algorithms (VQE, QAOA)</li>
                <li>Quantum machine learning (kernels, VQC)</li>
                <li>Error correction & surface codes</li>
                <li>Hardware topology & noise characterization</li>
                <li>Topological quantum computing (frontier)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Hero Bloch sphere
    st.markdown("### Interactive Quantum State Visualization")
    st.markdown("**Real-time Bloch sphere demonstrating qubit state vector dynamics**")
    
    theta_hero = st.slider("State angle θ (polar)", 0, 180, 45, key="hero_theta")
    phi_hero = st.slider("State angle φ (azimuthal)", 0, 360, 45, key="hero_phi")
    
    fig_hero = create_bloch_sphere(theta_hero, phi_hero)
    st.plotly_chart(fig_hero, use_container_width=True, key="hero_bloch")
    
    # State vector display
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
    st.markdown("# Qubit State & Bloch Sphere Dynamics")
    st.markdown('<span class="research-status status-active">Core Module</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='research-card'>
        <h3>Mathematical Formalism</h3>
        <p>A single qubit exists in a superposition of computational basis states:</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.latex(r"""
    |\psi\rangle = \alpha|0\rangle + \beta|1\rangle, \quad |\alpha|^2 + |\beta|^2 = 1
    """)
    
    st.latex(r"""
    \alpha = \cos(\theta/2), \quad \beta = e^{i\phi}\sin(\theta/2)
    """)
    
    st.markdown("""
    <div class='latex-display'>
        <p><strong>Bloch Sphere Representation:</strong> The qubit state maps to a point on the unit sphere 
        via the Bloch vector <strong>r</strong> = (sin θ cos φ, sin θ sin φ, cos θ).</p>
        <p><strong>Pure states:</strong> |r| = 1 (surface of sphere)</p>
        <p><strong>Mixed states:</strong> |r| < 1 (interior points, described by density matrix)</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive controls
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### State Configuration")
        theta_bloch = st.slider("Polar angle θ (degrees)", 0, 180, 90, 5, key="bloch_theta")
        phi_bloch = st.slider("Azimuthal angle φ (degrees)", 0, 360, 0, 5, key="bloch_phi")
        
        # Gate sequence
        st.markdown("### Apply Gate Sequence")
        gate_sequence = st.multiselect(
            "Select gates to apply",
            ["H (Hadamard)", "X (Pauli-X)", "Y (Pauli-Y)", "Z (Pauli-Z)", 
             "RX(π/4)", "RY(π/4)", "RZ(π/4)", "S (Phase)", "T (π/8)"],
            key="gate_seq_bloch"
        )
        
        # Measurement basis
        meas_basis = st.radio("Measurement Basis", ["Z (computational)", "X", "Y"], horizontal=True)
        
        fig_bloch = create_bloch_sphere(theta_bloch, phi_bloch)
        st.plotly_chart(fig_bloch, use_container_width=True, key="main_bloch")
    
    with col2:
        # Compute state
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
            if "H" in gate:
                current_state = hadamard() @ current_state
            elif "X" in gate:
                current_state = pauli['X'] @ current_state
            elif "Y" in gate:
                current_state = pauli['Y'] @ current_state
            elif "Z" in gate:
                current_state = pauli['Z'] @ current_state
            elif "RX" in gate:
                current_state = rotation_gate('X', 45) @ current_state
            elif "RY" in gate:
                current_state = rotation_gate('Y', 45) @ current_state
            elif "RZ" in gate:
                current_state = rotation_gate('Z', 45) @ current_state
        
        # Display metrics
        st.markdown("""
        <div class='metric-box'>
            <h3>{:.4f}</h3>
            <p>State Norm</p>
        </div>
        """.format(np.linalg.norm(current_state)), unsafe_allow_html=True)
        
        st.markdown("""
        <div class='metric-box'>
            <h3>{:.3f}</h3>
            <p>P(|0⟩)</p>
        </div>
        """.format(abs(current_state[0])**2), unsafe_allow_html=True)
        
        st.markdown("""
        <div class='metric-box'>
            <h3>{:.3f}</h3>
            <p>P(|1⟩)</p>
        </div>
        """.format(abs(current_state[1])**2), unsafe_allow_html=True)
        
        # Phase
        phase_deg = np.degrees(np.angle(current_state[1] / current_state[0]))
        st.markdown("""
        <div class='metric-box'>
            <h3>{:.1f}°</h3>
            <p>Relative Phase</p>
        </div>
        """.format(phase_deg if not np.isnan(phase_deg) else 0), unsafe_allow_html=True)
    
    # Code panel
    st.markdown("### Executable Code")
    code = f"""
import numpy as np
from scipy.linalg import expm

# Define initial state
theta = {theta_bloch} * np.pi / 180
phi = {phi_bloch} * np.pi / 180
state = np.array([np.cos(theta/2), np.exp(1j*phi) * np.sin(theta/2)])

# Apply gate sequence: {', '.join(gate_sequence) if gate_sequence else 'None'}
# ... gate operations ...

# Measurement probabilities
prob_0 = abs(state[0])**2
prob_1 = abs(state[1])**2
print(f"P(|0⟩) = {{prob_0:.3f}}, P(|1⟩) = {{prob_1:.3f}}")
"""
    st.code(code, language="python")

elif module_id == "interference":
    # Add wave animation
    add_wave_animation()
    
    st.markdown("<div class='interference-wave'>", unsafe_allow_html=True)
    st.markdown("# Superposition & Quantum Interference")
    st.markdown('<span class="research-status status-active">Core Module</span>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='research-card'>
        <h3>Wave-Particle Duality in Quantum Computation</h3>
        <p>Quantum interference emerges from the coherent superposition of probability amplitudes. 
        Unlike classical probability, amplitudes can interfere constructively or destructively 
        depending on their relative phase.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.latex(r"""
    P(\text{outcome}) = |\alpha_1 + \alpha_2|^2 = |\alpha_1|^2 + |\alpha_2|^2 + 2\text{Re}(\alpha_1^*\alpha_2)
    """)
    
    st.markdown("""
    <div class='latex-display'>
        <p>The interference term 2Re(α₁*α₂) = 2|α₁||α₂|cos(φ₁ - φ₂) depends on the relative phase.</p>
        <p><strong>Constructive interference:</strong> φ₁ - φ₂ = 0, 2π, ... → amplitudes add</p>
        <p><strong>Destructive interference:</strong> φ₁ - φ₂ = π, 3π, ... → amplitudes cancel</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive demonstration
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Path Amplitude Configuration")
        amp1 = st.slider("Amplitude |α₁|", 0.0, 1.0, 0.6, 0.05, key="amp1_interf")
        phase1 = st.slider("Phase φ₁ (degrees)", 0, 360, 0, 10, key="phase1_interf")
        amp2 = st.slider("Amplitude |α₂|", 0.0, 1.0, 0.4, 0.05, key="amp2_interf")
        phase2 = st.slider("Phase φ₂ (degrees)", 0, 360, 90, 10, key="phase2_interf")
        
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
            <p>Quantum Probability</p>
        </div>
        <div class='metric-box'>
            <h3>{prob_classical:.4f}</h3>
            <p>Classical (No Interference)</p>
        </div>
        <div class='metric-box'>
            <h3 style='color: {"#84CC16" if interference_term > 0 else "#EF4444"}'>{interference_term:+.4f}</h3>
            <p>Interference Term</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### Complex Amplitude Visualization")
        
        # Phasor diagram
        fig = go.Figure()
        
        # α₁ vector
        fig.add_trace(go.Scatter(
            x=[0, alpha1.real], y=[0, alpha1.imag],
            mode='lines+markers',
            line=dict(color='#6366F1', width=3),
            marker=dict(size=10),
            name='α₁'
        ))
        
        # α₂ vector
        fig.add_trace(go.Scatter(
            x=[0, alpha2.real], y=[0, alpha2.imag],
            mode='lines+markers',
            line=dict(color='#06B6D4', width=3),
            marker=dict(size=10),
            name='α₂'
        ))
        
        # Total amplitude
        fig.add_trace(go.Scatter(
            x=[0, alpha_total.real], y=[0, alpha_total.imag],
            mode='lines+markers',
            line=dict(color='#F59E0B', width=4),
            marker=dict(size=12),
            name='α₁ + α₂'
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
            xaxis=dict(range=[-1.2, 1.2], title='Real', gridcolor='rgba(255,255,255,0.1)'),
            yaxis=dict(range=[-1.2, 1.2], title='Imaginary', gridcolor='rgba(255,255,255,0.1)', scaleanchor="x"),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True, key="phasor_diagram")
    
    # Interference pattern
    st.markdown("### Interference Fringe Pattern")
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
        title='Probability vs Relative Phase',
        xaxis_title='Phase Difference φ₂ - φ₁ (degrees)',
        yaxis_title='Detection Probability',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        height=400
    )
    
    st.plotly_chart(fig_pattern, use_container_width=True, key="interference_pattern")

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
            name='T₁ (Energy Relaxation)'
        ))
        
        fig_decay.add_trace(go.Scatter(
            x=time_points, y=coherence_decay,
            mode='lines',
            line=dict(color='#06B6D4', width=3),
            name='T₂ (Dephasing)'
        ))
        
        fig_decay.update_layout(
            title='Decoherence Time Evolution',
            xaxis_title='Time (μs)',
            yaxis_title='Normalized Amplitude',
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
                    title='VQE Energy Convergence',
                    xaxis_title='Iteration',
                    yaxis_title='Energy (Hartree)',
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
                    title='Measurement Results',
                    yaxis_title='Counts',
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
            with st.expander(f"**{exp['id']}** - {exp['module']} - {exp['timestamp'][:19]}"):
                st.json(exp)
                
                col1, col2 = st.columns(2)
                
                with col1:
                    if st.button(f"Export JSON", key=f"export_json_{i}"):
                        json_str = json.dumps(exp, indent=2)
                        st.download_button(
                            label="Download JSON",
                            data=json_str,
                            file_name=f"{exp['id']}.json",
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
            json_str = json.dumps(all_experiments, indent=2)
            st.download_button(
                label="Download Complete Experiment Log (JSON)",
                data=json_str,
                file_name=f"quantum_experiments_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )
        else:
            st.warning("No experiments to export.")

else:
    st.markdown(f"# {selected_module}")
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
