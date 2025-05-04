# app/main.py
import streamlit as st
from app.ingest_compress import load_and_compress_csv
from app.casual_analysis import get_causal_graph, run_counterfactual
from app.explainable_ai import train_explainer
from app.llm_interface import ask_ollama

st.title("ChronoSage - Causal, Compressed, Explainable Time-Series Engine")

uploaded_file = st.file_uploader("Upload CSV", type="csv")
if uploaded_file:
    df, compressed = load_and_compress_csv(uploaded_file)
    st.write("Data Preview:", df.head())

    if st.button("Generate Causal Graph"):
        results, _ = get_causal_graph(df)
        st.write("Causal Results:", results)

    target = st.selectbox("Select target column", df.columns)
    if st.button("Explain Target"):
        shap_values, _ = train_explainer(df, target)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        shap.plots.beeswarm(shap_values)
        st.pyplot()

    col = st.selectbox("Column to Change", df.columns)
    old = st.text_input("Old Value")
    new = st.text_input("New Value")
    if st.button("Run Counterfactual"):
        new_df = run_counterfactual(df, col, old, new)
        st.write(new_df.head())

    question = st.text_input("Ask Ollama a question about the data:")
    if st.button("Ask"):
        answer = ask_ollama(question, context=df.head().to_string())
        st.write("Answer:", answer)
