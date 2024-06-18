# Para atualizar um projeto existente no perfil do usuário, você pode seguir estes passos:

# Obter o Projeto: Primeiro, você precisa obter o projeto que deseja atualizar. Isso geralmente é feito através de um identificador único (como o ID do projeto) passado na URL.

# Verificar Propriedade: É importante verificar se o projeto realmente pertence ao usuário que está tentando atualizá-lo. Isso evita que usuários alterem projetos de outros usuários.

# Usar o Formulário para Atualizar: Use um formulário (como ProjectForm) para coletar as atualizações do usuário. Este formulário pode ser pré-preenchido com os dados existentes do projeto.

# Salvar as Atualizações: Após o usuário enviar o formulário com as atualizações, valide o formulário e salve as alterações no banco de dados.

# Aqui está um exemplo de como isso pode ser implementado em Django:


# from django.shortcuts import get_object_or_404, redirect, render
# from .forms import ProjectForm
# from .models import Project

# @login_required(login_url="login")
# def update_project(request, project_id):
#     # Obter o projeto ou retornar um erro 404 se não encontrado
#     project = get_object_or_404(Project, id=project_id, profile=request.user.profile)

#     # Verificar se o método é POST
#     if request.method == "POST":
#         # Instanciar o formulário com os dados enviados e a instância do projeto
#         form = ProjectForm(request.POST, instance=project)
#         if form.is_valid():
#             # Salvar o projeto atualizado
#             form.save()
#             # Redirecionar para o detalhe do perfil ou para a página do projeto
#             return redirect("profile-detail", pk=request.user.profile.id)
#     else:
#         # Se não for POST, exibir o formulário com os dados existentes do projeto
#         form = ProjectForm(instance=project)

#     # Renderizar a página de atualização com o formulário
#     return render(request, "update_project.html", {"project_form": form})


# Para excluir um projeto do perfil do usuário, você pode seguir estes passos:

# Obter o Projeto: Primeiro, obtenha o projeto que deseja excluir. Isso geralmente é feito através de um identificador único (como o ID do projeto) passado na URL.

# Verificar Propriedade: Certifique-se de que o projeto realmente pertence ao usuário que está tentando excluí-lo. Isso evita que usuários excluam projetos de outros usuários.

# Excluir o Projeto: Se o projeto pertencer ao usuário, proceda com a exclusão.

# Redirecionar: Após a exclusão, redirecione o usuário para uma página apropriada, como a lista de projetos ou a página de perfil do usuário.

# Aqui está um exemplo de como isso pode ser implementado em Django, assumindo que você já tem um modelo Project e uma função de autenticação:


# from django.shortcuts import get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
# from .models import Project

# @login_required(login_url="login")
# def delete_project(request, project_id):
#     # Obter o projeto ou retornar um erro 404 se não encontrado
#     project = get_object_or_404(Project, id=project_id, profile=request.user.profile)

#     # Verificar se o método é POST (para evitar exclusão via GET)
#     if request.method == "POST":
#         # Excluir o projeto
#         project.delete()
#         # Redirecionar para a página de perfil ou lista de projetos
#         return redirect("profile-detail", pk=request.user.profile.id)

#     # Se não for POST, talvez renderizar uma página de confirmação de exclusão
#     return render(request, "confirm_delete_project.html", {"project": project})


# Neste exemplo, delete_project é uma função que exclui um projeto existente. Ela obtém o projeto usando get_object_or_404, o que garante que o projeto existe e pertence ao perfil do usuário autenticado. A exclusão é realizada apenas se o método da requisição for POST, o que é uma prática recomendada para evitar exclusões acidentais ou maliciosas via GET. Após a exclusão, o usuário é redirecionado para uma página apropriada.


# def create_institution(request):
#     institution_form = CertifyingInstitutionForm(request.POST or None)
#     if request.method == "POST" and institution_form.is_valid():
#         institution_form.save()
#         return redirect("profile-detail")
#     return render(
#         request,
#         "create_institution.html",
#         {"institution_form": institution_form},
#     )


# <!-- {% extends 'base.html' %}

# {% block title %}Create Institution{% endblock %}

# {% block content %}
#     <header class="profile-infos-container"><h1>Crie sua instituição!</h1></header>
#         <div class="section-login-container">
#             <form method="post" action="{% url 'create_institution' %}" class="form-register-container">
#                 {% csrf_token %}
#                 {% for field in institution_form %}
#                     <div class="form-field-container">
#                         <label class="field-label">{{ field.label }}</label>
#                         {{ field }}
#                         {% if field.errors %}
#                             <div class="field-errors">
#                                 {% for error in field.errors %}
#                                     <p>{{ error }}</p>
#                                 {% endfor %}
#                             </div>
#                         {% endif %}
#                     </div>
#                 {% endfor %}
#                 <button class="button-register" type="submit">Crie Instituição</button>
#             </form>
#         </div>
# {% endblock %} -->
