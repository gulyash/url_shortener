import hashlib

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.views.generic.base import TemplateView

from tokenizer.models import Url
from url_shortener import settings


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        url_list = Url.objects.filter(user=request.user).order_by('-id')
        context = {
            'url_list': url_list,
        }

        return render(request, 'home.html', context)

    def post(self, request, *args, **kwargs):
        url_list = Url.objects.filter(user=request.user).order_by('-id')
        context = {
            'url_list': url_list,
        }

        token = 'kekekekek'
        try:
            url = Url.objects.get(token=token)
            context['current'] = url.pk
        except Url.DoesNotExist:
            try:
                url = Url(url=request.POST['url'], user=request.user, token=token)
                url.full_clean()
                url.save()
                context['current'] = url.pk
                return redirect('home')
            except ValidationError as e:
                context['errors'] = e.messages[0]


def shortcut(request, token):
    if not request.session.exists(request.session.session_key):
        request.session.create()

    url_item = get_object_or_404(Url, token=token)

    return redirect(url_item.url)