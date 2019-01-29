from django import forms
from django.utils.text import slugify

from blogs.models import Blog


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['name', 'description']

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        if Blog.objects.filter(name=slugify(name)).exists():
            raise forms.ValidationError('Blog {0} already exists'.format(name))
        return name
