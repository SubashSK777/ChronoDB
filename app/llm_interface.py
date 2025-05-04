# app/llm_interface.py
import subprocess

def ask_ollama(question, context=""):
    prompt = f"Context:\n{context}\n\nQuestion: {question}"
    result = subprocess.run(
        ["ollama", "run", "llama2"],
        input=prompt.encode(),
        stdout=subprocess.PIPE
    )
    return result.stdout.decode()
