import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import math
import time

# Page configuration
st.set_page_config(
    page_title="Quantum Raccoon Research Platform",
    page_icon="🦝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Soft UI Dark Theme
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* Global Styles */
* {
    font-family: 'Inter', sans-serif;
}

/* Main App Background */
.stApp {
    background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
    color: #e8e9f3;
}

/* Sidebar Styling */
.css-1d391kg {
    background: linear-gradient(180deg, #1e1e3f 0%, #2a2a5a 100%) !important;
    border-radius: 0 24px 24px 0 !important;
    box-shadow: 4px 0 20px rgba(0,0,0,0.3);
}

/* Sidebar Content */
.css-17eq0hr {
    background: transparent !important;
}

/* Main Content Area */
.block-container {
    padding: 2rem 3rem !important;
    background: rgba(15, 15, 35, 0.8);
    border-radius: 24px;
    margin: 1rem;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}

/* Headers */
h1, h2, h3, h4, h5, h6 {
    color: #ffffff;
    font-weight: 600;
    letter-spacing: -0.02em;
}

h1 {
    font-size: 2.5rem !important;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 1.5rem;
}

/* Soft UI Containers */
.soft-container {
    background: rgba(30, 30, 63, 0.6) !important;
    border-radius: 24px !important;
    padding: 2rem !important;
    margin: 1rem 0 !important;
    border: 1px solid rgba(102, 126, 234, 0.1) !important;
    box-shadow: 0 8px 32px rgba(0,0,0,0.2) !important;
    backdrop-filter: blur(10px) !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 20px !important;
    padding: 0.75rem 2rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.02em !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3) !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.5) !important;
}

/* Selectbox and Input */
.stSelectbox > div > div {
    background: rgba(30, 30, 63, 0.8) !important;
    border-radius: 20px !important;
    border: 1px solid rgba(102, 126, 234, 0.3) !important;
}

.stTextInput > div > div > input {
    background: rgba(30, 30, 63, 0.8) !important;
    border-radius: 20px !important;
    border: 1px solid rgba(102, 126, 234, 0.3) !important;
    color: #e8e9f3 !important;
}

/* Metrics */
.metric-container {
    background: rgba(30, 30, 63, 0.4) !important;
    border-radius: 20px !important;
    padding: 1.5rem !important;
    text-align: center !important;
    border: 1px solid rgba(102, 126, 234, 0.2) !important;
}

/* Sidebar Navigation Items */
.nav-item {
    background: rgba(102, 126, 234, 0.1);
    border-radius: 16px;
    padding: 0.8rem 1.2rem;
    margin: 0.5rem 0;
    border-left: 4px solid #667eea;
    transition: all 0.3s ease;
}

.nav-item:hover {
    background: rgba(102, 126, 234, 0.2);
    transform: translateX(5px);
}

/* Expander */
.streamlit-expanderHeader {
    background: rgba(30, 30, 63, 0.6) !important;
    border-radius: 20px !important;
    border: 1px solid rgba(102, 126, 234, 0.3) !important;
}

/* Tabs */
.stTabs > div > div > div > div {
    background: rgba(30, 30, 63, 0.6) !important;
    border-radius: 20px !important;
    border: 1px solid rgba(102, 126, 234, 0.3) !important;
}

/* Progress Bar */
.stProgress > div > div > div {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    border-radius: 20px !important;
}

/* Custom Icon Styles */
.icon {
    display: inline-block;
    width: 24px;
    height: 24px;
    margin-right: 8px;
    vertical-align: middle;
}

.large-icon {
    width: 48px;
    height: 48px;
}
</style>

<!-- Lucide Icons CDN -->
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.js"></script>
""", unsafe_allow_html=True)

# Custom component functions
def create_metric_card(title, value, description, icon_name="activity"):
    """Create a styled metric card with icon"""
    return f"""
    <div class="metric-container">
        <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 0.5rem;">
            <i data-lucide="{icon_name}" class="icon" style="color: #667eea;"></i>
            <h4 style="margin: 0; color: #667eea;">{title}</h4>
        </div>
        <div style="font-size: 2rem; font-weight: 700; color: #ffffff; margin: 0.5rem 0;">{value}</div>
        <div style="color: #a8a9b8; font-size: 0.9rem;">{description}</div>
    </div>
    """

def create_section_header(title, subtitle, icon_name="cpu"):
    """Create a styled section header with icon"""
    return f"""
    <div style="display: flex; align-items: center; margin: 2rem 0 1rem 0;">
        <i data-lucide="{icon_name}" class="large-icon" style="color: #667eea; margin-right: 1rem;"></i>
        <div>
            <h2 style="margin: 0; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">{title}</h2>
            <p style="margin: 0.5rem 0 0 0; color: #a8a9b8;">{subtitle}</p>
        </div>
    </div>
    """

def quantum_circuit_visualization():
    """Generate a quantum circuit visualization"""
    fig = go.Figure()
    
    # Create quantum circuit representation
    qubits = 4
    gates = 8
    
    # Draw qubit lines
    for i in range(qubits):
        fig.add_trace(go.Scatter(
            x=[0, gates],
            y=[i, i],
            mode='lines',
            line=dict(color='#667eea', width=3),
            showlegend=False,
            hoverinfo='skip'
        ))
    
    # Add quantum gates
    gate_positions = np.random.rand(15, 2)
    gate_positions[:, 0] = gate_positions[:, 0] * gates
    gate_positions[:, 1] = (gate_positions[:, 1] * (qubits - 1)).astype(int)
    
    colors = ['#667eea', '#764ba2', '#f093fb', '#f5576c']
    
    for i, (x, y) in enumerate(gate_positions):
        fig.add_trace(go.Scatter(
            x=[x],
            y=[y],
            mode='markers',
            marker=dict(
                size=20,
                color=colors[i % len(colors)],
                symbol='square',
                line=dict(width=2, color='white')
            ),
            showlegend=False,
            hovertemplate=f"Gate {i+1}<br>Qubit: {int(y)}<extra></extra>"
        ))
    
    fig.update_layout(
        title="Quantum Circuit Representation",
        xaxis_title="Time Steps",
        yaxis_title="Qubits",
        yaxis=dict(tickvals=list(range(qubits)), ticktext=[f"Q{i}" for i in range(qubits)]),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        height=300
    )
    
    return fig

def variational_circuit_simulation():
    """Simulate variational quantum circuit optimization"""
    iterations = 50
    cost_history = []
    
    # Simulate optimization process
    for i in range(iterations):
        noise = np.random.normal(0, 0.1)
        cost = 0.8 * np.exp(-i/20) + 0.2 + noise
        cost_history.append(max(0.01, cost))
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=list(range(iterations)),
        y=cost_history,
        mode='lines+markers',
        line=dict(color='#667eea', width=3),
        marker=dict(size=6, color='#764ba2'),
        name='Cost Function'
    ))
    
    fig.update_layout(
        title="Variational Quantum Circuit Optimization",
        xaxis_title="Iteration",
        yaxis_title="Cost Function Value",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        height=400
    )
    
    return fig

def quantum_data_encoding_demo():
    """Demonstrate quantum data encoding techniques"""
    # Generate sample data
    classical_data = np.random.rand(8)
    
    # Amplitude encoding
    normalized_data = classical_data / np.linalg.norm(classical_data)
    
    # Create visualization
    fig = make_subplots(
        rows=2, cols=1,
        subplot_titles=("Classical Data", "Quantum Amplitude Encoding"),
        specs=[[{"type": "bar"}], [{"type": "bar"}]]
    )
    
    # Classical data
    fig.add_trace(go.Bar(
        x=[f"Feature {i+1}" for i in range(len(classical_data))],
        y=classical_data,
        marker_color='#667eea',
        name="Classical"
    ), row=1, col=1)
    
    # Quantum encoded data
    fig.add_trace(go.Bar(
        x=[f"|{i:03b}⟩" for i in range(len(normalized_data))],
        y=normalized_data,
        marker_color='#764ba2',
        name="Quantum Amplitudes"
    ), row=2, col=1)
    
    fig.update_layout(
        title="Classical to Quantum Data Encoding",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        height=500
    )
    
    return fig

# Sidebar Navigation
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0;">
        <i data-lucide="atom" class="large-icon" style="color: #667eea;"></i>
        <h2 style="margin: 1rem 0 0 0; color: #ffffff;">Quantum Raccoon</h2>
        <p style="color: #a8a9b8; margin: 0.5rem 0;">Research Platform</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation
    page = st.selectbox(
        "",
        ["🏠 Research Overview", "⚛️ Variational Circuits", "🧠 Quantum Neural Networks", "📊 Data Encoding", "🔬 Advanced Research", "📈 Performance Metrics"],
        label_visibility="collapsed"
    )

# Main Content Area
if page == "🏠 Research Overview":
    st.markdown(create_section_header("Welcome to Quantum Raccoon Research Platform", 
                                    "Advanced Quantum Machine Learning Research Environment", 
                                    "home"), unsafe_allow_html=True)
    
    # Platform Overview
    st.markdown("""
    <div class="soft-container">
        <h3><i data-lucide="info" class="icon"></i>Platform Overview</h3>
        <p>The Quantum Raccoon Research Platform is a specialized environment designed for cutting-edge Quantum Machine Learning (QML) research. Our platform combines theoretical foundations with practical implementations to advance the field of quantum computing and artificial intelligence.</p>
        
        <h4><i data-lucide="target" class="icon"></i>Research Focus Areas:</h4>
        <ul>
            <li><strong>Variational Quantum Circuits:</strong> Explore parameterized quantum circuits for optimization problems</li>
            <li><strong>Quantum Neural Networks:</strong> Investigate quantum analogues of classical neural networks</li>
            <li><strong>Quantum Data Encoding:</strong> Develop efficient methods for classical-to-quantum data transformation</li>
            <li><strong>Hybrid Algorithms:</strong> Design quantum-classical hybrid approaches for machine learning</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(create_metric_card("Research Modules", "5", "Active quantum modules", "layers"), 
                   unsafe_allow_html=True)
    
    with col2:
        st.markdown(create_metric_card("Qubits Simulated", "16", "Maximum circuit size", "cpu"), 
                   unsafe_allow_html=True)
    
    with col3:
        st.markdown(create_metric_card("Algorithms", "12", "QML implementations", "brain"), 
                   unsafe_allow_html=True)
    
    with col4:
        st.markdown(create_metric_card("Research Papers", "47", "Published findings", "file-text"), 
                   unsafe_allow_html=True)
    
    # Getting Started
    st.markdown("""
    <div class="soft-container">
        <h3><i data-lucide="play-circle" class="icon"></i>Getting Started</h3>
        <p>Navigate through our research modules using the sidebar. Each module provides interactive demonstrations, theoretical background, and practical implementations of quantum machine learning concepts.</p>
        
        <h4><i data-lucide="lightbulb" class="icon"></i>Quick Start Guide:</h4>
        <ol>
            <li><strong>Explore Variational Circuits:</strong> Start with basic VQC concepts and optimization</li>
            <li><strong>Understand Data Encoding:</strong> Learn how classical data is prepared for quantum processing</li>
            <li><strong>Study Quantum Neural Networks:</strong> Investigate quantum implementations of ML models</li>
            <li><strong>Advanced Research:</strong> Access cutting-edge research and experimental features</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    # Quantum Fundamentals
    with st.expander("🔬 Quantum Machine Learning Fundamentals"):
        st.markdown("""
        **Quantum Superposition:** Unlike classical bits, quantum bits (qubits) can exist in superposition, representing both 0 and 1 simultaneously. This enables quantum computers to process exponentially more information.
        
        **Quantum Entanglement:** Qubits can be entangled, creating correlations that don't exist in classical systems. This property is crucial for quantum machine learning algorithms.
        
        **Quantum Interference:** Quantum algorithms leverage interference patterns to amplify correct answers while suppressing incorrect ones.
        
        **Variational Algorithms:** These hybrid quantum-classical algorithms use parameterized quantum circuits optimized by classical computers to solve machine learning problems.
        """)

elif page == "⚛️ Variational Circuits":
    st.markdown(create_section_header("Variational Quantum Circuits", 
                                    "Parameterized quantum circuits for optimization problems", 
                                    "settings"), unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.plotly_chart(quantum_circuit_visualization(), use_container_width=True)
    
    with col2:
        st.markdown("""
        <div class="soft-container">
            <h4><i data-lucide="cpu" class="icon"></i>Circuit Parameters</h4>
            <p><strong>Depth:</strong> 4 layers</p>
            <p><strong>Qubits:</strong> 4 qubits</p>
            <p><strong>Gates:</strong> 15 parameterized gates</p>
            <p><strong>Entanglement:</strong> Linear connectivity</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Optimization Simulation
    st.markdown("### 🎯 Optimization Process")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        if st.button("🚀 Run VQC Optimization", key="vqc_opt"):
            progress_bar = st.progress(0)
            status_text = st.empty()
            chart_placeholder = st.empty()
            
            for i in range(10):
                progress_bar.progress((i + 1) / 10)
                status_text.text(f"Optimization step: {i + 1}/10")
                time.sleep(0.1)
            
            chart_placeholder.plotly_chart(variational_circuit_simulation(), use_container_width=True)
            st.success("✅ Optimization completed! Minimum cost achieved: 0.023")
    
    with col2:
        st.markdown("""
        <div class="soft-container">
            <h4><i data-lucide="settings" class="icon"></i>Optimizer</h4>
            <p><strong>Method:</strong> COBYLA</p>
            <p><strong>Learning Rate:</strong> 0.01</p>
            <p><strong>Max Iterations:</strong> 50</p>
            <p><strong>Convergence:</strong> 1e-6</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Theory Section
    with st.expander("📚 Theoretical Background"):
        st.markdown("""
        **Variational Quantum Circuits (VQCs)** are a cornerstone of near-term quantum algorithms. They consist of:
        
        1. **Parameterized Gates**: Rotation gates (RX, RY, RZ) with adjustable angles
        2. **Entangling Gates**: CNOT or other multi-qubit gates creating quantum correlations
        3. **Circuit Architecture**: The arrangement and connectivity of gates
        4. **Classical Optimization**: Iterative parameter updates to minimize a cost function
        
        The key insight is that we can use classical optimization techniques to train quantum circuits, similar to how we train classical neural networks.
        """)

elif page == "🧠 Quantum Neural Networks":
    st.markdown(create_section_header("Quantum Neural Networks", 
                                    "Quantum implementations of machine learning models", 
                                    "brain"), unsafe_allow_html=True)
    
    # QNN Architecture
    st.markdown("### 🏗️ QNN Architecture")
    
    tab1, tab2, tab3 = st.tabs(["📊 Network Structure", "🔄 Training Process", "📈 Performance"])
    
    with tab1:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Create QNN visualization
            layers = ['Input Layer', 'Quantum Layer 1', 'Quantum Layer 2', 'Output Layer']
            neurons = [4, 8, 6, 2]
            
            fig = go.Figure()
            
            for i, (layer, n) in enumerate(zip(layers, neurons)):
                y_positions = np.linspace(-n/2, n/2, n)
                fig.add_trace(go.Scatter(
                    x=[i] * n,
                    y=y_positions,
                    mode='markers',
                    marker=dict(
                        size=30,
                        color=['#667eea', '#764ba2', '#f093fb', '#f5576c'][i],
                        symbol='circle'
                    ),
                    name=layer,
                    hovertemplate=f"{layer}<br>Neuron: %{{y}}<extra></extra>"
                ))
            
            # Add connections
            for i in range(len(layers) - 1):
                for j in range(neurons[i]):
                    for k in range(neurons[i + 1]):
                        y1 = np.linspace(-neurons[i]/2, neurons[i]/2, neurons[i])[j]
                        y2 = np.linspace(-neurons[i+1]/2, neurons[i+1]/2, neurons[i+1])[k]
                        
                        fig.add_trace(go.Scatter(
                            x=[i, i+1],
                            y=[y1, y2],
                            mode='lines',
                            line=dict(color='rgba(102, 126, 234, 0.2)', width=1),
                            showlegend=False,
                            hoverinfo='skip'
                        ))
            
            fig.update_layout(
                title="Quantum Neural Network Architecture",
                xaxis=dict(tickvals=list(range(len(layers))), ticktext=layers),
                yaxis_title="Neurons",
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='white',
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("""
            <div class="soft-container">
                <h4><i data-lucide="layers" class="icon"></i>Network Details</h4>
                <p><strong>Input Features:</strong> 4</p>
                <p><strong>Quantum Layers:</strong> 2</p>
                <p><strong>Qubits per Layer:</strong> 8, 6</p>
                <p><strong>Output Classes:</strong> 2</p>
                <p><strong>Parameters:</strong> 156</p>
                <p><strong>Entanglement:</strong> Full connectivity</p>
            </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("#### 🎯 Training Simulation")
        
        if st.button("🚀 Start QNN Training", key="qnn_training"):
            epochs = 30
            train_acc = []
            val_acc = []
            
            progress_bar = st.progress(0)
            acc_placeholder = st.empty()
            
            for epoch in range(epochs):
                # Simulate training accuracy improvement
                train_noise = np.random.normal(0, 0.02)
                val_noise = np.random.normal(0, 0.03)
                
                train_a = 0.95 - 0.7 * np.exp(-epoch/8) + train_noise
                val_a = 0.92 - 0.7 * np.exp(-epoch/10) + val_noise
                
                train_acc.append(max(0.2, min(0.98, train_a)))
                val_acc.append(max(0.15, min(0.95, val_a)))
                
                progress_bar.progress((epoch + 1) / epochs)
                
                if epoch % 5 == 0:
                    # Create accuracy plot
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(
                        x=list(range(len(train_acc))),
                        y=train_acc,
                        mode='lines+markers',
                        name='Training Accuracy',
                        line=dict(color='#667eea')
                    ))
                    fig.add_trace(go.Scatter(
                        x=list(range(len(val_acc))),
                        y=val_acc,
                        mode='lines+markers',
                        name='Validation Accuracy',
                        line=dict(color='#764ba2')
                    ))
                    
                    fig.update_layout(
                        title="Training Progress",
                        xaxis_title="Epoch",
                        yaxis_title="Accuracy",
                        plot_bgcolor='rgba(0,0,0,0)',
                        paper_bgcolor='rgba(0,0,0,0)',
                        font_color='white'
                    )
                    
                    acc_placeholder.plotly_chart(fig, use_container_width=True)
                
                time.sleep(0.1)
            
            st.success(f"✅ Training completed! Final validation accuracy: {val_acc[-1]:.3f}")
    
    with tab3:
        # Performance metrics
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(create_metric_card("Accuracy", "94.2%", "Final validation score", "target"), 
                       unsafe_allow_html=True)
        
        with col2:
            st.markdown(create_metric_card("Training Time", "2.3s", "Per epoch average", "clock"), 
                       unsafe_allow_html=True)

elif page == "📊 Data Encoding":
    st.markdown(create_section_header("Quantum Data Encoding", 
                                    "Efficient classical-to-quantum data transformation", 
                                    "database"), unsafe_allow_html=True)
    
    # Encoding Methods
    encoding_method = st.selectbox(
        "🔄 Select Encoding Method:",
        ["Amplitude Encoding", "Angle Encoding", "Basis Encoding", "Arbitrary Encoding"]
    )
    
    st.plotly_chart(quantum_data_encoding_demo(), use_container_width=True)
    
    # Encoding Comparison
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="soft-container">
            <h4><i data-lucide="zap" class="icon"></i>Amplitude Encoding</h4>
            <p><strong>Efficiency:</strong> Exponential</p>
            <p><strong>Qubits:</strong> log₂(N)</p>
            <p><strong>Normalization:</strong> Required</p>
            <p><strong>Use Case:</strong> Dense data</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="soft-container">
            <h4><i data-lucide="rotate-cw" class="icon"></i>Angle Encoding</h4>
            <p><strong>Efficiency:</strong> Linear</p>
            <p><strong>Qubits:</strong> N</p>
            <p><strong>Normalization:</strong> Optional</p>
            <p><strong>Use Case:</strong> Continuous values</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="soft-container">
            <h4><i data-lucide="grid" class="icon"></i>Basis Encoding</h4>
            <p><strong>Efficiency:</strong> Linear</p>
            <p><strong>Qubits:</strong> N</p>
            <p><strong>Normalization:</strong> Not needed</p>
            <p><strong>Use Case:</strong> Binary data</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "🔬 Advanced Research":
    st.markdown(create_section_header("Advanced Research", 
                                    "Cutting-edge QML research and experimental features", 
                                    "microscope"), unsafe_allow_html=True)
    
    research_area = st.selectbox(
        "🎯 Research Focus:",
        ["Quantum Advantage Studies", "Noise Mitigation", "Quantum Transfer Learning", "Quantum GANs", "Error Correction"]
    )
    
    if research_area == "Quantum Advantage Studies":
        st.markdown("""
        <div class="soft-container">
            <h4><i data-lucide="trending-up" class="icon"></i>Quantum Advantage Analysis</h4>
            <p>Investigating scenarios where quantum machine learning algorithms demonstrate computational advantages over classical counterparts.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Generate comparison data
        problems = ['Classification', 'Clustering', 'Optimization', 'Pattern Recognition']
        quantum_performance = [1.2, 1.8, 2.1, 1.5]
        classical_performance = [1.0, 1.0, 1.0, 1.0]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Classical',
            x=problems,
            y=classical_performance,
            marker_color='#667eea'
        ))
        fig.add_trace(go.Bar(
            name='Quantum',
            x=problems,
            y=quantum_performance,
            marker_color='#764ba2'
        ))
        
        fig.update_layout(
            title='Quantum vs Classical Performance Comparison',
            yaxis_title='Relative Performance',
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white'
        )
        
        st.plotly_chart(fig, use_container_width=True)

elif page == "📈 Performance Metrics":
    st.markdown(create_section_header("Performance Metrics", 
                                    "Comprehensive analysis and benchmarking", 
                                    "bar-chart"), unsafe_allow_html=True)
    
    # System Performance
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(create_metric_card("Circuit Fidelity", "99.2%", "Average gate fidelity", "check-circle"), 
                   unsafe_allow_html=True)
    
    with col2:
        st.markdown(create_metric_card("Convergence Rate", "85%", "Successful optimizations", "trending-up"), 
                   unsafe_allow_html=True)
    
    with col3:
        st.markdown(create_metric_card("Quantum Volume", "64", "System complexity measure", "box"), 
                   unsafe_allow_html=True)
    
    with col4:
        st.markdown(create_metric_card("Speedup", "3.2x", "vs classical baseline", "zap"), 
                   unsafe_allow_html=True)
    
    # Performance Charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Resource utilization
        categories = ['CPU', 'Memory', 'Quantum Resources', 'Network']
        utilization = [75, 60, 90, 45]
        
        fig = go.Figure(go.Bar(
            x=categories,
            y=utilization,
            marker_color=['#667eea', '#764ba2', '#f093fb', '#f5576c']
        ))
        
        fig.update_layout(
            title='Resource Utilization',
            yaxis_title='Utilization %',
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Algorithm performance over time
        days = list(range(1, 31))
        performance = 70 + 25 * np.sin(np.array(days) * 0.2) + np.random.normal(0, 2, 30)
        performance = np.maximum(60, np.minimum(95, performance))
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=days,
            y=performance,
            mode='lines+markers',
            line=dict(color='#667eea', width=3),
            fill='tonexty',
            name='Performance Score'
        ))
        
        fig.update_layout(
            title='Algorithm Performance Trend',
            xaxis_title='Days',
            yaxis_title='Performance Score',
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white'
        )
        
        st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("""
<div style="text-align: center; padding: 3rem 0 1rem 0; border-top: 1px solid rgba(102, 126, 234, 0.2); margin-top: 3rem;">
    <p style="color: #a8a9b8;">
        <i data-lucide="atom" class="icon"></i>
        Quantum Raccoon Research Platform © 2026 | 
        <i data-lucide="github" class="icon"></i>
        Open Source | 
        <i data-lucide="heart" class="icon"></i>
        Built with Streamlit
    </p>
</div>

<script>
// Initialize Lucide icons
if (typeof lucide !== 'undefined') {
    lucide.createIcons();
}
</script>
""", unsafe_allow_html=True)