import os
from datetime import date
import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def prep_template_values():
    current_year = date.today().year
        
    template_values = {
        'current_year': current_year,
    }
    return template_values    

class IndexHandler(webapp2.RequestHandler):
    def get(self):
        template_values = prep_template_values()
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', IndexHandler)
], debug=True)