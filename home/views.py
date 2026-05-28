from django.shortcuts import render


def home(request):
    context={
        'text':'Olá Home',
        }
    return render(request,
                template_name='home/index.html',
                context=context,
                )
