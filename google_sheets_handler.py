import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

def connect_to_google():
    """Connect to Google Sheets"""
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
    
    creds = Credentials.from_service_account_file('password.json', scopes=scopes)
    client = gspread.authorize(creds)
    return client

def save_to_google(sheet_url, data):
    """Save batch data to Google Sheet"""
    try:
        client = connect_to_google()
        sheet = client.open_by_url(sheet_url).sheet1
        
        # Create row from data
        row = [
            data.get('batch_id', ''),
            data.get('date', ''),
            data.get('technician', ''),
            data.get('strain', ''),
            data.get('temp_c', ''),
            data.get('time_min', ''),
            data.get('thc_percent', ''),
            data.get('degradation_index', '')
        ]
        
        sheet.append_row(row)
        return True
    except Exception as e:
        print(f"Error saving to Google: {e}")
        return False

def get_all_from_google(sheet_url):
    """Get all data from Google Sheet"""
    try:
        client = connect_to_google()
        sheet = client.open_by_url(sheet_url).sheet1
        data = sheet.get_all_records()
        return pd.DataFrame(data)
    except Exception as e:
        print(f"Error reading from Google: {e}")
        return pd.DataFrame()
