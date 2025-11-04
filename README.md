# 🚗 Getaround ML Price Optimization & Delay Analysis

A comprehensive machine learning project for car rental price prediction and delay conflict analysis, featuring two deployed web applications and complete ML pipeline implementation.

![Python](https://img.shields.io/badge/python-v3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)
![XGBoost](https://img.shields.io/badge/XGBoost-2.0+-orange.svg)
![Docker](https://img.shields.io/badge/Docker-enabled-blue.svg)

## 🎯 Project Overview

This project addresses two key challenges in car rental platforms:

1. **📊 Delay Analysis**: Understanding how late returns affect future rentals
2. **💰 Price Optimization**: ML-powered dynamic pricing based on car specifications

**Live Applications:**
- 🌐 **Interactive Dashboard**: [Delay Analysis Dashboard](https://huggingface.co/spaces/AgaHei/getaround-dashboard)
- 🔧 **API Service**: [Price Prediction API](https://agahei-getaround-pricing-api.hf.space)

## 🏆 Key Achievements

- ✅ **Production ML API** with 174€+ accurate price predictions
- ✅ **Interactive Streamlit Dashboard** for business insights
- ✅ **Complete MLOps Pipeline** from data to deployment
- ✅ **Docker Containerization** for scalable deployment
- ✅ **Comprehensive Documentation** with Swagger UI

## 📊 Model Performance

### Price Prediction Model (XGBoost)
- **Algorithm**: Optimized XGBoost Regressor with GridSearchCV
- **Features**: 59 engineered features from categorical encoding
- **Performance Metrics**:
  - RMSE: ~16.33
  - MAE: ~10.10  
  - R² Score: ~0.76
- **Deployment**: FastAPI with automatic documentation

### Business Impact Analysis
- **Delay Threshold Optimization**: Interactive simulation tool
- **Connect vs All Cars**: Comparative analysis capabilities
- **Revenue Impact Assessment**: Real-time threshold testing

## 🚀 Live Applications

### 1. 📊 Delay Analysis Dashboard
**URL**: https://huggingface.co/spaces/AgaHei/getaround-dashboard

**Features**:
- Interactive threshold simulation (15-600 minutes)
- Connect vs All Cars scope selection
- Real-time conflict analysis
- Visual delay distribution with KDE
- Business insights and recommendations

### 2. 🔧 Price Prediction API
**URL**: https://agahei-getaround-pricing-api.hf.space

**Endpoints**:
- `POST /predict` - Get price predictions
- `GET /docs` - Interactive API documentation  
- `GET /example` - Sample input examples
- `GET /health` - Service health check

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

## 📁 Project Structure

```
Project Getaround Dev/
├── 📊 notebooks/
│   ├── getaround_pricing.ipynb        # ML model development & training
│   └── getaround_EDA.ipynb           # Exploratory data analysis
├── 📈 data/
│   ├── get_around_pricing_project.csv      # Original pricing dataset
│   └── cleaned_getaround_data.csv         # Processed delay analysis data
├── 🤖 models/
│   └── best_xgb_model.pkl           # Trained XGBoost model
├── 🔧 Deployment Files/
│   ├── smart_input_encoder.py       # Data preprocessing utilities
│   ├── feature_order.txt           # Model feature specification
│   ├── requirements.txt            # Python dependencies
│   └── Dockerfile                 # Container configuration
└── 📚 Documentation/
    ├── README.md                   # This file
    └── .gitignore                 # Git exclusions

Deployment HF Dashboard/
└── getaround-dashboard/
    ├── app.py                     # Streamlit dashboard application
    ├── requirements.txt           # Dashboard dependencies
    └── data/                      # Dashboard data files

Deployment HF Pricing API/
└── hf-space/
    ├── app.py                     # FastAPI application
    ├── smart_input_encoder.py     # Input processing
    ├── feature_order.txt          # Model features
    ├── models/                    # ML model files
    └── data/                      # Reference datasets
```

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

## 🔧 Local Development Setup

### Prerequisites
- Python 3.10+
- Git
- Docker (optional)

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AgaHei/getaround-project.git
   cd getaround-project
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Jupyter notebooks**:
   ```bash
   jupyter notebook notebooks/
   ```

5. **Test API locally** (from deployment folder):
   ```bash
   cd "Deployment HF Pricing API/hf-space"
   python app.py
   ```

6. **Run dashboard locally** (from dashboard folder):
   ```bash
   cd "Deployment HF Dashboard/getaround-dashboard"  
   streamlit run app.py
   ```

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

This project was developed as part of the Jedha Data Science certification program. 

### Development Workflow
1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📝 License

This project is part of an educational certification program. Please respect academic integrity guidelines.

## 🙏 Acknowledgments

- **Jedha Data Science Program**: Comprehensive ML engineering curriculum
- **Hugging Face Spaces**: Excellent platform for ML application deployment
- **FastAPI & Streamlit Communities**: Amazing frameworks for rapid development
- **XGBoost Team**: Powerful gradient boosting implementation

---

## 📞 Contact

**Project Developer**: AgaHei  
**Live Applications**: 
- [Dashboard](https://huggingface.co/spaces/AgaHei/getaround-dashboard)
- [API](https://agahei-getaround-pricing-api.hf.space)

**Note**: This project demonstrates end-to-end ML engineering skills including data analysis, model development, API creation, web application deployment, and production monitoring.

---

*Last Updated: November 2025*