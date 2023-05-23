import os

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

os.path.dirname(__file__)
tmp = os.path.abspath(os.path.join(PROJECT_ROOT_PATH, '..', 'tmp'))
if not os.path.exists('tmp'):
    os.mkdir(tmp)
