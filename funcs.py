#!/usr/bin/python3

# This file contains my functions that will be used around this project

from bs4 import BeautifulSoup
import requests


class MyFuncs:
    def soupify(self, content):
        soup = BeautifulSoup(str(content), "lxml")
        return soup

    def soup_request(self, url):
        return self.soupify(self.request(url))

    def request(self, url):
        response = requests.get(url)
        return response.content

    def read_file(self, path):
        with open(path, "r") as f:
            content = f.read()
        return content

    def write_file(self, path, content):
        with open(path, "w") as f:
            f.write(str(content))

    def append_file(self, path, content):
        with open(path, "a") as f:
            f.write(str(content) + "\n")
