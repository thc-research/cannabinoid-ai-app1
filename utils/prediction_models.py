
"""
AI Prediction Models for Cannabinoid Extraction
Based on research: PNN-GA optimization [^21^], Random Forest, LSTM
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor, IsolationForest
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import joblib
import warnings
warnings.filterwarnings('ignore')

class ExtractionOptimizer:
    """
    Random Forest model for optimizing extraction parameters
    Predicts: Yield, Efficiency, Potency Retention

    Based on DoE data from Excel workbook
    """

    def __init__(self):
        self.model = RandomForestRegressor(
            n_estimators=100,
            max_depth=10,
            random_state=42
        )
        self.scaler = StandardScaler()
        self.is_trained = False

    def train(self, X, y):
        """Train the model with historical batch data"""
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)
        self.is_trained = True

    def predict(self, X):
        """Predict extraction efficiency"""
        if not self.is_trained:
            # Return simulated prediction based on heuristics
            temp, time, rpm, weight, moisture = X[0]
            # Higher temp (less negative) = lower efficiency
            # Optimal around -60 to -80
            base_eff = 85
            temp_bonus = abs(temp + 60) * 0.1 if temp < -60 else -abs(temp + 40) * 0.2
            time_factor = -0.05 * (time - 20)**2

            return np.array([base_eff + temp_bonus + time_factor])

        X_scaled = self.scaler.transform(X)
        return self.model.predict(X_scaled)

    def optimize_parameters(self, bounds=None):
        """
        Genetic Algorithm optimization (simplified)
        Returns optimal temp, time, rpm
        """
        if bounds is None:
            bounds = {
                'temp': (-80, -40),
                'time': (15, 25),
                'rpm': (1000, 1400)
            }

        # Grid search for optimal (simplified GA)
        best_score = 0
        best_params = None

        for temp in range(-80, -39, 5):
            for time in range(15, 26, 2):
                for rpm in range(1000, 1401, 100):
                    score = self.predict(np.array([[temp, time, rpm, 2000, 1.8]]))[0]
                    if score > best_score:
                        best_score = score
                        best_params = {'temp': temp, 'time': time, 'rpm': rpm}

        return best_params, best_score

    def save(self, filepath):
        joblib.dump({'model': self.model, 'scaler': self.scaler}, filepath)

    def load(self, filepath):
        data = joblib.load(filepath)
        self.model = data['model']
        self.scaler = data['scaler']
        self.is_trained = True


class DegradationPredictor:
    """
    Time-series predictor for cannabinoid degradation
    Uses simplified LSTM-like approach
    Predicts CBN formation and shelf-life
    """

    def __init__(self):
        self.degradation_rates = {
            'Room Temp (20°C)': 0.5,  # % per month
            'Refrigerated (4°C)': 0.2,
            'Frozen (-20°C)': 0.05
        }

    def predict_degradation(self, initial_thc, initial_cbn, storage_temp, months):
        """
        Predict THC degradation and CBN formation over time

        Model: First-order kinetics
        THC(t) = THC0 * exp(-k*t)
        CBN(t) = CBN0 + (THC0 - THC(t)) * conversion_factor
        """
        rate = self.degradation_rates.get(storage_temp, 0.3)

        time_points = np.arange(0, months + 1)
        thc_values = initial_thc * np.exp(-rate * time_points / 12)
        cbn_values = initial_cbn + (initial_thc - thc_values) * 0.3

        return time_points, thc_values, cbn_values

    def estimate_shelf_life(self, initial_thc, threshold=0.9):
        """
        Estimate shelf-life until THC degrades to threshold

        Returns: months until 10% degradation
        """
        # Simplified calculation
        for temp_name, rate in self.degradation_rates.items():
            months_to_threshold = -12 * np.log(threshold) / rate
            print(f"{temp_name}: {months_to_threshold:.1f} months")

        return months_to_threshold

    def predict_optimal_storage(self, target_shelf_life_months):
        """Recommend storage conditions for target shelf-life"""
        recommendations = []

        for temp_name, rate in self.degradation_rates.items():
            achievable_months = -12 * np.log(0.9) / rate
            if achievable_months >= target_shelf_life_months:
                recommendations.append({
                    'temp': temp_name,
                    'max_months': achievable_months,
                    'suitable': True
                })
            else:
                recommendations.append({
                    'temp': temp_name,
                    'max_months': achievable_months,
                    'suitable': False
                })

        return recommendations


class AnomalyDetector:
    """
    Isolation Forest for detecting anomalous batches
    """

    def __init__(self):
        self.model = IsolationForest(
            contamination=0.1,
            random_state=42
        )
        self.is_trained = False

    def train(self, X):
        """Train on normal batch data"""
        self.model.fit(X)
        self.is_trained = True

    def detect(self, X):
        """
        Returns: -1 for anomaly, 1 for normal
        """
        if not self.is_trained:
            # Simple rule-based detection
            efficiency, degradation = X[0]
            if efficiency < 70 or degradation > 5:
                return np.array([-1])
            return np.array([1])

        return self.model.predict(X)

    def anomaly_score(self, X):
        """Return anomaly score (lower = more anomalous)"""
        return self.model.decision_function(X) if self.is_trained else np.array([0])


class PotencyClassifier:
    """
    SVM/Neural Network for classifying product grade
    Input: Cannabinoid profile
    Output: Grade (A/B/C), Pass/Fail
    """

    def __init__(self):
        self.model = SVC(probability=True, random_state=42)
        self.scaler = StandardScaler()
        self.is_trained = False

    def calculate_grade(self, total_cannabinoids, degradation_index, isomerization_ratio):
        """
        Rule-based grading (can be replaced with ML model)

        Grade A: >90% cannabinoids, <2% degradation, <3% isomerization
        Grade B: >85% cannabinoids, <3% degradation, <5% isomerization
        Grade C: >80% cannabinoids, <5% degradation, <10% isomerization
        Fail: <80% or >5% degradation
        """
        if total_cannabinoids >= 90 and degradation_index < 2 and isomerization_ratio < 3:
            return 'A', 'Pass'
        elif total_cannabinoids >= 85 and degradation_index < 3 and isomerization_ratio < 5:
            return 'B', 'Pass'
        elif total_cannabinoids >= 80 and degradation_index < 5:
            return 'C', 'Pass'
        else:
            return 'F', 'Fail'

    def predict_compliance(self, cbd_thc_ratio, total_thc, product_type='hemp'):
        """
        Predict regulatory compliance

        Hemp: CBD/THC > 20, Total THC < 0.3%
        Cannabis: No restrictions (but track potency)
        """
        if product_type == 'hemp':
            is_compliant = (cbd_thc_ratio > 20) and (total_thc < 0.3)
            return {
                'compliant': is_compliant,
                'cbd_thc_check': cbd_thc_ratio > 20,
                'thc_check': total_thc < 0.3
            }
        return {'compliant': True, 'note': 'Cannabis product - no THC limit'}


# Utility functions
def calculate_degradation_index(cbn, total_thc):
    """Calculate degradation index as per CoA"""
    return (cbn / total_thc * 100) if total_thc > 0 else 0

def calculate_isomerization_ratio(d8_thc, d9_thc):
    """Calculate isomerization ratio as per CoA"""
    return (d8_thc / d9_thc * 100) if d9_thc > 0 else 0

def estimate_extraction_efficiency(initial_potency, final_potency, mass_yield):
    """
    Estimate extraction efficiency
    Efficiency = (Final potency × Final mass) / (Initial potency × Initial mass)
    """
    return (final_potency * mass_yield) / initial_potency * 100
