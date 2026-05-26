from django.shortcuts import render


def home(request):
    context={
        'text':'Estamos na home2',
        }
    return render(request,
                template_name='home/index.html',
                context=context,
                )
