import requests


class Notifications:
    def __init__(self, message, event, key, title="iftt"):
        self.title = title
        self.message = message
        self.event = event
        self.key = key
        self.url = f"https://maker.ifttt.com/trigger/{self.event}/with/key/{self.key}?value1={self.title}&value2={self.message}"
        self.response = requests.get(self.url)