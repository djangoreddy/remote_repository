from django.db import models
from multiselectfield import MultiSelectField


class ENQdata(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=100)
    Course_Choices = (
        ('PYTHON', 'Python'),
        ('DJANGO', 'Django'),
        ('UI', 'Ui'),
        ('REST API', 'Rest api')
    )
    course = MultiSelectField(choices=Course_Choices, max_length=200)
    Teacher_Choices = (
        ('NAGUR', 'Nagur'),
        ('DURGA', 'Durga'),
        ('SAI', 'Sai'),
        ('HARI', 'Hari')
    )
    teacher = MultiSelectField(choices=Teacher_Choices, max_length=200)
    Braches_Choices = (
        ('HYD', 'Hyd'),
        ('Bang', 'Bang'),
        ('VSKP', 'Vskp')
    )
    braches = MultiSelectField(choices=Braches_Choices, max_length=200)
    gender = models.CharField(max_length=200)
    start_date = models.DateField(max_length=100)
