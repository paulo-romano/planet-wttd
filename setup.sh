git clone https://github.com/CleitonDeLima/planet-wttd.git
cd planet-wttd
python -m venv .planet-wttd
source .planet-wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test