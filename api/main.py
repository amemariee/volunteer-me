#Just a test page don't know if going to keep

import webapp2
import jinja2
import os



the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class mainPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/welcome.html')
        self.response.write(about_template.render())

class questionPage(webapp2.RequestHandler):
    def get(self):
        print "====InfoPage(get)===="
        index_template = the_jinja_env.get_template('templates/messages.html')
        self.response.write(index_template.render())
        
class resultsPage(webapp2.RequestHandler):
    def post(self):
        print "====InfoPage(get)===="
        index_template = the_jinja_env.get_template('templates/pagethree.html')
        self.response.write(index_template.render())



app = webapp2.WSGIApplication([
    ('/', mainPage),
    ("/question",questionPage),
    ("/results", resultsPage)
], debug=True)