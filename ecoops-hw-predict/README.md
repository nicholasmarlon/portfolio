# 🔋 EcoOps: Hardware Predictive Analytics & FinOps

> **Predictive Maintenance & Asset Lifecycle Management Platform** designed to reduce electronic waste (ESG) and optimize hardware operational budgets (FinOps).

---

## 🚀 About The Project
**EcoOps** is an end-to-end data analytics and hardware intelligence pipeline. It ingests native OS diagnostic reports, extracts deep device metrics, models battery degradation curves, and calculates **Remaining Useful Life (RUL)** to prevent unexpected hardware failures in enterprise environments.

Tested and validated on real hardware telemetry (Samsung Book).

---

## 🛠️ Tech Stack & Architecture
- **Language:** Python 3.9
- **Data Ingestion & Parsing:** BeautifulSoup4 (HTML Report Extraction)
- **Data Processing & Analysis:** Pandas, NumPy
- **Dashboard Frontend:** Streamlit
- **Environment Management:** Native Windows PowerShell & Python PIP

---

## 📂 Project Structure
\\\	ext
ecoops-hw-predict/
│
├── data/
│   └── raw/               # Raw OS telemetry reports (e.g., battery-report.html)
├── src/
│   ├── parser.py          # ETL pipeline for diagnostic telemetry extraction
│   └── model.py           # Core analytical motor for RUL & FinOps metrics
│
├── app.py                 # Streamlit interactive executive dashboard
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
\\\

---

## ⚙️ Getting Started & Local Execution

1. **Clone the repository:**
   \\\ash
   git clone https://github.com/YOUR_USERNAME/ecoops-hw-predict.git
   cd ecoops-hw-predict
   \\\

2. **Install dependencies:**
   \\\ash
   python -m pip install -r requirements.txt
   \\\

3. **Generate your hardware telemetry report (Windows):**
   \\\ash
   powercfg /batteryreport
   \\\
   *Move the generated attery-report.html into the data/raw/ folder.*

4. **Run the Interactive Dashboard:**
   \\\ash
   streamlit run app.py
   \\\

---

## 💡 Business Impact (FinOps & ESG)
- **FinOps:** Minimizes premature hardware replacement costs by accurately forecasting component lifespans.
- **ESG:** Drives sustainability by extending asset operational cycles and reducing corporate electronic waste (e-waste).

---
*Developed by Nicholas Barbosa*
