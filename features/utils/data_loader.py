import json
import os

def load_test_data(filename):
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', filename)
    with open(data_path, 'r', encoding='utf-8') as f:
        return json.load(f)
