
"""
Certificate of Analysis Generator
Matches Treehouse CoA format
"""

from fpdf import FPDF
from datetime import datetime
import pandas as pd

class CoAGenerator(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)

    def header(self):
        # Logo placeholder
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'CERTIFICATE OF ANALYSIS', 0, 1, 'C')
        self.ln(5)

    def generate_coa(self, data, output_path):
        """Generate CoA PDF matching Treehouse format"""
        self.add_page()

        # Sample info section
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Sample Information', 0, 1)
        self.set_font('Arial', '', 10)

        info_lines = [
            f"Client: {data.get('client', 'Treehouse')}",
            f"Batch ID: {data.get('batch_id', '')}",
            f"Sample Type: {data.get('sample_type', 'Distillate')}",
            f"Sample Weight: {data.get('sample_weight', 143)} mg",
            f"Analysis Date: {data.get('analysis_date', datetime.now().strftime('%Y-%m-%d'))}",
            f"Analyst: {data.get('analyst', 'Nigel Reeves')}"
        ]

        for line in info_lines:
            self.cell(0, 6, line, 0, 1)

        self.ln(5)

        # Instrument conditions
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Instrument Conditions', 0, 1)
        self.set_font('Arial', '', 10)

        instrument_lines = [
            "Instrument: Varian 3900 GC-FID",
            "Column: RTX-5MS 30m x 0.25mm x 0.25μm",
            "Carrier: Helium at 1 mL/min",
            "Detector: FID @ 250°C",
            "Injector: 250°C",
            "Injection: 1 μL autosampler",
            "Split Ratio: 1:50"
        ]

        for line in instrument_lines:
            self.cell(0, 6, line, 0, 1)

        self.ln(5)

        # Results table
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Cannabinoid Analysis Results', 0, 1)

        # Table header
        self.set_fill_color(200, 200, 200)
        self.set_font('Arial', 'B', 10)
        self.cell(60, 8, 'Component', 1, 0, 'C', True)
        self.cell(40, 8, '% w/w', 1, 0, 'C', True)
        self.cell(40, 8, 'mg/g', 1, 0, 'C', True)
        self.cell(40, 8, 'mg/mL', 1, 1, 'C', True)

        # Table data
        self.set_font('Arial', '', 10)

        components = [
            ('CBC', data.get('cbc', 0.1738)),
            ('CBD', data.get('cbd', 0.7541)),
            ('Δ8-THC', data.get('d8_thc', 3.3685)),
            ('Δ9-THC', data.get('d9_thc', 84.7281)),
            ('CBG', data.get('cbg', 1.5392)),
            ('CBN', data.get('cbn', 1.8792))
        ]

        total = sum([c[1] for c in components])

        for name, value in components:
            self.cell(60, 7, name, 1)
            self.cell(40, 7, f"{value:.4f}", 1, 0, 'R')
            self.cell(40, 7, f"{value*10:.4f}", 1, 0, 'R')
            self.cell(40, 7, f"{value*9:.4f}", 1, 1, 'R')  # Assuming density 0.9

        # Total row
        self.set_font('Arial', 'B', 10)
        self.cell(60, 8, 'TOTAL CANNABINOIDS', 1, 0, 'L', True)
        self.cell(40, 8, f"{total:.4f}", 1, 0, 'R', True)
        self.cell(40, 8, f"{total*10:.4f}", 1, 0, 'R', True)
        self.cell(40, 8, f"{total*9:.4f}", 1, 1, 'R', True)

        self.ln(10)

        # Calculated metrics
        self.set_font('Arial', 'B', 11)
        total_thc = data.get('d9_thc', 84.7281) + data.get('d8_thc', 3.3685)
        degradation_idx = (data.get('cbn', 1.8792) / total_thc * 100) if total_thc > 0 else 0

        self.cell(0, 8, f"Total THC (Δ9 + Δ8): {total_thc:.2f}%", 0, 1)
        self.cell(0, 8, f"Degradation Index: {degradation_idx:.2f}%", 0, 1)

        # Notes
        self.ln(5)
        self.set_font('Arial', 'B', 10)
        self.cell(0, 8, 'Notes:', 0, 1)
        self.set_font('Arial', '', 9)

        notes = [
            "• Δ9-THC is the combination of THC and THCA",
            "• CBD is the combination of CBD and CBDA",
            "• % is the percentage weight of the component found in the sample",
            "• Components referenced against certified calibration standards",
            "• Date of last calibration: 16/3/2023",
            "• This test does not include: pesticides, heavy metals, mycotoxins, molds, residual solvents"
        ]

        for note in notes:
            self.cell(0, 5, note, 0, 1)

        # Signature
        self.ln(10)
        self.set_font('Arial', 'B', 10)
        self.cell(0, 8, f"Analyst: {data.get('analyst', 'Nigel Reeves')}", 0, 1)
        self.cell(0, 8, f"Date: {datetime.now().strftime('%Y-%m-%d')}", 0, 1)

        # Save
        self.output(output_path)
        return output_path


def generate_coa_pdf(data):
    """Helper function to generate CoA"""
    generator = CoAGenerator()
    output_path = f"coa_{data.get('batch_id', 'unknown')}.pdf"
    return generator.generate_coa(data, output_path)
