# 🚨 Anomaly Detection System

A machine learning-based Anomaly Detection System built using Python, Streamlit, and Teachable Machine. This project identifies anomalies in uploaded data or images and visualizes results through an interactive web interface.

---

## 📌 Features

- ✅ Image-based anomaly detection using **Google Teachable Machine**
- ✅ Real-time prediction using a **Streamlit web app**
- ✅ Option to upload and classify custom input (image/video)
- ✅ Visualization of normal vs anomalous predictions
- ✅ Extendable for other data types (e.g., time series, sensor data)

---

## 🧠 Technologies Used

- **Python 3.x**
- **Streamlit** – Web interface
- **Teachable Machine** – Pretrained image classification model
- **Pandas, NumPy** – Data processing
- **OpenCV** (optional) – Image handling
- **Matplotlib/Plotly** – Visualization (if required)

---

## 🛠️ Setup Instructions

# 1. Clone the Repository
git clone https://github.com/yourusername/anomaly-detection-system.git
cd anomaly-detection-system

2. Create a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate      # On Mac/Linux
venv\Scripts\activate         # On Windows

3. Install Dependencies
pip install -r requirements.txt

4. Run the Streamlit App
streamlit run app.py
The app will open in your browser at http://localhost:8501.

📂 Project Structure
anomaly-detection-system/
│
├── app.py                  # Streamlit app
├── model/                  # Teachable Machine exported model
├── uploads/                # Uploaded files/images
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── utils/                  # Helper functions (e.g., predictions, preprocessing)
📈 Future Improvements
Add support for real-time webcam anomaly detection

Extend to detect anomalies in time-series or tabular data

Save and track anomaly logs over time

Deploy using cloud platforms (Streamlit Cloud, Heroku, etc.)

🤝 Acknowledgments
Teachable Machine by Google

Streamlit Docs

Open-source community for helpful libraries and examples

📬 Contact
For questions or collaboration:
📧 vaishnavsuhani2004@gmail.com
