from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from receitas.models import Receita

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
        id = request.user.id

        receitas = Receita.objects.order_by('-date_receita').filter(pessoa=id)

        return render(request, 'usuarios/dashboard.html', {'receitas' : receitas})
    else:
        return redirect('receita')

def cria_receita(request):

    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id)

        receita = Receita.objects.create(pessoa=user, nome_receita=nome_receita, ingredientes=ingredientes, modo_preparo=modo_preparo, tempo_preparo=tempo_preparo, rendimento=rendimento, categoria=categoria,foto_receita=foto_receita)
        receita.save()

        return redirect('dashboard')
    else:
        return render(request, 'usuarios/cria_receita.html')


