from django.http import response, HttpResponse
from django.views import generic

class PostView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello World")