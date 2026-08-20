from django.shortcuts import render
from django.contrib.auth.models import User

def app(request):
    return render(request, 'app.html')


def cadastro(request):

    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'cadastro.html', {
                'erro': 'As senhas não coincidem.'
            })

        if User.objects.filter(username=usuario).exists():
            return render(request, 'cadastro.html', {
                'erro': 'Nome de usuário já cadastrado.'
            })

        if User.objects.filter(email=email).exists():
            return render(request, 'cadastro.html', {
                'erro': 'E-mail já cadastrado.'
            })

        User.objects.create_user(
            username=usuario,
            email=email,
            password=password
        )

        return render(request, 'cadastro.html', {
            'sucesso': 'Usuário cadastrado com sucesso!'
        })

    return render(request, 'cadastro.html')


def painel(request):
    return render(request, 'painel.html')