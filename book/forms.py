from django import forms

from .models import Book, Impression


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ("title", )


class ImageForm(forms.Form):

    image = forms.ImageField()