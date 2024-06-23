import argparse
from app import create_app
from Functions import schedule_pipeline

parser = argparse.ArgumentParser(description='Start the app.')
parser.add_argument('--connectionstring', type=str, default='mongodb://localhost:27017/',
                    help='give the connection details')

args = parser.parse_args()

#app = create_app()

if __name__ == '__main__':
    #app.run(debug=True, port=8080,host="0.0.0.0")
    schedule_pipeline()