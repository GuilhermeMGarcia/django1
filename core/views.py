from django.shortcuts import render


def index(request):
    # Tela inicial de Django1
    context = {
        'curso': 'Programaçao Django Framework',
        'outro': 'Django é massa',
    }

    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')
