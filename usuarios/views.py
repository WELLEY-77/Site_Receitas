from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth

def cadastro(request):

    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if not nome.strip():
            print('Campo nome nao pode ficar em branco')
            return redirect('cadastro')
        
        if not email.strip():
            print('Campo nome nao pode ficar em branco')
            return redirect('cadastro')
        
        if senha != senha2:
            print('Senha incorreta')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            print('Usuario ja cadastrado')
            return redirect('cadastro')
        
        user = User.objects.create_user(username=nome, email=email, password=senha2)
        user.save()
        
        print('Usuario cadastrado com sucesso')

        return redirect('login')
    else:
        return render(request ,'usuarios/cadastro.html')

def login(request):

    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        if email == '' or senha == '':
            print('Os campos nao podem ficar em branco')
            return redirect('login')
        
        print(email, senha)

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            print(nome)
            if user is not None:
                auth.login(request, user)
                print('Login efetuado com sucesso')
                return redirect('dashboard')

    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('receita')

def dashboard(request):

    if request.user.is_authenticated:
        return render(request, 'usuarios/dashboard.html')
    else:
        return redirect('receita')

def cria_receita(request):
    return render(request, 'usuarios/cria_receita.html')


