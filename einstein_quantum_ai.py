import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from scipy import stats
import pandas as pd
import time

# Page configuration
st.set_page_config(
    page_title="Einstein & Quantum AI Lab",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: white;
    }
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-size: 18px;
        padding: 12px 28px;
        border-radius: 10px;
        border: none;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    .quantum-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        color: white;
    }
    h1, h2, h3 {
        color: #00d4ff !important;
    }
    .equation {
        background: rgba(0, 212, 255, 0.1);
        padding: 15px;
        border-left: 4px solid #00d4ff;
        border-radius: 8px;
        font-family: 'Courier New', monospace;
        font-size: 18px;
        margin: 15px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; font-size: 50px;'>🌌 Einstein's Quantum Universe & AI Lab 🧠</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #667eea;'>Advanced Quantum Physics & Quantum AI Exploration</h3>", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("## 🎯 Navigation")
page = st.sidebar.selectbox(
    "Select Module:",
    ["🏠 Overview", "💡 Photoelectric Effect", "🔗 Quantum Entanglement (EPR)", 
     "🌊 Wave-Particle Duality", "🧮 Quantum Computing Basics", "🤖 Quantum AI Algorithms",
     "🔬 Quantum Machine Learning", "🎮 Interactive Simulations"]
)

# ===== OVERVIEW PAGE =====
if page == "🏠 Overview":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class='quantum-card'>
        <h2>👨‍🔬 Albert Einstein: The Revolutionary</h2>
        <p style='font-size: 18px; line-height: 1.8;'>
        Albert Einstein (1879-1955) revolutionized our understanding of physics and laid crucial groundwork 
        for quantum mechanics, despite his famous skepticism about quantum theory's completeness.
        </p>
        <h3>Key Contributions to Quantum Physics:</h3>
        <ul style='font-size: 16px; line-height: 2;'>
            <li><b>Photoelectric Effect (1905):</b> Demonstrated light behaves as particles (photons)</li>
            <li><b>EPR Paradox (1935):</b> Questioned quantum entanglement and non-locality</li>
            <li><b>Wave-Particle Duality:</b> Confirmed de Broglie's matter waves</li>
            <li><b>Stimulated Emission:</b> Foundation for lasers and quantum optics</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='quantum-card' style='text-align: center;'>
            <div style='font-size: 120px;'>👨‍🔬</div>
            <h3>Albert Einstein</h3>
            <p style='font-size: 16px;'>
            "God does not play dice<br>with the universe"<br>
            <i>- Einstein's famous quote about quantum randomness</i>
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Timeline
    st.markdown("### 📅 Quantum Physics Timeline")
    
    timeline_data = {
        'Year': [1900, 1905, 1913, 1924, 1927, 1935, 1964, 1994, 2019],
        'Event': [
            'Planck: Quantum hypothesis',
            'Einstein: Photoelectric effect',
            'Bohr: Atomic model',
            'de Broglie: Matter waves',
            'Heisenberg: Uncertainty principle',
            'Einstein-Podolsky-Rosen paradox',
            "Bell's theorem",
            "Shor's quantum algorithm",
            'Google: Quantum supremacy'
        ],
        'Impact': [10, 10, 9, 8, 10, 9, 10, 9, 10]
    }
    
    df = pd.DataFrame(timeline_data)
    
    fig = px.scatter(df, x='Year', y='Impact', text='Event', size='Impact',
                     color='Impact', color_continuous_scale='plasma',
                     title='Major Quantum Physics Milestones')
    fig.update_traces(textposition='top center', textfont_size=10)
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        showlegend=False,
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Quantum vs Classical
    st.markdown("### ⚔️ Classical vs Quantum Paradigms")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='quantum-card'>
        <h3>🏛️ Classical Physics (Einstein's Comfort Zone)</h3>
        <ul style='font-size: 16px;'>
            <li>Deterministic: Future is predictable</li>
            <li>Local realism: Objects have properties independent of measurement</li>
            <li>Continuous energy and states</li>
            <li>No spooky action at a distance</li>
            <li>Wave OR particle behavior</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='quantum-card'>
        <h3>⚛️ Quantum Physics (The Reality)</h3>
        <ul style='font-size: 16px;'>
            <li>Probabilistic: Only probabilities are certain</li>
            <li>Measurement affects reality</li>
            <li>Quantized energy levels</li>
            <li>Non-local entanglement</li>
            <li>Wave AND particle behavior simultaneously</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# ===== PHOTOELECTRIC EFFECT =====
elif page == "💡 Photoelectric Effect":
    st.markdown("## 💡 The Photoelectric Effect: Einstein's Nobel Prize Work")
    
    st.markdown("""
    <div class='quantum-card'>
    <h3>🎯 The Breakthrough</h3>
    <p style='font-size: 18px;'>
    In 1905, Einstein explained why light can knock electrons out of metal. This proved light 
    consists of particles (photons) with energy E = hν, revolutionizing physics and earning him 
    the 1921 Nobel Prize.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Theory
    st.markdown("### 📐 The Mathematics")
    
    st.markdown("""
    <div class='equation'>
    <b>Einstein's Photoelectric Equation:</b><br><br>
    E<sub>kinetic</sub> = hν - φ<br><br>
    where:<br>
    • E<sub>kinetic</sub> = kinetic energy of ejected electron<br>
    • h = Planck's constant (6.626 × 10⁻³⁴ J·s)<br>
    • ν = frequency of incident light<br>
    • φ = work function (minimum energy to eject electron)
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive simulation
    st.markdown("### 🎮 Interactive Photoelectric Simulator")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### 🎛️ Control Panel")
        
        frequency = st.slider(
            "Light Frequency (×10¹⁴ Hz)", 
            3.0, 12.0, 7.0, 0.5,
            help="Adjust the frequency of incident light"
        )
        
        work_function = st.slider(
            "Work Function φ (eV)", 
            1.0, 5.0, 2.5, 0.5,
            help="Material's work function"
        )
        
        intensity = st.slider(
            "Light Intensity", 
            1, 10, 5, 1,
            help="Number of photons"
        )
    
    with col2:
        # Calculate
        h = 6.626e-34  # Planck's constant
        freq_hz = frequency * 1e14
        photon_energy_J = h * freq_hz
        photon_energy_eV = photon_energy_J / 1.602e-19
        
        kinetic_energy = photon_energy_eV - work_function
        
        # Visualization
        fig = go.Figure()
        
        # Energy levels
        fig.add_shape(type="line", x0=0, x1=10, y0=0, y1=0,
                     line=dict(color="gray", width=3),
                     name="Fermi Level")
        
        fig.add_shape(type="line", x0=0, x1=10, y0=work_function, y1=work_function,
                     line=dict(color="red", width=3, dash="dash"),
                     name="Vacuum Level")
        
        # Photons
        for i in range(min(intensity, 5)):
            x_pos = 2 + i * 1.5
            fig.add_annotation(
                x=x_pos, y=photon_energy_eV,
                text="📡", font=dict(size=30),
                showarrow=True, arrowhead=2, arrowsize=1,
                arrowcolor="yellow", ax=0, ay=-50
            )
        
        # Electrons if energy sufficient
        if kinetic_energy > 0:
            for i in range(min(intensity, 5)):
                x_pos = 2 + i * 1.5
                fig.add_annotation(
                    x=x_pos, y=work_function + kinetic_energy,
                    text="⚡", font=dict(size=25),
                    showarrow=True, arrowhead=2, arrowsize=1,
                    arrowcolor="cyan", ax=0, ay=50
                )
        
        fig.update_layout(
            title="Photoelectric Effect Visualization",
            xaxis_title="Position",
            yaxis_title="Energy (eV)",
            plot_bgcolor='rgba(20,20,50,0.9)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            height=500,
            yaxis=dict(range=[-1, max(photon_energy_eV, work_function) + 2])
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Results
    st.markdown("### 📊 Results")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class='metric-card'>
        <h3>Photon Energy</h3>
        <h2>{photon_energy_eV:.2f} eV</h2>
        <p>E = hν</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='metric-card'>
        <h3>Work Function</h3>
        <h2>{work_function:.2f} eV</h2>
        <p>φ (Material property)</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        if kinetic_energy > 0:
            st.markdown(f"""
            <div class='metric-card' style='background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);'>
            <h3>Kinetic Energy</h3>
            <h2>{kinetic_energy:.2f} eV</h2>
            <p>✅ Electrons Ejected!</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class='metric-card' style='background: linear-gradient(135deg, #ee0979 0%, #ff6a00 100%);'>
            <h3>Kinetic Energy</h3>
            <h2>{kinetic_energy:.2f} eV</h2>
            <p>❌ No Emission</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Key insights
    st.markdown("""
    <div class='quantum-card'>
    <h3>🔑 Key Insights</h3>
    <ul style='font-size: 16px;'>
        <li><b>Threshold Frequency:</b> Below certain frequency, no electrons are emitted regardless of intensity</li>
        <li><b>Instantaneous Emission:</b> Electrons are emitted immediately when hν > φ</li>
        <li><b>Intensity Effect:</b> Higher intensity means more photons, thus more electrons (but same KE)</li>
        <li><b>Quantum Nature:</b> This proved light consists of discrete energy packets (photons)</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ===== QUANTUM ENTANGLEMENT =====
elif page == "🔗 Quantum Entanglement (EPR)":
    st.markdown("## 🔗 The EPR Paradox: Einstein's Quantum Challenge")
    
    st.markdown("""
    <div class='quantum-card'>
    <h3>👻 "Spooky Action at a Distance"</h3>
    <p style='font-size: 18px;'>
    In 1935, Einstein, Podolsky, and Rosen published a thought experiment challenging quantum mechanics' 
    completeness. They argued that quantum entanglement implied either: (1) information travels faster 
    than light, or (2) quantum mechanics is incomplete. This led to profound questions about reality itself.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Bell's Inequality
    st.markdown("### 📊 Bell's Theorem: Testing Reality")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='quantum-card'>
        <h3>🎲 Einstein's View (Local Realism)</h3>
        <p style='font-size: 16px;'>
        Particles have predetermined properties ("hidden variables") that determine 
        measurement outcomes. No faster-than-light communication.
        </p>
        <div class='equation'>
        Bell's Inequality:<br>
        |C(a,b) - C(a,c)| ≤ 1 + C(b,c)
        </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='quantum-card'>
        <h3>⚛️ Quantum Mechanics View</h3>
        <p style='font-size: 16px;'>
        Particles exist in superposition until measured. Entangled particles 
        instantaneously affect each other regardless of distance.
        </p>
        <div class='equation'>
        Quantum Prediction:<br>
        Violates Bell's Inequality!<br>
        Experiments prove QM correct
        </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Interactive Entanglement Simulator
    st.markdown("### 🎮 Entanglement Simulator")
    
    if st.button("🌀 Create Entangled Pair"):
        st.markdown("#### Creating Entangled Photon Pair...")
        
        # Animation
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            st.markdown("""
            <div class='quantum-card' style='text-align: center;'>
            <h4>Photon A</h4>
            <div style='font-size: 80px;'>📡</div>
            <p>Spin: Superposition</p>
            <div style='font-size: 30px;'>|↑⟩ + |↓⟩</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class='quantum-card' style='text-align: center;'>
            <h4>Entanglement Source</h4>
            <div style='font-size: 80px;'>⚛️</div>
            <p>Creating pair...</p>
            <div style='font-size: 30px;'>🔗</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class='quantum-card' style='text-align: center;'>
            <h4>Photon B</h4>
            <div style='font-size: 80px;'>📡</div>
            <p>Spin: Superposition</p>
            <div style='font-size: 30px;'>|↑⟩ + |↓⟩</div>
            </div>
            """, unsafe_allow_html=True)
        
        time.sleep(1)
        
        # Measure
        if st.button("🔬 Measure Photon A"):
            measurement_a = np.random.choice(['↑', '↓'])
            measurement_b = '↓' if measurement_a == '↑' else '↑'
            
            st.success(f"📡 Photon A measured: **{measurement_a}**")
            st.success(f"📡 Photon B instantly becomes: **{measurement_b}**")
            st.warning("⚡ Correlation appears instantaneous, regardless of distance!")
            st.balloons()
    
    # Experimental data
    st.markdown("### 📈 Real Experimental Results")
    
    # Simulate Bell test data
    angles = np.linspace(0, 180, 50)
    quantum_correlation = -np.cos(np.radians(angles))
    classical_limit = np.where(angles <= 45, -1, np.where(angles <= 135, 2*angles/90 - 3, 1))
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=angles, y=quantum_correlation,
        mode='lines', name='Quantum Mechanics',
        line=dict(color='cyan', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=angles, y=classical_limit,
        mode='lines', name='Classical (Bell Inequality)',
        line=dict(color='red', width=3, dash='dash')
    ))
    
    # Add experimental points
    exp_angles = [0, 22.5, 45, 67.5, 90, 112.5, 135, 157.5, 180]
    exp_values = -np.cos(np.radians(exp_angles)) + np.random.normal(0, 0.02, len(exp_angles))
    
    fig.add_trace(go.Scatter(
        x=exp_angles, y=exp_values,
        mode='markers', name='Experimental Data',
        marker=dict(color='yellow', size=10, symbol='diamond')
    ))
    
    fig.update_layout(
        title="Bell Test: Quantum Mechanics vs Classical Predictions",
        xaxis_title="Measurement Angle (degrees)",
        yaxis_title="Correlation C(a,b)",
        plot_bgcolor='rgba(20,20,50,0.9)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    <div class='quantum-card'>
    <h3>🏆 The Verdict</h3>
    <p style='font-size: 16px;'>
    <b>Experiments consistently violate Bell's inequality</b>, confirming quantum mechanics and 
    disproving local realism. Einstein was wrong about "spooky action," but his challenge led to 
    profound understanding of quantum entanglement, now used in:
    </p>
    <ul style='font-size: 16px;'>
        <li>Quantum cryptography (unhackable communication)</li>
        <li>Quantum teleportation</li>
        <li>Quantum computing</li>
        <li>Quantum sensing</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ===== WAVE-PARTICLE DUALITY =====
elif page == "🌊 Wave-Particle Duality":
    st.markdown("## 🌊 Wave-Particle Duality: The Quantum Mystery")
    
    st.markdown("""
    <div class='quantum-card'>
    <h3>🎭 The Double Nature of Reality</h3>
    <p style='font-size: 18px;'>
    Einstein's work on the photoelectric effect showed light behaves as particles (photons). 
    Yet light also exhibits wave properties (interference, diffraction). This fundamental 
    duality extends to all matter, as described by de Broglie's relation.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # de Broglie relation
    st.markdown("### 📐 de Broglie's Matter Waves")
    
    st.markdown("""
    <div class='equation'>
    <b>de Broglie Wavelength:</b><br><br>
    λ = h / p = h / (mv)<br><br>
    where:<br>
    • λ = wavelength<br>
    • h = Planck's constant<br>
    • p = momentum<br>
    • m = mass, v = velocity
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive calculator
    st.markdown("### 🧮 de Broglie Wavelength Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        particle_type = st.selectbox(
            "Select Particle:",
            ["Electron", "Proton", "Neutron", "Baseball", "Custom"]
        )
        
        masses = {
            "Electron": 9.109e-31,
            "Proton": 1.673e-27,
            "Neutron": 1.675e-27,
            "Baseball": 0.145,
            "Custom": 1.0
        }
        
        if particle_type == "Custom":
            mass = st.number_input("Mass (kg):", value=1.0, format="%.3e")
        else:
            mass = masses[particle_type]
            st.info(f"Mass: {mass:.3e} kg")
        
        velocity = st.slider("Velocity (m/s):", 1, 1000000, 1000, step=1000)
    
    with col2:
        h = 6.626e-34
        momentum = mass * velocity
        wavelength = h / momentum
        
        st.markdown(f"""
        <div class='metric-card'>
        <h3>de Broglie Wavelength</h3>
        <h2>{wavelength:.3e} m</h2>
        <p>Momentum: {momentum:.3e} kg·m/s</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Comparison
        if wavelength > 1e-6:
            st.success("✅ Observable wave effects possible!")
        elif wavelength > 1e-10:
            st.info("⚛️ Atomic scale - quantum effects important")
        else:
            st.warning("🔬 Too small - classical behavior dominates")
    
    # Double-slit experiment simulation
    st.markdown("### 🎯 Double-Slit Experiment Simulator")
    
    experiment_mode = st.radio(
        "Detection Mode:",
        ["Both slits open (no detection)", "Both slits open (with detection)", "Single slit"],
        horizontal=True
    )
    
    # Generate interference pattern
    x = np.linspace(-5, 5, 1000)
    
    if experiment_mode == "Both slits open (no detection)":
        # Wave interference
        d = 2.0  # slit separation
        L = 100  # screen distance
        wavelength_sim = 1.0
        
        theta = x / L
        path_diff = d * np.sin(theta)
        phase_diff = 2 * np.pi * path_diff / wavelength_sim
        
        intensity = (np.cos(phase_diff / 2)) ** 2
        
        st.success("🌊 WAVE BEHAVIOR: Interference pattern observed!")
        
    elif experiment_mode == "Both slits open (with detection)":
        # Particle behavior - two peaks
        intensity = (stats.norm.pdf(x, -1.5, 0.5) + stats.norm.pdf(x, 1.5, 0.5))
        
        st.warning("👁️ PARTICLE BEHAVIOR: Measuring which slit destroys interference!")
        
    else:  # Single slit
        intensity = stats.norm.pdf(x, 0, 1.0)
        
        st.info("📍 SINGLE SLIT: Simple diffraction pattern")
    
    # Plot
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=x, y=intensity,
        fill='tozeroy',
        line=dict(color='cyan', width=2),
        name='Intensity'
    ))
    
    fig.update_layout(
        title=f"Detection Pattern: {experiment_mode}",
        xaxis_title="Position on Screen",
        yaxis_title="Intensity",
        plot_bgcolor='rgba(20,20,50,0.9)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        height=400,
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    <div class='quantum-card'>
    <h3>🧠 The Deep Mystery</h3>
    <p style='font-size: 16px;'>
    The double-slit experiment reveals the heart of quantum mechanics:
    </p>
    <ul style='font-size: 16px;'>
        <li><b>Unobserved:</b> Particles behave as waves, creating interference patterns</li>
        <li><b>Observed:</b> Act of measurement collapses wavefunction, showing particle behavior</li>
        <li><b>Complementarity:</b> Cannot observe wave and particle nature simultaneously</li>
        <li><b>Einstein's Concern:</b> "Does the moon exist only when we look at it?"</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ===== QUANTUM COMPUTING BASICS =====
elif page == "🧮 Quantum Computing Basics":
    st.markdown("## 🧮 Quantum Computing: Harnessing Quantum Weirdness")
    
    st.markdown("""
    <div class='quantum-card'>
    <h3>💻 From Einstein's Quantum to Quantum Computers</h3>
    <p style='font-size: 18px;'>
    While Einstein questioned quantum mechanics, his work laid foundations for quantum computing—
    a revolutionary technology exploiting superposition, entanglement, and interference to solve 
    problems exponentially faster than classical computers.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Qubit explanation
    st.markdown("### ⚛️ Qubits: Quantum Bits")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='quantum-card'>
        <h3>🖥️ Classical Bit</h3>
        <p style='font-size: 16px;'>
        Can be in one of two states:<br>
        • 0 or 1<br>
        • ON or OFF<br>
        • TRUE or FALSE
        </p>
        <div style='text-align: center; font-size: 60px; margin: 20px;'>0 | 1</div>
        <p style='text-align: center;'><b>One state at a time</b></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='quantum-card'>
        <h3>⚛️ Quantum Bit (Qubit)</h3>
        <p style='font-size: 16px;'>
        Can be in superposition:<br>
        • |ψ⟩ = α|0⟩ + β|1⟩<br>
        • Both 0 AND 1 simultaneously<br>
        • |α|² + |β|² = 1
        </p>
        <div style='text-align: center; font-size: 60px; margin: 20px;'>|0⟩ + |1⟩</div>
        <p style='text-align: center;'><b>Superposition of states</b></p>
        </div>
        """, unsafe_allow_html=True)
    
    # Bloch sphere visualization
    st.markdown("### 🌐 Bloch Sphere: Visualizing Qubit States")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        theta = st.slider("Theta (θ):", 0.0, 180.0, 45.0, 5.0)
        phi = st.slider("Phi (φ):", 0.0, 360.0, 45.0, 5.0)
        
        theta_rad = np.radians(theta)
        phi_rad = np.radians(phi)
        
        alpha = np.cos(theta_rad / 2)
        beta = np.sin(theta_rad / 2) * np.exp(1j * phi_rad)
        
        prob_0 = abs(alpha) ** 2
        prob_1 = abs(beta) ** 2
        
        st.markdown(f"""
        <div class='quantum-card'>
        <h4>Qubit State</h4>
        <p>|ψ⟩ = {alpha.real:.3f}|0⟩ + {beta.real:.3f}e^(i{phi_rad:.2f})|1⟩</p>
        <p><b>Measurement Probabilities:</b></p>
        <p>P(0) = {prob_0:.3f}</p>
        <p>P(1) = {prob_1:.3f}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Create Bloch sphere
        fig = go.Figure()
        
        # Sphere surface
        u = np.linspace(0, 2 * np.pi, 50)
        v = np.linspace(0, np.pi, 50)
        x_sphere = np.outer(np.cos(u), np.sin(v))
        y_sphere = np.outer(np.sin(u), np.sin(v))
        z_sphere = np.outer(np.ones(np.size(u)), np.cos(v))
        
        fig.add_trace(go.Surface(
            x=x_sphere, y=y_sphere, z=z_sphere,
            opacity=0.2,
            colorscale='Blues',
            showscale=False
        ))
        
        # State vector
        x_state = np.sin(theta_rad) * np.cos(phi_rad)
        y_state = np.sin(theta_rad) * np.sin(phi_rad)
        z_state = np.cos(theta_rad)
        
        fig.add_trace(go.Scatter3d(
            x=[0, x_state], y=[0, y_state], z=[0, z_state],
            mode='lines+markers',
            line=dict(color='red', width=8),
            marker=dict(size=[0, 10], color='red'),
            name='State |ψ⟩'
        ))
        
        # Axes
        fig.add_trace(go.Scatter3d(
            x=[0, 0], y=[0, 0], z=[0, 1.3],
            mode='lines+text',
            line=dict(color='white', width=4),
            text=['', '|0⟩'],
            textposition='top center',
            name='Z-axis'
        ))
        
        fig.update_layout(
            title="Bloch Sphere Representation",
            scene=dict(
                xaxis=dict(showgrid=False, showticklabels=False, title='X'),
                yaxis=dict(showgrid=False, showticklabels=False, title='Y'),
                zaxis=dict(showgrid=False, showticklabels=False, title='Z'),
                bgcolor='rgba(20,20,50,0.9)'
            ),
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            height=500,
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Quantum gates
    st.markdown("### 🔧 Quantum Gates")
    
    gate = st.selectbox(
        "Select Quantum Gate:",
        ["Hadamard (H)", "Pauli-X", "Pauli-Y", "Pauli-Z", "CNOT"]
    )
    
    if gate == "Hadamard (H)":
        st.markdown("""
        <div class='quantum-card'>
        <h4>Hadamard Gate: Creating Superposition</h4>
        <div class='equation'>
        H|0⟩ = (|0⟩ + |1⟩) / √2<br>
        H|1⟩ = (|0⟩ - |1⟩) / √2
        </div>
        <p>Creates equal superposition - foundation of quantum algorithms!</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif gate == "Pauli-X":
        st.markdown("""
        <div class='quantum-card'>
        <h4>Pauli-X Gate: Quantum NOT</h4>
        <div class='equation'>
        X|0⟩ = |1⟩<br>
        X|1⟩ = |0⟩
        </div>
        <p>Flips qubit state - quantum equivalent of classical NOT gate</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif gate == "CNOT":
        st.markdown("""
        <div class='quantum-card'>
        <h4>CNOT Gate: Creating Entanglement</h4>
        <div class='equation'>
        CNOT|00⟩ = |00⟩<br>
        CNOT|01⟩ = |01⟩<br>
        CNOT|10⟩ = |11⟩<br>
        CNOT|11⟩ = |10⟩
        </div>
        <p>Two-qubit gate that creates entanglement - enables quantum parallelism!</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Quantum advantage
    st.markdown("### 🚀 Quantum Advantage")
    
    n_qubits = st.slider("Number of Qubits:", 1, 20, 10)
    
    classical_states = n_qubits
    quantum_states = 2 ** n_qubits
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class='metric-card' style='background: linear-gradient(135deg, #ff6b6b 0%, #ff8e53 100%);'>
        <h3>Classical Computer</h3>
        <h2>{classical_states} bits</h2>
        <p>Can represent {classical_states} states</p>
        <p>(one at a time)</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='metric-card' style='background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);'>
        <h3>Quantum Computer</h3>
        <h2>{n_qubits} qubits</h2>
        <p>Can represent {quantum_states:,} states</p>
        <p>(simultaneously!)</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.success(f"🚀 Quantum advantage: {quantum_states / classical_states:.1f}× more states with superposition!")

# ===== QUANTUM AI ALGORITHMS =====
elif page == "🤖 Quantum AI Algorithms":
    st.markdown("## 🤖 Quantum AI: The Next Frontier")
    
    st.markdown("""
    <div class='quantum-card'>
    <h3>🧠 Merging Quantum Computing with AI</h3>
    <p style='font-size: 18px;'>
    Quantum AI leverages quantum phenomena to enhance machine learning algorithms, promising 
    exponential speedups in optimization, pattern recognition, and data analysis. Key algorithms 
    include quantum neural networks, variational quantum eigensolvers, and quantum-enhanced sampling.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Algorithm selection
    algorithm = st.selectbox(
        "Select Quantum Algorithm:",
        ["Grover's Search", "Quantum Fourier Transform", "Variational Quantum Eigensolver (VQE)", 
         "Quantum Approximate Optimization (QAOA)"]
    )
    
    if algorithm == "Grover's Search":
        st.markdown("### 🔍 Grover's Search Algorithm")
        
        st.markdown("""
        <div class='quantum-card'>
        <h4>The Quantum Search Advantage</h4>
        <p style='font-size: 16px;'>
        Searches unsorted database of N items in O(√N) time vs. classical O(N).<br>
        For 1 million items: Classical needs ~1M operations, Quantum needs ~1000!
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Interactive demo
        database_size = st.slider("Database Size (N):", 100, 10000, 1000, 100)
        
        classical_ops = database_size / 2  # Average case
        quantum_ops = np.sqrt(database_size) * (np.pi / 4)
        
        speedup = classical_ops / quantum_ops
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div class='metric-card'>
            <h3>Classical Search</h3>
            <h2>{classical_ops:.0f}</h2>
            <p>operations (average)</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class='metric-card' style='background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);'>
            <h3>Grover's Algorithm</h3>
            <h2>{quantum_ops:.0f}</h2>
            <p>operations</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class='metric-card' style='background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);'>
            <h3>Speedup</h3>
            <h2>{speedup:.1f}×</h2>
            <p>faster!</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Visualization
        sizes = np.logspace(2, 6, 50)
        classical = sizes / 2
        quantum = np.sqrt(sizes) * (np.pi / 4)
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=sizes, y=classical,
            mode='lines',
            name='Classical O(N)',
            line=dict(color='red', width=3)
        ))
        
        fig.add_trace(go.Scatter(
            x=sizes, y=quantum,
            mode='lines',
            name='Grover O(√N)',
            line=dict(color='cyan', width=3)
        ))
        
        fig.update_layout(
            title="Grover's Search: Quantum Speedup",
            xaxis_title="Database Size (N)",
            yaxis_title="Operations Required",
            xaxis_type="log",
            yaxis_type="log",
            plot_bgcolor='rgba(20,20,50,0.9)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    elif algorithm == "Variational Quantum Eigensolver (VQE)":
        st.markdown("### 🧪 Variational Quantum Eigensolver (VQE)")
        
        st.markdown("""
        <div class='quantum-card'>
        <h4>Quantum Chemistry & Optimization</h4>
        <p style='font-size: 16px;'>
        VQE finds ground state energies of molecules - crucial for drug discovery and materials science. 
        Combines quantum and classical computing in a hybrid approach.
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Simulate VQE optimization
        if st.button("🔬 Run VQE Simulation"):
            progress_bar = st.progress(0)
            status = st.empty()
            
            iterations = 50
            energies = []
            
            # Simulate energy convergence
            for i in range(iterations):
                progress_bar.progress((i + 1) / iterations)
                
                # Simulate energy decreasing with noise
                energy = -1.0 + 1.0 * np.exp(-i / 10) + np.random.normal(0, 0.05)
                energies.append(energy)
                
                status.markdown(f"""
                <div class='quantum-card'>
                <h4>Iteration {i+1}/{iterations}</h4>
                <p>Current Energy: {energy:.4f} Ha</p>
                <p>Optimizing variational parameters...</p>
                </div>
                """, unsafe_allow_html=True)
                
                time.sleep(0.05)
            
            # Plot convergence
            fig = go.Figure()
            
            fig.add_trace(go.Scatter(
                x=list(range(iterations)),
                y=energies,
                mode='lines+markers',
                name='Energy',
                line=dict(color='cyan', width=2),
                marker=dict(size=5)
            ))
            
            fig.add_hline(y=-1.0, line_dash="dash", line_color="green", 
                         annotation_text="True Ground State")
            
            fig.update_layout(
                title="VQE Energy Convergence",
                xaxis_title="Iteration",
                yaxis_title="Energy (Hartree)",
                plot_bgcolor='rgba(20,20,50,0.9)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='white',
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            st.success(f"✅ Converged! Ground state energy: {energies[-1]:.4f} Ha")
            st.balloons()
    
    # Quantum ML applications
    st.markdown("### 🎯 Quantum Machine Learning Applications")
    
    applications = {
        "🧬 Drug Discovery": "Simulating molecular interactions exponentially faster",
        "💰 Financial Optimization": "Portfolio optimization and risk analysis",
        "🔐 Cryptography": "Post-quantum encryption and quantum key distribution",
        "🤖 Pattern Recognition": "Enhanced image and speech recognition",
        "🌡️ Climate Modeling": "Complex system simulations",
        "🚗 Autonomous Vehicles": "Real-time decision optimization",
    }
    
    cols = st.columns(2)
    for i, (app, desc) in enumerate(applications.items()):
        with cols[i % 2]:
            st.markdown(f"""
            <div class='quantum-card'>
            <h4>{app}</h4>
            <p style='font-size: 14px;'>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

# ===== QUANTUM MACHINE LEARNING =====
elif page == "🔬 Quantum Machine Learning":
    st.markdown("## 🔬 Quantum Machine Learning: Theory & Practice")
    
    st.markdown("""
    <div class='quantum-card'>
    <h3>🎓 The Intersection of Quantum Physics and AI</h3>
    <p style='font-size: 18px;'>
    Quantum Machine Learning (QML) applies quantum algorithms to ML tasks, potentially offering 
    exponential advantages in training speed, model capacity, and pattern recognition capabilities.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # QML approach
    approach = st.radio(
        "Select QML Approach:",
        ["Quantum Neural Networks", "Quantum Kernel Methods", "Quantum Data Encoding"],
        horizontal=True
    )
    
    if approach == "Quantum Neural Networks":
        st.markdown("### 🧠 Quantum Neural Networks (QNN)")
        
        st.markdown("""
        <div class='quantum-card'>
        <h4>Parameterized Quantum Circuits</h4>
        <p style='font-size: 16px;'>
        QNNs use parameterized quantum circuits as neural network layers, with quantum gates 
        acting as trainable parameters. The quantum state evolves through the circuit, and 
        measurement provides the output.
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Build a simple QNN
        col1, col2 = st.columns(2)
        
        with col1:
            n_qubits = st.slider("Number of Qubits:", 2, 5, 3)
            n_layers = st.slider("Circuit Depth:", 1, 5, 2)
            
            st.markdown(f"""
            <div class='quantum-card'>
            <h4>Network Architecture</h4>
            <p>Qubits: {n_qubits}</p>
            <p>Layers: {n_layers}</p>
            <p>Parameters: {n_qubits * n_layers * 3}</p>
            <p>Hilbert Space Dimension: {2**n_qubits}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Visualize circuit
            st.markdown("""
            <div class='quantum-card'>
            <h4>Quantum Circuit</h4>
            <pre style='color: cyan; font-size: 12px;'>
q0: ──H──RY(θ₀)──●──────────RY(θ₃)──
                 │
q1: ──H──RY(θ₁)──X──●───────RY(θ₄)──
                    │
q2: ──H──RY(θ₂)─────X───────RY(θ₅)──
            </pre>
            <p style='font-size: 14px;'>
            H: Hadamard gate (superposition)<br>
            RY: Rotation gate (trainable)<br>
            ●─X: CNOT (entanglement)
            </p>
            </div>
            """, unsafe_allow_html=True)
        
        # Training simulation
        if st.button("🏋️ Train Quantum Neural Network"):
            st.markdown("#### Training Progress")
            
            epochs = 30
            progress = st.progress(0)
            loss_container = st.empty()
            
            losses = []
            accuracies = []
            
            for epoch in range(epochs):
                # Simulate loss decrease
                loss = 1.0 * np.exp(-epoch / 10) + 0.1 + np.random.normal(0, 0.05)
                accuracy = 1.0 - loss
                
                losses.append(loss)
                accuracies.append(accuracy)
                
                progress.progress((epoch + 1) / epochs)
                
                # Plot current state
                fig = go.Figure()
                
                fig.add_trace(go.Scatter(
                    x=list(range(len(losses))),
                    y=losses,
                    mode='lines+markers',
                    name='Loss',
                    yaxis='y',
                    line=dict(color='red', width=2)
                ))
                
                fig.add_trace(go.Scatter(
                    x=list(range(len(accuracies))),
                    y=accuracies,
                    mode='lines+markers',
                    name='Accuracy',
                    yaxis='y2',
                    line=dict(color='cyan', width=2)
                ))
                
                fig.update_layout(
                    title="QNN Training Metrics",
                    xaxis_title="Epoch",
                    yaxis=dict(title="Loss", side='left'),
                    yaxis2=dict(title="Accuracy", side='right', overlaying='y'),
                    plot_bgcolor='rgba(20,20,50,0.9)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font_color='white',
                    height=400
                )
                
                loss_container.plotly_chart(fig, use_container_width=True)
                
                time.sleep(0.1)
            
            st.success(f"✅ Training Complete! Final Accuracy: {accuracies[-1]:.2%}")
            st.balloons()
    
    elif approach == "Quantum Kernel Methods":
        st.markdown("### 🎯 Quantum Kernel Methods")
        
        st.markdown("""
        <div class='quantum-card'>
        <h4>Quantum Feature Maps</h4>
        <p style='font-size: 16px;'>
        Classical data is encoded into quantum states. The kernel is computed as the overlap 
        between quantum states: K(x, y) = |⟨φ(x)|φ(y)⟩|²
        </p>
        <div class='equation'>
        Quantum Advantage: Quantum feature maps can access exponentially large feature spaces!
        </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Generate sample data
        np.random.seed(42)
        n_samples = st.slider("Number of Samples:", 20, 100, 50)
        
        # Create spiral dataset
        theta = np.linspace(0, 4 * np.pi, n_samples // 2)
        r = np.linspace(0.5, 2, n_samples // 2)
        
        X1 = np.column_stack([r * np.cos(theta), r * np.sin(theta)])
        X2 = np.column_stack([-r * np.cos(theta), -r * np.sin(theta)])
        
        X = np.vstack([X1, X2])
        y = np.hstack([np.zeros(n_samples // 2), np.ones(n_samples // 2)])
        
        # Classical kernel
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Classical RBF Kernel")
            
            fig = go.Figure()
            
            fig.add_trace(go.Scatter(
                x=X[y == 0, 0], y=X[y == 0, 1],
                mode='markers',
                name='Class 0',
                marker=dict(size=10, color='red')
            ))
            
            fig.add_trace(go.Scatter(
                x=X[y == 1, 0], y=X[y == 1, 1],
                mode='markers',
                name='Class 1',
                marker=dict(size=10, color='cyan')
            ))
            
            fig.update_layout(
                title="Classical Feature Space",
                plot_bgcolor='rgba(20,20,50,0.9)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='white',
                height=400,
                showlegend=True
            )
            
            st.plotly_chart(fig, use_container_width=True)
            st.info("📊 Classes overlap - difficult to separate")
        
        with col2:
            st.markdown("#### Quantum Kernel")
            
            # Simulate quantum feature space (higher dimensional projection)
            theta_q = np.arctan2(X[:, 1], X[:, 0])
            r_q = np.sqrt(X[:, 0]**2 + X[:, 1]**2)
            
            X_quantum = np.column_stack([
                r_q * np.cos(2 * theta_q),
                r_q * np.sin(2 * theta_q)
            ])
            
            fig = go.Figure()
            
            fig.add_trace(go.Scatter(
                x=X_quantum[y == 0, 0], y=X_quantum[y == 0, 1],
                mode='markers',
                name='Class 0',
                marker=dict(size=10, color='red')
            ))
            
            fig.add_trace(go.Scatter(
                x=X_quantum[y == 1, 0], y=X_quantum[y == 1, 1],
                mode='markers',
                name='Class 1',
                marker=dict(size=10, color='cyan')
            ))
            
            fig.update_layout(
                title="Quantum Feature Space",
                plot_bgcolor='rgba(20,20,50,0.9)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='white',
                height=400,
                showlegend=True
            )
            
            st.plotly_chart(fig, use_container_width=True)
            st.success("✅ Classes separated - easier classification!")
        
        st.markdown("""
        <div class='quantum-card'>
        <h4>🎯 Key Advantage</h4>
        <p style='font-size: 16px;'>
        Quantum kernels can map data to exponentially high-dimensional spaces efficiently, 
        enabling classification of patterns impossible for classical kernels.
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    else:  # Quantum Data Encoding
        st.markdown("### 📊 Quantum Data Encoding")
        
        st.markdown("""
        <div class='quantum-card'>
        <h4>Encoding Classical Data into Quantum States</h4>
        <p style='font-size: 16px;'>
        Classical data must be encoded into quantum states for processing. Different encoding 
        strategies offer various advantages for QML algorithms.
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        encoding_type = st.selectbox(
            "Select Encoding Method:",
            ["Amplitude Encoding", "Angle Encoding", "Basis Encoding"]
        )
        
        # Example data
        data_point = st.text_input("Enter data (comma-separated):", "0.5, 0.8, -0.3, 0.1")
        data = np.array([float(x.strip()) for x in data_point.split(",")])
        
        if encoding_type == "Amplitude Encoding":
            st.markdown("""
            <div class='equation'>
            <b>Amplitude Encoding:</b><br>
            |ψ⟩ = Σᵢ xᵢ|i⟩ (normalized)<br><br>
            • Most efficient: n qubits encode 2ⁿ values<br>
            • Requires normalization: Σ|xᵢ|² = 1<br>
            • Exponential capacity advantage
            </div>
            """, unsafe_allow_html=True)
            
            # Normalize
            data_norm = data / np.linalg.norm(data)
            n_qubits_needed = int(np.ceil(np.log2(len(data))))
            
            st.markdown(f"""
            <div class='quantum-card'>
            <h4>Encoding Result</h4>
            <p>Original data length: {len(data)}</p>
            <p>Qubits required: {n_qubits_needed}</p>
            <p>Normalized amplitudes: {data_norm}</p>
            <p><b>Efficiency: {len(data)} values in {n_qubits_needed} qubits!</b></p>
            </div>
            """, unsafe_allow_html=True)
            
        elif encoding_type == "Angle Encoding":
            st.markdown("""
            <div class='equation'>
            <b>Angle Encoding:</b><br>
            |ψ⟩ = ⊗ᵢ (cos(xᵢ)|0⟩ + sin(xᵢ)|1⟩)<br><br>
            • One value per qubit<br>
            • Encodes in rotation angles<br>
            • Simple and intuitive
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class='quantum-card'>
            <h4>Encoding Result</h4>
            <p>Data points: {len(data)}</p>
            <p>Qubits required: {len(data)}</p>
            <p>Rotation angles: {data}</p>
            </div>
            """, unsafe_allow_html=True)

# ===== INTERACTIVE SIMULATIONS =====
elif page == "🎮 Interactive Simulations":
    st.markdown("## 🎮 Interactive Quantum Simulations")
    
    simulation = st.selectbox(
        "Choose Simulation:",
        ["🌀 Quantum Teleportation", "🎲 Quantum Random Walk", "🔮 Quantum State Tomography", 
         "⚡ Quantum Error Correction"]
    )
    
    if simulation == "🌀 Quantum Teleportation":
        st.markdown("### 🌀 Quantum Teleportation Protocol")
        
        st.markdown("""
        <div class='quantum-card'>
        <h4>The "Spooky" Protocol</h4>
        <p style='font-size: 16px;'>
        Teleport a quantum state from Alice to Bob using entanglement and classical communication. 
        Note: No faster-than-light communication - classical bits still needed!
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 Start Teleportation"):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("""
                <div class='quantum-card' style='text-align: center;'>
                <h4>Alice</h4>
                <div style='font-size: 60px;'>👩‍🔬</div>
                <p>Has quantum state |ψ⟩</p>
                <div style='font-size: 30px;'>|ψ⟩ = α|0⟩ + β|1⟩</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                <div class='quantum-card' style='text-align: center;'>
                <h4>Entangled Pair</h4>
                <div style='font-size: 60px;'>🔗</div>
                <p>Shared Bell state</p>
                <div style='font-size: 20px;'>(|00⟩ + |11⟩)/√2</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown("""
                <div class='quantum-card' style='text-align: center;'>
                <h4>Bob</h4>
                <div style='font-size: 60px;'>👨‍🔬</div>
                <p>Will receive |ψ⟩</p>
                <div style='font-size: 30px;'>?</div>
                </div>
                """, unsafe_allow_html=True)
            
            time.sleep(1)
            
            st.markdown("#### Step 1: Alice performs Bell measurement")
            time.sleep(1)
            
            measurement = np.random.choice(['00', '01', '10', '11'])
            st.info(f"📡 Alice measures: {measurement}")
            st.markdown("#### Step 2: Alice sends classical bits to Bob")
            time.sleep(1)
            
            st.success(f"📞 Classical communication: {measurement}")
            st.markdown("#### Step 3: Bob applies correction")
            time.sleep(1)
            
            corrections = {
                '00': 'I (do nothing)',
                '01': 'X (bit flip)',
                '10': 'Z (phase flip)',
                '11': 'XZ (both flips)'
            }
            
            st.success(f"🔧 Bob applies gate: {corrections[measurement]}")
            st.markdown("#### Result: Teleportation Complete! 🎉")
            
            st.markdown("""
            <div class='quantum-card' style='text-align: center; background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);'>
            <h3>✅ Success!</h3>
            <p style='font-size: 20px;'>Bob now has the exact quantum state |ψ⟩</p>
            <p style='font-size: 16px;'>Alice's original state was destroyed (no-cloning theorem)</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.balloons()
    
    elif simulation == "🎲 Quantum Random Walk":
        st.markdown("### 🎲 Quantum vs Classical Random Walk")
        
        steps = st.slider("Number of Steps:", 10, 100, 50)
        
        if st.button("🚶 Run Random Walks"):
            # Classical random walk
            classical_pos = [0]
            for _ in range(steps):
                classical_pos.append(classical_pos[-1] + np.random.choice([-1, 1]))
            
            # Quantum random walk (simplified)
            quantum_prob = np.zeros(2 * steps + 1)
            quantum_prob[steps] = 1  # Start at center
            
            for _ in range(steps):
                new_prob = np.zeros(2 * steps + 1)
                for i in range(len(quantum_prob)):
                    if quantum_prob[i] > 0:
                        # Quantum interference
                        if i > 0:
                            new_prob[i - 1] += quantum_prob[i] * 0.5
                        if i < len(quantum_prob) - 1:
                            new_prob[i + 1] += quantum_prob[i] * 0.5
                quantum_prob = new_prob
                quantum_prob /= np.sum(quantum_prob)  # Normalize
            
            # Plot
            fig = go.Figure()
            
            fig.add_trace(go.Scatter(
                x=list(range(len(classical_pos))),
                y=classical_pos,
                mode='lines+markers',
                name='Classical Walk',
                line=dict(color='red', width=2)
            ))
            
            positions = np.arange(-steps, steps + 1)
            quantum_pos_expected = np.sum(positions * quantum_prob)
            
            fig.add_hline(
                y=quantum_pos_expected,
                line_dash="dash",
                line_color="cyan",
                annotation_text=f"Quantum (spread: {np.std(positions, where=quantum_prob>0.01):.1f})"
            )
            
            fig.update_layout(
                title="Random Walk Comparison",
                xaxis_title="Step",
                yaxis_title="Position",
                plot_bgcolor='rgba(20,20,50,0.9)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='white',
                height=500
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            st.markdown("""
            <div class='quantum-card'>
            <h4>🔑 Key Difference</h4>
            <p>
            <b>Classical:</b> Random, diffuses slowly (~√N)<br>
            <b>Quantum:</b> Interference effects spread faster (~N)
            </p>
            <p>Quantum walks are used in quantum search and graph algorithms!</p>
            </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 30px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
     border-radius: 20px; margin-top: 40px;'>
    <h2 style='color: white;'>🌌 "The most incomprehensible thing about the world is that it is comprehensible." 🌌</h2>
    <p style='color: white; font-size: 18px; margin-top: 20px;'>
        <b>- Albert Einstein</b>
    </p>
    <p style='color: white; font-size: 16px; margin-top: 30px;'>
        Continue exploring the fascinating intersection of quantum physics and artificial intelligence!<br>
        The quantum revolution is just beginning. 🚀
    </p>
</div>
""", unsafe_allow_html=True)
