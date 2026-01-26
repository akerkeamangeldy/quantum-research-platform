Simple Streamlit demo

Setup and run (Windows PowerShell):

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Open the local URL printed by Streamlit (usually http://localhost:8501).

New demo: `streamlit_apex.py`

Run the new Apex Team rockers demo:

```powershell
streamlit run streamlit_apex.py
```

Open http://localhost:8501 and select the `Apex Team — Rockers Showcase` app from the running apps (or open the URL printed by Streamlit).

Quantum demo: `streamlit_quantum.py`

Run the Apex Team quantum playground demo:

```powershell
streamlit run streamlit_quantum.py
```

This app is interactive: move the `theta` and `phi` sliders, press gates (`X`, `H`), and press `Measure` to see sampled outcomes. Explanations are written inside the app in simple language.
