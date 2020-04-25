from django import forms
from gestion.models import Batalla, demonio, Lugar, Objetos_Dororo

class FKdemon (forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{}".format(obj.nombre)

class FKplace (forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{}".format(obj.nombre)

class insertBattle (forms.ModelForm):
    Demonio = FKdemon(queryset=demonio.objects.order_by('id'))
    lugar = FKplace(queryset=Lugar.objects.order_by('id'))
    class Meta:
        model = Batalla
        fields = ['ganador','Demonio','lugar']
        labels = {'ganador':'Ganador'}
        widget = {'ganador':forms.TextInput()}

    def __init__(self,*args,**kwargs):
       super().__init__ (*args,**kwargs)
       for field in iter(self.fields):
           self.fields[field].widget.attrs.update({
               'class':'from-control'
           }) 
           self.fields['Demonio'].label = 'Demonio al cual se enfrentara'
           self.fields['lugar'].label = 'Lugar de ubicacion del demonio'

class addObject (forms.ModelForm):
    class Meta:
        model = Objetos_Dororo
        fields = ['nombre','procedencia']
        labels = {'nombre':'Nombre','procedencia':'Procedencia'}
        widget = {'nombre':forms.TextInput(),'procedencia':forms.TextInput()}
    
    def __init__(self,*args,**kwargs):
       super().__init__ (*args,**kwargs)
       for field in iter(self.fields):
           self.fields[field].widget.attrs.update({
               'class':'from-control'
           }) 