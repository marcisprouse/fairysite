from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, HTML, Div
from crispy_forms.bootstrap import FormActions


class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_method = 'post'
        self.helper.form_action = '/contact'

        # self.helper.add_input(Submit('submit', 'Submit', css_class='btn--big--round--primary'))
        self.helper.layout = Layout(
            Fieldset(
                'Contact us for a no-obligation inquiry{% if user.first_name %}, {{ user.first_name }}!{% else %}!{% endif %}',
                HTML('<br>'),
                'name',
                HTML('<br>'),
                'email',
                HTML('<br>'),
                'message'
            ),
            HTML('<br>'),
            FormActions(
                Div(
                    Submit('submit', 'Submit', css_id='submit', css_class='btn--big--round--primary', style='background:#3C4AED;color:white;font-weight:bold;width:60px;'),
                    css_id='submit',
                    css_class='btn--big--round--primary'
                    )
            )
        )


    name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(max_length=254, widget=forms.Textarea(attrs={
                              'style': 'height: 200px;width:300px'}),)
