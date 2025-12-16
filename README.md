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

### 1. Clone the Repository
```bash
git clone https://github.com/gramdishatrust/VARTA-AI.git

```
2. Install Dependencies
## 🛠️ Installation
As given in [GoogleColab file gemma_3_1b_it_test.ipynb](gemma_3_1b_it_test.ipynb)

🔧 Configuration
1. HuggingFace Authentication

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

2. Select GPU in Colab
   <img width="838" height="784" alt="image" src="https://github.com/user-attachments/assets/8c8b5c2a-6f19-433a-9446-677a33412963" />

3. Upload Initial Dataset
   Upload the initial file to Colab File Upload [nf_datasett.jsonl] (nf_datasett.jsonl)
   <img width="579" height="745" alt="image" src="https://github.com/user-attachments/assets/edf7e930-951e-4ebc-8c9c-540db631b414" />
   ## Choose your LM Model 

<img width="431" height="242" alt="image" src="https://github.com/user-attachments/assets/fcc746d9-1880-4364-9802-0c0f904ac58f" />



4. Enable Gated Access to Models on Huggingface
   <img width="1465" height="983" alt="image" src="https://github.com/user-attachments/assets/68778112-cc04-47e6-a416-257226d5f604" />

   ensure the access is granted for the Model as here
   <img width="739" height="364" alt="image" src="https://github.com/user-attachments/assets/6dceb069-54df-4029-8dd6-27ca825335c9" />

5. Run the Sections on Colab sequentially - it is important not to Run them all together for efficiency reasons. At this stage the dependency libraries will be redundantly installed and the "7. TRAIN AND VALIDATE MODEL" sections takes a lot of compute space and time to Train and Validate the model.

6. As the Epoch loops are configured to 3 choose the checkpoint files for Model based on the least Training Losses as indicated by Colab. In our case it is checkpoint 252
   <img width="896" height="430" alt="image" src="https://github.com/user-attachments/assets/70441c36-b55d-44c3-bed4-9a3f217e62de" />

7. Download the files from the checkpoint and upload them to Huggingface Model for which these are built. In our case this remains google/gemma-3-1b-it
   <img width="871" height="169" alt="image" src="https://github.com/user-attachments/assets/515318bf-7962-482d-8d00-a5a651d7a5fd" />

8. Now create Spaces on Huggingface and use this interface to create the first file in the Space
<img width="1107" height="487" alt="image" src="https://github.com/user-attachments/assets/d5c9f8b4-6cbe-4be7-866b-cd5e90dde3e6" />

9. Now use the file for the Spaces chatbot as![app.py](app.py) and ![requirements.txt](requirements.txt) - move these files also the Spaces on Huggingface.Make sure to modify the Model in the app.py file so that the Model may be linked to the Spaces.
<img width="1060" height="184" alt="image" src="https://github.com/user-attachments/assets/be14da78-08cc-45bd-affc-23d15ed72642" />
<img width="1556" height="663" alt="image" src="https://github.com/user-attachments/assets/3cbc2572-2d8d-4137-8dd4-c63ff3e2a740" />


11. Replace the secret key (Spaces --> Settings) - which was generated in Huggingface earlier and used for the Google Colab model in step 1 above. Replace it in the variable HF_TOKEN as given in the app.py file with the same key.
<img width="1767" height="446" alt="image" src="https://github.com/user-attachments/assets/3cca7995-2b1f-4bc1-a6ee-12cd106f219e" />

    
13. Run the Spaces Model - in our case this Gradio
    
    
   
   
   




