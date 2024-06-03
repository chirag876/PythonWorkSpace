# ---------------------------------------------------------------- with swagger
# from flask import Flask, request, jsonify, send_file
# import pandas as pd
# from Swagger_config.swagger_configuration import configure_swagger, SWAGGER_URL, serve_swagger_json
# import json

# app = Flask(__name__)
# # SWAGGER_URL = '/swagger'
# # # Swagger UI configuration
# # swaggerui_blueprint = configure_swagger()
# # app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# # @app.route('/swagger.json')
# # def swagger():
# #     return serve_swagger_json()

# @app.route('/csv-to-json', methods=['POST'])
# def csv_to_json():
#     try:
#         # Check if the request contains a file
#         if 'file' not in request.files:
#             return jsonify({'error': 'No file part'}), 400

#         file = request.files['file']

#         # Check if the file is empty
#         if file.filename == '':
#             return jsonify({'error': 'No selected file'}), 400

#         # Check if the file is a CSV
#         if not file.filename.lower().endswith('.csv'):
#             return jsonify({'error': 'File must be a CSV'}), 400
#         # Read CSV and convert to JSON
#         df = pd.read_csv(file)
#         json_data = df.to_json(orient='records')

#         json_data_object = json.loads(json_data)

#         return jsonify({'data': json_data_object})

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True, port=8080)

# ------------------------------------------------------------------------------- with UI 
from flask import Flask, request, jsonify, send_file, render_template
import pandas as pd
import tempfile

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/styles.css')
def styles():
    return send_file('static/styles.css')

@app.route('/csv-to-json', methods=['POST'])
def csv_to_json():
    try:
        # Check if the request contains a file
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files['file']

        # Check if the file is empty
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        # Check if the file is a CSV
        if not file.filename.lower().endswith('.csv'):
            return jsonify({'error': 'File must be a CSV'}), 400

        # Read CSV and convert to JSON
        df = pd.read_csv(file)
        json_data = df.to_json(orient='records')

        # Get the original filename with extension (including .csv)
        filename = file.filename

        # Save the JSON data to a temporary file with the original filename
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.json')
        temp_file.write(json_data.encode('utf-8'))
        temp_file.close()

        # Serve the temporary file as a download with the original filename
        return send_file(temp_file.name, as_attachment=True)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8080)
