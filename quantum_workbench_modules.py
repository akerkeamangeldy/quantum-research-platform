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
            <span class='metric-value' style='font-size: 20px;'>{theta_bloch}┬░</span>
            <span class='metric-label'> | ╬╕ = {np.radians(theta_bloch):.4f} rad</span>
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
                    <div class='rotary-value'>{phi_bloch}┬░</div>
                </div>
                <div class='rotary-label'>╧Ж = {np.radians(phi_bloch):.4f} rad</div>
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
            if "h" in gate_lower or "╨░╨┤╨░╨╝╨░╤А" in gate_lower:
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
            <h3>{phase_deg if not np.isnan(phase_deg) else 0:.1f}┬░</h3>
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
print(f"P(|0тЯй) = {{prob_0:.3f}}, P(|1тЯй) = {{prob_1:.3f}}")
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
        
        # ╬▒тВБ vector
        fig.add_trace(go.Scatter(
            x=[0, alpha1.real], y=[0, alpha1.imag],
            mode='lines+markers',
            line=dict(color='#6366F1', width=3),
            marker=dict(size=10),
            name=t('charts.common_traces.alpha1')
        ))
        
        # ╬▒тВВ vector
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
    if bell_state.startswith("╬жтБ║"):
        state = np.array([1, 0, 0, 1]) / np.sqrt(2)
        circuit_desc = "H on q0, CNOT(q0, q1)"
    elif bell_state.startswith("╬жтБ╗"):
        state = np.array([1, 0, 0, -1]) / np.sqrt(2)
        circuit_desc = "H on q0, Z on q0, CNOT(q0, q1)"
    elif bell_state.startswith("╬итБ║"):
        state = np.array([0, 1, 1, 0]) / np.sqrt(2)
        circuit_desc = "H on q0, X on q1, CNOT(q0, q1)"
    else:  # ╬итБ╗
        state = np.array([0, 1, -1, 0]) / np.sqrt(2)
        circuit_desc = "H on q0, X on q1, Z on q1, CNOT(q0, q1)"
    
    # Display circuit
    st.markdown(f"{t('ent_circuit_label')} `{circuit_desc}`")
    
    # State vector visualization
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"#### {t('ent_state_title')}")
        basis_labels = ['|00тЯй', '|01тЯй', '|10тЯй', '|11тЯй']
        amplitudes_real = np.real(state)
        amplitudes_imag = np.imag(state)
        
        # Enhanced visualization with area-glow effects
        fig_amp = go.Figure()
        fig_amp.add_trace(go.Bar(
            x=basis_labels,
            y=amplitudes_real,
            name='Re(╧И)',
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
            name='Im(╧И)',
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
    # Flip state: ╧Г_y тКЧ ╧Г_y
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
    st.markdown(f"# {t('noise.page_title')}")
    st.markdown(f'<span class="research-status status-active">{t("status_badges.active")}</span>', unsafe_allow_html=True)
    
    st.markdown(f"""<div class='research-card'>
        <h3>{t('noise.card_title')}</h3>
        <p>{t('noise.card_desc')}</p>
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
        st.markdown(f"### {t('noise.section_init')}")
        theta_noise = st.slider(t('noise.slider_theta'), 0, 180, 90, 5, key="theta_noise")
        phi_noise = st.slider(t('noise.slider_phi'), 0, 360, 0, 5, key="phi_noise")
        
        # Prepare initial density matrix
        theta_rad = np.radians(theta_noise)
        phi_rad = np.radians(phi_noise)
        psi = np.array([np.cos(theta_rad/2), np.exp(1j*phi_rad)*np.sin(theta_rad/2)])
        rho_initial = np.outer(psi, psi.conj())
        
        st.markdown(f"### {t('noise.section_channel')}")
        noise_type = st.selectbox(t('noise.select_channel'), 
                                  [t('noise.channel_depolarizing'), t('noise.channel_dephasing'), t('noise.channel_amplitude')],
                                  key="noise_channel")
        noise_strength = st.slider(t('noise.slider_strength'), 0.0, 1.0, 0.3, 0.05, key="noise_str")
        
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
            <h3>{purity_initial:.4f} тЖТ {purity_noisy:.4f}</h3>
            <p>{t('noise.metric_purity')}</p>
        </div>
        <div class='metric-box'>
            <h3>{bloch_length_initial:.4f} тЖТ {bloch_length_noisy:.4f}</h3>
            <p>{t('noise.metric_bloch')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Density matrix heatmaps
        fig_dm = make_subplots(
            rows=2, cols=2,
            subplot_titles=(t('noise.chart_re_initial'), t('noise.chart_im_initial'), 
                          t('noise.chart_re_noise'), t('noise.chart_im_noise')),
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
        st.markdown(f"### {t('noise.section_relaxation')}")
        
        T1 = st.number_input(t('noise.input_t1'), min_value=10, max_value=200, value=100, key="T1_val")
        T2 = st.number_input(t('noise.input_t2'), min_value=10, max_value=200, value=50, key="T2_val")
        
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
        
        st.markdown(f"""
        <div class='latex-display'>
            <h4>{t('noise.phys_interp_title')}</h4>
            <p><strong>TтВБ:</strong> {t('noise.phys_interp_t1')}</p>
            <p><strong>TтВВ:</strong> {t('noise.phys_interp_t2')}</p>
            <p><strong>{t('noise.phys_interp_fidelity')}</strong></p>
        </div>
        """, unsafe_allow_html=True)

elif module_id == "vqe":
    # Add energy field effect
    add_energy_field()
    
    st.markdown("<div class='vqe-landscape'>", unsafe_allow_html=True)
    st.markdown(f"# {t('vqe.page_title')}")
    st.markdown(f'<span class="research-status status-active">{t("status_badges.variational")}</span>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class='research-card'>
        <h3>{t('vqe.card_title')}</h3>
        <p>{t('vqe.card_desc')}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.latex(r"""
    E(\theta) = \langle\psi(\theta)|H|\psi(\theta)\rangle = \text{Tr}(H\rho(\theta))
    """)
    
    st.latex(r"""
    \theta^* = \arg\min_\theta E(\theta)
    """)
    
    st.markdown(f"""
    <div class='latex-display'>
        <p><strong>{t('vqe.intro_ansatz')}</strong> {t('vqe.intro_ansatz_desc')}</p>
        <p><strong>{t('vqe.intro_hamiltonian')}</strong> {t('vqe.intro_hamiltonian_desc')}</p>
        <p><strong>{t('vqe.intro_optimizer')}</strong> {t('vqe.intro_optimizer_desc')}</p>
        <p><strong>{t('vqe.intro_output')}</strong> {t('vqe.intro_output_desc')}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # VQE configuration
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown(f"### {t('vqe.section_config')}")
        
        ansatz_depth = st.slider(t('vqe.slider_depth'), 1, 5, 2, key="vqe_depth")
        n_iterations = st.slider(t('vqe.slider_iterations'), 20, 100, 50, 10, key="vqe_iter")
        optimizer_choice = st.selectbox(t('vqe.select_optimizer'), ["COBYLA", "SPSA", "Powell"], key="vqe_opt")
        noise_model = st.checkbox(t('vqe.checkbox_noise'), value=True, key="vqe_noise")
        
        # Hamiltonian (HтВВ molecule example)
        st.markdown(f"**{t('vqe.hamiltonian_label')}** {t('vqe.hamiltonian_h2')}")
        st.code("H = -1.0523 * II + 0.3979 * ZZ + 0.3979 * XX - 0.0112 * ZI - 0.0112 * IZ", language="text")
        
        # Exact ground state (for comparison)
        E_exact = -1.137  # HтВВ exact ground state energy
        
        if st.button(t('vqe.button_run'), type="primary", key="run_vqe"):
            progress_bar = st.progress(0)
            status_text = st.empty()
            energy_plot = st.empty()
            
            # Simulate VQE optimization
            energies = []
            params_history = []
            
            # Initial parameters
            n_params = ansatz_depth * 3  # ╬╕, ╧Ж, ╬╗ per layer
            params = np.random.uniform(0, 2*np.pi, n_params)
            
            for iteration in range(n_iterations):
                progress_bar.progress((iteration + 1) / n_iterations)
                status_text.markdown(f"**{t('vqe.status_iteration')} {iteration + 1}/{n_iterations}**")
                
                # Simulate energy convergence
                # Real VQE would compute тЯи╧И(╬╕)|H|╧И(╬╕)тЯй
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
                    name=t('charts.vqe.energy_trace')
                ))
                
                fig_conv.add_hline(
                    y=E_exact,
                    line_dash="dash",
                    line_color='#84CC16',
                    annotation_text=f"{t('charts.vqe.exact_annotation')} {E_exact:.6f} Ha",
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
            
            st.success(f"тЬУ {t('vqe.success_converged')} {final_energy:.6f} Ha | {t('vqe.metric_error')}: {error:.6f} Ha | {t('vqe.metric_accuracy')}: {accuracy:.2f}%")
            
            # Chemical accuracy check
            chemical_accuracy = 0.0016  # 1 kcal/mol in Hartree
            if error < chemical_accuracy:
                st.markdown(f"""
                <div class='experiment-panel' style='border-left-color: #84CC16;'>
                    <h4 style='color: #84CC16;'>{t('vqe.chem_accuracy_title')}</h4>
                    <p>{t('vqe.chem_accuracy_desc')}</p>
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
        st.markdown(f"### {t('vqe.section_theory')}")
        
        st.markdown(f"""
        <div class='experiment-panel'>
            <h4>{t('vqe.theory_ansatz_title')}</h4>
            <p>{t('vqe.theory_ansatz_subtitle')}</p>
            <ul>
                <li>{t('vqe.theory_ansatz_ry')}</li>
                <li>{t('vqe.theory_ansatz_rz')}</li>
                <li>{t('vqe.theory_ansatz_cnot')}</li>
            </ul>
            <p>{t('vqe.theory_ansatz_depth')} = {ansatz_depth}</p>
            <p>{t('vqe.theory_ansatz_params')} = {ansatz_depth * 3}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class='experiment-panel'>
            <h4>{t('vqe.theory_landscape_title')}</h4>
            <p>{t('vqe.theory_landscape_desc')}</p>
            <p><strong>{t('vqe.theory_challenges')}</strong></p>
            <ul>
                <li>{t('vqe.theory_challenge_1')}</li>
                <li>{t('vqe.theory_challenge_2')}</li>
                <li>{t('vqe.theory_challenge_3')}</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class='metric-box'>
            <h3>{2**2}</h3>
            <p>{t('vqe.metric_hilbert')}</p>
        </div>
        """, unsafe_allow_html=True)

elif module_id == "qaoa":
    # Add energy field effect for optimization landscape
    add_energy_field()
    
    st.markdown("<div class='vqe-landscape'>", unsafe_allow_html=True)
    st.markdown(f"# {t('qaoa.page_title')}")
    st.markdown(f'<span class="research-status status-active">{t("status_badges.combinatorial")}</span>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class='research-card'>
        <h3>{t('qaoa.card_title')}</h3>
        <p>{t('qaoa.card_desc')}</p>
        
        <p><strong>{t('qaoa.key_concept_label')}</strong> {t('qaoa.key_concept_text')}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Problem Selection
    st.markdown(f"### {t('qaoa.section_problem')}")
    problem_type = st.selectbox(
        t('qaoa.select_problem'),
        [t('qaoa.problem_maxcut'), t('qaoa.problem_partition'), t('qaoa.problem_coloring')],
        help=t('qaoa.problem_help')
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
            num_nodes = st.slider(t('qaoa.slider_nodes'), 3, 6, 4, help=t('qaoa.nodes_help'))
        with col2:
            p_layers = st.slider(t('qaoa.slider_layers'), 1, 5, 2, help=t('qaoa.layers_help'))
        
        # Generate random graph (adjacency matrix)
        np.random.seed(42)
        adj_matrix = np.random.randint(0, 2, size=(num_nodes, num_nodes))
        adj_matrix = np.triu(adj_matrix, k=1)  # Upper triangular
        adj_matrix = adj_matrix + adj_matrix.T  # Make symmetric
        
        # Display graph
        st.markdown(f"#### {t('qaoa.graph_structure')}")
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
        st.markdown(f"#### {t('qaoa.qaoa_params')}")
        
        if st.button(t('qaoa.button_run'), type="primary"):
            with st.spinner(t('qaoa.status_running')):
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
                
                st.success(f"тЬЕ Found MaxCut solution: {best_bitstring} with cut value {best_cost}")
                st.info("ЁЯТ╛ Experiment logged! Visit 'Reproducibility & Export' to download results.")
    
    elif problem_type == "Number Partitioning":
        st.info("Number Partitioning implementation coming soon!")
    
    elif problem_type == "Graph Coloring":
        st.info("Graph Coloring implementation coming soon!")

elif module_id == "qml":
    # Add neural network background
    add_neural_network_bg()
    
    st.markdown("<div class='qml-neural'>", unsafe_allow_html=True)
    st.markdown(f"# {t('qml.page_title')}")
    st.markdown(f'<span class="research-status status-active">{t("status_badges.hybrid")}</span>', unsafe_allow_html=True)
    
    st.markdown(f"""<div class='research-card'>
        <h3>{t('qml.card_title')}</h3>
        <p>{t('qml.card_desc')}</p>
    </div>
    """, unsafe_allow_html=True)
    
    qml_method = st.selectbox(t('qml.select_method'), 
                              [t('qml.method_qk_svm'), t('qml.method_vqc')],
                              key="qml_method")
    
    if qml_method == t('qml.method_qk_svm'):
        st.markdown(f"### {t('qml.section_kernel')}")
        
        st.latex(r"""
        K(x, x') = |\langle\phi(x)|\phi(x')\rangle|^2
        """)
        
        st.markdown(f"""<div class='latex-display'>
            <p><strong>{t('qml.feature_map_label')}</strong> {t('qml.feature_map_desc')}</p>
            <p><strong>{t('qml.kernel_label')}</strong> {t('qml.kernel_desc')}</p>
            <p><strong>{t('qml.classical_ml_label')}</strong> {t('qml.classical_ml_desc')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Generate synthetic dataset
        from sklearn.datasets import make_moons
        from sklearn.svm import SVC
        from sklearn.model_selection import train_test_split
        
        n_samples = st.slider(t('qml.slider_samples'), 50, 200, 100, 10, key="qml_samples")
        noise_level = st.slider(t('qml.slider_noise'), 0.0, 0.3, 0.1, 0.05, key="qml_noise")
        
        if st.button(t('buttons.train_qk_svm'), type="primary", key="train_qk_svm"):
            # Generate data
            X, y = make_moons(n_samples=n_samples, noise=noise_level, random_state=42)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
            
            # Simulate quantum kernel computation
            # In reality: K[i,j] = |тЯи╧Ж(x_i)|╧Ж(x_j)тЯй|┬▓
            # Here: approximate with RBF + quantum-inspired transformation
            
            progress = st.progress(0)
            status = st.empty()
            
            status.markdown(f"**{t('qml.status_computing')}**")
            progress.progress(0.3)
            time.sleep(0.5)
            
            # Classical baseline
            clf_classical = SVC(kernel='rbf', gamma='scale')
            clf_classical.fit(X_train, y_train)
            acc_classical = clf_classical.score(X_test, y_test)
            
            status.markdown(f"**{t('qml.status_training')}**")
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
                    <p>{t('qml.metric_classical')}</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class='metric-box'>
                    <h3>{acc_quantum:.3f}</h3>
                    <p>{t('qml.metric_quantum')}</p>
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
                                        subplot_titles=(t('qml.chart_classical'), t('qml.chart_quantum')))
            
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
            
            st.success(f"{t('qml.success_training')} {(acc_quantum - acc_classical)*100:+.2f}%")

elif module_id == "circuits":
    # Add matrix rain effect
    add_matrix_rain()
    
    st.markdown("<div class='circuit-flow'>", unsafe_allow_html=True)
    st.markdown(f"# {t('circuits.page_title')}")
    st.markdown(f'<span class="research-status status-active">{t("status_badges.active")}</span>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class='research-card'>
        <h3>{t('circuits.card_title')}</h3>
        <p>{t('circuits.card_desc')}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.latex(r"""
    U_{\text{total}} = U_n \cdots U_2 U_1, \quad |\psi_{\text{out}}\rangle = U_{\text{total}}|\psi_{\text{in}}\rangle
    """)
    
    st.markdown(f"""
    <div class='latex-display'>
        <p><strong>{t('circuits.theory_unitary')}</strong> {t('circuits.theory_unitary_desc')}</p>
        <p><strong>{t('circuits.theory_reversible')}</strong> {t('circuits.theory_reversible_desc')}</p>
        <p><strong>{t('circuits.theory_composition')}</strong> {t('circuits.theory_composition_desc')}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Circuit builder
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown(f"### {t('circuits.section_build')}")
        
        # Initial state selection
        init_state = st.radio(t('circuits.select_init'), 
                             ["|0тЯй", "|1тЯй", "|+тЯй = (|0тЯй+|1тЯй)/тИЪ2", "|-тЯй = (|0тЯй-|1тЯй)/тИЪ2", t('circuits.state_custom')],
                             key="circuit_init_state")
        
        if t('circuits.state_custom') in init_state:
            custom_theta = st.slider(t('circuits.slider_custom_theta'), 0, 180, 90, 5, key="custom_circuit_theta")
            custom_phi = st.slider(t('circuits.slider_custom_phi'), 0, 360, 0, 5, key="custom_circuit_phi")
            theta_rad = np.radians(custom_theta)
            phi_rad = np.radians(custom_phi)
            state = np.array([np.cos(theta_rad/2), np.exp(1j*phi_rad)*np.sin(theta_rad/2)])
        elif "|0тЯй" in init_state:
            state = np.array([1, 0], dtype=complex)
        elif "|1тЯй" in init_state:
            state = np.array([0, 1], dtype=complex)
        elif "|+тЯй" in init_state:
            state = np.array([1, 1], dtype=complex) / np.sqrt(2)
        else:  # |-тЯй
            state = np.array([1, -1], dtype=complex) / np.sqrt(2)
        
        # Gate palette
        st.markdown(f"### {t('circuits.section_gates')}")
        
        gate_options = ["H", "X", "Y", "Z", "S", "T", "RX(╧А/2)", "RY(╧А/2)", "RZ(╧А/2)", "RX(╧А)", "RY(╧А)"]
        selected_gates = st.multiselect(t('circuits.select_gates'), gate_options, key="circuit_gates")
        
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
                angle = 90 if "╧А/2" in gate_name else 180
                gate = rotation_gate('X', angle)
            elif "RY" in gate_name:
                angle = 90 if "╧А/2" in gate_name else 180
                gate = rotation_gate('Y', angle)
            elif "RZ" in gate_name:
                angle = 90 if "╧А/2" in gate_name else 180
                gate = rotation_gate('Z', angle)
            
            state = gate @ state
            total_unitary = gate @ total_unitary
            circuit_states.append(state.copy())
            circuit_labels.append(gate_name)
        
        # Display circuit diagram (text-based)
        st.markdown("### Circuit Diagram")
        circuit_str = "q: |╧ИтВАтЯйтФАтФА"
        for gate_name in selected_gates:
            circuit_str += f"[{gate_name}]тФАтФА"
        circuit_str += "|╧ИтВЩтЯй"
        
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
                "╬▒ (|0тЯй)": f"{state_vec[0].real:.3f}{state_vec[0].imag:+.3f}i",
                "╬▓ (|1тЯй)": f"{state_vec[1].real:.3f}{state_vec[1].imag:+.3f}i",
                "P(|0тЯй)": f"{prob_0:.3f}",
                "P(|1тЯй)": f"{prob_1:.3f}",
                "Phase (┬░)": f"{np.degrees(phase):.1f}"
            })
        
        import pandas as pd
        df_evolution = pd.DataFrame(evolution_data)
        st.dataframe(df_evolution, use_container_width=True)
        
        # Total unitary matrix
        st.markdown(f"### {t('circuits.section_unitary')}")
        st.markdown(t('circuits.unitary_desc'))
        
        col_u1, col_u2 = st.columns(2)
        
        with col_u1:
            st.markdown(f"**{t('circuits.real_part')}**")
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
            <p><strong>UтАаU = I:</strong> {"тЬУ Valid" if identity_check else "тЬЧ Invalid"}</p>
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
                <p>P(|0тЯй)</p>
            </div>
            <div class='metric-box'>
                <h3>{abs(final_state[1])**2:.3f}</h3>
                <p>P(|1тЯй)</p>
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
                        x=['|0тЯй', '|1тЯй'],
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
                    <p><strong>Theoretical:</strong> P(|0тЯй) = {prob_0:.3f}, P(|1тЯй) = {1-prob_0:.3f}</p>
                    <p><strong>Measured:</strong> P(|0тЯй) = {count_0/shots:.3f}, P(|1тЯй) = {count_1/shots:.3f}</p>
                    <p><strong>Statistical error:</strong> ~1/тИЪ{shots} тЙИ {1/np.sqrt(shots):.3f}</p>
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
print(f"Final state: |╧ИтЯй = {{state[0]:.3f}}|0тЯй + {{state[1]:.3f}}|1тЯй")
print(f"Probabilities: P(|0тЯй) = {{abs(state[0])**2:.3f}}, P(|1тЯй) = {{abs(state[1])**2:.3f}}")
"""
    st.code(code_circuit, language="python")

elif module_id == "export":
    st.markdown("<div class='overview-bg'>", unsafe_allow_html=True)
    st.markdown(f"# {t('export.page_title')}")
    st.markdown(f'<span class="research-status status-active">{t("status_badges.infrastructure")}</span>', unsafe_allow_html=True)
    
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
            <li>тЬУ Unique experiment ID (hash-based)</li>
            <li>тЬУ Timestamp (ISO 8601 format)</li>
            <li>тЬУ Complete parameter specification</li>
            <li>тЬУ Random seed for deterministic reproduction</li>
            <li>тЬУ Backend configuration (simulator/hardware)</li>
            <li>тЬУ Noise model details</li>
            <li>тЬУ Result metrics and uncertainties</li>
            <li>тЬУ Code version (commit hash if available)</li>
            <li>тЬУ Dependencies and environment</li>
            <li>тЬУ Citations and references</li>
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
    st.markdown(f"# {t('qec.page_title')}")
    st.markdown(f'<span class="research-status status-active">{t("status_badges.fault_tolerant")}</span>', unsafe_allow_html=True)
    
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
        
        # Encode logical |0тЯй = |000тЯй
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
    st.markdown(f"# {t('hardware.page_title')}")
    st.markdown(f'<span class="research-status status-active">{t("status_badges.active")}</span>', unsafe_allow_html=True)
    
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
        <span class='metric-label'>тЪб QUBIT CONNECTIVITY MAP - VOLUMETRIC RENDERING</span>
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
            hovertemplate=f'<b>Connection {i} тЖФ {j}</b><br>Fidelity: {fidelity:.3f}<extra></extra>',
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
        hovertemplate='<b>Qubit %{text}</b><br>TтВВ: %{customdata:.1f}╬╝s<extra></extra>',
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
    st.markdown(f"# {t('complexity.page_title')}")
    st.markdown(f'<span class="research-status status-active">{t("status_badges.frontier")}</span>', unsafe_allow_html=True)
    
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
            <p><strong>Quantum:</strong> Polynomial time O((log N)┬│)</p>
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
                st.success(f"тЬЕ {N_factor} = {factors[0]} ├Ч {factors[1]}")
            else:
                st.info(f"{N_factor} is prime")
    
    elif algorithm == "Grover's Search":
        st.markdown("""
        <div class='research-card'>
            <h3>Grover's Algorithm (1996)</h3>
            <p><strong>Problem:</strong> Search unstructured database of N items</p>
            <p><strong>Classical:</strong> O(N) - must check each item</p>
            <p><strong>Quantum:</strong> O(тИЪN) - quadratic speedup</p>
            
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
                <h3>{speedup:.1f}├Ч</h3>
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
    st.markdown(f"# {t('topological.page_title')}")
    st.markdown(f'<span class="research-status status-frontier">{t("status_badges.frontier")}</span>', unsafe_allow_html=True)
    
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
        ["Identity (No Braid)", "╧ГтВБ (Braid 1-2)", "╧ГтВВ (Braid 2-3)", "╧ГтВБ╧ГтВВ╧ГтВБ (Yang-Baxter)"]
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
        
    elif braid_type == "╧ГтВБ (Braid 1-2)":
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
    <p><strong>Quantum ├Ч AI Research Workbench</strong> | Production Research Platform</p>
    <p>Academic-Grade Quantum Computing Experiments тАв Reproducible Results тАв Publication-Ready Visualizations</p>
    <p style='font-size: 12px; margin-top: 12px;'>
        Built with Streamlit тАв Qiskit тАв NumPy тАв SciPy тАв Plotly
    </p>
</div>
""", unsafe_allow_html=True)
