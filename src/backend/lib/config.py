import json
import os
import pathlib
import sys


class Config:
    """
    Main System Configuration
    """

    _fp = "config.json"

    def __init__(self, root):
        """
        Initialize main configuration options
        """
        _cp = pathlib.Path.joinpath(root, self._fp)
        _data = self.open_file(_cp)
        breakpoint()
        self.book_path = _data["BOOKPATH"]
        self.TITLE = _data["TITLE"]
        self.VERSION = _data["VERSION"]
        self.TITLE = self.TITLE + " ver " + self.VERSION
        self.book_shelf = _data["BOOKSHELF"]
        self.catalogue_db = _data["DATABASE"]
        self.user = _data["USER"]
        self.password = _data["PASSWORD"]
        self.db_host = _data["DB_HOST"]
        self.db_port = _data["DB_PORT"]
        self.file_array = [
            self.book_shelf,
        ]
        self.root = root
        self.auto_scan = True

        self.allowed_hosts = _data["ALLOWED_HOSTS"]
        self.db_user = _data["USER"]
        self.db_pass = _data["PASSWORD"]
        self.SECRET = _data["SECRET"]

    def open_file(self, _cp):
        """
        Opens config.json and reads in configuration options
        """
        with open(str(_cp), "r") as read_file:
            data = json.load(read_file)
        return data
