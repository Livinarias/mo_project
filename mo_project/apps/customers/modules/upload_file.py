from django import forms

class UploadFileForm(forms.Form):
    """class form to upload file"""

    archivo = forms.FileField(label='Selecciona un archivo CSV')
