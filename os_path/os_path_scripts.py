import os

CURRENT_FILE_PATH = os.path.abspath(__file__)

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

os.path.dirname(__file__)
tmp = os.path.join(PROJECT_ROOT_PATH, '..', 'tmp')
if not os.path.exists('tmp'):
    os.mkdir(tmp)
