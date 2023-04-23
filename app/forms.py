from django import forms
class studentform(forms.Form):
    g=[('male','MALE'),('female','FEMALE')]
    c=[('java','JAVA'),('PYTHON','python'),('sql',"SQL")]
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    url=forms.URLField()
    date=forms.DateField()
    email=forms.EmailField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    address=forms.CharField(max_length=300,widget=forms.Textarea(attrs={'cols':5,'rows':7}))
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #course=forms.MultipleChoiceField(choices=c)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)