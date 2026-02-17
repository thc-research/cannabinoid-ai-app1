
# 🏗️ AI App Architecture Deep Dive

## System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              USER INTERFACE                                  │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │  Dashboard  │  │ Batch Entry │  │ AI Predict  │  │   CoA Generator     │ │
│  │  (Streamlit)│  │   (Forms)   │  │  (Sliders)  │  │     (PDF Export)    │ │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────────┬──────────┘ │
│         └─────────────────┴─────────────────┴────────────────────┘           │
│                                    │                                         │
│                           State Management                                   │
│                         (st.session_state)                                   │
└────────────────────────────────────┼─────────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           APPLICATION LAYER                                  │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │                     Data Processor (ETL Pipeline)                     │   │
│  │  • Excel Import/Export  • Validation  • Metric Calculation           │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │                     AI Model Serving Layer                            │   │
│  │  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌─────────────┐ │   │
│  │  │  Extraction  │ │  Degradation │ │   Anomaly    │ │   Potency   │ │   │
│  │  │  Optimizer   │ │  Predictor   │ │   Detector   │ │  Classifier │ │   │
│  │  │  (Random     │ │   (LSTM/     │ │   (Isolation │ │    (SVM)    │ │   │
│  │  │   Forest)    │ │   Kinetics)  │ │    Forest)   │ │             │ │   │
│  │  └──────────────┘ └──────────────┘ └──────────────┘ └─────────────┘ │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
└────────────────────────────────────┼─────────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                             DATA LAYER                                       │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────────────┐   │
│  │   SQLite DB      │  │   Model Storage  │  │   File System            │   │
│  │   (batches,      │  │   (.pkl, .h5)    │  │   (CoA PDFs, exports)    │   │
│  │    analytics)    │  │                  │  │                          │   │
│  └──────────────────┘  └──────────────────┘  └──────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Data Flow

### 1. Batch Entry Flow
```
User Input → Form Validation → Metric Calculation → AI Prediction → Database Save → Dashboard Update
```

### 2. CoA Generation Flow
```
Analytical Data → Validation → Metric Calculation → PDF Generation → Download
```

### 3. AI Prediction Flow
```
Parameters Input → Feature Engineering → Model Inference → Results Display → Recommendation
```

## AI Model Details

### Model 1: Extraction Optimizer
```python
Algorithm: Random Forest Regressor
Input Features: [temp, time, rpm, solvent_ratio, material_type, moisture]
Output: efficiency, yield, potency_retention

Hyperparameters:
- n_estimators: 100
- max_depth: 10
- min_samples_split: 5
- random_state: 42

Training Data: Historical batches (n>50 for good performance)
Validation: 80/20 split, cross-validation
```

### Model 2: Degradation Predictor
```python
Algorithm: First-order kinetics + optional LSTM
Formula: C(t) = C₀ × exp(-k×t)

Rate Constants (k):
- Room Temp: 0.5%/month
- Refrigerated: 0.2%/month
- Frozen: 0.05%/month

LSTM Architecture (if time-series data available):
- Input: 30 days history
- Layers: 2 LSTM (64, 32 units)
- Output: 30 days prediction
- Loss: MSE
```

### Model 3: Anomaly Detector
```python
Algorithm: Isolation Forest
Contamination: 0.1 (10% expected outliers)
Features: [efficiency, degradation_index, isomerization_ratio, yield]

Anomaly Score Interpretation:
- > 0.2: Normal
- 0 to 0.2: Suspicious
- < 0: Anomaly (investigate)
```

## Database Schema

```sql
-- Batches table
CREATE TABLE batches (
    batch_id TEXT PRIMARY KEY,
    date TEXT,
    technician TEXT,
    strain TEXT,
    material_type TEXT,
    initial_weight_g REAL,
    moisture_content REAL,
    extraction_temp_c INTEGER,
    extraction_time_min INTEGER,
    rpm INTEGER,
    final_weight_g REAL,
    total_thc REAL,
    total_cbd REAL,
    total_cannabinoids REAL,
    degradation_index REAL,
    isomerization_ratio REAL,
    extraction_efficiency REAL,
    process_yield REAL,
    status TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Analytical results (CoA data)
CREATE TABLE analytical_results (
    test_id TEXT PRIMARY KEY,
    batch_id TEXT,
    test_date TEXT,
    d9_thc REAL,
    d8_thc REAL,
    cbd REAL,
    cbda REAL,
    cbg REAL,
    cbn REAL,
    cbc REAL,
    method TEXT,
    analyst TEXT,
    FOREIGN KEY (batch_id) REFERENCES batches (batch_id)
);

-- Process parameters (time-series)
CREATE TABLE process_params (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    batch_id TEXT,
    timestamp TEXT,
    temp_set REAL,
    temp_actual REAL,
    vacuum_mbar REAL,
    rpm INTEGER,
    FOREIGN KEY (batch_id) REFERENCES batches (batch_id)
);
```

## API Endpoints (Future FastAPI Backend)

```python
# Potential REST API structure

POST /api/batches              # Create new batch
GET  /api/batches/{id}         # Get batch details
GET  /api/batches              # List batches (paginated)
PUT  /api/batches/{id}         # Update batch

POST /api/predict/efficiency   # Predict extraction efficiency
POST /api/predict/degradation  # Predict shelf-life
POST /api/predict/anomaly      # Detect anomalies

POST /api/coa/generate         # Generate CoA PDF
GET  /api/coa/{batch_id}       # Download CoA

GET  /api/analytics/summary    # Dashboard KPIs
GET  /api/analytics/trends     # Time-series data
GET  /api/analytics/correlation # Correlation matrix
```

## Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Frontend | Streamlit | Interactive UI |
| Visualization | Plotly | Charts & graphs |
| ML/AI | Scikit-learn | Random Forest, SVM, Isolation Forest |
| Deep Learning | TensorFlow/Keras | LSTM (optional) |
| Database | SQLite | Local data storage |
| PDF Generation | FPDF2 | CoA certificates |
| Data Processing | Pandas, NumPy | ETL, calculations |

## Performance Benchmarks

| Operation | Expected Time | Optimization |
|-----------|--------------|--------------|
| Batch Save | < 100ms | SQLite write |
| AI Prediction | < 50ms | Cached model |
| CoA Generation | < 2s | PDF rendering |
| Dashboard Load | < 1s | Cached queries |
| Data Export | < 5s | Streaming write |

## Security Architecture

```
┌─────────────────────────────────────────┐
│           User Authentication           │
│    (Optional: OAuth2, LDAP, SAML)       │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│         Input Validation Layer          │
│    • SQL injection prevention           │
│    • XSS protection                     │
│    • File upload validation             │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│         Business Logic Layer            │
│    • Role-based access control          │
│    • Audit logging                      │
│    • Data encryption (optional)         │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│           Data Storage                  │
│    • Database encryption at rest        │
│    • Secure backup                      │
│    • Access logging                     │
└─────────────────────────────────────────┘
```

## Scalability Roadmap

### Phase 1: Single User (Current)
- SQLite database
- Local Streamlit instance
- File-based model storage

### Phase 2: Multi-User (Future)
- PostgreSQL database
- Redis caching layer
- User authentication
- Role-based access

### Phase 3: Enterprise (Future)
- Microservices architecture
- Kubernetes deployment
- Real-time streaming (Kafka)
- Distributed training (Spark)
- Multi-region deployment
