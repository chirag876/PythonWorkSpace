import argparse
from app import create_app

parser = argparse.ArgumentParser(description='Start the app.')
parser.add_argument('--connectionstring', type=str, default='mongodb://localhost:27017/',
                    help='give the connection details')

args = parser.parse_args()

app = create_app(args.connectionstring)

if __name__ == '__main__':
    app.run(debug=True, port=8080,host="0.0.0.0")