from django.shortcuts import render, redirect
from time import gmtime, strftime
from core.models import Plataforma
from django.core.mail import send_mail
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import View
import threading


def send_async_email(mail_subject, mail_message, from_email, to_email):
    send_mail(mail_subject, mail_message, from_email, [to_email])

# Create your views here.
from django.shortcuts import render, HttpResponse
def index(request):
    # send_mail(
    #     'Asunto del correo DESDE DJANGO', 
    #     'Este es el mensaje. DESDE DJANGO!!!!', 
    #     'fboisier@codingdojo.la',  
    #     ['martin@ifx.net'],
    # )

    email_thread = threading.Thread(
        target=send_async_email,
        args=(
            'Asunto del correo ASINCRONO',
            'Este es el mensaje.',
            'fboisier@codingdojo.la',
            'martin@ifx.net'
        )
    )
    email_thread.start()

    return HttpResponse("HE MANDADO UN CORREO!!!!")

def user_id(request, user_id):
    return HttpResponse(user_id)

def nombre(request, nombre, apellido):
    return HttpResponse(f"{nombre} {apellido}")
    
def inicio(request):
    context = {
        "name": "Noelle",
        "favorite_color": "turquoise",
        "pets": ["Bruce", "Fitz", "Georgie"],
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, "inicio.html", context)


def some_function(request):
    if request.method == "GET":

        request.session['francisco'] = "ESTO ES DATO DESDE SESSION" 

        return render(request, "formulario.html")
    if request.method == "POST":
        print("procesando el formulario", request.POST)
        return redirect("/formulario")
    
def procesar_datos(request):
    if request.method == "POST":
        print("procesando el formulario", request.POST)
        return redirect("/formulario")
    

    
def plataformas(request):
    context = {
        "all_plataformas": Plataforma.objects.all()
    }
    return render(request, "plataformas.html", context)

@permission_required('core.delete_movie', login_url='/admin')
def permisos(request):
    return render(request, "permisos.html")


class ManejoPermisosMixin(PermissionRequiredMixin, View):
    permission_required = 'core.delete_movie'
    login_url = '/admin'
    permission_denied_message = "No tienes permisos para elimilar peliculas"
    
    def handle_no_permission(self):
        return redirect(self.login_url)


class Permisos(ManejoPermisosMixin):
    
    def get(self, request):
        return render(request, "permisos.html")
