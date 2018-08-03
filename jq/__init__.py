#!/usr/bin/env python3

import sys
import mysql.connector
from collections import OrderedDict
from tempfile import TemporaryFile

import click
import pandoc
import requests
from bs4 import BeautifulSoup
from jinja2 import Environment, PackageLoader


@click.command()
@click.argument('folder')



def main(folder):

   print("Test", folder)

   cnx = mysql.connector.connect(user='jiraro', password='8816de6ce230447005b42267',
                                 host='140.252.32.64',
                                 database='jira') #mebsuta
   cursor = cnx.cursor()

   query = ("show tables")

   cursor.execute(query)

   for line in cursor:
      print(line)

   cursor.close()
   cnx.close()

if __name__ == '__main__':
    main()
