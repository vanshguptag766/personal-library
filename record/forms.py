from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    publication_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'publication_date', 'pages', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Book Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author Name'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ISBN'}),
            'publication_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Pages'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Book Description', 'rows': 4}),
        }

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        # Check if ISBN already exists, excluding the current instance
        if isbn:
            qs = Book.objects.filter(isbn=isbn)
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise forms.ValidationError('A book with this ISBN already exists.')
        return isbn
