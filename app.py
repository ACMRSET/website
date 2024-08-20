from dotenv import load_dotenv
from scripts.main import app

load_dotenv()

if __name__ == "__main__" :
    app.run(debug=False, port=5002)