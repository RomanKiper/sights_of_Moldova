from django import forms
from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Катеория не выбрана"


    class Meta:
        model = Attractions
        fields =  ['name', 'slug', 'description', 'photo',  'is_published', 'cat']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }






    # name = forms.CharField(max_length=255, label='Заголовок')
    # slug = forms.SlugField(max_length=255, label="URL")
    # description = forms.CharField(widget=forms.Textarea(attrs={'color': 60, 'rows': 10}), label="Описание")
    # is_published = forms.BooleanField(label="Публикация", required=False, initial=True)
    # cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категории", empty_label="Категория не выбрана")



