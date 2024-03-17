from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class index_view(TemplateView):
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        ctx = {}
        return self.render_to_response(ctx)