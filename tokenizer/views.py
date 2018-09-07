from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.utils.crypto import get_random_string
from django.views.generic.base import TemplateView

from tokenizer.models import Url


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        url_list = Url.objects.filter(user=request.user).order_by('-id')
        context = {
            'url_list': url_list,
        }
        return render(request, 'home.html', context)


class UrlGen(LoginRequiredMixin, TemplateView):
    def post(self, request, *args, **kwargs):
        token = self.get_unique_token()
        try:
            url = Url(url=request.POST['url'], user=request.user, token=token)
            url.full_clean()
            url.save()
            return redirect('home')
        except ValidationError as e:
            pass

    def get_unique_token(self):
        while True:
            token = get_random_string(length=16)
            if not Url.objects.filter(token=token).exists():
                break
        return token


def shortcut(request, token):
    if not request.session.exists(request.session.session_key):
        request.session.create()

    url_item = get_object_or_404(Url, token=token)

    return redirect(url_item.url)
