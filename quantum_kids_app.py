import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time
from PIL import Image, ImageDraw
import io

# Page config
st.set_page_config(
    page_title="🌟 Quantum World for Kids!",
    page_icon="🐱",
    layout="wide"
)

# Custom CSS for kid-friendly design
st.markdown("""
    <style>
    .big-font {
        font-size: 30px !important;
        font-weight: bold;
        color: #FF6B6B;
    }
    .fun-box {
        background-color: #FFE66D;
        padding: 20px;
        border-radius: 15px;
        border: 5px solid #4ECDC4;
    }
    .stButton>button {
        background-color: #FF6B6B;
        color: white;
        font-size: 20px;
        padding: 10px 24px;
        border-radius: 12px;
        border: 3px solid #95E1D3;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; color: #FF6B6B;'>🌟 Welcome to the Magical Quantum World! 🌟</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #4ECDC4;'>Learn about tiny tiny tiny things that are super cool! 🚀</h3>", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.markdown("## 🎨 Choose Your Adventure!")
page = st.sidebar.radio(
    "",
    ["🏠 Home", "🍎 Newton's Apple Magic", "🐱 Schrödinger's Cat", "✨ Quantum Superposition", "🤖 Quantum AI Magic", "🎮 Play & Learn"]
)

# ===== HOME PAGE =====
if page == "🏠 Home":
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🍎 Newton's Apple")
        st.write("Learn about gravity and tiny particles!")
        
    with col2:
        st.markdown("### 🐱 Magic Cat")
        st.write("A cat that's awake AND asleep!")
        
    with col3:
        st.markdown("### 🤖 Quantum AI")
        st.write("Super smart computers!")
    
    st.markdown("---")
    st.markdown("## 🌈 What is Quantum Physics?")
    st.markdown("""
    <div class='fun-box'>
    <p style='font-size: 20px;'>
    Imagine you have the TINIEST Lego blocks in the whole universe! 🧱<br><br>
    
    These blocks are SO tiny that you can't see them even with a microscope! 🔬<br><br>
    
    These tiny blocks do MAGICAL things:<br>
    ✨ They can be in two places at once!<br>
    ✨ They can spin both ways at the same time!<br>
    ✨ They can talk to each other super fast, faster than anything!<br><br>
    
    That's QUANTUM PHYSICS! The science of the tiniest, most magical things! 🎪
    </p>
    </div>
    """, unsafe_allow_html=True)

# ===== NEWTON'S APPLE PAGE =====
elif page == "🍎 Newton's Apple Magic":
    st.markdown("## 🍎 Newton's Apple Story")
    
    st.markdown("""
    ### Once upon a time... 📖
    
    A smart man named Isaac Newton was sitting under an apple tree. 🌳
    
    **BONK!** 🍎 An apple fell on his head!
    
    He wondered: "Why do apples fall DOWN and not UP?" 🤔
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🌍 Big Things (Like Apples)")
        
        if st.button("🍎 Drop the Apple!"):
            # Create animation
            progress_bar = st.progress(0)
            apple_position = st.empty()
            
            for i in range(100):
                progress_bar.progress(i + 1)
                apple_height = 100 - i
                apple_position.markdown(f"""
                <div style='height: 300px; position: relative;'>
                    <div style='position: absolute; top: {apple_height}%; left: 50%; transform: translateX(-50%); font-size: 50px;'>
                        🍎
                    </div>
                    <div style='position: absolute; bottom: 0; left: 50%; transform: translateX(-50%); font-size: 30px;'>
                        🌍
                    </div>
                </div>
                """, unsafe_allow_html=True)
                time.sleep(0.02)
            
            st.success("The apple falls DOWN because Earth pulls it! This is called GRAVITY! 🌍⬇️")
        
        st.markdown("""
        **Big things follow simple rules:**
        - They always fall down ⬇️
        - They go one way at a time ➡️
        - You can see where they are 👀
        """)
    
    with col2:
        st.markdown("### ⚛️ Tiny Quantum Things")
        
        if st.button("✨ Release Quantum Particle!"):
            st.markdown("""
            <div style='height: 300px; position: relative; background: linear-gradient(180deg, #667eea 0%, #764ba2 100%); border-radius: 10px;'>
                <div style='position: absolute; top: 30%; left: 20%; font-size: 30px;'>✨</div>
                <div style='position: absolute; top: 60%; left: 40%; font-size: 30px;'>✨</div>
                <div style='position: absolute; top: 45%; left: 70%; font-size: 30px;'>✨</div>
                <div style='position: absolute; top: 80%; left: 60%; font-size: 30px;'>✨</div>
                <div style='text-align: center; padding-top: 120px; color: white; font-size: 24px;'>
                    The particle is EVERYWHERE at once! 🤯
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.success("Tiny particles can be in MANY places at the same time! That's QUANTUM MAGIC! ✨")
        
        st.markdown("""
        **Tiny things are magical:**
        - They can be in many places! 🌟
        - They can spin both ways! 🔄
        - They do spooky things! 👻
        """)
    
    st.markdown("---")
    st.markdown("""
    ### 🎓 What Did We Learn?
    
    **Newton taught us:** Big things (like apples 🍎) fall down because of gravity!
    
    **Quantum Physics teaches us:** Tiny things (like electrons ⚛️) are MAGICAL and don't follow the same rules!
    
    It's like how YOU follow rules at school 🏫, but your toys can do ANYTHING in your imagination! 🎨
    """)

# ===== SCHRÖDINGER'S CAT PAGE =====
elif page == "🐱 Schrödinger's Cat":
    st.markdown("## 🐱 The Amazing Story of Schrödinger's Cat!")
    
    st.markdown("""
    ### 🎪 The Most Famous Cat in Science!
    
    A scientist named Schrödinger thought of a VERY silly idea to explain quantum physics!
    
    Let me tell you the story... 📖
    """)
    
    st.markdown("---")
    
    # Interactive cat demo
    st.markdown("### 🎁 The Magic Box Mystery!")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        Imagine we have a **magic box** 📦 with a cute cat inside! 🐱
        
        Here's the MAGICAL part:
        - We can't see inside the box! 🙈
        - Until we open it, the cat is **BOTH awake AND sleeping** at the same time! 🤯
        - It's like magic! ✨
        """)
        
        if 'box_opened' not in st.session_state:
            st.session_state.box_opened = False
        
        col_a, col_b, col_c = st.columns([1, 2, 1])
        with col_b:
            if not st.session_state.box_opened:
                if st.button("🎁 OPEN THE MAGIC BOX!", key="open_box"):
                    st.session_state.box_opened = True
                    st.session_state.cat_state = np.random.choice(["awake", "sleeping"])
                    st.rerun()
            else:
                if st.button("📦 Close Box & Try Again!", key="close_box"):
                    st.session_state.box_opened = False
                    st.rerun()
    
    with col2:
        st.markdown("### The Magic Box:")
        
    # Display the box
    if not st.session_state.box_opened:
        st.markdown("""
        <div style='text-align: center; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
             padding: 60px; border-radius: 20px; border: 5px solid #FFE66D;'>
            <div style='font-size: 100px;'>📦</div>
            <div style='font-size: 30px; color: white; margin-top: 20px;'>❓</div>
            <p style='color: white; font-size: 20px; margin-top: 20px;'>
                The cat is BOTH awake 😺 AND sleeping 😴!<br>
                This is called SUPERPOSITION! ✨
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        if st.session_state.cat_state == "awake":
            st.markdown("""
            <div style='text-align: center; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                 padding: 60px; border-radius: 20px; border: 5px solid #4ECDC4;'>
                <div style='font-size: 100px;'>😺</div>
                <p style='color: white; font-size: 24px; margin-top: 20px;'>
                    MEOW! The cat is AWAKE! 🎉
                </p>
            </div>
            """, unsafe_allow_html=True)
            st.balloons()
        else:
            st.markdown("""
            <div style='text-align: center; background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
                 padding: 60px; border-radius: 20px; border: 5px solid #95E1D3;'>
                <div style='font-size: 100px;'>😴</div>
                <p style='color: white; font-size: 24px; margin-top: 20px;'>
                    Zzzzz... The cat is SLEEPING! 💤
                </p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Explanation
    st.markdown("""
    ### 🎓 What Does This Mean?
    
    <div class='fun-box'>
    <p style='font-size: 18px;'>
    
    **In the REAL quantum world:**
    
    🌟 Tiny particles can be in TWO states at once! Just like our cat being awake AND sleeping!
    
    🔍 But when we LOOK at them (like opening the box), they choose ONE state!
    
    🎲 It's like magic dice that show ALL numbers until you look at them!
    
    🤯 This is called **QUANTUM SUPERPOSITION** - a super big word that means "being in many states at once!"
    
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Fun activity
    st.markdown("### 🎮 Try This Game!")
    
    if st.button("🎲 Play Quantum Guessing Game!"):
        st.markdown("**Guess: Will the cat be awake or sleeping?**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("😺 I guess AWAKE!"):
                result = np.random.choice(["awake", "sleeping"])
                if result == "awake":
                    st.success("🎉 YOU GUESSED RIGHT! The cat is awake! 😺")
                    st.balloons()
                else:
                    st.info("💤 Oops! The cat is sleeping! Try again! 😴")
        
        with col2:
            if st.button("😴 I guess SLEEPING!"):
                result = np.random.choice(["awake", "sleeping"])
                if result == "sleeping":
                    st.success("🎉 YOU GUESSED RIGHT! The cat is sleeping! 😴")
                    st.balloons()
                else:
                    st.info("😺 Oops! The cat is awake! Try again!")

# ===== QUANTUM SUPERPOSITION PAGE =====
elif page == "✨ Quantum Superposition":
    st.markdown("## ✨ Quantum Superposition - Being in Two Places at Once!")
    
    st.markdown("""
    ### 🎪 Imagine This Magic Trick!
    
    What if you could be in your room AND in the playground at the SAME TIME? 🤯
    
    That's what tiny particles can do! It's called **SUPERPOSITION**!
    """)
    
    # Interactive demo
    st.markdown("### 🎯 The Two-Door Magic Trick!")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style='text-align: center; padding: 20px; background-color: #FFE66D; border-radius: 10px;'>
            <div style='font-size: 60px;'>🚪</div>
            <p style='font-size: 18px;'><b>Door 1</b></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='text-align: center; padding: 20px;'>
            <div style='font-size: 60px;'>🧒</div>
            <p style='font-size: 18px;'><b>You!</b></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='text-align: center; padding: 20px; background-color: #95E1D3; border-radius: 10px;'>
            <div style='font-size: 60px;'>🚪</div>
            <p style='font-size: 18px;'><b>Door 2</b></p>
        </div>
        """, unsafe_allow_html=True)
    
    if st.button("👟 Normal Walk - Choose ONE Door"):
        choice = np.random.choice([1, 2])
        if choice == 1:
            st.info("🚶 You walked through Door 1! You can only go through ONE door!")
        else:
            st.info("🚶 You walked through Door 2! You can only go through ONE door!")
    
    if st.button("✨ QUANTUM Walk - Go Through BOTH!"):
        st.markdown("""
        <div style='text-align: center; background: linear-gradient(90deg, #FFE66D 0%, #95E1D3 100%); 
             padding: 40px; border-radius: 15px; margin: 20px 0;'>
            <div style='font-size: 80px;'>✨🧒✨</div>
            <p style='font-size: 24px; font-weight: bold;'>
                WOW! You went through BOTH doors at the same time! 🤯
            </p>
            <p style='font-size: 18px;'>
                This is QUANTUM SUPERPOSITION! Being in two places at once!
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()
    
    st.markdown("---")
    
    # Spinning top demo
    st.markdown("### 🔄 The Magic Spinning Top!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🔵 Normal Spinning Top")
        if st.button("Spin Normal Top 🔵"):
            st.markdown("""
            <div style='text-align: center; padding: 30px; background-color: #E8F4F8; border-radius: 10px;'>
                <div style='font-size: 60px;'>🔵➡️</div>
                <p style='font-size: 18px;'>Spinning clockwise ➡️</p>
            </div>
            """, unsafe_allow_html=True)
            st.write("Normal things spin in ONE direction!")
    
    with col2:
        st.markdown("#### ⚛️ Quantum Spinning Top")
        if st.button("Spin Quantum Top ⚛️"):
            st.markdown("""
            <div style='text-align: center; padding: 30px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px;'>
                <div style='font-size: 60px;'>⚛️↔️</div>
                <p style='font-size: 18px; color: white;'>Spinning BOTH ways! ↔️</p>
                <p style='font-size: 16px; color: white;'>Clockwise ➡️ AND Counter-clockwise ⬅️</p>
            </div>
            """, unsafe_allow_html=True)
            st.write("Quantum things can spin BOTH ways at once! 🤯")
    
    st.markdown("---")
    
    # Explanation
    st.markdown("""
    ### 🎓 What Did We Learn?
    
    <div class='fun-box'>
    <p style='font-size: 18px;'>
    
    **Superposition means:**
    
    ✨ Being in TWO places at once<br>
    ✨ Having TWO colors at once<br>
    ✨ Spinning TWO ways at once<br>
    ✨ Being awake AND asleep at once (like Schrödinger's cat!)<br><br>
    
    🔬 Scientists use this magic to build super powerful computers!<br><br>
    
    🎪 It's like having superpowers, but only TINY particles can do it!<br><br>
    
    👀 When we look at them, they have to CHOOSE one thing! The magic disappears!
    
    </p>
    </div>
    """, unsafe_allow_html=True)

# ===== QUANTUM AI PAGE =====
elif page == "🤖 Quantum AI Magic":
    st.markdown("## 🤖 Quantum AI - Super Smart Computers!")
    
    st.markdown("""
    ### 🎮 What is AI (Artificial Intelligence)?
    
    **AI** is like having a ROBOT BRAIN 🧠 that can:
    - Learn new things 📚
    - Solve puzzles 🧩
    - Play games 🎮
    - Talk to you! 💬
    """)
    
    st.markdown("---")
    
    # Compare normal vs quantum AI
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🖥️ Normal Computer Brain")
        st.markdown("""
        <div style='background-color: #E8F4F8; padding: 20px; border-radius: 10px;'>
            <p style='font-size: 40px; text-align: center;'>🖥️</p>
            <p style='font-size: 18px;'>
            Normal computers think like this:<br><br>
            
            Question: "What's 2 + 2?"<br>
            💭 Thinking... thinking... thinking...<br>
            ✅ Answer: 4!<br><br>
            
            They check ONE answer at a time! ⏱️
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### ⚛️ Quantum Computer Brain")
        st.markdown("""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 10px;'>
            <p style='font-size: 40px; text-align: center;'>⚛️</p>
            <p style='font-size: 18px; color: white;'>
            Quantum computers are MAGICAL:<br><br>
            
            Question: "What's the best ice cream?"<br>
            💭 Checking ALL flavors AT ONCE!<br>
            ✅ Answer in super-speed! ⚡<br><br>
            
            They check MANY answers at the SAME time! 🤯
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Interactive puzzle demo
    st.markdown("### 🧩 Let's Play a Puzzle Game!")
    
    st.markdown("**Find the MAGIC NUMBER! (Between 1-10)**")
    
    magic_number = np.random.randint(1, 11)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🖥️ Normal Computer Way")
        if st.button("🔍 Let Normal Computer Search"):
            progress = st.progress(0)
            status = st.empty()
            
            for i in range(1, 11):
                progress.progress(i * 10)
                status.write(f"🤔 Checking number {i}...")
                time.sleep(0.5)
                if i == magic_number:
                    status.write(f"✅ Found it! The magic number is {magic_number}!")
                    break
            
            st.info("⏱️ This took a while! Normal computers check ONE number at a time!")
    
    with col2:
        st.markdown("#### ⚛️ Quantum Computer Way")
        if st.button("⚡ Let Quantum Computer Search"):
            with st.spinner("✨ Checking ALL numbers at once..."):
                time.sleep(1)  # Just for effect
            
            st.success(f"⚡ Found it instantly! The magic number is {magic_number}!")
            st.balloons()
            st.info("🚀 Quantum computers are SUPER FAST! They check EVERYTHING at once!")
    
    st.markdown("---")
    
    # What can Quantum AI do?
    st.markdown("### 🌟 What Can Quantum AI Do?")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style='text-align: center; background-color: #FFE66D; padding: 20px; border-radius: 10px;'>
            <div style='font-size: 50px;'>🏥</div>
            <p style='font-size: 16px;'><b>Help Doctors</b></p>
            <p>Find medicines super fast!</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='text-align: center; background-color: #95E1D3; padding: 20px; border-radius: 10px;'>
            <div style='font-size: 50px;'>🌍</div>
            <p style='font-size: 16px;'><b>Save Earth</b></p>
            <p>Solve climate problems!</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='text-align: center; background-color: #FF6B6B; padding: 20px; border-radius: 10px; color: white;'>
            <div style='font-size: 50px;'>🚀</div>
            <p style='font-size: 16px;'><b>Space Travel</b></p>
            <p>Plan trips to stars!</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Fun facts
    st.markdown("""
    ### 🎓 Cool Facts About Quantum AI!
    
    <div class='fun-box'>
    <p style='font-size: 18px;'>
    
    🔢 **Quantum Bits (Qubits)**: Normal computers use 0 and 1. Quantum computers use 0, 1, AND BOTH at the same time! 🤯<br><br>
    
    ❄️ **Super Cold**: Quantum computers need to be VERY cold - colder than space! 🥶<br><br>
    
    🎯 **Solving Big Puzzles**: They can solve puzzles that would take normal computers MILLIONS of years! ⏰<br><br>
    
    🔮 **Future is Quantum**: Scientists are building these right now to make the world better! 🌈<br><br>
    
    🎪 **It's Magic Science**: It's real, but feels like magic! That's why science is so cool! ✨
    
    </p>
    </div>
    """, unsafe_allow_html=True)

# ===== PLAY & LEARN PAGE =====
elif page == "🎮 Play & Learn":
    st.markdown("## 🎮 Fun Games to Learn Quantum Physics!")
    
    # Game selector
    game = st.selectbox(
        "Choose a game! 🎯",
        ["🎨 Quantum Coloring", "🎲 Superposition Dice", "🔮 Quantum Memory Game", "⚡ Speed Quiz"]
    )
    
    if game == "🎨 Quantum Coloring":
        st.markdown("### 🎨 Quantum Coloring - Colors that Mix!")
        
        st.markdown("""
        In quantum world, things can be TWO colors at once!
        
        Pick two colors and see the magic! ✨
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            color1 = st.color_picker("Pick first color 🎨", "#FF6B6B")
        
        with col2:
            color2 = st.color_picker("Pick second color 🎨", "#4ECDC4")
        
        if st.button("✨ Create Quantum Color!"):
            st.markdown(f"""
            <div style='text-align: center;'>
                <div style='display: inline-block; width: 100px; height: 100px; background-color: {color1}; 
                     border-radius: 50%; margin: 10px; border: 3px solid black;'></div>
                <div style='display: inline-block; font-size: 40px; margin: 10px;'>+</div>
                <div style='display: inline-block; width: 100px; height: 100px; background-color: {color2}; 
                     border-radius: 50%; margin: 10px; border: 3px solid black;'></div>
                <div style='display: inline-block; font-size: 40px; margin: 10px;'>=</div>
                <div style='display: inline-block; width: 150px; height: 150px; 
                     background: linear-gradient(135deg, {color1} 0%, {color2} 100%); 
                     border-radius: 50%; margin: 10px; border: 5px solid gold; box-shadow: 0 0 20px gold;'></div>
            </div>
            <p style='text-align: center; font-size: 24px; margin-top: 20px;'>
                ✨ QUANTUM SUPERPOSITION COLOR! ✨<br>
                It's BOTH colors at once! 🌈
            </p>
            """, unsafe_allow_html=True)
            st.balloons()
    
    elif game == "🎲 Superposition Dice":
        st.markdown("### 🎲 Superposition Dice - Showing All Numbers!")
        
        st.markdown("""
        Normal dice show ONE number. Quantum dice show ALL numbers until you look! 👀
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Normal Dice 🎲")
            if st.button("🎲 Roll Normal Dice"):
                result = np.random.randint(1, 7)
                st.markdown(f"""
                <div style='text-align: center; background-color: #FFE66D; padding: 40px; border-radius: 15px;'>
                    <div style='font-size: 80px;'>🎲</div>
                    <p style='font-size: 40px; font-weight: bold;'>{result}</p>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("#### Quantum Dice ⚛️")
            if st.button("✨ Roll Quantum Dice"):
                # Show all possibilities first
                st.markdown("""
                <div style='text-align: center; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                     padding: 40px; border-radius: 15px;'>
                    <p style='color: white; font-size: 24px;'>Showing ALL numbers at once!</p>
                    <p style='font-size: 40px;'>1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣</p>
                    <p style='color: white; font-size: 18px;'>Now you looked! It chooses...</p>
                """, unsafe_allow_html=True)
                
                time.sleep(1)
                
                result = np.random.randint(1, 7)
                st.markdown(f"""
                    <p style='font-size: 50px; font-weight: bold; text-align: center;'>{result}!</p>
                </div>
                """, unsafe_allow_html=True)
    
    elif game == "🔮 Quantum Memory Game":
        st.markdown("### 🔮 Quantum Memory Game")
        
        st.markdown("The particle is hiding in ONE of these boxes! Can you find it? 🔍")
        
        if 'particle_location' not in st.session_state:
            st.session_state.particle_location = np.random.randint(0, 3)
            st.session_state.guessed = False
        
        if st.button("🔄 New Game"):
            st.session_state.particle_location = np.random.randint(0, 3)
            st.session_state.guessed = False
            st.rerun()
        
        cols = st.columns(3)
        
        for i, col in enumerate(cols):
            with col:
                if st.button(f"📦 Box {i+1}", key=f"box_{i}"):
                    st.session_state.guessed = True
                    if i == st.session_state.particle_location:
                        st.success("🎉 YOU FOUND IT! The particle was here! ✨")
                        st.balloons()
                    else:
                        st.error(f"💫 Not here! The particle was in Box {st.session_state.particle_location + 1}!")
        
        if not st.session_state.guessed:
            st.info("✨ The particle is in SUPERPOSITION - it's in ALL boxes until you check! 🤯")
    
    elif game == "⚡ Speed Quiz":
        st.markdown("### ⚡ Quantum Speed Quiz!")
        
        questions = [
            {
                "q": "Can tiny particles be in two places at once?",
                "a": ["Yes! ✅", "No ❌"],
                "correct": 0
            },
            {
                "q": "What is Schrödinger's famous example about?",
                "a": ["A cat 🐱", "A dog 🐕", "A bird 🐦"],
                "correct": 0
            },
            {
                "q": "Are quantum computers faster than normal computers?",
                "a": ["Yes! ⚡", "No 🐌"],
                "correct": 0
            },
            {
                "q": "What falls down because of gravity?",
                "a": ["Apples 🍎", "Birds 🐦", "Clouds ☁️"],
                "correct": 0
            }
        ]
        
        if 'quiz_score' not in st.session_state:
            st.session_state.quiz_score = 0
            st.session_state.quiz_question = 0
        
        if st.session_state.quiz_question < len(questions):
            current_q = questions[st.session_state.quiz_question]
            
            st.markdown(f"#### Question {st.session_state.quiz_question + 1}: {current_q['q']}")
            
            for i, answer in enumerate(current_q['a']):
                if st.button(answer, key=f"q_{st.session_state.quiz_question}_a_{i}"):
                    if i == current_q['correct']:
                        st.success("🎉 Correct!")
                        st.session_state.quiz_score += 1
                    else:
                        st.error("💫 Oops! Try to remember for next time!")
                    
                    st.session_state.quiz_question += 1
                    time.sleep(1)
                    st.rerun()
        else:
            st.markdown(f"""
            <div style='text-align: center; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                 padding: 40px; border-radius: 15px;'>
                <h2 style='color: white;'>🎉 Quiz Complete! 🎉</h2>
                <p style='font-size: 40px; color: white;'>Your Score: {st.session_state.quiz_score}/{len(questions)}</p>
                <p style='font-size: 24px; color: white;'>You're a Quantum Superstar! ⭐</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("🔄 Play Again"):
                st.session_state.quiz_score = 0
                st.session_state.quiz_question = 0
                st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <p style='font-size: 20px; color: #667eea;'>
        🌟 Keep exploring the magical world of quantum physics! 🌟<br>
        Remember: Science is like magic, but REAL! ✨<br>
        <b>You're never too young to be a scientist! 🔬</b>
    </p>
</div>
""", unsafe_allow_html=True)
