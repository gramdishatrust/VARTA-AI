Natural Farming QA baseline Model 🌱
Fine-tune Google's Gemma 3 1B model for answering questions about natural farming practices using Supervised Fine-Tuning (SFT).

📋 Overview
This project demonstrates how to fine-tune the google/gemma-3-1b-it model on a custom dataset of natural farming questions and answers. The model is trained to provide knowledgeable responses about sustainable and natural farming techniques.

🚀 Features
Model: Google Gemma 3 1B Instruction-Tuned
Training Method: Supervised Fine-Tuning (SFT) using TRL library
Hardware Support: GPU acceleration with automatic mixed precision
📋 Requirements
Hardware
Google Colab with GPU runtime (T4 or better)
Software Dependencies
torch
tensorboard
transformers
datasets
accelerate
evaluate
trl
sentencepiece
huggingface-hub
🛠️ Installation
Clone the repository
git clone https://github.com/prikshitkverma/Gemma_fine_tuning.git
cd Gemma_fine_tuning
Install dependencies
pip install -q -U torch tensorboard
pip install -q -U transformers datasets accelerate evaluate trl sentencepiece
📊 Dataset Format
Format
Your dataset should be in JSONL format with the following structure:
json{
  "messages": [
    {"role": "user", "content": "What is natural farming?"},
    {"role": "assistant", "content": "Natural farming is an agricultural practice that..."}
  ]
}
Example Dataset
jsonl{"messages": [{"role": "user", "content": "How do I make compost?"}, {"role": "assistant", "content": "To make compost, collect organic materials like..."}]}
{"messages": [{"role": "user", "content": "What is mulching?"}, {"role": "assistant", "content": "Mulching is the practice of covering soil with..."}]}
{"messages": [{"role": "user", "content": "Best crops for beginners?"}, {"role": "assistant", "content": "For beginners, consider starting with tomatoes..."}]}


🔧 Configuration
1. Hugging Face Authentication
Option 1: Direct Token (Default)
Replace the placeholder token in the script:
pythonHF_TOKEN = "hf_your_actual_token_here"
login(token=HF_TOKEN)
Option 2: Google Colab Secret Vault
Uncomment the following lines:
pythonfrom google.colab import userdata
HF_TOKEN = userdata.get('HF_TOKEN')
login(token=HF_TOKEN)
Getting Your Hugging Face Token:

Visit https://huggingface.co/settings/tokens
Create a new token with "write" access
Copy and paste it into the script


2. Model Configuration
base_model = "google/gemma-3-1b-it"
output_dir = "./gemma-natural-farming-qa"  # keep ypur desired name 
data_file = "/content/nf_datasett.jsonl"   # Update path as needed

Ensure your Hugging Face token has read permissions
Verify token is correctly set in the code
For limited GPU memory:


🙏 Acknowledgments
Google for the Gemma model series
Hugging Face for the transformers and TRL libraries
📚 Additional Resources
Gemma Model Documentation
TRL Library Documentation
Hugging Face Fine-tuning Guide
Note: This model is for educational and research purposes. Always verify agricultural advice with local experts and extension services.
