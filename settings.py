import os
from dotenv import load_dotenv
load_dotenv()


def get(key):
    env = os.environ.get(key)
    return env
