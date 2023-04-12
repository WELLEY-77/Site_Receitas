from django.shortcuts import redirect, render
from django.contrib.auth.models import User

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
    return render(request, 'usuarios/login.html')

def logout(request):
    pass

def dashboard(request):
    pass
