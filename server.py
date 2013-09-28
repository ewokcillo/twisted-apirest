from twisted.web import server, resource
from twisted.internet import reactor

from mongoengine import connect
from models import Items

connect('scrapy')

class Simple(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        request.setHeader("content-type", "application/json")
        return Items.objects.to_json()

site = server.Site(Simple())
reactor.listenTCP(8080, site)
reactor.run()
