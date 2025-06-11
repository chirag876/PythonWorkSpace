import pandas as pd
from sdv.metadata import SingleTableMetadata
from sdv.evaluation.single_table import evaluate_quality
from datetime import datetime
import os

def load_data(real_path, synthetic_path, metadata_path):
    real_data = pd.read_csv(real_path)
    synthetic_data = pd.read_csv(synthetic_path)
    metadata = SingleTableMetadata.load_from_json(filepath=metadata_path)
    metadata.validate()
    return real_data, synthetic_data, metadata

def generate_text_report(quality_report, real_data, synthetic_data, text_path, real_path, synthetic_path):
    report_lines = []
    report_lines.append("="*80)
    report_lines.append("SDV Synthetic Data Quality Report")
    report_lines.append("="*80)
    report_lines.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append(f"Real Data: {real_path} ({len(real_data)} rows, {len(real_data.columns)} columns)")
    report_lines.append(f"Synthetic Data: {synthetic_path} ({len(synthetic_data)} rows, {len(synthetic_data.columns)} columns)")
    report_lines.append("="*80)

    overall_score = quality_report.get_score()
    report_lines.append("\n1. Overall Quality Score")
    report_lines.append("-"*50)
    report_lines.append(f"Score: {overall_score:.2%} (Higher is better)")
    report_lines.append("Description: Aggregated score of column shapes and pair trends.")

    report_lines.append("\n2. Column Shapes (Distribution Similarity)")
    report_lines.append("-"*50)
    report_lines.append("Evaluates how well synthetic data matches the distribution of individual columns.")
    report_lines.append("\n{:<30} {:<20} {:<10}".format("Column", "Metric", "Score"))
    report_lines.append("-"*60)
    column_shapes = quality_report.get_details(property_name='Column Shapes')
    for _, row in column_shapes.iterrows():
        report_lines.append("{:<30} {:<20} {:<10.2%}".format(
            row['Column'], row['Metric'], row['Score']
        ))

    report_lines.append("\n3. Column Pair Trends (Correlation Similarity)")
    report_lines.append("-"*50)
    report_lines.append("Evaluates how well synthetic data captures correlations between column pairs.")
    report_lines.append("\n{:<30} {:<30} {:<10}".format("Column 1", "Column 2", "Score"))
    report_lines.append("-"*60)
    column_pairs = quality_report.get_details(property_name='Column Pair Trends')
    for _, row in column_pairs.iterrows():
        report_lines.append("{:<30} {:<30} {:<10.2%}".format(
            row['Column 1'], row['Column 2'], row['Score']
        ))

    report_lines.append("\n" + "="*80)
    report_lines.append("End of Report")
    report_lines.append("="*80)

    with open(text_path, 'w', encoding='utf-8') as f:
        for line in report_lines:
            f.write(line + "\n")
    print(f"\n✅ Text report saved to: {text_path}")

def generate_html_report(quality_report, real_data, synthetic_data, html_path, real_path, synthetic_path):
    overall_score = quality_report.get_score()
    column_shapes = quality_report.get_details(property_name='Column Shapes')
    column_pairs = quality_report.get_details(property_name='Column Pair Trends')

    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>SDV Synthetic Data Quality Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; padding: 20px; }}
        h1, h2 {{ color: #2E4053; }}
        table {{ width: 100%; border-collapse: collapse; margin-bottom: 30px; }}
        th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
        .section-title {{ margin-top: 40px; }}
    </style>
</head>
<body>
    <h1>SDV Synthetic Data Quality Report</h1>
    <p><strong>Generated on:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    <p><strong>Real Data:</strong> {real_path} ({len(real_data)} rows, {len(real_data.columns)} columns)</p>
    <p><strong>Synthetic Data:</strong> {synthetic_path} ({len(synthetic_data)} rows, {len(synthetic_data.columns)} columns)</p>

    <h2 class="section-title">1. Overall Quality Score</h2>
    <table>
        <tr><th>Metric</th><th>Value</th></tr>
        <tr><td>Score</td><td>{overall_score:.2%}</td></tr>
        <tr><td>Description</td><td>Aggregated score of column shapes and pair trends. Higher is better.</td></tr>
    </table>

    <h2 class="section-title">2. Column Shapes (Distribution Similarity)</h2>
    <p>Evaluates how well synthetic data matches the distribution of individual columns.</p>
    <table>
        <tr><th>Column</th><th>Metric</th><th>Score</th></tr>
    """
    for _, row in column_shapes.iterrows():
        html += f"<tr><td>{row['Column']}</td><td>{row['Metric']}</td><td>{row['Score']:.2%}</td></tr>\n"

    html += """
    </table>
    <h2 class="section-title">3. Column Pair Trends (Correlation Similarity)</h2>
    <p>Evaluates how well synthetic data captures correlations between column pairs.</p>
    <table>
        <tr><th>Column 1</th><th>Column 2</th><th>Score</th></tr>
    """
    for _, row in column_pairs.iterrows():
        html += f"<tr><td>{row['Column 1']}</td><td>{row['Column 2']}</td><td>{row['Score']:.2%}</td></tr>\n"

    html += """
    </table>
</body>
</html>
    """
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ HTML report saved to: {html_path}")

def generate_quality_reports(
    real_data_path='flat-training.csv',
    synthetic_data_path='synthetic_data.csv',
    metadata_path='metadata.json',
    text_report_path='quality_report.txt',
    html_report_path='quality_report.html'
):
    try:
        real_data, synthetic_data, metadata = load_data(real_data_path, synthetic_data_path, metadata_path)
        print("✅ Data and metadata loaded and validated.")
        
        quality_report = evaluate_quality(real_data=real_data, synthetic_data=synthetic_data, metadata=metadata)
        print("✅ Quality evaluation completed.")

        generate_text_report(quality_report, real_data, synthetic_data, text_report_path, real_data_path, synthetic_data_path)
        generate_html_report(quality_report, real_data, synthetic_data, html_report_path, real_data_path, synthetic_data_path)

    except Exception as e:
        print(f"❌ Error during report generation: {str(e)}")

# Main Execution
if __name__ == "__main__":
    generate_quality_reports()
