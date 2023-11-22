from django import forms
from . models import PostModel
from tinymce.widgets import TinyMCE

class PostModelForm(forms.ModelForm):
    #content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = PostModel
        # fields = ('profe', 'categoria','imagen','contenido')
        fields = ('content',)