
from demo_case import create_app, db
from flask_migrate import Migrate, current_app as log
from flask_cors import CORS
from gevent import pywsgi
app = create_app("product")
migrate = Migrate(app, db)

CORS(app, resources=r'/*')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.before_request
def before_request():
    log.logger.info("every before_request")


@app.after_request
def after_request(response):
    log.logger.info("every after_request")
    return response


@app.teardown_request
def teardown_request(response):
    log.logger.info("every teardown_request")
    return response


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('127.0.0.1', 5000), app, log=app.logger)  # 把单线程改造成了单线程异步方式
    server.serve_forever()
    # app.run()  # 启动的是单线程服务，性能很低
