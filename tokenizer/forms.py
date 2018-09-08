from django.forms import ModelForm

from tokenizer.models import Url


class UrlForm(ModelForm):

    class Meta:
        model = Url
        fields = ('url', )
