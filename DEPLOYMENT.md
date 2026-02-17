
# 🚀 Deployment Guide

## Option 1: Local Development

```bash
# 1. Navigate to app directory
cd cannabinoid_ai_app

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run app
streamlit run app.py

# 6. Open browser to http://localhost:8501
```

## Option 2: Streamlit Cloud (Free Hosting)

1. **Push to GitHub**
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/cannabinoid-ai-app.git
git push -u origin main
```

2. **Deploy on Streamlit Cloud**
- Go to [streamlit.io/cloud](https://streamlit.io/cloud)
- Sign in with GitHub
- Click "New app"
- Select repository, branch, and app.py
- Click "Deploy"

3. **Access Your App**
- URL: `https://yourusername-cannabinoid-ai-app.streamlit.app`
- Auto-updates on git push

## Option 3: Docker Deployment

```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

```bash
# Build and run
docker build -t cannabinoid-ai .
docker run -p 8501:8501 cannabinoid-ai
```

## Option 4: AWS/Azure/GCP

### AWS EC2
```bash
# 1. Launch EC2 instance (t2.medium recommended)
# 2. SSH into instance
ssh -i key.pem ubuntu@your-ec2-ip

# 3. Install dependencies
sudo apt update
sudo apt install python3-pip
pip3 install -r requirements.txt

# 4. Run with nohup
nohup streamlit run app.py --server.port 80 &
```

### Google Cloud Run
```bash
# Build and deploy
gcloud builds submit --tag gcr.io/your-project/cannabinoid-ai
gcloud run deploy --image gcr.io/your-project/cannabinoid-ai --platform managed
```

## 🔐 Environment Variables (Optional)

Create `.env` file for sensitive configurations:

```bash
# .env
DB_PATH=data/extraction.db
MODEL_PATH=models/
DEBUG=False
SECRET_KEY=your-secret-key-here
```

Load in app:
```python
from dotenv import load_dotenv
load_dotenv()
```

## 📊 Performance Optimization

### For Large Datasets (>10,000 batches)

1. **Use PostgreSQL instead of SQLite**
```python
# In data_processor.py
import psycopg2
# Replace sqlite3 connection with PostgreSQL
```

2. **Enable Caching**
```python
@st.cache_data(ttl=3600)
def load_large_dataset():
    return pd.read_sql_query("SELECT * FROM batches", conn)
```

3. **Model Optimization**
```python
# Use lighter models for faster inference
from sklearn.ensemble import GradientBoostingRegressor  # Faster than RF
```

## 🔄 CI/CD Pipeline

### GitHub Actions (.github/workflows/deploy.yml)

```yaml
name: Deploy to Streamlit Cloud

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9

    - name: Install dependencies
      run: |
        pip install -r requirements.txt

    - name: Run tests
      run: |
        python -m pytest tests/

    - name: Deploy to Streamlit
      env:
        STREAMLIT_TOKEN: ${{ secrets.STREAMLIT_TOKEN }}
      run: |
        # Deployment script
```

## 🛡️ Security Considerations

1. **Input Validation**
   - All user inputs validated in forms
   - SQL injection prevention (parameterized queries)
   - XSS protection (Streamlit handles this)

2. **Data Privacy**
   - No data leaves your server (self-hosted)
   - Optional: Encrypt database at rest

3. **Access Control**
   - Add authentication:
   ```python
   import streamlit_authenticator as stauth
   ```

## 📈 Monitoring

### Add to app.py:
```python
# Track usage
import logging
logging.basicConfig(filename='app.log', level=logging.INFO)

# Log predictions
logging.info(f"Prediction made: {prediction} for batch {batch_id}")
```

### Streamlit Analytics:
```bash
pip install streamlit-analytics
```

## 🆘 Troubleshooting

### Issue: "Module not found"
```bash
pip install -r requirements.txt --upgrade
```

### Issue: "Port already in use"
```bash
# Kill process on port 8501
lsof -ti:8501 | xargs kill -9
```

### Issue: "Out of memory"
```bash
# Reduce data loading batch size
# In data_processor.py, add LIMIT to queries
```

### Issue: "Model predictions slow"
```bash
# Use model quantization or lighter algorithms
# Cache model in memory (singleton pattern)
```

## 📞 Support

For deployment issues:
- Streamlit Docs: [docs.streamlit.io](https://docs.streamlit.io)
- Community: [discuss.streamlit.io](https://discuss.streamlit.io)
- GitHub Issues: [github.com/yourusername/cannabinoid-ai-app/issues](https://github.com/yourusername/cannabinoid-ai-app/issues)
