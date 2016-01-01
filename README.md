# Planet WTTD

https://planet-wttd.herokuapp.com/

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone https://github.com/CleitonDeLima/planet-wttd.git planet-wttd
cd planet-wttd
python -m venv .planet-wttd
source .planet-wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

### setup.sh

Ou se preferir você pode baixar o `setup.sh` que ele faz tudo pra você.

```console
wget --output-document=setup.sh https://goo.gl/fPVKXM
source setup.sh
```
