
# Excel to AI Migration Guide

## Overview
This guide helps you transition from Excel-based tracking to the AI-powered platform.

## Key Differences

| Aspect | Excel | AI App |
|--------|-------|--------|
| Data Entry | Manual cells | Smart web forms |
| Calculations | Formulas | Python + AI models |
| CoA Generation | Template copy | One-click PDF |
| Analytics | Static charts | Interactive plots |
| Alerts | Conditional formatting | AI anomaly detection |

## Migration Steps

### 1. Export Excel Data
```python
import pandas as pd
batches = pd.read_excel('workbook.xlsx', sheet_name='MASTER_BATCH_LOG')
batches.to_csv('migration.csv', index=False)
```

### 2. Import to AI App
Use the Data Processor utility to import historical data.

### 3. Train AI Models
Use your historical data to train the prediction models.

### 4. Validate
Compare Excel calculations with AI predictions to ensure accuracy.

### 5. Go Live
Switch to AI app for new batches, keep Excel as backup.

## Time Savings
- Excel: ~15 minutes per batch
- AI App: ~3 minutes per batch
- **80% time reduction**

## Support
See README.md for detailed usage instructions.
