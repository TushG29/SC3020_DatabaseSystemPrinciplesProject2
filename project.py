from explore import backend
from interface import frontend
from multiprocessing import Process
import signal

if __name__ == '__main__':
    flask_process = Process(target=backend)
    flask_process.start()
    frontend()
    flask_process.kill()