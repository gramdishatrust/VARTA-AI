🌱 Natural Farming QA - Gemma 3 Fine-Tuning
Fine-tune Google's Gemma 3 1B model for answering questions about natural farming practices using Supervised Fine-Tuning (SFT).

📋 Overview
This project demonstrates how to fine-tune the google/gemma-3-1b-it model on a custom dataset of natural farming questions and answers. The model is trained to provide knowledgeable responses about sustainable and natural farming techniques.
🚀 Features

Model: Google Gemma 3 1B Instruction-Tuned
Training Method: Supervised Fine-Tuning (SFT) using TRL library
Hardware Support: GPU acceleration with automatic mixed precision
Easy Integration: Works seamlessly with Hugging Face Hub
Custom Dataset: Train on your own natural farming Q&A data


📋 Requirements
Hardware

Google Colab with GPU runtime (T4 or better recommended)
Alternative: Local machine with CUDA-compatible GPU (8GB+ VRAM)

Software Dependencies
txttorch
tensorboard
transformers
datasets
accelerate
evaluate
trl
sentencepiece
huggingface-hub

🛠️ Installation
1. Clone the Repository
bashgit clone https://github.com/prikshitkverma/Gemma_fine_tuning.git
cd Gemma_fine_tuning
2. Install Dependencies
bashpip install -q -U torch tensorboard
pip install -q -U transformers datasets accelerate evaluate trl sentencepiece huggingface-hub

📊 Dataset Format
Required Structure
Your dataset should be in JSONL format with the following structure:
json{
  "messages": [
    {
      "role": "user",
      "content": "What is natural farming?"
    },
    {
      "role": "assistant",
      "content": "Natural farming is an agricultural practice that..."
    }
  ]
}
Example Dataset (nf_dataset.jsonl)
jsonl{"messages": [{"role": "user", "content": "How do I make compost?"}, {"role": "assistant", "content": "To make compost, collect organic materials like kitchen scraps, leaves, and grass clippings. Layer them in a bin, keep moist, and turn regularly for aeration."}]}
{"messages": [{"role": "user", "content": "What is mulching?"}, {"role": "assistant", "content": "Mulching is the practice of covering soil with organic materials like straw, leaves, or wood chips to retain moisture, suppress weeds, and improve soil health."}]}
{"messages": [{"role": "user", "content": "Best crops for beginners?"}, {"role": "assistant", "content": "For beginners, consider starting with tomatoes, lettuce, radishes, and herbs like basil. These are forgiving and provide quick results."}]}
Dataset Guidelines
FieldDescriptionroleEither "user" (question) or "assistant" (answer)contentThe actual text of the question or answerFormatEach line is a complete JSON object (JSONL)

🔧 Configuration
1. Hugging Face Authentication
Option A: Direct Token (Default)
Replace the placeholder token in your script:
pythonHF_TOKEN = "hf_your_actual_token_here"
from huggingface_hub import login
login(token=HF_TOKEN)
Option B: Google Colab Secret Vault
Uncomment and use these lines:
pythonfrom google.colab import userdata
HF_TOKEN = userdata.get('HF_TOKEN')
from huggingface_hub import login
login(token=HF_TOKEN)
Getting Your Hugging Face Token

Visit https://huggingface.co/settings/tokens
Create a new token with "write" access
Copy and paste it into your script

2. Model Configuration
python# Base model from Hugging Face
base_model = "google/gemma-3-1b-it"

# Output directory for fine-tuned model
output_dir = "./gemma-natural-farming-qa"  # Change as needed

# Path to your training data
data_file = "/content/nf_dataset.jsonl"  # Update with your path
3. Training Parameters (Optional)
Customize these in your training script:
pythontraining_args = {
    "num_train_epochs": 3,
    "per_device_train_batch_size": 4,
    "learning_rate": 2e-5,
    "warmup_steps": 100,
    "logging_steps": 10,
    "save_steps": 100,
}



📝 License
This project is licensed under the Apache 2.0 License - see the LICENSE file for details.

🙏 Acknowledgments

Google for the Gemma model series
Hugging Face for the transformers and TRL libraries
TRL Team for the Supervised Fine-Tuning framework


⚠️ Disclaimer
This model is for educational and research purposes. Always verify agricultural advice with local experts, agricultural extension services, and scientific sources before implementation.

Made with ❤️ for sustainable agriculture
⭐ Star this repo if you find it helpful!
</div>
