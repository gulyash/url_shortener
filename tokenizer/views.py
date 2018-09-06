from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateResponseMixin, ContextMixin, View


class HomePageView(TemplateResponseMixin, ContextMixin, View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
