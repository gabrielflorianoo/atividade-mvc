from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Animal

# Create your views here.
def index(req: HttpRequest):
    name = req.GET.get('name', 'Visitante')  # Pegando o parâmetro 'name' da URL, com valor padrão
    message = f"Bem-vindo, {name}! Ambiente configurado."
    return HttpResponse(message)

def animals(req: HttpRequest):
    # Se o usuário enviou o formulário
    if req.method == "POST":
        try:
            name = req.POST.get('animal_name')  # Obtendo o nome do animal
            species = req.POST.get('species')  # Obtendo a espécie do animal
            emoji = req.POST.get('emoji')      # Obtendo o emoji do animal

            # Criando uma nova instância de Animal e salvando no banco
            animal = Animal(name=name, species=species, emoji=emoji)
            animal.save()

            context = {
                'name': name,
                'species': species,
                'emoji': emoji,
            }

            return render(req, 'animal.html', context)
        except:
            return HttpResponse('Algo deu errado no envio do formulário 😥')

    return render(req, 'index.html')

def list_animals(req: HttpRequest):
    animals = Animal.objects.all()

    return render(req, 'animals_list.html', { 'animals': animals })