from flask import Flask, render_template, request, send_file, jsonify
import pandas as pd
import os
import chardet

app = Flask(__name__)

# Define the directory for uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
def ensure_upload_directory():
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

# Function to read a CSV file with the correct encoding
def read_csv_with_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    encoding = result['encoding']
    try:
        df = pd.read_csv(file_path, encoding=encoding)
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='iso-8859-1')
    except pd.errors.ParserError:
        df = pd.read_csv(file_path, encoding=encoding, on_bad_lines='skip')
    return df

# Dummy function for map_and_append_data
def map_and_append_data(source_df, destination_df, output_path):
    # Your actual data processing and CSV appending logic goes here
    # For now, it will just save the source file as the output
    source_df.to_csv(output_path, index=False)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    ensure_upload_directory()
    
    source_file = request.files['source_file']
    destination_file = request.files['destination_file']
    
    source_path = os.path.join(app.config['UPLOAD_FOLDER'], source_file.filename)
    destination_path = os.path.join(app.config['UPLOAD_FOLDER'], destination_file.filename)
    
    source_file.save(source_path)
    destination_file.save(destination_path)
    
    source_df = read_csv_with_encoding(source_path)
    destination_df = read_csv_with_encoding(destination_path)
    
    unmapped_columns = {'source': source_df.columns.tolist(), 'destination': destination_df.columns.tolist()}
    return jsonify(unmapped_columns)

@app.route('/process', methods=['POST'])
def process_files():
    column_mapping = request.json['mapping']
    
    source_path = os.path.join(app.config['UPLOAD_FOLDER'], request.json['source_file'])
    destination_path = os.path.join(app.config['UPLOAD_FOLDER'], request.json['destination_file'])
    source_df = read_csv_with_encoding(source_path)
    destination_df = read_csv_with_encoding(destination_path)
    
    # Apply the mapping logic using column_mapping provided by user
    # ...

    output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.csv')
    map_and_append_data(source_df, destination_df, output_path)
    
    return jsonify({'success': True, 'output_file': 'output.csv'})

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
