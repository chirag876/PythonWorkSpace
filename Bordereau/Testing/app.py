from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import pandas as pd
import chardet
import os
from fuzzywuzzy import fuzz, process

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'Documents'  # Ensure this directory exists or is created on startup
ALLOWED_EXTENSIONS = {'csv'}

# Helper function to check file extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Helper function to read a CSV file with the correct encoding
def read_csv_with_detected_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read(100000))  # Read enough sample to detect encoding
    encoding = result['encoding']

    try:
        return pd.read_csv(file_path, encoding=encoding)
    except UnicodeDecodeError:
        # If the encoding detected doesn't work, try another common encoding
        return pd.read_csv(file_path, encoding='ISO-8859-1')
    except Exception as e:
        # Handle other exceptions
        print(f"Error reading file {file_path}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame or handle error accordingly

# Helper function to auto-map columns using fuzzy matching
def auto_map_columns(source_columns, destination_columns, threshold=85):
    mapping = {}
    for source_col in source_columns:
        match, score = process.extractOne(source_col, destination_columns, scorer=fuzz.token_sort_ratio)
        if score >= threshold:
            mapping[source_col] = match
    return mapping

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'source_file' not in request.files or 'destination_file' not in request.files:
        return jsonify({'error': 'No file part'})

    source_file = request.files['source_file']
    destination_file = request.files['destination_file']

    if source_file.filename == '' or destination_file.filename == '':
        return jsonify({'error': 'No selected file'})

    if source_file and allowed_file(source_file.filename) and destination_file and allowed_file(destination_file.filename):
        source_filename = secure_filename(source_file.filename)
        destination_filename = secure_filename(destination_file.filename)

        source_filepath = os.path.join(app.config['UPLOAD_FOLDER'], source_filename)
        destination_filepath = os.path.join(app.config['UPLOAD_FOLDER'], destination_filename)

        source_file.save(source_filepath)
        destination_file.save(destination_filepath)

        source_df = read_csv_with_detected_encoding(source_filepath)
        destination_df = read_csv_with_detected_encoding(destination_filepath)

        mapping = auto_map_columns(source_df.columns.tolist(), destination_df.columns.tolist())

        unmapped_source_cols = [col for col in source_df.columns if col not in mapping]
        mapped_destination_cols = mapping.values()
        unmapped_destination_cols = [col for col in destination_df.columns if col not in mapped_destination_cols]

        return jsonify({
            'mapping': mapping,
            'unmapped_source_cols': unmapped_source_cols,
            'unmapped_destination_cols': unmapped_destination_cols
        })

    return jsonify({'error': 'Invalid file type'})

if __name__ == '__main__':
    # Ensure the upload folder exists
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    
    app.run(debug=True)
