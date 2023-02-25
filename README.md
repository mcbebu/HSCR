# Flask wsgi backend

## Setup
1. (optional) Use a virtualenv
   * Why use a venv? It isolates your dependencies and helps prevent version conflicts with other projects or system dependencies.
   1. `python -m venv venv` will create a venv in a directory named venv
   2. `source ./venv/bin/activate` will activate the venv
2. Install dependencies
  * `pip install -r requirements.txt`
3. Run the app
  * `waitress-serve --listen=127.0.0.1:5000 wsgi:app`
4. Visit localhost:5000 in your web browser.
