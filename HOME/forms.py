from django import forms

class FormularioNuevoProducto(forms.Form):
    Titulo= forms.CharField()
    Categoria=forms.Select()
    Imagen = forms.FileInput()
    Descripcion=forms.Textarea()
    Precio = forms.FloatField()