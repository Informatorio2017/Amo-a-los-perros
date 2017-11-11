from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Evento

class EventoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EventoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'evento_id'
        self.helper.form_class = 'form'
        self.helper.form_method = 'post'
        self.helper.form_action = '.'

        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        fields = [
            'tipo',
            'titulo',
            'autor',
            'descripcion',
        ] 
        model = Evento