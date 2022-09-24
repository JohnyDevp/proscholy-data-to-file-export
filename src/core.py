#for making a graphql request and further result get
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport


#for converting json into pdf
import jpype
jpype.startJVM() 
import pdfkit

#regex
import re

#my module for color for string
from props import bcolors

#constants
PROSCHOLY_PATH = "https://zpevnik.proscholy.cz/graphql"

HTML_HEAD = """
    <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
        </head>
        <body> """ 

HTML_FOOT = """
    </body>
    </html>
"""

def jsonProcessing():
    ()

def slidesToPPT():
    ()

def pageToPDF():
    ()
