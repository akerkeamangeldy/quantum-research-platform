import streamlit as st
import numpy as np

st.set_page_config(page_title="Apex Team — Quantum Playground", layout="centered")
st.title("Apex Team — Quantum Playground")

st.markdown(
    """
    **Welcome!** This is a fun, tiny interactive demo about qubits, quantum measurement,
    and a baby-friendly explanation of quantum ideas — explained simply so anyone (even a 5-year-old)
    can get a feel for them.
    """
)

st.header("What is a qubit? (like a magic coin)")
st.write(
    "A qubit is like a magic coin that can be both heads and tails at the same time — until you look!"
)

st.subheader("Play with a single qubit")
theta = st.slider("Angle theta (how much heads vs tails)", 0.0, np.pi, float(np.pi / 3))
phi = st.slider("Phase phi (a funny twist, try different values)", 0.0, 2 * np.pi, 0.0)

st.write("Try pressing the gates to change the qubit, then press Measure to see the result.")

# Represent qubit state: |psi> = cos(theta/2)|0> + e^{i phi} sin(theta/2)|1>
def make_state(theta, phi):
    a = np.cos(theta / 2)
    b = np.exp(1j * phi) * np.sin(theta / 2)
    return np.array([a, b], dtype=complex)

state = make_state(theta, phi)

st.subheader("Current quantum state")
st.write("State vector (complex amplitudes):")
st.latex(r"\begin{bmatrix} %s \\ %s \end{bmatrix}" % (f"{state[0]:.3f}", f"{state[1]:.3f}"))

prob0 = np.abs(state[0]) ** 2
prob1 = np.abs(state[1]) ** 2

st.write("Probabilities:")
st.bar_chart({"|0> (heads)": prob0, "|1> (tails)": prob1})

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Apply X (flip)"):
        # Pauli-X flips amplitudes
        state = np.array([state[1], state[0]])
        prob0 = np.abs(state[0]) ** 2
        prob1 = np.abs(state[1]) ** 2
        st.experimental_rerun()
with col2:
    if st.button("Apply H (mix)"):
        # Hadamard on basis |0>,|1>
        h = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
        state = h.dot(state)
        prob0 = np.abs(state[0]) ** 2
        prob1 = np.abs(state[1]) ** 2
        st.experimental_rerun()
with col3:
    if st.button("Reset"):
        st.experimental_rerun()

st.subheader("Measure (look at the magic coin)")
shots = st.number_input("How many times to measure (repeat)", min_value=1, max_value=1000, value=50)
if st.button("Measure"):
    # sample measurement outcomes according to probabilities
    outcomes = np.random.choice([0, 1], size=shots, p=[prob0, prob1])
    counts0 = int((outcomes == 0).sum())
    counts1 = int((outcomes == 1).sum())
    st.write(f"Measured {counts0} heads (|0>) and {counts1} tails (|1>) out of {shots} tries.")
    st.bar_chart({"|0> (heads)": counts0 / shots, "|1> (tails)": counts1 / shots})

st.markdown("---")

st.header("Quantum machine learning — super simple idea")
st.write(
    "Machine learning can learn patterns. Imagine teaching a program to guess whether our magic coin will be heads or tails more often, by looking at the angle (theta)."
)

# Tiny toy dataset: sample several thetas and label by prob0>prob1
thetas = np.linspace(0, np.pi, 9)
labels = (np.cos(thetas / 2) ** 2 > 0.5).astype(int)  # 1 if more |0>
st.write("Here are some example thetas and whether they produce more heads (1) or tails (0):")
st.table({"theta": thetas.round(2), "more_heads(1)/tails(0)": labels})

st.write(
    "A tiny learner can pick a threshold: if theta is less than about 1.0, it predicts heads, otherwise tails. Try it!"
)
threshold = st.slider("Learner threshold for theta", 0.0, float(np.pi), 1.0)
preds = (thetas < threshold).astype(int)
acc = (preds == labels).mean()
st.write(f"Learner accuracy on examples: {acc*100:.1f}%")

st.markdown("---")
st.header("Explain like you're five")
st.write(
    "- A qubit is a magic coin that can be both heads and tails until you look.\n"
    "- `theta` changes how much it likes heads vs tails.\n"
    "- `phi` is a tiny twist — it changes how the magic behaves when we mix coins.\n"
    "- Gates like `X` and `H` are like toy moves: `X` flips the coin, `H` mixes it so it becomes very unsure.\n"
    "- Measuring is looking: you see either heads or tails, and randomness decides each time according to probabilities."
)

st.markdown("---")
st.caption("Demo made for fun by Apex Team — enjoy exploring qubits!")

st.markdown("---")
st.header("История про Шрёдингера и кота — по-простому (на русском)")
st.write(
    "Я люблю Эрвина Шрёдингера — он придумал важные идеи о том, как ведут себя очень маленькие частички."
)

st.subheader("Короткая история")
st.write(
    "Эрвин Шрёдингер был умным учёным. Он придумал уравнение — как карта, которая показывает, какие бывают варианты для частички и как они меняются со временем."
)

st.subheader("Кот Шрёдингера — мысленный эксперимент")
st.write(
    "Представь коробку и игрушечного кота. Внутри коробки есть волшебная штука, которая иногда делает игрушку ‘в порядке’, а иногда ‘не в порядке’. Пока ты не открыл коробку, мы не знаем — и поэтому можно сказать, что кошка как будто в двух состояниях сразу. Когда откроешь — увидишь только одно. Шрёдингер придумал это, чтобы показать, как странно работают правила квантового мира, если их переносить на большие вещи."
)

if 'cat_in_box' not in st.session_state:
    st.session_state['cat_in_box'] = False
    st.session_state['cat_alive'] = None

col_a, col_b = st.columns([1, 2])
with col_a:
    if st.button('Положить кота в коробку'):
        st.session_state['cat_in_box'] = True
        st.session_state['cat_alive'] = None
        st.experimental_rerun()
    if st.button('Открыть коробку'):
        if not st.session_state['cat_in_box']:
            st.info('Сначала положи кота в коробку.')
        else:
            # измерение: 50/50
            alive = np.random.rand() < 0.5
            st.session_state['cat_alive'] = bool(alive)
            st.session_state['cat_in_box'] = False
            st.experimental_rerun()

with col_b:
    if st.session_state['cat_in_box']:
        st.markdown('📦 КОРОБКА закрыта — не заглядывай!')
        st.write('Кошка может быть и "в порядке", и "не в порядке" одновременно, пока мы не посмотрим.')
    elif st.session_state['cat_alive'] is None:
        st.markdown('🛋️ Коробка пуста — положи кота и нажми «Открыть коробку».')
    else:
        if st.session_state['cat_alive']:
            st.markdown('😺 Кот жив!')
            st.write('Мы открыли коробку и увидели, что кот в порядке. Так бывает — результат случайный.')
        else:
            st.markdown('💤 Кот не в порядке (это мысл experiment — игрушечная ситуация).')
            st.write('Мы открыли коробку и увидели другой результат. Шрёдингер хотел показать, как странно это выглядит.')

st.markdown('---')
st.header('Что Шрёдингер дал науке — простыми словами')
st.write(
    '1) Уравнение Шрёдингера — это как карта для частичек: оно говорит, какие варианты у них есть и как они меняются.\n'
    '2) Его идеи помогли учёным предсказывать поведение атомов и молекул — это лежит в основе многих технологий, например, лазеров и электроники.\n'
    '3) Мы используем эти идеи в квантовой физике и сейчас учимся строить компьютеры нового типа — квантовые компьютеры.'
)

st.write('Если хочешь, я могу добавить картинку кота, анимацию открытия коробки или небольшую игру, где ребёнок сам будет измерять кота много раз и смотреть, как часто выпадает тот или иной результат. Что добавить дальше?')
