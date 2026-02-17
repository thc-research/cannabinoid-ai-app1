
"""
Data Processing Utilities
Handles ETL from Excel, database operations, and metric calculations
"""

import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime

class DataProcessor:
    """Process and validate batch data"""

    def __init__(self, db_path='data/extraction.db'):
        self.db_path = db_path
        self.init_database()

    def init_database(self):
        """Initialize SQLite database with tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Batches table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS batches (
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
            )
        """)

        conn.commit()
        conn.close()

    def calculate_metrics(self, data):
        """Calculate all derived metrics"""
        # Total cannabinoids
        data['total_cannabinoids'] = (
            data.get('d9_thc', 0) + data.get('d8_thc', 0) + 
            data.get('cbd', 0) + data.get('cbg', 0) + 
            data.get('cbn', 0) + data.get('cbc', 0)
        )

        # Total THC
        data['total_thc'] = data.get('d9_thc', 0) + data.get('d8_thc', 0)

        # Degradation index
        if data['total_thc'] > 0:
            data['degradation_index'] = (data.get('cbn', 0) / data['total_thc']) * 100
        else:
            data['degradation_index'] = 0

        # Isomerization ratio
        if data.get('d9_thc', 0) > 0:
            data['isomerization_ratio'] = (data.get('d8_thc', 0) / data['d9_thc']) * 100
        else:
            data['isomerization_ratio'] = 0

        return data


def calculate_metrics_standalone(data):
    """Standalone metric calculation"""
    processor = DataProcessor()
    return processor.calculate_metrics(data)
