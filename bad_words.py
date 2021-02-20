import requests

def get_bw():
    bw = requests.get('https://www.cs.cmu.edu/~biglou/resources/bad-words.txt')
    bw = bw.text.split('\n')
    bw.pop(0)
    bw.pop(-1)
    return bw