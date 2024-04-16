from django import forms

from catalog.models import Product, Versions


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('category', 'name', 'description', 'price_per_unit', 'preview')

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']

        for word in forbidden_words:
            if word in name:
                self.add_error('name', f'Слово "{word}" запрещено в поле "Name".')
            if word in description:
                self.add_error('description', f'Слово "{word}" запрещено в поле "Description".')

        return cleaned_data


class VersionForm(forms.ModelForm):

    class Meta:
        model = Versions
        fields = '__all__'
