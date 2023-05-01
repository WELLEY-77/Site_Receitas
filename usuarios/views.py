from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita

def cadastro(request):

    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if campo_vazio(nome):
            messages.warning(request, 'O campo não pode ficar em branco! ')
            return redirect('cadastro')
        
        if campo_vazio(email):
            messages.warning(request, 'O campo não pode ficar em branco! ')
            return redirect('cadastro')
        
        if senhas_sao_diferentes(senha, senha2):
            messages.error(request, 'As senhas não são iguais')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Usuario já cadastrado')
            return redirect('cadastro')
        
        if User.objects.filter(username=nome).exists():
            messages.warning(request, 'Usuario já cadastrado')
            return redirect('cadastro')
        
        user = User.objects.create_user(username=nome, email=email, password=senha2)
        user.save()
        
        messages.success(request, 'Usuario cadastrado com sucesso')

        return redirect('login')
    else:
        return render(request ,'usuarios/cadastro.html')

def login(request):

    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        if email == '' or senha == '':
            messages.warning(request, 'Os campos não podem ficar em branco')
            return redirect('login')
        

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
        
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login efetuado com sucesso')
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

def campo_vazio(campo):
    return not campo.strip()

def senhas_sao_diferentes(senha, senha2):
    return senha != senha2

