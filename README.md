🌱 VARTA-AI - xLM Fine-Tuning  
Fine-tune xLM ({Small,Large},Language Models) for a conversational approach to Agroecology - Natural Farming using Supervised Fine-Tuning (SFT). The name of the project is VARTA-AI (Vital Agroecological Resource Tracking Analytics - AI)

---

## 📋 Overview
VARTA-AI project demonstrates how to develop and fine-tune Language Models - Small and Large for Agroecological Production Systems. At present the `google/gemma-3-1b-it` model is trained on a custom dataset of Natural Farming, as practiced in India (especially Himachal Pradesh). The model is trained to provide knowledgeable responses about Agroecology and Sustainable Agricultural Practices for crop production and natural farming techniques. The Model also create a Knowledge base which may be continously trained for improved qualitative responses to queries by Farmers and Researchers. 

## Background
This project is mentored by Gram Disha Trust as part of the VARTA (Vital Agroecological Resource Tracking Analytics) framework. The systems architecture of VARTA also links to an Internet of Things (IoT) implementation of VARTA ( VARTA-IoT ). More details at this location - https://gramdisha.org/iot-agritech-smallholders/#:~:text=been%20finalized%20as%3A-,Vital%20Agroecological%20Resource%20Tracking%20Analytics%20(VARTA),-VARTA%20(phonetically%20V%C4%81rt%C4%81
 
---

## 🚀 Initial Features
- **Model:** Google Gemma 3 1B Instruction-Tuned - additionally Interations also possible with - SmoLLM 2, Llama 3.2, Qwen 2.5
- **Training Method:** Supervised Fine-Tuning (SFT) using TRL library  
- **Easy Integration:** Works seamlessly with Hugging Face Hub  
- **Custom Dataset:** Train on your own Agroecological Production related Q&A data  

---

## 📋 Requirements

### Hardware
- Google Colab with GPU runtime (T4 or better recommended)  OR Kegel with GPU (upto 30 Hours Monthly)


### Software Libary Dependencies on Python
- torch  
- tensorboard  
- transformers  
- datasets  
- accelerate  
- evaluate  
- trl  
- sentencepiece  
- huggingface-hub  

---

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/gramdishatrust/VARTA-AI.git
cd xLM_fine_tuning 
```
2. Install Dependencies
```bash
pip install -q -U torch tensorboard
pip install -q -U transformers datasets accelerate evaluate trl sentencepiece huggingface-hub
```
Dataset Format
Required Structure
```bash
Your dataset should be in JSONL format with the following structure:
{
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
```
Example Dataset (nf_dataset.jsonl)
```bash
{"messages": [{"role": "user", "content": "How do I make compost?"}, {"role": "assistant", "content": "To make compost, collect organic materials like kitchen scraps, leaves, and grass clippings. Layer them in a bin, keep moist, and turn regularly for aeration."}]}
{"messages": [{"role": "user", "content": "What is mulching?"}, {"role": "assistant", "content": "Mulching is the practice of covering soil with organic materials like straw, leaves, or wood chips to retain moisture, suppress weeds, and improve soil health."}]}
{"messages": [{"role": "user", "content": "Best crops for beginners?"}, {"role": "assistant", "content": "For beginners, consider starting with tomatoes, lettuce, radishes, and herbs like basil. These are forgiving and provide quick results."}]}
```
🔧 Configuration
1. Hugging Face Authentication
Option A: Direct Token (Default)
```bash
HF_TOKEN = "hf_your_actual_token_here"
from huggingface_hub import login
login(token=HF_TOKEN)
```
Option B: Google Colab Secret Vault

Uncomment and use these lines:
```bash
from google.colab import userdata
HF_TOKEN = userdata.get('HF_TOKEN')
from huggingface_hub import login
login(token=HF_TOKEN)
```
Getting Your Hugging Face Token

Visit https://huggingface.co/settings/tokens

Create a new token with "write" access

Copy and paste it into your script

2. Model Configuration
```bash
# Base model from Hugging Face
base_model = "google/gemma-3-1b-it"

# Output directory for fine-tuned model
output_dir = "./gemma-natural-farming-qa"  # Change as needed

# Path to your training data
data_file = "/content/nf_dataset.jsonl"  # Update with your path
```




