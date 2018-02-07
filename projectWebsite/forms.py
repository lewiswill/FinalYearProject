from django import forms

class HeadlineForm(forms.Form):
    user_headline = forms.CharField(label='Enter Fake News Headline:', max_length=100)

def clean(self):
    cleaned_data = super(HeadlineForm, self).clean()
    user_headline = cleaned_data.get('user_headline')
    if not user_headline:
        raise forms.ValidationError('You have to enter a headline!')