from django import forms
from . import models, kivano_kg, faberlic_com

class ParserProductForm(forms.Form):
    MEDIA_CHOISCES = (
        ('kivano.kg', 'kivano.kg'),
        ('faberlic.com', 'faberlic.com'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOISCES)

    class Meta:
        filds = [
            'media_type',
        ]
    def parser_data(self):
        if self.data['media_type'] == 'kivano.kg':
            kivano_parser = kivano_kg.parser()
            for i in kivano_parser:
                models.KivanoProducts.objects.create(**i)
        elif self.data['media_type'] == 'faberlic.com':
            faberlic_parser = faberlic_com.parser()
            for i in faberlic_parser:
                models.FaberlicProducts.objects.create(**i)
