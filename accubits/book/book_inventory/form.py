from django import forms


class BookForm(forms.Form):
    name = forms.CharField(max_length=127)
    author = forms.CharField(max_length=127)
    count = forms.IntegerField(max_value=127)


class BookBorrowForm(forms.Form):
    book_id = forms.CharField(max_length=127)
    user_id = forms.CharField()
    date = forms.EmailField()


