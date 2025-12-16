

# 💼 CareerCompassAI – AI-Powered Job Recommendation System

### 👨‍💻 Author: [Sandeepkumar C M](https://github.com/sandeepkumarcm)

---

## 🎥 Demo Video
▶️ https://youtu.be/Tw1c-TbWEWw

---


## 🚀 Overview
CareerCompassAI is an **AI-driven Job Recommendation System** that analyzes uploaded resumes and intelligently matches candidates with relevant job descriptions based on their **skills, experience, and profile**.

It uses **Natural Language Processing (NLP)** and **Semantic Search** (Sentence-BERT + FAISS) for high-accuracy results.

---

## 🧠 Features
✅ Upload a PDF resume for personalized job recommendations  
✅ Uses **SentenceTransformer embeddings** for semantic understanding  
✅ TF-IDF filtering for faster and relevant job retrieval  
✅ Simple **Streamlit-based Web App** interface  
✅ Dataset-driven: works with your own job listings (JobsFE.csv)

---

## 🛠️ Technologies Used
- **Python**
- **Streamlit** (Frontend)
- **FAISS** (Vector search)
- **Sentence Transformers (SBERT)**
- **PyMuPDF** (Resume text extraction)
- **Scikit-learn (TF-IDF)**

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/sandeepkumarcm/CareerCompassAI.git
cd CareerCompassAI

2️⃣ Install the dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit app
streamlit run app.py


Then open your browser at http://localhost:8501

📂 Dataset

Make sure the file JobsFE.csv is in the same directory.
It contains job roles, skills, and job descriptions used for matching.

🤖 How It Works

Resume Extraction – Text is extracted from the uploaded PDF using PyMuPDF

TF-IDF Filtering – Quickly filters out irrelevant jobs

Semantic Search (FAISS) – Finds jobs semantically closest to your profile

Recommendation Output – Displays top matching jobs on Streamlit

🧭 Future Enhancements

🔹 Add support for DOCX and TXT resume formats
🔹 Include LinkedIn-style job filters
🔹 Improve job ranking using advanced embeddings (e.g., OpenAI, Gemini models)
🔹 Add a recruiter dashboard for analytics

👨‍💻 Author

Sandeepkumar C M
📧 cmsandeeepkumar049@gmail.com

🔗 LinkedIn

💻 GitHub

📌 License

This project is open-source under the MIT License.
Feel free to fork and improve!


