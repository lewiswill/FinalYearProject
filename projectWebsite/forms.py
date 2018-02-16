from django import forms
from projectWebsite.models import user_headline_model
from django.forms import Textarea
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field

class headline_form(forms.ModelForm):
    class Meta:
        model = user_headline_model
        fields = ('user_headline',)
        widgets = {
            'user_headline': Textarea(attrs={'placeholder': 'Copy & Paste a headline, then click submit to see what the Algorithm thinks!','cols': 80, 'rows': 2}),
        }
        labels = {
            'user_headline' : _(''),
        }
        error_messages = {
            'name': {
                'max_length': _("This headline is too long."),
                },
        }
#def clean(self, commit=True):
 #   headline = (HeadlineForm, self).save(commit=False)
  #  headline.user_headline = cleaned_data.get('user_headline')
   # if commit:
    #    headline.save()
    #return headline

    #if not user_headline:
     #   raise forms.ValidationError('You have to enter a headline!')