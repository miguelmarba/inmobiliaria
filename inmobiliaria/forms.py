from django import forms

from .models import Contacto

class ContactoModelForm(forms.ModelForm):
	class Meta:
		model = Contacto
		fields = ["nombre", "email", "comentario"]

	def clean(self, *args, **kwargs):
		form_email = self.cleaned_data.get("email")
		qs = Contacto.objects.filter(email = form_email)
		if qs.exists():
			raise forms.ValidationError("Email ya existe. Ingresa otro diferente")
		return super(ContactoModelForm, self).clean(*args, **kwargs)

class ContactoForm(forms.Form):
	nombre = forms.CharField(max_length = 100)
	email = forms.EmailField(max_length = 50)
	comentario = forms.CharField(widget = forms.Textarea)

	#def clean(self, *args, **kwargs):
	#	form_email = self.cleaned_data.get("email")
	#	qs = Contacto.objects.filter(email = form_email)
	#	if qs.exists():
	#		raise forms.ValidationError("Email ya existe. Ingresa otro diferente")
	#	return super(ContactoForm, self).clean(*args, **kwargs)