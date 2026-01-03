# 🚗 Getaround ML Engineering Portfolio

A comprehensive machine learning project showcasing complete MLOps capabilities for car rental price optimization and delay analysis. Features three deployed professional applications demonstrating end-to-end ML pipeline implementation. Built as part of the Jedha Machine Learning Engineer certification (Bloc 5).

![Python](https://img.shields.io/badge/python-v3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)
![MLflow](https://img.shields.io/badge/MLflow-2.8+-purple.svg)
![XGBoost](https://img.shields.io/badge/XGBoost-2.0+-orange.svg)
![Docker](https://img.shields.io/badge/Docker-enabled-blue.svg)

## 🎯 Project Overview

This project addresses three key challenges in car rental platforms:

1. **📊 Delay Analysis**: Understanding how late returns affect future rentals
2. **💰 Price Optimization**: ML-powered dynamic pricing based on car specifications
3. **🔬 Experiment Tracking**: Professional ML development with versioning and monitoring

**🌟 Live Applications Portfolio:**
- 🌐 **Interactive Dashboard**: [Delay Analysis & Business Intelligence](https://huggingface.co/spaces/AgaHei/getaround-dashboard)
- 🤖 **Production API**: [Price Prediction Service](https://agahei-getaround-pricing-api.hf.space/docs)
- 🔬 **Experiment Tracking**: [MLflow Professional Dashboard](https://huggingface.co/spaces/AgaHei/getaround-mlflow)

## 🏆 Key Achievements & Professional Skills Demonstrated

- ✅ **Production ML API** with 174€+ accurate price predictions
- ✅ **Interactive Business Dashboard** with real-time analysis
- ✅ **Professional Experiment Tracking** with MLflow integration
- ✅ **Docker Containerization** for scalable deployments
- ✅ **Comprehensive Documentation** with API specifications
- ✅ **Model Versioning & Monitoring** with experiment management

## � Application Portfolio

### 1. 🌐 Interactive Dashboard
**Live Demo**: [Getaround Delay Analysis Dashboard](https://huggingface.co/spaces/AgaHei/getaround-dashboard)

**Key Features:**
- Real-time delay conflict analysis
- Interactive threshold optimization (15-600 minutes)
- Connect vs All Cars scope selection  
- Revenue impact calculations
- Performance-optimized with caching
- Professional business intelligence insights

### 2. 🤖 Price Prediction API  
**Live Demo**: [Getaround Pricing API](https://agahei-getaround-pricing-api.hf.space/docs)

**Key Features:**
- RESTful API with FastAPI framework
- Real-time price predictions (174€+ accuracy)
- Automatic interactive documentation (Swagger UI)
- Professional endpoint testing interface
- Production-ready with proper validation

### 3. 🔬 MLflow Experiment Tracking
**Live Demo**: [MLflow Professional Dashboard](https://huggingface.co/spaces/AgaHei/getaround-mlflow)

**Key Features:**
- Complete experiment versioning
- Model performance comparison across 4 algorithms
- Hyperparameter tracking and optimization history
- Professional ML development workflow
- Visual experiment analysis dashboard

## 🧠 Machine Learning Pipeline

### Model Development & Performance

**Implemented Models:**
1. **🚀 XGBoost Regressor** (Primary Model)
   - Performance: 174.24€ RMSE
   - Features: Advanced gradient boosting with hyperparameter optimization
   - Strengths: Excellent handling of mixed data types and outliers

2. **🌲 Random Forest Regressor** (Backup Model)  
   - Performance: 198.58€ RMSE
   - Features: Ensemble learning with robust predictions
   - Strengths: Interpretable feature importance and stable results

3. **📈 Linear Regression** (Baseline Model)
   - Performance: 244.81€ RMSE
   - Features: Simple linear relationship modeling
   - Strengths: Fast training and interpretable coefficients

4. **🎯 Ridge Regression** (Regularized Model)
   - Performance: 244.81€ RMSE  
   - Features: L2 regularization for overfitting control
   - Strengths: Balanced bias-variance trade-off

### Professional ML Development Process
- ✅ Comprehensive EDA with business insights
- ✅ Advanced feature engineering and selection
- ✅ GridSearchCV hyperparameter optimization
- ✅ Cross-validation and robust evaluation
- ✅ Model versioning with MLflow tracking
- ✅ Production deployment with monitoring


**Example Usage**:
```bash
curl -X POST 'https://agahei-getaround-pricing-api.hf.space/predict' \
  -H 'Content-Type: application/json' \
  -d '{
    "mileage": 50000,
    "engine_power": 120,
    "private_parking_available": true,
    "has_gps": true,
    "has_air_conditioning": true,
    "automatic_car": false,
    "has_getaround_connect": true,
    "has_speed_regulator": true,
    "winter_tires": false,
    "model_key": "Citroën",
    "fuel": "petrol",
    "paint_color": "black",
    "car_type": "sedan"
  }'
```

**Response**:
```json
{
  "predicted_price": 174.38,
  "currency": "EUR",
  "period": "per day",
  "status": "success"
}
```

## 📁 Repository Structure

This GitHub repository contains the essential ML development files (cleaned for professional presentation):

```
getaround-pricing-api/
├── 📊 notebooks/
│   ├── getaround_pricing.ipynb        # Complete ML pipeline & model training
│   └── getaround_EDA.ipynb           # Exploratory data analysis & insights
├── 📈 data/
│   ├── get_around_pricing_project.csv      # Original pricing dataset (1.7MB)
│   ├── cleaned_getaround_data.csv         # Processed delay analysis data
│   └── get_around_delay_analysis.xlsx     # Business analysis dataset
├── 🤖 models/
│   └── optimized_model.pkl          # Production XGBoost model (55MB)
├── � Core ML Files/
│   ├── Getaround_Project_AH.ppt      # Presentation of the project
│   ├── smart_input_encoder.py       # Production data preprocessing
│   ├── feature_order.txt           # Model feature specification (59 features)
│   ├── requirements.txt            # Python dependencies
│   ├── README.md                   # Professional documentation
│   └── .gitignore                 # Repository cleanup configuration
```

### 🚀 **Deployment Repositories** (Separate HF Spaces)

The live applications are deployed from separate repositories optimized for production:

- **📊 Dashboard**: `Deployment HF Dashboard/getaround-dashboard/`
  - Repository: https://huggingface.co/spaces/AgaHei/getaround-dashboard  
  - Live App: https://huggingface.co/spaces/AgaHei/getaround-dashboard

- **🔧 API**: `Deployment HF Pricing API/hf-space/`
  - Repository: https://huggingface.co/spaces/AgaHei/getaround-pricing-api
  - Live API: https://agahei-getaround-pricing-api.hf.space

- **🔬 MLflow**: `MLflow-HF-Space/getaround-mlflow/`
  - Repository: https://huggingface.co/spaces/AgaHei/getaround-mlflow
  - Live Tracking: https://huggingface.co/spaces/AgaHei/getaround-mlflow

### 📝 **Development vs Deployment**

- **This Repository**: Clean ML development portfolio with notebooks, trained models, and core utilities
- **HF Spaces**: Production-optimized deployments with containerized applications and live APIs
- **Professional Structure**: Repository cleaned for certification/portfolio presentation

## 🛠️ Technologies Used

### Machine Learning & Data Science
- **Python 3.10+**: Core programming language
- **Pandas & NumPy**: Data manipulation and analysis
- **Scikit-learn**: Model training and evaluation
- **XGBoost**: Gradient boosting for price prediction
- **Matplotlib & Seaborn**: Data visualization

### Web Applications
- **FastAPI**: High-performance API framework
- **Streamlit**: Interactive dashboard framework
- **Pydantic**: Data validation and serialization
- **Uvicorn**: ASGI server for FastAPI

### DevOps & Deployment
- **Docker**: Containerization for reproducible deployments
- **Hugging Face Spaces**: Cloud hosting platform
- **Git**: Version control and collaboration
- **MLflow**: Experiment tracking (development)

### Data Processing
- **Pandas get_dummies**: Categorical variable encoding
- **StandardScaler**: Feature normalization
- **Custom encoders**: Production data preprocessing

## 🧪 Model Development Process

### 1. **Exploratory Data Analysis**
- Comprehensive dataset analysis (4,843 cars, 15+ features)
- Price distribution and outlier detection
- Feature correlation analysis
- Business insights extraction

### 2. **Data Preprocessing**
- Categorical encoding with proper handling
- Feature scaling for numerical variables
- 59-feature engineering from categorical variables
- Train/test split with stratification

### 3. **Model Training & Optimization**
- Compared Linear Regression, Random Forest, XGBoost
- Hyperparameter tuning with GridSearchCV
- Cross-validation for robust performance assessment
- Feature importance analysis

### 4. **Model Deployment**
- Smart input encoder for production data handling
- RESTful API with comprehensive error handling
- Interactive documentation with Swagger UI
- Health monitoring and logging

## 📈 Business Impact

### Delay Analysis Insights
- **Optimal Threshold Identification**: Data-driven delay policies
- **Revenue Protection**: Minimize conflicts while maximizing availability
- **Connect Strategy**: Specialized analysis for connected cars

### Price Optimization Benefits
- **Dynamic Pricing**: Real-time price adjustments based on car specs
- **Market Competitive**: ML-powered pricing strategies  
- **Revenue Optimization**: Maximize rental income per vehicle

## 🧪 Testing

### API Testing
Visit the interactive documentation at `/docs` endpoint for comprehensive API testing.

### Model Validation
- Cross-validation scores available in notebooks
- Test predictions with provided examples
- Performance metrics tracked throughout development

## 📚 Documentation

- **📖 Interactive API Docs**: Available at `/docs` endpoint of deployed API
- **📊 Model Development**: Detailed process in Jupyter notebooks
- **🎯 Business Analysis**: Insights available in dashboard application
- **🔧 Deployment Guides**: Configuration files and Docker setup

## 👥 Contributing

This project was developed as part of the Jedha Data Science and Engineering Fullstack certification program. 


## 📝 License

This project is part of an educational certification program. Please respect academic integrity guidelines.

## 🙏 Acknowledgments

- **Jedha Data Science Program**: Comprehensive ML engineering curriculum
- **Hugging Face Spaces**: Excellent platform for ML application deployment
- **FastAPI & Streamlit Communities**: Amazing frameworks for rapid development
- **XGBoost Team**: Powerful gradient boosting implementation

---

*Last Updated: December 2025 - Repository cleaned for professional portfolio presentation*