from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm


def cadastrar_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # 1. Salva o usuário no banco de dados (criptografando a senha)
            usuario = form.save()

            # 2. Pega o grupo selecionado no formulário
            grupo_selecionado = form.cleaned_data['cargo']

            # 3. Vincula o usuário a esse grupo nativo do Django
            usuario.groups.add(grupo_selecionado)

            messages.success(
                request, f"Usuário {usuario.username} cadastrado com sucesso como {grupo_selecionado.name}!")
            # Por enquanto redireciona para a própria tela
            return redirect('cadastro_usuario')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/cadastro_usuario.html', {'form': form})
