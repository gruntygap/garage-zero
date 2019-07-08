from app import app
import config

if __name__ == '__main__':
    if config.prod:
        app.run(host="0.0.0.0", port=80)
    else:
        app.run(host="0.0.0.0", port=80, debug=True)

