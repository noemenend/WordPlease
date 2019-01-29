from bootstrap_datepicker_plus import DatePickerInput
from django import forms

from blogs.models import Blog
from posts.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields =['blog', 'title', 'resume', 'body', 'image', 'categories', 'pub_date', 'status']
        widgets = {
            'pub_date': DatePickerInput(
                options={
                    "format": "MM/DD/YYYY",  # moment date-time format
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                }
            ),

        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['blog'].queryset = Blog.objects.filter(author=user)