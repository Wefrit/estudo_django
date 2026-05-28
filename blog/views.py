from django.shortcuts import render


def blog (request):
    context = {
        'text': 'Olá Blog',
        'title': 'Pagina do blog ',
    }
    return render(request,
                'blog/index.html',
                context,
    )

def exemplo(request):
    context={
            'text':'Olá exemplo',
            'title': 'Pagina do exemplo '
            }
    return render(request,
                'blog/exemplo.html',
                context,
    )
