from django import forms

class Form_add(forms.Form):
    CLASS_CHOICES = [
            (1, 'Setosa'),
            (2, 'Versicolour'),
            (3, 'Virginica'),
        ]
    sepal_length = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'sepal length'}), label='')
    sepal_width = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'sepal width'}), label='')
    petal_length = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'petal length'}), label='')
    petal_width = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'petal width'}), label='')
    iris_class = forms.ChoiceField(
        label="Class",
        choices=CLASS_CHOICES,
        widget=forms.RadioSelect()
    )

class Form_predict(forms.Form):
    sepal_length = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'sepal length'}), label='')
    sepal_width = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'sepal width'}), label='')
    petal_length = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'petal length'}), label='')
    petal_width = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'petal width'}), label='')
