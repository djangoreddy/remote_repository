from django import forms
from multiselectfield import MultiSelectFormField


class Forms(forms.Form):
    name = forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'your name',
                'class': 'form-control'
            }
        )

    )

    email = forms.EmailField(
        label="Enter your Email",
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'your Email',
                'class': 'form-control'
            }
        )

    )
    mobile = forms.IntegerField(
        label="Enter your mobile",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'your mobile',
                'class': 'form-control'
            }
        )

    )
    Course_Choices = (
        ('PYTHON', 'Python'),
        ('DJANGO', 'Django'),
        ('UI', 'Ui'),
        ('REST API', 'Rest api')
    )
    course = MultiSelectFormField(choices=Course_Choices, label="select course")
    Teacher_Choices = (
        ('NAGUR', 'Nagur'),
        ('DURGA', 'Durga'),
        ('SAI', 'Sai'),
        ('HARI', 'Hari')
    )
    teacher = MultiSelectFormField(choices=Teacher_Choices,label="select teacher")
    Braches_Choices = (
        ('HYD', 'Hyd'),
        ('Bang', 'Bang'),
        ('VSKP', 'Vskp')
    )
    braches = MultiSelectFormField(choices=Braches_Choices, label="select braches")

    Gender_Choices = (
        ('MALE', 'male'),
        ('FEMALE', 'female')
    )
    gender = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=Gender_Choices,label="select gender"
    )

    start_date = forms.DateField(
        widget=forms.SelectDateWidget()
    )
