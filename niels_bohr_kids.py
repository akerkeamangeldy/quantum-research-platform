import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time
import math

# Page config
st.set_page_config(
    page_title="🌟 Niels Bohr's Atomic Adventure!",
    page_icon="⚛️",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .big-title {
        font-size: 40px !important;
        font-weight: bold;
        color: #FF6B6B;
        text-align: center;
    }
    .fun-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 25px;
        border-radius: 20px;
        border: 5px solid #FFE66D;
        color: white;
    }
    .atom-box {
        background: radial-gradient(circle, #1e3c72 0%, #2a5298 100%);
        padding: 30px;
        border-radius: 20px;
        border: 3px solid #00d4ff;
        box-shadow: 0 0 30px rgba(0, 212, 255, 0.5);
    }
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-size: 22px;
        padding: 15px 30px;
        border-radius: 15px;
        border: none;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; color: #667eea;'>⚛️ Niels Bohr's Atomic Adventure! ⚛️</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #FF6B6B;'>🚀 Discover the MAGICAL World Inside Everything! 🌟</h3>", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("## 🎯 Choose Your Adventure!")
page = st.sidebar.radio(
    "",
    ["🏠 Meet Niels Bohr", "⚛️ The Atom - Tiny Solar System", "🎨 Magic Light & Colors", 
     "⚡ Energy Jumps!", "🎮 Interactive Lab", "🌈 Rainbow Maker"]
)

# ===== MEET NIELS BOHR =====
if page == "🏠 Meet Niels Bohr":
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        <div style='text-align: center; padding: 30px; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
             border-radius: 20px; border: 5px solid #FFE66D;'>
            <div style='font-size: 120px;'>👨‍🔬</div>
            <h2 style='color: white;'>Niels Bohr</h2>
            <p style='color: white; font-size: 18px;'>The Atom Detective!</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        ### 👋 Hello! I'm Niels Bohr!
        
        I was a scientist who loved to solve mysteries! 🔍
        
        **My Biggest Discovery:**
        
        🌟 I figured out what ATOMS look like!
        
        🌟 Atoms are the TINY building blocks of EVERYTHING!
        
        🌟 You, me, your toys, the stars - EVERYTHING is made of atoms!
        
        Let me show you my amazing discovery! 🎪
        """)
    
    st.markdown("---")
    
    # What are atoms?
    st.markdown("## 🤔 What Are Atoms?")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='fun-box' style='text-align: center;'>
            <div style='font-size: 60px;'>🏰</div>
            <h3>Like LEGO Blocks!</h3>
            <p style='font-size: 16px;'>Everything is built from tiny pieces!</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='fun-box' style='text-align: center;'>
            <div style='font-size: 60px;'>🔬</div>
            <h3>SO Tiny!</h3>
            <p style='font-size: 16px;'>A million atoms fit on a pencil tip!</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='fun-box' style='text-align: center;'>
            <div style='font-size: 60px;'>✨</div>
            <h3>Magical!</h3>
            <p style='font-size: 16px;'>They glow and make colors!</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Interactive demonstration
    st.markdown("## 🎪 Let's See How Small Atoms Are!")
    
    zoom_level = st.slider("🔍 Zoom in to see smaller and smaller!", 0, 5, 0)
    
    zoom_descriptions = [
        ("👋", "This is YOU!", "You are amazing!"),
        ("✋", "Your Hand", "You can see your hand easily!"),
        ("🔬", "Hair Strand", "Getting smaller... need a magnifying glass!"),
        ("🦠", "Bacteria", "Very tiny! Need a microscope!"),
        ("🧬", "DNA Molecule", "Super tiny! Special microscope needed!"),
        ("⚛️", "ATOM!", "The tiniest building block of everything!")
    ]
    
    emoji, title, desc = zoom_descriptions[zoom_level]
    
    size = 120 - (zoom_level * 15)
    
    st.markdown(f"""
    <div style='text-align: center; padding: 40px; background: radial-gradient(circle, #1e3c72 0%, #2a5298 100%); 
         border-radius: 20px; border: 5px solid #00d4ff;'>
        <div style='font-size: {size}px;'>{emoji}</div>
        <h2 style='color: #00d4ff; margin-top: 20px;'>{title}</h2>
        <p style='color: white; font-size: 20px;'>{desc}</p>
    </div>
    """, unsafe_allow_html=True)
    
    if zoom_level == 5:
        st.balloons()
        st.success("🎉 You found the ATOM! The smallest piece of matter!")

# ===== THE ATOM - TINY SOLAR SYSTEM =====
elif page == "⚛️ The Atom - Tiny Solar System":
    st.markdown("## 🌟 Bohr's Big Discovery: The Atom is Like a Tiny Solar System!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🌞 Our Solar System")
        st.markdown("""
        <div style='background-color: #1a1a2e; padding: 30px; border-radius: 20px; text-align: center;'>
            <div style='font-size: 80px;'>☀️</div>
            <p style='color: white; font-size: 18px; margin-top: 20px;'>
                The Sun is in the middle!<br>
                Planets go around it! 🪐🌍🌕
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### ⚛️ Bohr's Atom")
        st.markdown("""
        <div class='atom-box' style='text-align: center;'>
            <div style='font-size: 80px;'>⚛️</div>
            <p style='color: white; font-size: 18px; margin-top: 20px;'>
                The nucleus is in the middle! 🎯<br>
                Electrons go around it! ✨⚡✨
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Build an atom
    st.markdown("## 🏗️ Let's Build Your Own Atom!")
    
    st.markdown("""
    <div class='fun-box'>
        <h3>🎯 Atom Parts:</h3>
        <p style='font-size: 18px;'>
        <b>🔴 Nucleus (Center):</b> The "sun" - made of protons (+) and neutrons<br>
        <b>⚡ Electrons:</b> The "planets" - they zoom around the nucleus!<br>
        <b>🌀 Orbits:</b> The "paths" - like train tracks for electrons!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎨 Choose Your Atom Size!")
    
    num_electrons = st.slider("How many electrons? ⚡", 1, 5, 3)
    
    # Create animated atom using plotly
    fig = go.Figure()
    
    # Add nucleus
    fig.add_trace(go.Scatter(
        x=[0], y=[0],
        mode='markers+text',
        marker=dict(size=40, color='red', line=dict(color='orange', width=3)),
        text=['🎯'],
        textfont=dict(size=30),
        name='Nucleus',
        hovertext='Nucleus: The center of the atom!'
    ))
    
    # Add orbits and electrons
    colors = ['#00d4ff', '#ff6b6b', '#4ecdc4', '#ffe66d', '#95e1d3']
    
    for orbit in range(1, num_electrons + 1):
        radius = orbit * 1.5
        theta = np.linspace(0, 2*np.pi, 100)
        x_orbit = radius * np.cos(theta)
        y_orbit = radius * np.sin(theta)
        
        # Draw orbit
        fig.add_trace(go.Scatter(
            x=x_orbit, y=y_orbit,
            mode='lines',
            line=dict(color=colors[orbit-1], width=2, dash='dash'),
            name=f'Orbit {orbit}',
            hoverinfo='skip'
        ))
        
        # Add electron
        angle = (orbit - 1) * (2 * np.pi / num_electrons)
        x_electron = radius * np.cos(angle)
        y_electron = radius * np.sin(angle)
        
        fig.add_trace(go.Scatter(
            x=[x_electron], y=[y_electron],
            mode='markers+text',
            marker=dict(size=25, color=colors[orbit-1], 
                       line=dict(color='white', width=2)),
            text=['⚡'],
            textfont=dict(size=20),
            name=f'Electron {orbit}',
            hovertext=f'Electron {orbit}: Zooming around!'
        ))
    
    fig.update_layout(
        showlegend=False,
        width=600,
        height=600,
        plot_bgcolor='rgba(0,0,0,0.9)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False, zeroline=False, visible=False, range=[-10, 10]),
        yaxis=dict(showgrid=False, zeroline=False, visible=False, range=[-10, 10]),
        margin=dict(l=0, r=0, t=0, b=0)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.success(f"🎉 You created an atom with {num_electrons} electrons! Each electron zooms in its own orbit!")
    
    st.markdown("---")
    
    # Fun facts
    st.markdown("## 🎓 Amazing Atom Facts!")
    
    if st.button("🎲 Tell Me a Fun Fact!"):
        facts = [
            "⚛️ Atoms are 99.9% EMPTY SPACE! If an atom was a football stadium, the nucleus would be a marble in the center!",
            "⚡ Electrons move SO FAST - millions of times per second! Like the fastest race car EVER!",
            "🌟 Every atom in your body was made inside a STAR billions of years ago! You're made of stardust!",
            "🎯 The nucleus is SUPER tiny but has almost ALL the weight of the atom!",
            "🌈 Different atoms have different numbers of electrons - that's why we have different elements!"
        ]
        
        fact = np.random.choice(facts)
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
             padding: 30px; border-radius: 20px; border: 5px solid gold;'>
            <h3 style='color: white; text-align: center;'>🌟 DID YOU KNOW? 🌟</h3>
            <p style='color: white; font-size: 22px; text-align: center; margin-top: 20px;'>
                {fact}
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()

# ===== MAGIC LIGHT & COLORS =====
elif page == "🎨 Magic Light & Colors":
    st.markdown("## 🌈 Bohr Discovered Why Atoms Make Colors!")
    
    st.markdown("""
    <div class='fun-box'>
        <h2 style='text-align: center;'>🎪 The Magic Color Show! 🎪</h2>
        <p style='font-size: 20px; text-align: center;'>
            Niels Bohr discovered that when electrons jump between orbits,<br>
            they make LIGHT and COLORS! ✨🌈✨
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Explain colors
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔥 Heat Up an Atom!")
        
        if st.button("⚡ Give Energy to Atom!"):
            st.markdown("""
            <div class='atom-box' style='text-align: center; padding: 40px;'>
                <h3 style='color: #00d4ff;'>⚡ ZAP! ⚡</h3>
                <p style='color: white; font-size: 20px; margin: 20px 0;'>
                    The electron gets excited!<br>
                    It jumps to a HIGHER orbit! 🚀
                </p>
                <div style='font-size: 80px; animation: bounce 1s infinite;'>⚛️</div>
            </div>
            """, unsafe_allow_html=True)
            
            time.sleep(1)
            
            st.markdown("""
            <div style='background: linear-gradient(135deg, #ff6b6b 0%, #ffd93d 100%); 
                 text-align: center; padding: 40px; border-radius: 20px; border: 5px solid gold;'>
                <h3 style='color: white;'>✨ WHOOSH! ✨</h3>
                <p style='color: white; font-size: 20px; margin: 20px 0;'>
                    The electron falls back down!<br>
                    It releases LIGHT! 💡
                </p>
                <div style='font-size: 80px;'>🌟</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.balloons()
            st.success("🎉 That's how atoms make light and colors!")
    
    with col2:
        st.markdown("### 🌈 Different Jumps = Different Colors!")
        
        st.markdown("""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
             padding: 30px; border-radius: 20px; color: white;'>
            <p style='font-size: 18px;'>
            🔴 <b>BIG jump down</b> = RED light<br><br>
            🟠 <b>Medium jump</b> = ORANGE light<br><br>
            🟡 <b>Smaller jump</b> = YELLOW light<br><br>
            🟢 <b>Small jump</b> = GREEN light<br><br>
            🔵 <b>Tiny jump</b> = BLUE light<br><br>
            🟣 <b>Very tiny jump</b> = PURPLE light<br>
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Interactive color maker
    st.markdown("## 🎨 Make Your Own Atom Colors!")
    
    st.markdown("Choose how far the electron should jump! 🚀")
    
    jump_size = st.select_slider(
        "Electron Jump Size:",
        options=["Tiny Jump", "Small Jump", "Medium Jump", "Big Jump", "HUGE Jump"],
        value="Medium Jump"
    )
    
    color_map = {
        "Tiny Jump": ("#9D00FF", "🟣 PURPLE/VIOLET", "violet"),
        "Small Jump": ("#0080FF", "🔵 BLUE", "blue"),
        "Medium Jump": ("#00FF00", "🟢 GREEN", "green"),
        "Big Jump": ("#FFAA00", "🟠 ORANGE", "orange"),
        "HUGE Jump": ("#FF0000", "🔴 RED", "red")
    }
    
    color_code, color_name, color_word = color_map[jump_size]
    
    st.markdown(f"""
    <div style='background: radial-gradient(circle, {color_code} 0%, black 100%); 
         padding: 60px; border-radius: 20px; border: 5px solid {color_code}; 
         box-shadow: 0 0 50px {color_code}; text-align: center;'>
        <h2 style='color: white; text-shadow: 0 0 10px white;'>✨ FLASH! ✨</h2>
        <h1 style='color: white; font-size: 60px; text-shadow: 0 0 20px white;'>{color_name}</h1>
        <p style='color: white; font-size: 24px; margin-top: 20px;'>
            Your electron made {color_word} light! 🌟
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Real world examples
    st.markdown("## 🎆 Where Do We See This?")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style='background-color: #ff6b6b; padding: 25px; border-radius: 15px; text-align: center;'>
            <div style='font-size: 60px;'>🎆</div>
            <h4 style='color: white;'>Fireworks!</h4>
            <p style='color: white;'>Different atoms make different colors!</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background-color: #4ecdc4; padding: 25px; border-radius: 15px; text-align: center;'>
            <div style='font-size: 60px;'>💡</div>
            <h4 style='color: white;'>Neon Signs!</h4>
            <p style='color: white;'>Neon gas glows when electricity excites atoms!</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='background-color: #ffe66d; padding: 25px; border-radius: 15px; text-align: center;'>
            <div style='font-size: 60px;'>🌟</div>
            <h4 style='color: black;'>Stars!</h4>
            <p style='color: black;'>Star colors tell us what atoms they have!</p>
        </div>
        """, unsafe_allow_html=True)

# ===== ENERGY JUMPS =====
elif page == "⚡ Energy Jumps!":
    st.markdown("## ⚡ The Amazing Energy Ladder!")
    
    st.markdown("""
    <div class='fun-box'>
        <h2 style='text-align: center;'>🎢 Bohr's Energy Levels!</h2>
        <p style='font-size: 20px; text-align: center;'>
            Electrons can only live in SPECIAL orbits!<br>
            It's like a ladder - you can stand on steps, but not between them! 🪜
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Interactive energy ladder
    st.markdown("### 🪜 The Energy Ladder Game!")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### 🎮 Controls")
        
        if 'electron_level' not in st.session_state:
            st.session_state.electron_level = 1
        
        st.markdown(f"""
        <div style='background-color: #667eea; padding: 20px; border-radius: 15px; color: white; text-align: center;'>
            <h3>Current Level: {st.session_state.electron_level}</h3>
            <p style='font-size: 40px;'>⚡</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("⬆️ Jump UP! (Add Energy)"):
            if st.session_state.electron_level < 5:
                st.session_state.electron_level += 1
                st.success(f"🚀 Jumped to level {st.session_state.electron_level}!")
                st.balloons()
            else:
                st.warning("⚠️ Maximum level reached! The electron would escape!")
        
        if st.button("⬇️ Fall DOWN! (Release Light)"):
            if st.session_state.electron_level > 1:
                old_level = st.session_state.electron_level
                st.session_state.electron_level -= 1
                st.success(f"💡 Fell from {old_level} to {st.session_state.electron_level}! Made LIGHT!")
                
                # Show color based on jump
                colors = {4: "🔴 RED", 3: "🟠 ORANGE", 2: "🟡 YELLOW", 1: "🟢 GREEN"}
                if old_level - st.session_state.electron_level in colors:
                    st.info(f"Created {colors[old_level - st.session_state.electron_level]} light! ✨")
            else:
                st.warning("⚠️ Already at lowest level!")
        
        if st.button("🔄 Reset"):
            st.session_state.electron_level = 1
            st.rerun()
    
    with col2:
        st.markdown("#### 🪜 The Energy Ladder")
        
        # Draw the ladder
        ladder_html = "<div style='background: linear-gradient(180deg, #1e3c72 0%, #2a5298 100%); padding: 30px; border-radius: 20px; border: 3px solid #00d4ff;'>"
        
        for level in range(5, 0, -1):
            if level == st.session_state.electron_level:
                ladder_html += f"""
                <div style='background-color: #ffcc00; padding: 15px; margin: 10px 0; 
                     border-radius: 10px; border: 3px solid gold; box-shadow: 0 0 20px gold;'>
                    <span style='font-size: 40px;'>⚡</span>
                    <span style='font-size: 24px; color: black; font-weight: bold;'> ← Level {level} (Electron HERE!)</span>
                </div>
                """
            else:
                ladder_html += f"""
                <div style='background-color: rgba(255,255,255,0.1); padding: 15px; margin: 10px 0; 
                     border-radius: 10px; border: 2px solid white;'>
                    <span style='font-size: 24px; color: white;'>Level {level}</span>
                </div>
                """
        
        ladder_html += "</div>"
        st.markdown(ladder_html, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Explanation
    st.markdown("""
    ### 🎓 What Did We Learn?
    
    <div style='background-color: #ffe66d; padding: 25px; border-radius: 15px; border: 3px solid #ff6b6b;'>
        <p style='font-size: 20px; color: black;'>
        ⚡ <b>Electrons live in special orbits</b> - like rungs on a ladder!<br><br>
        
        ⬆️ <b>When they get energy</b> - they jump UP to higher levels!<br><br>
        
        ⬇️ <b>When they fall back down</b> - they release light!<br><br>
        
        🌈 <b>Bigger falls make different colors!</b><br><br>
        
        🎪 <b>This is QUANTUM MECHANICS</b> - electrons can only be in certain places!
        </p>
    </div>
    """, unsafe_allow_html=True)

# ===== INTERACTIVE LAB =====
elif page == "🎮 Interactive Lab":
    st.markdown("## 🔬 Welcome to Bohr's Laboratory!")
    
    st.markdown("""
    <div class='fun-box' style='text-align: center;'>
        <h2>🎪 Be a Scientist Like Niels Bohr! 🎪</h2>
        <p style='font-size: 20px;'>
            Do experiments and discover how atoms work!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Choose experiment
    experiment = st.selectbox(
        "🧪 Choose Your Experiment!",
        ["🎯 Shoot Electrons at Atoms", "🔥 Heat Different Elements", "⚡ Build Your Dream Atom", "🌈 Mix Atom Colors"]
    )
    
    if experiment == "🎯 Shoot Electrons at Atoms":
        st.markdown("### 🎯 Electron Target Practice!")
        
        st.markdown("""
        Try to hit the nucleus with an electron!<br>
        But remember - atoms are mostly EMPTY SPACE! 🤯
        """, unsafe_allow_html=True)
        
        if st.button("🚀 Launch Electron!"):
            hit = np.random.random() < 0.1  # 10% chance to hit
            
            progress_bar = st.progress(0)
            status = st.empty()
            
            for i in range(100):
                progress_bar.progress(i + 1)
                status.markdown(f"""
                <div style='text-align: center; font-size: 60px;'>
                    ⚡ {'→' * (i // 10)}
                </div>
                """, unsafe_allow_html=True)
                time.sleep(0.02)
            
            if hit:
                st.success("🎯 BULLSEYE! You hit the nucleus! That's super rare! You're amazing!")
                st.balloons()
            else:
                st.info("💨 Whoosh! The electron went right through! Atoms are 99.9% empty space!")
    
    elif experiment == "🔥 Heat Different Elements":
        st.markdown("### 🔥 The Flame Test!")
        
        st.markdown("Different elements make different colored flames! Choose an element to heat:")
        
        element = st.selectbox(
            "Choose Element:",
            ["Hydrogen", "Helium", "Lithium", "Sodium", "Copper", "Potassium"]
        )
        
        element_colors = {
            "Hydrogen": ("#FF00AA", "🟣 PINK/PURPLE", "Hydrogen is the simplest atom - just 1 electron!"),
            "Helium": ("#FFFF00", "🟡 YELLOW", "Helium makes balloons float!"),
            "Lithium": ("#FF0000", "🔴 CRIMSON RED", "Lithium is in batteries!"),
            "Sodium": ("#FFAA00", "🟠 BRIGHT ORANGE", "Sodium is in salt!"),
            "Copper": ("#00FF88", "🟢 GREEN", "Copper makes green fireworks!"),
            "Potassium": ("#CC88FF", "🟣 LIGHT PURPLE", "Potassium is in bananas!")
        }
        
        if st.button("🔥 HEAT IT UP!"):
            color, color_name, fact = element_colors[element]
            
            st.markdown(f"""
            <div style='background: radial-gradient(circle, {color} 0%, #000000 100%); 
                 padding: 80px; border-radius: 20px; border: 5px solid {color}; 
                 box-shadow: 0 0 60px {color}; text-align: center;'>
                <h1 style='color: white; font-size: 60px; text-shadow: 0 0 30px white;'>
                    🔥 {element} 🔥
                </h1>
                <h2 style='color: white; margin-top: 30px; text-shadow: 0 0 20px white;'>
                    {color_name}
                </h2>
                <p style='color: white; font-size: 22px; margin-top: 30px;'>
                    {fact}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.balloons()
            st.success("🎉 Each element has its own special color! That's how scientists identify them!")
    
    elif experiment == "⚡ Build Your Dream Atom":
        st.markdown("### ⚡ Atom Builder 3000!")
        
        col1, col2 = st.columns(2)
        
        with col1:
            protons = st.number_input("🔴 Number of Protons (Red):", 1, 10, 3)
            electrons = st.number_input("⚡ Number of Electrons (Yellow):", 1, 10, 3)
        
        with col2:
            neutrons = st.number_input("⚪ Number of Neutrons (White):", 0, 10, 3)
        
        if st.button("🏗️ BUILD MY ATOM!"):
            # Create atom visualization
            fig = go.Figure()
            
            # Nucleus
            fig.add_trace(go.Scatter(
                x=[0], y=[0],
                mode='markers+text',
                marker=dict(size=60, color='red'),
                text=[f'🎯<br>{protons}p {neutrons}n'],
                textfont=dict(size=12, color='white'),
                name='Nucleus'
            ))
            
            # Electrons
            for i in range(electrons):
                orbit = (i // 2) + 1
                radius = orbit * 2
                angle = (i % 2) * np.pi + (orbit * 0.5)
                x = radius * np.cos(angle)
                y = radius * np.sin(angle)
                
                # Orbit
                theta = np.linspace(0, 2*np.pi, 100)
                x_orbit = radius * np.cos(theta)
                y_orbit = radius * np.sin(theta)
                
                fig.add_trace(go.Scatter(
                    x=x_orbit, y=y_orbit,
                    mode='lines',
                    line=dict(color='cyan', width=2, dash='dash'),
                    showlegend=False
                ))
                
                fig.add_trace(go.Scatter(
                    x=[x], y=[y],
                    mode='markers+text',
                    marker=dict(size=20, color='yellow'),
                    text=['⚡'],
                    textfont=dict(size=16),
                    showlegend=False
                ))
            
            fig.update_layout(
                showlegend=False,
                width=600,
                height=600,
                plot_bgcolor='rgba(10,10,50,1)',
                paper_bgcolor='rgba(0,0,0,0)',
                xaxis=dict(showgrid=False, zeroline=False, visible=False, range=[-8, 8]),
                yaxis=dict(showgrid=False, zeroline=False, visible=False, range=[-8, 8]),
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Analysis
            if protons == electrons:
                st.success(f"⚖️ Perfect! Your atom is BALANCED! It's neutral! This is {get_element_name(protons)}!")
                st.balloons()
            elif protons > electrons:
                st.info(f"➕ Your atom is POSITIVE! It lost {protons - electrons} electron(s)! It's an ION!")
            else:
                st.info(f"➖ Your atom is NEGATIVE! It gained {electrons - protons} extra electron(s)! It's an ION!")
    
    elif experiment == "🌈 Mix Atom Colors":
        st.markdown("### 🌈 Quantum Color Mixer!")
        
        st.markdown("Mix light from different atoms to make new colors!")
        
        col1, col2 = st.columns(2)
        
        with col1:
            color1 = st.selectbox("First Atom Color:", ["Red", "Green", "Blue", "Yellow"])
        
        with col2:
            color2 = st.selectbox("Second Atom Color:", ["Red", "Green", "Blue", "Yellow"])
        
        color_codes = {
            "Red": "#FF0000",
            "Green": "#00FF00",
            "Blue": "#0000FF",
            "Yellow": "#FFFF00"
        }
        
        if st.button("🎨 MIX COLORS!"):
            c1 = color_codes[color1]
            c2 = color_codes[color2]
            
            st.markdown(f"""
            <div style='text-align: center;'>
                <div style='display: inline-block; width: 150px; height: 150px; background-color: {c1}; 
                     border-radius: 50%; margin: 20px; border: 5px solid white;'></div>
                <div style='display: inline-block; font-size: 50px; margin: 20px;'>+</div>
                <div style='display: inline-block; width: 150px; height: 150px; background-color: {c2}; 
                     border-radius: 50%; margin: 20px; border: 5px solid white;'></div>
                <div style='display: inline-block; font-size: 50px; margin: 20px;'>=</div>
                <div style='display: inline-block; width: 200px; height: 200px; 
                     background: linear-gradient(135deg, {c1} 0%, {c2} 100%); 
                     border-radius: 50%; margin: 20px; border: 8px solid gold; 
                     box-shadow: 0 0 40px gold;'></div>
            </div>
            """, unsafe_allow_html=True)
            
            st.success("🌟 You mixed quantum light! This is how we see all the colors in the world!")

# ===== RAINBOW MAKER =====
elif page == "🌈 Rainbow Maker":
    st.markdown("## 🌈 Bohr's Rainbow Machine!")
    
    st.markdown("""
    <div class='fun-box' style='text-align: center;'>
        <h2>🎪 The Ultimate Color Show! 🎪</h2>
        <p style='font-size: 20px;'>
            Watch atoms make ALL the colors of the rainbow!<br>
            Each color is an electron jumping! ✨
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    if st.button("🌈 START THE RAINBOW SHOW! 🌈"):
        colors = [
            ("#FF0000", "🔴 RED", "Big electron jump!"),
            ("#FF7F00", "🟠 ORANGE", "Large jump!"),
            ("#FFFF00", "🟡 YELLOW", "Medium jump!"),
            ("#00FF00", "🟢 GREEN", "Small jump!"),
            ("#0000FF", "🔵 BLUE", "Smaller jump!"),
            ("#4B0082", "🟣 INDIGO", "Tiny jump!"),
            ("#9400D3", "🟪 VIOLET", "Very tiny jump!")
        ]
        
        progress = st.progress(0)
        color_display = st.empty()
        
        for i, (color_code, color_name, description) in enumerate(colors):
            progress.progress((i + 1) * (100 // len(colors)))
            
            color_display.markdown(f"""
            <div style='background: radial-gradient(circle, {color_code} 0%, #000000 100%); 
                 padding: 100px; border-radius: 20px; border: 5px solid {color_code}; 
                 box-shadow: 0 0 60px {color_code}; text-align: center; 
                 animation: pulse 1s infinite;'>
                <h1 style='color: white; font-size: 80px; text-shadow: 0 0 30px white;'>
                    {color_name}
                </h1>
                <p style='color: white; font-size: 28px; margin-top: 30px; text-shadow: 0 0 10px white;'>
                    {description}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            time.sleep(1)
        
        st.balloons()
        st.success("🎉 You just saw the ENTIRE rainbow made by electron jumps! This is REAL science!")
    
    st.markdown("---")
    
    # Quiz game
    st.markdown("## 🎮 Rainbow Quiz Game!")
    
    if st.button("🎲 Start Quiz!"):
        if 'quiz_started' not in st.session_state:
            st.session_state.quiz_started = True
            st.session_state.quiz_score = 0
            st.session_state.quiz_question = 0
        
        questions = [
            ("What did Niels Bohr discover?", ["Atoms", "Dinosaurs", "Pizza"], 0),
            ("What is in the center of an atom?", ["Nucleus", "Electron", "Magic"], 0),
            ("What zooms around the nucleus?", ["Electrons", "Cars", "Birds"], 0),
            ("What happens when electrons jump down?", ["Make light", "Make noise", "Make ice cream"], 0),
            ("Are atoms mostly empty space?", ["Yes!", "No!", "Maybe"], 0)
        ]
        
        q, options, correct = questions[st.session_state.quiz_question]
        
        st.markdown(f"### Question {st.session_state.quiz_question + 1}: {q}")
        
        for i, option in enumerate(options):
            if st.button(option, key=f"quiz_{i}"):
                if i == correct:
                    st.success("🎉 CORRECT! You're a genius!")
                    st.session_state.quiz_score += 1
                    st.balloons()
                else:
                    st.error("❌ Oops! Try again next time!")
                
                st.session_state.quiz_question += 1
                
                if st.session_state.quiz_question >= len(questions):
                    st.markdown(f"""
                    <div style='background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                         padding: 50px; border-radius: 20px; text-align: center;'>
                        <h1 style='color: white;'>🏆 QUIZ COMPLETE! 🏆</h1>
                        <h2 style='color: white;'>Score: {st.session_state.quiz_score}/{len(questions)}</h2>
                        <p style='color: white; font-size: 24px;'>You're a Quantum Superstar! ⭐</p>
                    </div>
                    """, unsafe_allow_html=True)
                    del st.session_state.quiz_started
                    del st.session_state.quiz_score
                    del st.session_state.quiz_question
                else:
                    time.sleep(1)
                    st.rerun()

# Helper function
def get_element_name(protons):
    elements = {
        1: "Hydrogen", 2: "Helium", 3: "Lithium", 4: "Beryllium", 5: "Boron",
        6: "Carbon", 7: "Nitrogen", 8: "Oxygen", 9: "Fluorine", 10: "Neon"
    }
    return elements.get(protons, "Unknown Element")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 30px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
     border-radius: 20px;'>
    <h2 style='color: white;'>🌟 Thank You, Niels Bohr! 🌟</h2>
    <p style='color: white; font-size: 20px;'>
        Thanks to Niels Bohr, we understand atoms!<br>
        Now we can make computers, lasers, and amazing technology! 🚀<br><br>
        <b>Keep being curious! You could be the next great scientist! 🔬</b>
    </p>
</div>
""", unsafe_allow_html=True)
