
from __future__ import absolute_import, unicode_literals
def index(_resp):
    _resp.write("Pagina do Usuario")
def ola(_resp, nombre):
    _resp.write("Ola %s"% nombre)