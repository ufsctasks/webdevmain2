from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .models import user
from .models import member
from .models import visitor
from .models import post
from .models import event
from .models import donation
from .models import project

# Create your views here.

def home(request):

    return render(request, 'home.html')

def sobre(request):

    return render(request, 'sobre.html')

def eventos(request):
    eventos   = event.objects.all()
    return render(request, 'eventos.html', {'eventos': eventos})

def guia(request):

    posts = post.objects.all()

    return render(request, 'guia.html', {'posts': posts})

def prj(request):
    projetos   = project.objects.all()

    return render(request, 'prj.html', {'projetos': projetos})

def voluntariado(request):

    return render(request, 'voluntariado.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credenciais invalidas')
            return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email ja esta sendo usado')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Nome de usuario ja esta sendo usado')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                messages.info(request, 'Usuario criado com sucesso!')
                return redirect('login')
        else:
            messages.info(request, 'Senhas nao sao equivalentes')
            return redirect('register')
    else:
        return render(request, 'register.html')

def recovery(request):
    email = request.POST.get('email')
    return render(request, 'recovery.html')


def projeto_detail(request, projeto_id):
    projeto = get_object_or_404(project, id=projeto_id)

    return render(request, 'projeto_detail.html', {'projeto': projeto})


def logout(request):

    auth.logout(request)
    return redirect('/')


#   Errors views

def custom_404_view(request, exception=None):
    return HttpResponseNotFound(render(request, '404.html'))

def test_500_view(request):
    raise Exception("Testing 500 error page")
