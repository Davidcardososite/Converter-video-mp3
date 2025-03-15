# run.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

print(sys.path)


from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

