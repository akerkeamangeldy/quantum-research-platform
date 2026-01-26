import streamlit as st
import numpy as np
import io
import wave

st.set_page_config(page_title="Apex Team — Rockers Showcase", layout="centered")
st.title("Apex Team — Rockers Showcase")
st.markdown("A small demo that shows the `Apex Team` of rockers — pick a rocker and play a short riff.")


def generate_tone(freq=440.0, duration=1.0, volume=0.5, sample_rate=44100):
    """Return WAV bytes for a sine tone."""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(freq * t * 2 * np.pi)
    # simple envelope to avoid clicks
    envelope = np.linspace(0, 1, int(0.01 * sample_rate))
    tone[: envelope.size] *= envelope
    tone[-envelope.size :] *= envelope[::-1]
    audio = (tone * (32767 * volume)).astype(np.int16)
    buf = io.BytesIO()
    with wave.open(buf, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(audio.tobytes())
    buf.seek(0)
    return buf.read()


rockers = [
    {"name": "Axel", "role": "Lead Guitar", "seed": "axel-rock" , "freq": 440},
    {"name": "Roxy", "role": "Drums", "seed": "roxy-beat" , "freq": 220},
    {"name": "Slashy", "role": "Bass", "seed": "slashy-low" , "freq": 110},
]

cols = st.columns(len(rockers))
for col, rocker in zip(cols, rockers):
    with col:
        img_url = f"https://avatars.dicebear.com/api/avataaars/{rocker['seed']}.png?size=128"
        st.image(img_url, width=128)
        st.subheader(rocker["name"]) 
        st.caption(rocker["role"])
        if st.button(f"Play riff — {rocker['name']}"):
            wav = generate_tone(freq=rocker["freq"], duration=1.2, volume=0.6)
            st.audio(wav, format="audio/wav")

st.write('Enjoy the little demo — press a "Play riff" button to hear a short tone representing each rocker.')
