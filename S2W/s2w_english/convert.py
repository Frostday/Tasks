import requests


def convert_s2w(text):
    x = requests.get(f"http://localhost:5000/spoken_to_written?text={text}")
    # print("Output: " + x.text[1:-2])
    return x.text[1:-2]
