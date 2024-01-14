from django import forms

class Form_add(forms.Form):
    CLASS_CHOICES = [
            ('Setosa ', 'Setosa'),
            ('Versicolour', 'Versicolour'),
            ('Virginica', 'Virginica'),
        ]
    sepal_length = forms.DecimalField(decimal_places=2, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'sepal length'}), label='')
    sepal_width = forms.DecimalField(decimal_places=2, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'sepal width'}), label='')
    petal_length = forms.DecimalField(decimal_places=2, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'petal length'}), label='')
    petal_width = forms.DecimalField(decimal_places=2, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'petal width'}), label='')
    iris_class = forms.ChoiceField(
        label="Class",
        choices=CLASS_CHOICES,
        widget=forms.RadioSelect()
    )
