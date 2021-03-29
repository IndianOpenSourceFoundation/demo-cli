#!/usr/bin/env python

import argparse
from src.arguments.search import Search

version = "0.1"

parser = argparse.ArgumentParser()
parser.add_argument("-start",  
                    help="introduce you to dynamic",
                    action="store_true")

parser.add_argument("-s",
                    "--search",
                    help="search a question on StackOverflow",
                    action="store_true")

parser.add_argument("-V",
                    "--version",
                    version=f"Dynamic-CLI version {version}",
                    action='version')

parser.add_argument(
    "-n",
    "--new",
    help="Opens browser to create new StackOverflow question.",
    const=True,
    metavar="title (optional)",
    nargs="?")

parser.add_argument("-file",
                    "--file",
                    help="Save answer to a file",
                    action="store_true")

ARGV = parser.parse_args()

search_flag = Search(ARGV)

if __name__ == "__main__":
    if ARGV.start:
        print('''
        \U0001F604 Hello and Welcome to Dynamic CLI 
        \U0001F917 Use the following commands to get started 
        \U0001F50E Search on StackOverflow with '-s' 
        \U0001F4C4 Open browser to create new Stack Overflow question with '-n[title(optional)] 
        \U0001F4C2 Save answer to a file with '-file'
        \U00002728 Know the version of Dynamic CLI with '-V' 
        \U0001F609 See this message again with '-start'
        \U00002755 Get help with '-h'
        ''')
    else:
        search_flag.search_args()
