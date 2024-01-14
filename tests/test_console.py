#!/usr/bin/python3
"""The console tests"""

import unittest
import console
from console import HBNBCommand


class testconsole(unittest.TestCase):
    """tests class"""

    def create(self):
        """creating the instance"""
        return HBNBCommand()

    def test_EOF(self):
        """testing EOF"""
        cli = self.create()
        self.assertTrue(cli.onecmd("EOF"))

    def test_quit(self):
        """testing quit"""
        cli = self.create()
        self.assertTrue(cli.onecmd("quit"))
