import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page Configuration
st.set_page_config(
    page_title="Diabetes & Lifestyle Data Explorer",
    page_icon="📊",
    layout="wide"
)

# Load dataset efficiently with caching
@st.cache_data
def load_data():
    df = pd.read_csv('diabetes_binary_health_indicators.csv')
    return df

try:
    df = load_data()
except Exception as e:
    st.error("Dataset not found! Please ensure 'diabetes_binary_health_indicators.csv' is in the directory.")
    st.stop()

# Header Section
st.title("📊 Diabetes Risk & Lifestyle Factors Data Explorer")
st.markdown("""
An interactive statistical data explorer examining CDC health indicators. Analyze how lifestyle choices, 
body composition, and medical history correlate with diabetes prevalence through descriptive statistics and grouped visualizations.
""")

# Sidebar Navigation for Data Views
st.sidebar.header("🔍 Explorer Controls")
analysis_option = st.sidebar.selectbox(
    "Select Analysis View",
    ["Dataset Overview", "BMI & Physical Health Analysis", "Lifestyle Risk Factors (BP & Cholesterol)", "Correlation Heatmap"]
)

if analysis_option == "Dataset Overview":
    st.subheader("📋 Dataset Summary & Statistics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Records", f"{df.shape[0]:,}")
    col2.metric("Total Features", df.shape[1])
    col3.metric("Overall Diabetes Prevalence", f"{(df['Diabetes_binary'].mean() * 100):.2f}%")
    
    st.markdown("### Raw Data Preview")
    st.dataframe(df.head(10))
    
    st.markdown("### Summary Statistics Table")
    st.dataframe(df.describe().T)

elif analysis_option == "BMI & Physical Health Analysis":
    st.subheader("⚖️ Body Mass Index (BMI) vs. Diabetes Status")
    
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.boxplot(x='Diabetes_binary', y='BMI', data=df, palette='Set3', ax=ax)
    ax.set_title('BMI Distribution by Diabetes Status')
    ax.set_xticklabels(['No Diabetes', 'Diabetes / Prediabetes'])
    st.pyplot(fig)
    
    st.markdown("### Statistical Breakdown of BMI")
    bmi_summary = df.groupby('Diabetes_binary')['BMI'].agg(['count', 'mean', 'median', 'min', 'max', 'std'])
    bmi_summary.index = ['No Diabetes', 'Diabetes / Prediabetes']
    st.dataframe(bmi_summary)

elif analysis_option == "Lifestyle Risk Factors (BP & Cholesterol)":
    st.subheader("🩺 Clinical Risk Factors: Blood Pressure & Cholesterol")
    
    factor = st.selectbox("Choose Clinical Indicator to Compare:", ['HighBP', 'HighChol', 'Smoker', 'PhysActivity'])
    
    factor_labels = {
        'HighBP': 'High Blood Pressure',
        'HighChol': 'High Cholesterol',
        'Smoker': 'Smoking History',
        'PhysActivity': 'Regular Physical Activity'
    }
    
    fig, ax = plt.subplots(figsize=(8, 5))
    crosstab = pd.crosstab(df[factor], df['Diabetes_binary'], normalize='index') * 100
    crosstab.plot(kind='bar', stacked=True, ax=ax, colormap='Spectral')
    ax.set_title(f'Diabetes Prevalence Proportion by {factor_labels[factor]}')
    ax.set_xlabel(factor_labels[factor] + ' (0 = No, 1 = Yes)')
    ax.set_ylabel('Percentage (%)')
    ax.legend(['No Diabetes', 'Diabetes'], loc='upper right')
    st.pyplot(fig)
    
    st.markdown("### Crosstabulation Data Table (%)")
    st.dataframe(crosstab.rename(columns={0: 'No Diabetes (%)', 1: 'Diabetes (%)'}))

elif analysis_option == "Correlation Heatmap":
    st.subheader("🔥 Health Indicators Correlation Matrix")
    
    selected_cols = ['Diabetes_binary', 'HighBP', 'HighChol', 'BMI', 'Smoker', 'Stroke', 
                     'HeartDiseaseorAttack', 'PhysActivity', 'GenHlth', 'Age']
    
    fig, ax = plt.subplots(figsize=(10, 8))
    corr = df[selected_cols].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=ax)
    ax.set_title('Bivariate Correlation Heatmap')
    st.pyplot(fig)