# 🧪 Cannabinoid Extraction AI Platform

An intelligent web application for optimizing cannabinoid extraction processes, generating Certificates of Analysis (CoA), and predicting product quality using machine learning.

## 📋 Features

### 🤖 AI-Powered Modules

1. **Extraction Optimizer** (Random Forest)
   - Predicts optimal temperature, time, and RPM settings
   - Forecasts extraction efficiency and yield
   - Based on Design of Experiments (DoE) methodology

2. **Degradation Predictor** (Time-Series Analysis)
   - Predicts CBN formation over time
   - Estimates shelf-life under different storage conditions
   - First-order kinetics model

3. **Anomaly Detector** (Isolation Forest)
   - Identifies out-of-specification batches
   - Real-time quality alerts
   - Automated deviation detection

4. **CoA Generator**
   - Professional PDF certificates matching Treehouse format
   - Automated calculations (Degradation Index, Isomerization Ratio)
   - Digital signature ready

### 📊 Dashboard & Analytics

- Real-time KPI monitoring
- Interactive Plotly visualizations
- Temperature optimization studies
- Potency trend analysis
- Correlation matrices

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/yourusername/cannabinoid-ai-app.git
cd cannabinoid-ai-app

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app.py
```

### Access

Open your browser to: `http://localhost:8501`

## 📁 Project Structure

```
cannabinoid_ai_app/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── README.md                # This file
├── utils/
│   ├── __init__.py
│   ├── prediction_models.py # AI/ML models
│   ├── data_processor.py    # Database & ETL
│   └── coa_generator.py     # PDF CoA generation
├── models/                  # Trained model storage
│   └── (saved models)
└── data/                    # SQLite database
    └── extraction.db
```

## 🔬 AI Models Explained

### Extraction Optimizer
**Algorithm:** Random Forest Regressor  
**Inputs:**
- Temperature (-80°C to -20°C)
- Time (10-30 minutes)
- RPM (800-1500)
- Solvent ratio
- Material type
- Initial moisture

**Outputs:**
- Predicted extraction efficiency (%)
- Expected yield (%)
- Potency retention (%)

**Training Data:** Historical batch records from Excel workbook

### Degradation Predictor
**Algorithm:** First-order kinetics + LSTM  
**Formula:** `THC(t) = THC₀ × exp(-k×t)`

**Storage Condition Constants (k):**
- Room Temperature (20°C): 0.5%/month
- Refrigerated (4°C): 0.2%/month
- Frozen (-20°C): 0.05%/month

**Outputs:**
- THC degradation curve
- CBN formation prediction
- Shelf-life estimation

## 📈 Key Metrics

### Degradation Index
```
Degradation Index = (CBN / Total THC) × 100
```
- **< 2%**: Fresh (Excellent)
- **2-5%**: Moderate (Acceptable)
- **> 5%**: Degraded (Review process)

### Isomerization Ratio
```
Isomerization Ratio = (Δ8-THC / Δ9-THC) × 100
```
- **< 3%**: Natural extraction
- **3-10%**: Processed (some conversion)
- **> 10%**: High conversion (check pH)

### Extraction Efficiency
```
Efficiency = (Final cannabinoid mass / Initial cannabinoid mass) × 100
```

## 🎯 Usage Examples

### 1. Optimize Extraction Parameters
1. Navigate to "🤖 AI Predictions"
2. Select "Extraction Optimizer"
3. Adjust temperature, time, RPM sliders
4. View predicted efficiency gauge
5. Implement recommended settings

### 2. Generate CoA
1. Navigate to "📋 CoA Generator"
2. Enter batch information
3. Input analytical results (HPLC/GC-MS)
4. Click "Generate CoA"
5. Download PDF certificate

### 3. Monitor Quality
1. Navigate to "⚠️ Quality Control"
2. Review AI-generated alerts
3. Check anomaly detection scatter plot
4. Investigate flagged batches

## 🔧 Configuration

### Database
SQLite database auto-initializes on first run. Location: `data/extraction.db`

### Model Retraining
```python
from utils.prediction_models import ExtractionOptimizer

# Load historical data
X_train, y_train = load_batch_data()

# Train model
optimizer = ExtractionOptimizer()
optimizer.train(X_train, y_train)

# Save model
optimizer.save('models/extraction_optimizer.pkl')
```

## 📊 Data Integration

### Import from Excel
The app can import your existing Excel workbook:

```python
from utils.data_processor import load_batch_data

df = load_batch_data('Cannabinoid_Extraction_Research_Workbook.xlsx')
```

### Export to Excel
```python
from utils.data_processor import DataProcessor

processor = DataProcessor()
processor.export_to_excel('export.xlsx')
```

## 🛡️ Regulatory Compliance

- **21 CFR Part 11**: Audit trail logging (optional)
- **Data Integrity**: Electronic signatures ready
- **Traceability**: Batch ID linking throughout
- **Validation**: AI model performance metrics tracked

## 🔬 Research Applications

Based on current literature [^19^][^21^][^24^]:

1. **Real-time Process Control**: AI adjusts parameters every 30 seconds
2. **Digital Twins**: Virtual simulation of extraction scenarios
3. **Predictive Maintenance**: Forecast equipment failures 2 weeks ahead
4. **Hyperspectral Integration**: Inline potency monitoring (future)

## 📚 References

- [^19^] AI & IoT Transform Cannabis Extraction Process (Extraction Magazine, 2025)
- [^21^] Machine Learning-Aided Optimization (MDPI, 2025)
- [^24^] Applications of Machine Learning in Cannabis Research (ScienceDirect, 2025)

## 🤝 Contributing

1. Fork repository
2. Create feature branch (`git checkout -b feature/amazing`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing`)
5. Open Pull Request

## 📄 License

MIT License - Research and Development Use

## 📞 Support

For technical support or research collaboration:
- Email: [your-email@example.com]
- Issues: [GitHub Issues]

---

**Built with:** Python, Streamlit, Plotly, Scikit-learn, SQLite

**Version:** 2.0 (CoA-Integrated)
