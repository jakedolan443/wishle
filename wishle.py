from flask import Flask
from web.main import body


app = Flask(__name__, static_url_path='', 
            static_folder='web/static',
            template_folder='web/serve')
app.register_blueprint(body)
app.run(host="0.0.0.0", port=8080)


