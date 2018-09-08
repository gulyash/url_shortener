
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.utils.crypto import get_random_string
from django.views.generic import FormView
from django.views.generic.base import TemplateView

from tokenizer.forms import UrlForm
from tokenizer.models import Url


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = {}
        if request.user.is_authenticated:
            url_list = Url.objects.filter(user=request.user).order_by('-id')
            context['url_list'] = url_list
        return render(request, 'home.html', context)


class UrlGen(LoginRequiredMixin, FormView):
    SHORT_URL_LEN = 8

    def post(self, request, *args, **kwargs):
        form = UrlForm(request.POST)
        if form.is_valid():
            token = self.get_unique_token()
            url, created = Url.objects.get_or_create(user=request.user, **form.cleaned_data)
            if created:
                url.token = token
                url.full_clean()
                url.save()
            return redirect('home')

    def get_unique_token(self):
        tokens = set(Url.objects.all().values_list('token', flat=True))
        while True:
            token = get_random_string(length=self.SHORT_URL_LEN)
            if token not in tokens:
                return token


def shortcut(request, token):
    url_item = get_object_or_404(Url, token=token)
    url_item.redirect_count += 1
    url_item.save()
    return redirect(url_item.url)
