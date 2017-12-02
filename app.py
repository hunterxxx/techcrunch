#wiki text scrap
from bs4 import BeautifulSoup
#html request
import requests
from cherrypy.lib import static
import cherrypy
import os
from jinja2 import Environment, FileSystemLoader

localDir = os.path.dirname(__file__)
absDir = os.path.join(os.getcwd(), localDir)

env = Environment(loader=FileSystemLoader('html'))

class Landing_Page(object):
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('index.html')
        return tmpl.render(name="Bitcoin")

    @cherrypy.expose
    def newTransaction(self):
        tmpl = env.get_template('testing.html')
        return tmpl.render()

    def parse_code(parse_token):
        ind = parse_token.index("access_token")
        parsed = parse_token.split("&")[0][ind+13:]
        response =  requests.get("https://simulator-api.db.com/gw/dbapi/v1/ageCertificate?certificationMethod=LEGAL_AGE", headers = {"Authorization":"Bearer "+parsed})
        if(response.ok):
            bracket =  str(response.content).index("}")
        if(str(response.content)[15:bracket] == 'true'):
            return True
        elif(str(response.content)[15:bracket] == 'false'):
            return False
        else:
            print("connection broken")
            
config = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': int(os.environ.get('PORT', 5000)),
    },
    '/assets': {
        'tools.staticdir.root': os.path.dirname(os.path.abspath(__file__)),
        'tools.staticdir.on': True,
        'tools.staticdir.dir': 'assets',
    }
}

cherrypy.quickstart(Landing_Page(), '/', config=config)
