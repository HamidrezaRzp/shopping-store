from django.http import HttpResponse
from django.template import loader
from users.models import User

def main (request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())