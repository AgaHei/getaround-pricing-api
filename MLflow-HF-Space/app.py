import streamlit as st
import subprocess
import os
import time
import requests
from threading import Thread
import atexit

# Configuration
MLFLOW_PORT = 5000
MLFLOW_HOST = "0.0.0.0"

# Global variable to store MLflow process
mlflow_process = None

def start_mlflow_server():
    """Start MLflow tracking server"""
    global mlflow_process
    try:
        # Start MLflow server
        cmd = [
            "mlflow", "ui", 
            "--host", MLFLOW_HOST,
            "--port", str(MLFLOW_PORT),
            "--backend-store-uri", "file:///app/mlruns"
        ]
        
        mlflow_process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Wait a moment for server to start
        time.sleep(5)
        return True
        
    except Exception as e:
        st.error(f"Failed to start MLflow server: {e}")
        return False

def stop_mlflow_server():
    """Stop MLflow server"""
    global mlflow_process
    if mlflow_process:
        mlflow_process.terminate()
        mlflow_process = None

# Register cleanup function
atexit.register(stop_mlflow_server)

# Streamlit page configuration
st.set_page_config(
    page_title="🚗 Getaround MLflow Experiments",
    page_icon="📊",
    layout="wide"
)

# Header
st.title("🚗 Getaround ML Experiments Dashboard")
st.markdown("### 📊 MLflow Experiment Tracking for Pricing Model Development")

st.markdown("""
This dashboard provides access to all machine learning experiments conducted during the 
Getaround pricing optimization project development.
""")

# Check if MLflow data exists
if os.path.exists("mlruns"):
    experiments_count = len([d for d in os.listdir("mlruns") if os.path.isdir(os.path.join("mlruns", d)) and d != ".trash"])
    st.success(f"✅ Found {experiments_count} MLflow experiments ready to explore!")
else:
    st.error("❌ MLflow experiments directory not found. Please ensure 'mlruns' folder is uploaded.")
    st.stop()

# Information section
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **🎯 What you can explore:**
    - Model performance metrics (RMSE, MAE, R²)
    - Hyperparameter tuning results
    - Feature importance analysis  
    - Model comparison across experiments
    - Training logs and artifacts
    """)

with col2:
    st.markdown("""
    **🔧 Models tracked:**
    - Linear Regression baseline
    - Random Forest Regressor
    - XGBoost (basic configuration)
    - XGBoost (hyperparameter optimized)
    - Cross-validation results
    """)

# MLflow server management
st.divider()
st.markdown("### 🖥️ MLflow Tracking Server")

col1, col2 = st.columns([1, 2])

with col1:
    if st.button("🚀 Launch MLflow UI", type="primary"):
        with st.spinner("Starting MLflow server..."):
            if start_mlflow_server():
                st.success("✅ MLflow server started!")
                time.sleep(2)
                st.rerun()
            else:
                st.error("❌ Failed to start MLflow server")

with col2:
    # Check if MLflow server is running
    try:
        response = requests.get(f"http://{MLFLOW_HOST}:{MLFLOW_PORT}", timeout=2)
        if response.status_code == 200:
            st.success("🟢 MLflow server is running!")
            st.markdown(f"""
            **🔗 Access MLflow UI:**
            - Local: http://localhost:{MLFLOW_PORT}
            - Network: http://{MLFLOW_HOST}:{MLFLOW_PORT}
            """)
            
            # Embed MLflow UI in iframe
            st.markdown("### 📊 MLflow Experiments (Live)")
            st.markdown(f"""
            <iframe src="http://localhost:{MLFLOW_PORT}" width="100%" height="600" frameborder="0">
            </iframe>
            """, unsafe_allow_html=True)
        else:
            st.warning("🟡 MLflow server not responding. Click 'Launch MLflow UI' to start.")
    except requests.exceptions.RequestException:
        st.info("ℹ️ MLflow server not started. Click the button above to launch.")

# Instructions
st.divider()
st.markdown("### 📖 How to Use")

with st.expander("🔍 Exploring Experiments", expanded=False):
    st.markdown("""
    1. **Launch the MLflow UI** using the button above
    2. **Browse experiments** in the main interface
    3. **Compare runs** by selecting multiple experiments
    4. **View metrics** like RMSE, MAE, and R² scores
    5. **Download models** and artifacts for deployment
    6. **Check parameters** used in each experiment
    """)

with st.expander("📈 Understanding Metrics", expanded=False):
    st.markdown("""
    - **RMSE (Root Mean Square Error)**: Lower is better - measures prediction accuracy
    - **MAE (Mean Absolute Error)**: Lower is better - average prediction error  
    - **R² Score**: Higher is better (0-1) - explains variance in the data
    - **Training Time**: Duration of model training
    - **Parameters**: Hyperparameters used (learning_rate, max_depth, etc.)
    """)

# Project context
st.divider()
st.markdown("### 🎓 Project Context")
st.info("""
**Getaround Pricing Optimization Project (Jedha Bloc 5)**
This MLflow tracking contains all experiments conducted for the machine learning 
pricing optimization component of the Getaround project, including model selection, 
hyperparameter tuning, and performance evaluation.
""")

# Footer
st.markdown("---")
st.markdown("🚗 **Getaround ML Project** | 📊 **Powered by MLflow** | 🎓 **Jedha Data Science**")