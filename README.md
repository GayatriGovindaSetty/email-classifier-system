# 📧 Email Classification and PII Masking API

This project provides an API for classifying emails into predefined categories and masking sensitive personally identifiable information (PII) such as full names, emails, phone numbers, Aadhaar numbers, and more. Built using **FastAPI**, **Scikit-learn**, and deployed on **Hugging Face Spaces**.

---

## 🚀 Features

- 📨 Classifies email text into categories like spam, work, social, etc.
- 🛡️ Automatically detects and masks multiple types of PII:
  - Full Name
  - Email Address
  - Phone Number
  - Date of Birth
  - Aadhaar Number
  - Credit/Debit Card Number
  - CVV Number
  - Expiry Date
- ⚡ Real-time inference via FastAPI
- 🌐 Easily deployable to Hugging Face Spaces

---

## 📁 Project Structure
├── main.py # FastAPI app
├── models.py # Model training, loading, prediction
├── utils.py # PII masking logic
├── requirements.txt # Dependencies
├── svm_email_classifier.pkl # Trained SVM model (optional - generated after training)
├── combined_emails_with_natural_pii.csv # Dataset
└── README.md

---

## ⚙️ Setup Instructions

### ✅ Prerequisites

- Python 3.8+
- pip installed

---

### 🔧 Local Setup

1. **Clone the repository** *(or create a new directory with the above files)*:
   ```bash
   git clone <your-repo-url>
   cd email-classifier
Install dependencies:
pip install -r requirements.txt

Train the model (if not already trained):
python models.py

Run the API locally:
uvicorn main:app --reload

Open your browser and visit:
http://127.0.0.1:8000/docs

🧪 Example API Request
POST /classify

Body (JSON):
{
  "text": "Hello, my name is John Doe. My Aadhaar number is 1234-5678-9012. This is a work email."
}
Response:
{
  "category": "work",
  "masked_text": "Hello, my name is <full_name>. My Aadhaar number is <aadhar_num>. This is a work email."
}

---

🧬 PII Categories Masked
Entity	Mask	Detection Pattern Included
Full Name	            <full_name>	           Yes
Email Address	        <email>	               Yes
Phone Number	        <phone_number>	       Yes
Date of Birth	        <dob>	                 Yes
Aadhaar Number	      <aadhar_num>	         Yes
Credit/Debit Card No	<credit_debit_no>	     Yes
CVV Number	          <cvv_no>	             Yes
Expiry Date	          <expiry_no>	           Yes

🛰️ Deploying on Hugging Face Spaces
Go to Hugging Face Spaces

Click Create new Space

Fill in:

Space name (e.g., email-classifier)

SDK: Select "FastAPI"

Upload the following files:
main.py
models.py
utils.py
requirements.txt
combined_emails_with_natural_pii.csv

Optionally, create .gitattributes to avoid Git tracking issues.

Wait for the build to complete. Test at:
https://emailclassifier.hf.space/docs

---

🛠️ Tech Stack
Python 🐍
Scikit-learn 🤖
FastAPI ⚡
Joblib 🧠
Hugging Face Spaces 

---

🧩 Requirements
fastapi
uvicorn
scikit-learn
pandas
joblib
python-multipart
