#!/usr/bin/env python
#
# Copyright 2010 Hareesh Nagarajan.

"""Powers http://pravaas.org -> http://pravaas.ning.com

I need to stop paying ning.com $4.95/month for their redirection
service!
"""

__author__ = 'hareesh.nagarajan@gmail.com (Hareesh Nagarajan)'

import os
import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class RedirectHandler(webapp.RequestHandler):
  def get(self):
    self.redirect('http://pravaas.ning.com', permanent=True)

class ArchivesHandler(webapp.RequestHandler):
  def get(self):
    template_values = {
        'load_function' : 'initArchives()',
        'load_forum'    : 'archives_forum_embed',
        }
    path = os.path.join(os.path.dirname(__file__), 'archives.html')
    self.response.out.write(template.render(path, template_values))

class ForumHandler(webapp.RequestHandler):
  def get(self):
    template_values = {
        'load_function' : 'initForum()',
        'load_forum'    : 'forum_forum_embed',
        }
    path = os.path.join(os.path.dirname(__file__), 'forum.html')
    self.response.out.write(template.render(path, template_values))

class AboutHandler(webapp.RequestHandler):
  def get(self):
    template_values = {
        'load_function' : 'nothing()',
        }
    path = os.path.join(os.path.dirname(__file__), 'about.html')
    self.response.out.write(template.render(path, template_values))
    
def main():
  application = webapp.WSGIApplication([
      ('/redirect', RedirectHandler),
      ('/', ForumHandler),
      ('/about', AboutHandler),
      ('/archives', ArchivesHandler),
      ], debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()
