from naginie_demo import create_app
from config import DevConfig as Config

app = create_app(Config)

if __name__ == '__main__':
	app.run(host=Config.HOST, port=Config.PORT)