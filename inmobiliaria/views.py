from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail

from .forms import ContactoForm, ContactoModelForm
from .models import Contacto

def index(request):
	#return HttpResponse("Hola, estas en el INDEX de inmobiliaria")
	titulo = "Inicio inmobiliaria"

	if request.user.is_authenticated():
		titulo = "Bienvenido %s!" %(request.user)


	context = {
		"titulo": titulo
	}
	return render(request, "home.html", context)

@login_required
def contacto(request):
	form = ContactoModelForm(request.POST or None)

	#if request.method == "POST":
	#	print (request.POST)

	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()

		#form_nombre = form.cleaned_data.get("nombre")
		#form_email = form.cleaned_data.get("email")
		#form_comentario = form.cleaned_data.get("comentario")
		#obj_contacto = Contacto.objects.create(
		#	nombre = form_nombre,
		#	email = form_email,
		#	comentario = form_comentario,
		#	) 
		return HttpResponseRedirect("/inmobiliaria/contacto")
	

	#	print (form.cleaned_data)

	#if not form.is_valid():
	#	print (form.errors)


	context = {
		"form" : form
	}

	return render(request, "contacto.html", context)

def do_login(request):
	context = {
		"error": ""
	}
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			login(request, user)
			return redirect('/inmobiliaria/contacto')
	
		error = "El nombre de usuario y la contraseña son incorrectos. Por favor, inténtalo de nuevo."
		context = {
			"error": error
		}
	return render(request, 'login.html', context)


def do_logout(request):
	logout(request)
	return redirect('/inmobiliaria/login')

def reset_password(request):
	context = {
		"datos" : ""
	}
	if request.method == 'POST':
		try:
			user = User.objects.get(email=request.POST['username'])
		except User.DoesNotExist:
			return render(request, 'reset_password.html',	{
				'error_message': "Nombre de usuario no encontrado.",
			})
		
		error = "El nombre de usuario y la contraseña son incorrectos. Por favor, inténtalo de nuevo."
		context = {
			"error_message": user
		}

		try:
			pass
		except Exception as e:
			raise
		else:
			pass
		finally:
			pass

	return render(request, "reset_password.html", context)