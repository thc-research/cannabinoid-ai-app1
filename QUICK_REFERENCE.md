
# 🎯 Quick Reference Card

## 🚀 Launch App
```bash
cd cannabinoid_ai_app
streamlit run app.py
```

## 📊 Key Metrics (Auto-Calculated)
- **Total THC** = Δ9-THC + Δ8-THC
- **Degradation Index** = (CBN / Total THC) × 100
- **Isomerization Ratio** = (Δ8-THC / Δ9-THC) × 100
- **Extraction Efficiency** = (Output / Input) × 100

## 🎛️ AI Models
1. **Extraction Optimizer** → Predicts efficiency from parameters
2. **Degradation Predictor** → Forecasts shelf-life
3. **Anomaly Detector** → Flags out-of-spec batches
4. **Potency Classifier** → Auto-grades product quality

## ⚠️ Quality Thresholds
| Metric | Good | Warning | Critical |
|--------|------|---------|----------|
| Degradation Index | <2% | 2-5% | >5% |
| Isomerization | <3% | 3-10% | >10% |
| Total Cannabinoids | >90% | 85-90% | <85% |

## 🔧 Common Tasks
- **New Batch**: Dashboard → Batch Entry → Fill form → Save
- **Generate CoA**: CoA Generator → Enter results → Download PDF
- **Check Predictions**: AI Predictions → Select model → Adjust sliders
- **View Alerts**: Quality Control → Review flagged batches

## 📞 Support
- Technical: ARCHITECTURE.md
- Deployment: DEPLOYMENT.md
- Migration: MIGRATION_GUIDE.md

## 💡 Pro Tips
1. Use AI predictions BEFORE running extraction
2. Check Degradation Index for every batch
3. Export data monthly for backup
4. Retrain models quarterly with new data
