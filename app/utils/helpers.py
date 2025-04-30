import pandas as pd
from pathlib import Path
import streamlit as st

def load_data(base_dir):
    careers_path = base_dir / "app" / "data" / "careers.csv"
    return pd.read_csv(careers_path), None

def render_profession_card(profession, skills, resources, index):
    with st.expander(f"Option {index+1}: {profession}", expanded=index==0):
        col1, col2 = st.columns([1, 1])
        with col1:
            st.subheader("Key Skills")
            for skill in skills.split(", "):
                st.markdown(f"- {skill}")
        with col2:
            st.subheader("Recommended Resources")
            for resource in resources.split(", "):
                st.markdown(f"- {resource}")

def render_roadmap(roadmap):
    st.subheader("📚 Learning Roadmap")
    for phase in roadmap:
        st.markdown(f"### {phase['phase']} ({phase['duration']})")
        for task in phase['tasks']:
            st.markdown(f"- {task}")
        st.markdown("---")