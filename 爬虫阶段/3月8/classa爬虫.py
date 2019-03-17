import request
import re
import pymongo
import time

def get_response(url):
    response=request.get(url)
    html=response.text
    return html


def main():
    url='https://maoyan.com/board'