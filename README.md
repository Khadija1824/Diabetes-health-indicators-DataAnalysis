# 🩺 Diabetes Risk & Lifestyle Factors Analysis

An exploratory data analysis (EDA) and interactive dashboard project examining public health indicators from the CDC Behavioral Risk Factor Surveillance System (BRFSS) dataset. This project focuses entirely on descriptive statistics, data distributions, correlation analysis, and lifestyle impact visualization without machine learning black-box modeling.

---

## 🚀 Project Overview

Type 2 Diabetes is heavily influenced by a combination of lifestyle habits, body composition, and pre-existing medical conditions. This project aims to:
* Explore the statistical relationship between **Body Mass Index (BMI)** and diabetes prevalence.
* Analyze how clinical risk factors like **High Blood Pressure** and **High Cholesterol** amplify disease risk.
* Evaluate the protective buffer provided by **Regular Physical Activity**.
* Provide an interactive web-based dashboard for exploring health indicator statistics dynamically.

---

📊 Key Evaluation Insights
Body Weight Impact: Median BMI is notably higher among diabetic/prediabetic cohorts, highlighting weight management as a critical indicator.

Hypertension Correlation: High blood pressure shows a heavy overlap with diabetes risk, signifying a strong multi-morbidity link.

Physical Activity Buffer: Regular exercise patterns show an inverse relationship with disease prevalence.

Age-Driven Cumulative Risk: Risk concentrations grow progressively across advancing age brackets.

## 🛠️ Tech Stack & Requirements

Ensure you have **Python 3.8+** installed. The project relies on the following standard data science and web app libraries:

* **`pandas`** — Data manipulation and aggregation
* **`numpy`** — Numerical computations
* **`matplotlib`** & **`seaborn`** — Statistical charting and heatmaps
* **`streamlit`** — Interactive web dashboard framework

Install all dependencies via terminal:
```bash
pip install pandas numpy matplotlib seaborn streamlit
