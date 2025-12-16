import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os

# -------------------------
# Hugging Face private repo token (from Space secret)
# -------------------------
# Add your token in Space Settings → Secrets → Name: HF_TOKEN
HF_TOKEN = os.environ["HF_TOKEN"]

# -------------------------
# Load model from Hub
# -------------------------
MODEL_PATH = "Priikshit/nf_gemma_test"  # Your private fine-tuned Gemma-3 model

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, use_auth_token=HF_TOKEN)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    device_map="auto",
    torch_dtype=torch.float16,
    use_auth_token=HF_TOKEN
)

# -------------------------
# System prompt for domain restriction
# -------------------------
SYSTEM_PROMPT = (
    "You are NF_GPT — a Natural Farming domain expert chatbot. "
    "You must only answer questions related to natural farming, soil health, composting, "
    "organic pest control, sustainable agriculture, or crop management. "
    "If someone asks about anything else, politely say: "
    "'I'm sorry, I can only answer questions related to natural farming.'"
)

# -------------------------
# Response function
# -------------------------
def respond(message, history):
    # Combine chat history into prompt
    history_text = "\n".join([f"User: {u}\nAssistant: {a}" for u, a in history])
    prompt = f"{SYSTEM_PROMPT}\n\n{history_text}\nUser: {message}\nAssistant:"

    # Tokenize input
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    # Generate model output
    outputs = model.generate(
        **inputs,
        max_new_tokens=256,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        pad_token_id=tokenizer.eos_token_id,
    )

    # Decode generated tokens
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Extract assistant's latest reply
    if "Assistant:" in response:
        response = response.split("Assistant:")[-1].strip()

    return response

# -------------------------
# Build Gradio ChatInterface
# -------------------------
chatbot = gr.ChatInterface(
    fn=respond,
    title="🌾 VARTA AI",
    description="Ask questions about natural farming, compost, soil health, and sustainable agriculture.",
    theme="soft",
)

# -------------------------
# Launch app
# -------------------------
if __name__ == "__main__":
    chatbot.launch()