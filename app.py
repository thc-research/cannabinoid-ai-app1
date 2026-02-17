
"""
Cannabinoid Extraction AI Platform
Main Streamlit Application
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import sys
import os

# Add utils to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils.prediction_models import ExtractionOptimizer, DegradationPredictor
from utils.data_processor import DataProcessor, calculate_metrics_standalone

# Page configuration
st.set_page_config(
    page_title="Cannabinoid Extraction AI",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
.main-header {
    font-size: 2.5rem;
    font-weight: bold;
    color: #2E7D32;
    text-align: center;
    margin-bottom: 2rem;
}
.metric-card {
    background-color: #f0f2f6;
    border-radius: 10px;
    padding: 20px;
    border-left: 5px solid #2E7D32;
}
.alert-box {
    padding: 15px;
    border-radius: 5px;
    margin: 10px 0;
}
</style>
""", unsafe_allow_html=True)

# Initialize
if 'batch_data' not in st.session_state:
    st.session_state.batch_data = pd.DataFrame()

# Initialize AI models
optimizer = ExtractionOptimizer()
degrader = DegradationPredictor()

# Sidebar
st.sidebar.title("🔬 Navigation")
page = st.sidebar.radio(
    "Select Module:",
    ["🏠 Dashboard", "📊 Batch Entry", "🤖 AI Predictions", "📋 CoA Generator", "⚠️ Quality Control"]
)

# ==================== DASHBOARD ====================
if page == "🏠 Dashboard":
    st.markdown('<p class="main-header">Cannabinoid Extraction AI Platform</p>', 
                unsafe_allow_html=True)

    # Metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Batches", "24", "+3 vs last month")
    with col2:
        st.metric("Avg Efficiency", "87.3%", "+2.1%")
    with col3:
        st.metric("Degradation Index", "1.8%", "-0.3%", delta_color="inverse")
    with col4:
        st.metric("AI Accuracy", "94.2%", "+1.5%")

    st.markdown("---")

    # Charts
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("📊 Potency Trends")

        trend_data = pd.DataFrame({
            'Batch': ['THC-001', 'THC-002', 'THC-003', 'THC-004', 'THC-005'],
            'Total_THC': [88.1, 89.5, 90.2, 87.8, 91.3],
            'Degradation_Index': [2.1, 1.8, 1.5, 2.3, 1.4]
        })

        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(
            go.Scatter(x=trend_data['Batch'], y=trend_data['Total_THC'],
                      mode='lines+markers', name='Total THC %',
                      line=dict(color='#2E7D32', width=3)),
            secondary_y=False
        )
        fig.add_trace(
            go.Scatter(x=trend_data['Batch'], y=trend_data['Degradation_Index'],
                      mode='lines+markers', name='Degradation Index %',
                      line=dict(color='#C62828', width=3, dash='dash')),
            secondary_y=True
        )
        fig.update_layout(title="Potency vs Freshness", hovermode='x unified')
        st.plotly_chart(fig, use_container_width=True)

    with col_right:
        st.subheader("🎯 Temperature Optimization")

        temp_data = pd.DataFrame({
            'Temperature': ['-40°C', '-60°C', '-80°C'],
            'Efficiency': [82.5, 88.2, 91.4],
            'Degradation_Index': [2.1, 1.8, 1.5]
        })

        fig2 = px.bar(temp_data, x='Temperature', y='Efficiency',
                     title="Efficiency by Temperature",
                     color_discrete_sequence=['#2E7D32'])
        st.plotly_chart(fig2, use_container_width=True)

    # AI Insights
    st.markdown("---")
    st.subheader("🤖 AI Insights")

    insights_col1, insights_col2, insights_col3 = st.columns(3)

    with insights_col1:
        st.success("✅ **Optimization:** Switching to -80°C could improve potency retention by 3.2%")
    with insights_col2:
        st.warning("⚠️ **Alert:** Batch THC-004 shows elevated CBN (2.3%). Review distillation temp.")
    with insights_col3:
        st.info("📈 **Prediction:** Next batch predicted to achieve 92.1% potency")


# ==================== BATCH ENTRY ====================
elif page == "📊 Batch Entry":
    st.header("📊 New Batch Data Entry")

    with st.form("batch_entry"):
        col1, col2, col3 = st.columns(3)

        with col1:
            batch_id = st.text_input("Batch ID", 
                                    value=f"THC-{datetime.now().strftime('%y%m%d')}-001")
            strain = st.selectbox("Strain", ["OG Kush", "Sour Diesel", "Cherry Wine"])
            material = st.selectbox("Material", ["Flower", "Trim"])

        with col2:
            weight = st.number_input("Initial Weight (g)", value=2000.0)
            moisture = st.number_input("Moisture (%)", value=1.8)
            temp = st.selectbox("Temperature (°C)", [-40, -60, -80])

        with col3:
            time = st.slider("Time (min)", 10, 30, 20)
            rpm = st.number_input("RPM", value=1200)
            analyst = st.selectbox("Technician", ["Tech_A", "Tech_B"])

        st.subheader("Analytical Results")

        col4, col5, col6 = st.columns(3)

        with col4:
            d9 = st.number_input("Δ9-THC (%)", value=84.73)
            d8 = st.number_input("Δ8-THC (%)", value=3.37)
        with col5:
            cbd = st.number_input("CBD (%)", value=0.75)
            cbg = st.number_input("CBG (%)", value=1.54)
        with col6:
            cbn = st.number_input("CBN (%)", value=1.88)
            cbc = st.number_input("CBC (%)", value=0.17)

        submitted = st.form_submit_button("💾 Save & Analyze")

        if submitted:
            # Calculate metrics
            data = {
                'd9_thc': d9, 'd8_thc': d8, 'cbd': cbd,
                'cbg': cbg, 'cbn': cbn, 'cbc': cbc
            }

            results = calculate_metrics_standalone(data)

            # AI Prediction
            features = np.array([[temp, time, rpm, weight, moisture]])
            predicted_eff = optimizer.predict(features)[0]

            st.success(f"✅ Batch saved! Predicted Efficiency: {predicted_eff:.1f}%")

            # Display metrics
            m_col1, m_col2, m_col3, m_col4 = st.columns(4)
            with m_col1:
                st.metric("Total Cannabinoids", f"{results['total_cannabinoids']:.2f}%")
            with m_col2:
                st.metric("Total THC", f"{results['total_thc']:.2f}%")
            with m_col3:
                st.metric("Degradation Index", f"{results['degradation_index']:.2f}%")
            with m_col4:
                st.metric("Isomerization Ratio", f"{results['isomerization_ratio']:.2f}%")

# ==================== AI PREDICTIONS ====================
elif page == "🤖 AI Predictions":
    st.header("🤖 AI-Powered Predictions")

    model_type = st.selectbox(
        "Select Model:",
        ["Extraction Optimizer", "Degradation Predictor", "Shelf-Life Estimator"]
    )

    if model_type == "Extraction Optimizer":
        st.subheader("🔬 Optimize Extraction Parameters")

        col1, col2 = st.columns(2)

        with col1:
            opt_temp = st.slider("Temperature (°C)", -80, -20, -60)
            opt_time = st.slider("Time (min)", 10, 30, 20)
            opt_rpm = st.slider("RPM", 800, 1500, 1200)

        with col2:
            # Run prediction
            pred_input = np.array([[opt_temp, opt_time, opt_rpm, 2000, 1.8]])
            prediction = optimizer.predict(pred_input)[0]

            # Gauge chart
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=prediction,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Predicted Efficiency %"},
                gauge={'axis': {'range': [None, 100]},
                       'bar': {'color': "#2E7D32"},
                       'steps': [
                           {'range': [0, 70], 'color': "#ffebee"},
                           {'range': [70, 85], 'color': "#fff3e0"},
                           {'range': [85, 100], 'color': "#e8f5e9"}],
                       'threshold': {'line': {'color': "red", 'width': 4},
                                    'thickness': 0.75, 'value': 85}}
            ))
            st.plotly_chart(fig, use_container_width=True)

            st.info(f"🎯 **Recommendation:** Run at {opt_temp}°C for {opt_time} min → {prediction:.1f}% efficiency")

    elif model_type == "Degradation Predictor":
        st.subheader("⏱️ Shelf-Life Prediction")

        current_thc = st.number_input("Current THC (%)", value=88.0)
        current_cbn = st.number_input("Current CBN (%)", value=1.5)
        storage = st.selectbox("Storage", ["Room Temp", "Refrigerated", "Frozen"])
        months = st.slider("Months", 0, 24, 6)

        # Predict
        months_arr, thc_pred, cbn_pred = degrader.predict_degradation(
            current_thc, current_cbn, storage, months
        )

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=months_arr, y=thc_pred, mode='lines', 
                                name='THC %', line=dict(color='#2E7D32')))
        fig.add_trace(go.Scatter(x=months_arr, y=cbn_pred, mode='lines', 
                                name='CBN %', line=dict(color='#C62828')))
        fig.update_layout(title="Degradation Over Time", 
                         xaxis_title="Months", yaxis_title="Concentration %")
        st.plotly_chart(fig, use_container_width=True)

        # Shelf-life warning
        shelf_life = np.where(thc_pred < current_thc * 0.9)[0]
        if len(shelf_life) > 0:
            st.warning(f"⚠️ Predicted shelf-life: {shelf_life[0]} months (until 10% THC loss)")
        else:
            st.success(f"✅ Stable for {months}+ months")

# ==================== CoA GENERATOR ====================
elif page == "📋 CoA Generator":
    st.header("📋 Certificate of Analysis Generator")

    with st.form("coa_form"):
        st.subheader("Sample Information")

        col1, col2 = st.columns(2)
        with col1:
            coa_batch = st.text_input("Batch ID", "THC-240215-001")
            client = st.text_input("Client", "Treehouse")
            sample_type = st.selectbox("Type", ["Distillate", "Isolate", "Extract"])
        with col2:
            weight = st.number_input("Weight (mg)", value=143)
            date = st.date_input("Date", datetime.now())
            analyst = st.text_input("Analyst", "Nigel Reeves")

        st.subheader("Cannabinoid Results (%)")

        col3, col4, col5 = st.columns(3)
        with col3:
            coa_d9 = st.number_input("Δ9-THC", 0.0, 100.0, 84.73, format="%.4f")
            coa_d8 = st.number_input("Δ8-THC", 0.0, 100.0, 3.3685, format="%.4f")
        with col4:
            coa_cbd = st.number_input("CBD", 0.0, 100.0, 0.7541, format="%.4f")
            coa_cbg = st.number_input("CBG", 0.0, 100.0, 1.5392, format="%.4f")
        with col5:
            coa_cbn = st.number_input("CBN", 0.0, 100.0, 1.8792, format="%.4f")
            coa_cbc = st.number_input("CBC", 0.0, 100.0, 0.1738, format="%.4f")

        generate = st.form_submit_button("📄 Generate CoA")

        if generate:
            # Calculate totals
            total_thc = coa_d9 + coa_d8
            total_cann = total_thc + coa_cbd + coa_cbg + coa_cbn + coa_cbc
            degr_idx = (coa_cbn / total_thc * 100) if total_thc > 0 else 0

            st.success("✅ CoA Generated!")

            # Preview
            preview = pd.DataFrame({
                'Component': ['Δ9-THC', 'Δ8-THC', 'CBD', 'CBG', 'CBN', 'CBC', 'TOTAL'],
                '% w/w': [coa_d9, coa_d8, coa_cbd, coa_cbg, coa_cbn, coa_cbc, total_cann],
                'mg/g': [x*10 for x in [coa_d9, coa_d8, coa_cbd, coa_cbg, coa_cbn, coa_cbc, total_cann]]
            })
            st.table(preview)

            st.metric("Degradation Index", f"{degr_idx:.2f}%", 
                     delta="Fresh" if degr_idx < 2 else "Moderate" if degr_idx < 5 else "Degraded")

            st.download_button("⬇️ Download CoA PDF", b"PDF content", f"CoA_{coa_batch}.pdf")

# ==================== QUALITY CONTROL ====================
elif page == "⚠️ Quality Control":
    st.header("⚠️ AI Quality Control & Alerts")

    # Simulated alerts
    alerts = [
        {'level': 'Critical', 'batch': 'THC-004', 
         'msg': 'Degradation Index exceeded 5%', 'rec': 'Reduce distillation temp to 140°C'},
        {'level': 'Warning', 'batch': 'THC-002', 
         'msg': 'Isomerization Ratio elevated (4.2%)', 'rec': 'Check ethanol pH'},
        {'level': 'Info', 'batch': 'THC-001', 
         'msg': 'AI predicts 3.2% efficiency improvement possible', 'rec': 'Consider -80°C extraction'}
    ]

    for alert in alerts:
        if alert['level'] == 'Critical':
            st.error(f"🚨 **{alert['level']}: {alert['batch']}**\n{alert['msg']}\n💡 {alert['rec']}")
        elif alert['level'] == 'Warning':
            st.warning(f"⚠️ **{alert['level']}: {alert['batch']}**\n{alert['msg']}\n💡 {alert['rec']}")
        else:
            st.info(f"ℹ️ **{alert['level']}: {alert['batch']}**\n{alert['msg']}\n💡 {alert['rec']}")

    # Anomaly detection visualization
    st.subheader("🔍 Anomaly Detection")

    np.random.seed(42)
    normal = np.random.multivariate_normal([85, 2], [[10, 0.5], [0.5, 1]], 50)
    anomalies = np.array([[95, 8], [70, 6], [90, 7]])
    all_data = np.vstack([normal, anomalies])
    labels = ['Normal'] * 50 + ['Anomaly'] * 3

    fig = px.scatter(x=all_data[:, 0], y=all_data[:, 1], color=labels,
                    labels={'x': 'Efficiency %', 'y': 'Degradation Index %'},
                    title="Batch Performance Clustering",
                    color_discrete_map={'Normal': '#2E7D32', 'Anomaly': '#C62828'})
    st.plotly_chart(fig, use_container_width=True)

# Footer
st.sidebar.markdown("---")
st.sidebar.info("Cannabinoid Extraction AI v2.0 | Built with Streamlit & Python")
