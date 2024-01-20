from django import forms

def is_positive_validator(value):
    if value <= 0:
        raise forms.ValidationError("This field must be greater than 0")

class Form_add(forms.Form):
    CLASS_CHOICES = [
            (1, 'Setosa'),
            (2, 'Versicolour'),
            (3, 'Virginica'),
        ]
    sepal_length = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'sepal length'}), label='', validators=[is_positive_validator])
    sepal_width = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'sepal width'}), label='', validators=[is_positive_validator])
    petal_length = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'petal length'}), label='', validators=[is_positive_validator])
    petal_width = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'petal width'}), label='', validators=[is_positive_validator])
    iris_class = forms.ChoiceField(
        label="Class",
        choices=CLASS_CHOICES,
        widget=forms.RadioSelect()
    )

class Form_predict(forms.Form):
    sepal_length = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'sepal length'}), label='', validators=[is_positive_validator])
    sepal_width = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'sepal width'}), label='', validators=[is_positive_validator])
    petal_length = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'petal length'}), label='', validators=[is_positive_validator])
    petal_width = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'petal width'}), label='', validators=[is_positive_validator])
