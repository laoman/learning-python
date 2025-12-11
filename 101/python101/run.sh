python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

export FLASK_APP=app.py
export FLASK_ENV=development

flask run --host=0.0.0.0 --port=8000 --reload
