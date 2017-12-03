#wiki text scrap
from bs4 import BeautifulSoup
#html request
import requests
from cherrypy.lib import static
import cherrypy
import os
from jinja2 import Environment, FileSystemLoader
from requests.auth import HTTPDigestAuth
import ast

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
        #tmpl = env.get_template('testing.html')
        #return tmpl.render()
        raise cherrypy.HTTPRedirect("https://simulator-api.db.com/gw/oidc/authorize?response_type=token&redirect_uri=localhost:5000&client_id=49dff74c-4c3d-43dc-bbe5-cf2d8c9bf4e9")
        #return "https://simulator-api.db.com/gw/oidc/authorize?response_type=token&redirect_uri=localhost:5000&client_id=49dff74c-4c3d-43dc-bbe5-cf2d8c9bf4e9"



    @cherrypy.expose
    def some(self, code): 
        r = requests.post("https://simulator-api.db.com/gw/oidc/token", data={"grant_type":"authorization_code",
                                                                          "code":code,
                                                                          "redirect_uri":"http://localhost:5000/some"},
                                                                           auth=('9afba87e-d902-450d-8942-79d7a5e0b0a3','ANQLk7veOPIrOUlec4uBUA8--6d6R9V-DM4zD95NnikzjJPs3prjJZXIldpW-KwZ-w-x8I1ghQVWJj3jgx884QQ'))

        access_token = ast.literal_eval(r.content.decode())["access_token"]
        def parse_code(parsed):
#        ind = parse_token.index("access_token")
#        parsed = parse_token.split("&")[0][ind+13:]
            response =  requests.get("https://simulator-api.db.com/gw/dbapi/v1/ageCertificate?certificationMethod=LEGAL_AGE", headers = {"Authorization":"Bearer "+parsed})
            if(response.ok):
                bracket =  str(response.content).index("}")
            if(str(response.content)[15:bracket] == 'true'):
                return True
            elif(str(response.content)[15:bracket] == 'false'):
                return False
            else:
                print("connection broken")
                
        legal = (parse_code(access_token))
        if(legal):
            # The user is legal he can gamble
            tmpl = env.get_template('some.html')
            return tmpl.render()
        else:
            # Please reach your leagal age


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

