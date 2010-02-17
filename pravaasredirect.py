#!/usr/bin/env python
#
# Copyright 2010 Hareesh Nagarajan.

"""Powers http://pravaas.org -> http://pravaas.ning.com

I need to stop paying ning.com $4.95/month for their redirection
service!
"""

__author__ = 'hareesh.nagarajan@gmail.com (Hareesh Nagarajan)'

import wsgiref.handlers
from google.appengine.ext import webapp

class RedirectHandler(webapp.RequestHandler):
  def get(self):
    self.redirect('http://pravaas.ning.com', permanent=True)

def main():
  application = webapp.WSGIApplication([
      ('/', RedirectHandler),
      ], debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()
