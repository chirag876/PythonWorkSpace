#copy flask code
import os
from flask import Flask, request, redirect, url_for, send_file, send_from_directory, render_template
from mapping import main
app = Flask(__name__)


input_path = 'C:/Users/Anirudh/Desktop/company/column_mapping/input'
#OUTPUT_path = 'C:/Users/Anirudh/Desktop/company/Main/Main/output'
app.config['OUTPUT_PATH'] = 'C:/Users/Anirudh/Desktop/company/column_mapping/output' 

@app.route('/processdata', methods = ['GET','POST'])
def process():
    source_file = request.files['source_file']
    benchmark_file = request.files['benchmark_file']
    config_file = request.files['config_file']

    if source_file and benchmark_file and config_file:
        source_path = os.path.join(input_path, 'source.csv')
        benchmark_path = os.path.join(input_path, 'benchmark.csv')
        config_path = os.path.join(input_path, 'config.json')

        source_file.save(source_path)
        benchmark_file.save(benchmark_path)
        config_file.save(config_path)

        output_path = os.path.join('C:/Users/Anirudh/Desktop/company/column_mapping/output', 'output.csv')
        schema_path = os.path.join('C:/Users/Anirudh/Desktop/company/column_mapping/output', 'schema.csv')

        # Run the main function with the uploaded file objects and output paths
        main(source_path, benchmark_path, output_path, schema_path, config_path)
        return send_file(os.path.join(output_path), as_attachment=True)
            
    
        
        #return render_template('download.html')
        #return redirect(url_for("download"))

    return 'Upload all the files.'

@app.route('/download')
def download():
  return render_template(download.html, files = os.listdir("output"))

@app.route('/download_output')
def download_output():
    filename = 'output.csv'
    return send_from_directory(app.config['OUTPUT_PATH'], filename, as_attachment=True)

@app.route('/download_schema')
def download_schema(filename):
    filename = 'schema.csv'
    return send_from_directory(app.config['OUTPUT_PATH'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)