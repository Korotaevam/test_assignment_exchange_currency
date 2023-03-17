from django.shortcuts import render


def start(request):
    name = 'Currency exchange'

    context = {
        'name': name
    }

    return render(request=request, template_name='exchange_curr/index.html', context=context)
