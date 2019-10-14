from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import Snippet
from django.core.validators import RegexValidator
# the forms modules is called as the same as the models module.

class NameWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        super().__init__([
            forms.TextInput(),
            forms.TextInput()
        ],attrs)

    def decompress(self, value):
        if value:
            return  value.split(' ')
        return['','']


# the widget is called this at the main thing
class NameField( forms.MultiValueField ):
    widget = NameWidget()
    def __init__(self,*args,**kwargs):
        fields=(
            forms.CharField(validators=[
                RegexValidator(r'[a-zA-Z]+','Enter a Valid FIRST Name(only the Letters)')
            ]),# first name
            forms.CharField(validators=[
                RegexValidator(r'[a-zA-Z]+','Enter a Valid SECOND Name(only the Letters)')
            ]),# first name # last name
        )
        super().__init__(fields, *args,**kwargs)

    def compress(self, data_list):

        return (f'{data_list[0]} {data_list[1]}')
# the compress function is used to take two inputs and make it into one with a space within it


class contactForms(forms.Form):
    name = NameField()
    email = forms.EmailField(label= 'Email')
    category = forms.ChoiceField(choices=[('question','Question'),('other','other')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)


    def __init__(self,*args,**kwargs):
     super().__init__(*args,**kwargs)
     self.helper = FormHelper
     self.helper.form_method ='post'
     self.helper.layout = Layout(
         'name',
         'email',
         'category',
         'subject',
         'body',
         Submit('submit','Submit',css_class='btn-success')

     )


class SnippetForms(forms.ModelForm):
    class Meta:
        model =Snippet
        fields =('name','body')
