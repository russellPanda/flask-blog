import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from blog import create_app


if __name__ == '__main__':
    app=create_app('production')
    app.run(debug=True,host="127.0.0.1")
