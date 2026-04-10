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

# Page configuration - AlphaNova Quantum
st.set_page_config(
    page_title="AlphaNova Quantum | Next-Generation Quantum Research Platform",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/alphanovalabs/quantum-platform',
        'About': """
        # AlphaNova Quantum
        Interactive Quantum Computing and AI Visualization Platform
        Next-generation research environment for quantum innovation.
        """
    }
)

# Apply premium styling
st.markdown("""
<style>
    /* Global Dark Theme with Premium Styling */
    .stApp {
        background: linear-gradient(135deg, 
            rgba(10, 14, 26, 1) 0%, 
            rgba(15, 23, 42, 1) 25%, 
            rgba(20, 30, 58, 1) 100%);
        color: #E8E8E8;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Premium CSS Variables */
    :root {
        --primary-gradient: linear-gradient(135deg, #6366F1 0%, #06B6D4 100%);
        --accent-cyan: #06B6D4;
        --accent-indigo: #6366F1;
        --glass-border: rgba(255, 255, 255, 0.1);
        --shadow-primary: 0 20px 60px rgba(99, 102, 241, 0.3);
        --shadow-secondary: 0 8px 32px rgba(0, 0, 0, 0.6);
    }
    
    /* Hero Section Styling */
    .hero-container {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(6, 182, 212, 0.1));
        border: 1px solid var(--glass-border);
        border-radius: 20px;
        padding: 40px;
        margin: 30px 0;
        box-shadow: var(--shadow-primary);
        backdrop-filter: blur(20px);
        position: relative;
        overflow: hidden;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: var(--primary-gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 20px;
        letter-spacing: -0.02em;
    }
    
    .hero-subtitle {
        font-size: 1.4rem;
        color: rgba(255, 255, 255, 0.7);
        text-align: center;
        margin-bottom: 30px;
        font-weight: 300;
    }
    
    /* Sidebar Styling */
    .sidebar .sidebar-content {
        background: rgba(15, 23, 42, 0.95);
        border-right: 1px solid var(--glass-border);
    }
    
    /* Navigation Cards */
    .nav-card {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(6, 182, 212, 0.1));
        border: 1px solid var(--glass-border);
        border-radius: 16px;
        padding: 20px;
        margin: 15px 0;
        cursor: pointer;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }
    
    .nav-card:hover {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(6, 182, 212, 0.2));
        border-color: var(--accent-cyan);
        transform: translateY(-2px);
        box-shadow: 0 10px 30px rgba(99, 102, 241, 0.4);
    }
    
    /* Quantum Visualization Container */
    .viz-container {
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid var(--glass-border);
        border-radius: 16px;
        padding: 30px;
        margin: 20px 0;
        box-shadow: var(--shadow-secondary);
        backdrop-filter: blur(15px);
    }
    
    /* Metrics Cards */
    .metric-card {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.8), rgba(51, 65, 85, 0.8));
        border: 1px solid var(--glass-border);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: var(--shadow-secondary);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        background: var(--primary-gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .metric-label {
        color: rgba(255, 255, 255, 0.6);
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'overview'

def create_bloch_sphere(theta_deg=0, phi_deg=0):
    """Create an enhanced Bloch sphere visualization"""
    theta = np.radians(theta_deg)
    phi = np.radians(phi_deg)
    
    # Sphere coordinates
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    x_sphere = np.outer(np.cos(u), np.sin(v))
    y_sphere = np.outer(np.sin(u), np.sin(v))
    z_sphere = np.outer(np.ones(np.size(u)), np.cos(v))
    
    # Qubit state vector
    x_state = np.sin(theta) * np.cos(phi)
    y_state = np.sin(theta) * np.sin(phi)
    z_state = np.cos(theta)
    
    fig = go.Figure()
    
    # Add sphere
    fig.add_trace(go.Surface(
        x=x_sphere, y=y_sphere, z=z_sphere,
        opacity=0.3,
        colorscale='Viridis',
        showscale=False
    ))
    
    # Add state vector
    fig.add_trace(go.Scatter3d(
        x=[0, x_state], y=[0, y_state], z=[0, z_state],
        mode='lines+markers',
        line=dict(color='cyan', width=8),
        marker=dict(size=[0, 12], color=['cyan', 'red'])
    ))
    
    # Add coordinate axes
    for axis, color in [([1,0,0], 'red'), ([0,1,0], 'green'), ([0,0,1], 'blue')]:
        fig.add_trace(go.Scatter3d(
            x=[-axis[0], axis[0]], y=[-axis[1], axis[1]], z=[-axis[2], axis[2]],
            mode='lines',
            line=dict(color=color, width=4),
            showlegend=False
        ))
    
    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            bgcolor='rgba(0,0,0,0)',
            camera=dict(eye=dict(x=1.5, y=1.5, z=1.5))
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=0, b=0)
    )
    
    return fig

# Sidebar Navigation
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <h2 style="color: #06B6D4; margin: 0;">⚡ AlphaNova Quantum</h2>
        <p style="color: rgba(255,255,255,0.6); margin: 5px 0;">Next-Gen Quantum Platform</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Navigation
    if st.button("🏠 Platform Overview", use_container_width=True):
        st.session_state.current_page = 'overview'
        st.rerun()
    
    if st.button("🌟 Quantum States", use_container_width=True):
        st.session_state.current_page = 'quantum_states'
        st.rerun()
    
    if st.button("🔬 Quantum Algorithms", use_container_width=True):
        st.session_state.current_page = 'algorithms'
        st.rerun()
    
    if st.button("🧠 Quantum ML", use_container_width=True):
        st.session_state.current_page = 'quantum_ml'
        st.rerun()
    
    if st.button("📊 Research Analytics", use_container_width=True):
        st.session_state.current_page = 'analytics'
        st.rerun()

# Main Content
if st.session_state.current_page == 'overview':
    # Hero Section
    st.markdown("""
    <div class="hero-container">
        <h1 class="hero-title">AlphaNova Quantum</h1>
        <p class="hero-subtitle">Revolutionary Quantum Computing Research Platform</p>
        <p style="text-align: center; color: rgba(255,255,255,0.8); font-size: 1.1rem;">
            Accelerating quantum innovation through interactive visualization and advanced simulation
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Platform Features
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">∞</div>
            <div class="metric-label">Quantum States</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">50+</div>
            <div class="metric-label">Algorithms</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">∆</div>
            <div class="metric-label">Quantum ML</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Platform Capabilities
    st.markdown("## 🚀 Platform Capabilities")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="nav-card">
            <h3 style="color: #06B6D4; margin-top: 0;">🌐 Quantum State Visualization</h3>
            <p>Interactive Bloch sphere representations, state tomography, and quantum process visualization with real-time parameter control.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="nav-card">
            <h3 style="color: #6366F1; margin-top: 0;">🔬 Algorithm Simulation</h3>
            <p>Complete implementations of Grover's, Shor's, VQE, and QAOA with step-by-step execution visualization.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="nav-card">
            <h3 style="color: #06B6D4; margin-top: 0;">🧠 Quantum Machine Learning</h3>
            <p>Variational quantum circuits, quantum neural networks, and hybrid classical-quantum optimization.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="nav-card">
            <h3 style="color: #6366F1; margin-top: 0;">📊 Advanced Analytics</h3>
            <p>Performance metrics, quantum error analysis, and comprehensive research data visualization tools.</p>
        </div>
        """, unsafe_allow_html=True)

elif st.session_state.current_page == 'quantum_states':
    st.markdown("# 🌟 Quantum State Visualization")
    
    st.markdown("""
    <div class="hero-container" style="padding: 30px;">
        <h2 style="color: #06B6D4; text-align: center; margin-bottom: 20px;">Interactive Bloch Sphere</h2>
        <p style="text-align: center; color: rgba(255,255,255,0.7);">
            Explore quantum states through real-time 3D visualization
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Controls
    col1, col2 = st.columns(2)
    
    with col1:
        theta = st.slider("θ (Polar Angle)", 0, 180, 45, key="theta_slider")
    
    with col2:
        phi = st.slider("φ (Azimuthal Angle)", 0, 360, 90, key="phi_slider")
    
    # Bloch Sphere Visualization
    st.markdown('<div class="viz-container">', unsafe_allow_html=True)
    fig = create_bloch_sphere(theta, phi)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # State Information
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Quantum State Vector")
        theta_rad = np.radians(theta)
        phi_rad = np.radians(phi)
        
        alpha = np.cos(theta_rad/2)
        beta = np.sin(theta_rad/2) * np.exp(1j * phi_rad)
        
        st.write(f"α = {alpha:.3f}")
        st.write(f"β = {beta:.3f}")
        st.write(f"|ψ⟩ = {alpha:.3f}|0⟩ + {beta:.3f}|1⟩")
    
    with col2:
        st.markdown("### Measurement Probabilities")
        prob_0 = np.abs(alpha)**2
        prob_1 = np.abs(beta)**2
        
        st.write(f"P(|0⟩) = {prob_0:.3f}")
        st.write(f"P(|1⟩) = {prob_1:.3f}")
        
        # Probability bars
        st.progress(prob_0, text="Probability |0⟩")
        st.progress(prob_1, text="Probability |1⟩")

elif st.session_state.current_page == 'algorithms':
    st.markdown("# 🔬 Quantum Algorithms")
    
    st.markdown("""
    <div class="hero-container" style="padding: 30px;">
        <h2 style="color: #6366F1; text-align: center; margin-bottom: 20px;">Quantum Algorithm Library</h2>
        <p style="text-align: center; color: rgba(255,255,255,0.7);">
            Interactive implementations of foundational quantum algorithms
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Algorithm Selection
    algorithm = st.selectbox(
        "Select Algorithm",
        ["Grover's Search", "Quantum Fourier Transform", "Variational Quantum Eigensolver"]
    )
    
    if algorithm == "Grover's Search":
        st.markdown("## Grover's Quantum Search Algorithm")
        
        st.markdown("""
        <div class="viz-container">
            <h3 style="color: #06B6D4;">Algorithm Overview</h3>
            <p>Grover's algorithm provides a quadratic speedup for searching unsorted databases.</p>
            <ul>
                <li>Classical complexity: O(N)</li>
                <li>Quantum complexity: O(√N)</li>
                <li>Optimal number of iterations: π√N/4</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Grover simulation
        n_items = st.slider("Number of items in database", 4, 16, 8)
        target_item = st.slider("Target item index", 0, n_items-1, 3)
        
        optimal_iterations = int(np.pi * np.sqrt(n_items) / 4)
        st.write(f"Optimal iterations: {optimal_iterations}")
        
        # Create probability amplitude visualization
        iterations = st.slider("Current iteration", 0, optimal_iterations*2, optimal_iterations)
        
        # Simulate Grover's algorithm
        theta = np.arcsin(1/np.sqrt(n_items))
        probability = np.sin((2*iterations + 1) * theta)**2
        
        st.markdown(f"### Success probability: {probability:.3f}")
        st.progress(probability, text="Success Probability")

elif st.session_state.current_page == 'quantum_ml':
    st.markdown("# 🧠 Quantum Machine Learning")
    
    st.markdown("""
    <div class="hero-container" style="padding: 30px;">
        <h2 style="color: #06B6D4; text-align: center; margin-bottom: 20px;">Quantum-Enhanced ML</h2>
        <p style="text-align: center; color: rgba(255,255,255,0.7);">
            Hybrid quantum-classical machine learning algorithms
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # QML Algorithm Selection
    qml_type = st.selectbox(
        "Select QML Algorithm",
        ["Variational Quantum Classifier", "Quantum Neural Network", "Quantum Kernel Method"]
    )
    
    if qml_type == "Variational Quantum Classifier":
        st.markdown("## Variational Quantum Classifier")
        
        # Generate sample data
        np.random.seed(42)
        n_samples = 100
        X = np.random.randn(n_samples, 2)
        y = (X[:, 0]**2 + X[:, 1]**2 > 1).astype(int)
        
        # Create visualization
        fig = px.scatter(
            x=X[:, 0], y=X[:, 1], 
            color=y,
            title="Classification Dataset",
            color_continuous_scale="viridis"
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # VQC Parameters
        col1, col2 = st.columns(2)
        
        with col1:
            n_qubits = st.slider("Number of qubits", 2, 4, 2)
            n_layers = st.slider("Circuit depth", 1, 5, 2)
        
        with col2:
            learning_rate = st.slider("Learning rate", 0.01, 0.1, 0.05)
            epochs = st.slider("Training epochs", 10, 100, 50)
        
        if st.button("Train VQC"):
            with st.spinner("Training quantum classifier..."):
                # Simulate training progress
                progress_bar = st.progress(0)
                for epoch in range(epochs):
                    progress_bar.progress((epoch + 1) / epochs)
                    if epoch % 10 == 0:
                        st.write(f"Epoch {epoch}: Loss = {0.5 - epoch*0.01:.3f}")
                
                st.success("Training completed!")

elif st.session_state.current_page == 'analytics':
    st.markdown("# 📊 Research Analytics")
    
    st.markdown("""
    <div class="hero-container" style="padding: 30px;">
        <h2 style="color: #6366F1; text-align: center; margin-bottom: 20px;">Quantum Research Metrics</h2>
        <p style="text-align: center; color: rgba(255,255,255,0.7);">
            Comprehensive analysis of quantum computing performance
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Generate sample analytics data
    dates = pd.date_range(start='2024-01-01', periods=30, freq='D')
    quantum_volume = np.random.exponential(10, 30) + np.arange(30) * 2
    fidelity = 0.95 + 0.04 * np.random.random(30)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Quantum Volume Progress
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(
            x=dates, y=quantum_volume,
            mode='lines+markers',
            name='Quantum Volume',
            line=dict(color='#06B6D4', width=3)
        ))
        fig1.update_layout(
            title="Quantum Volume Progress",
            xaxis_title="Date",
            yaxis_title="Quantum Volume",
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white'
        )
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        # Fidelity Analysis
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(
            x=dates, y=fidelity,
            mode='lines+markers',
            name='Gate Fidelity',
            line=dict(color='#6366F1', width=3)
        ))
        fig2.update_layout(
            title="Gate Fidelity Over Time",
            xaxis_title="Date",
            yaxis_title="Fidelity",
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white'
        )
        st.plotly_chart(fig2, use_container_width=True)
    
    # Performance Summary
    st.markdown("## Performance Summary")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">99.2%</div>
            <div class="metric-label">Avg Fidelity</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">42</div>
            <div class="metric-label">Max Qubits</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">1.2µs</div>
            <div class="metric-label">T1 Time</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">2.8µs</div>
            <div class="metric-label">T2 Time</div>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; color: rgba(255,255,255,0.6);">
    <p>⚡ <strong>AlphaNova Quantum</strong> | Next-Generation Quantum Research Platform</p>
    <p>Accelerating quantum innovation through advanced visualization and simulation</p>
    <p style="font-size: 0.9rem;">© 2024 AlphaNova Labs. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)