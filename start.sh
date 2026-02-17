#!/bin/bash

echo "🧪 Starting Cannabinoid Extraction AI Platform..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -q -r requirements.txt

# Create necessary directories
mkdir -p data models

# Run application
echo "🚀 Launching Streamlit app..."
streamlit run app.py
