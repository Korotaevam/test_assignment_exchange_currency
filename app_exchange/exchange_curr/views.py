import requests
from django.shortcuts import render


def start(request):
    response = requests.get(url='https://api.exchangerate-api.com/v4/latest/USD').json()
    currencies = response.get('rates')
    name = 'Currency exchange'

    if request.method == 'GET':
        print('get', request.GET)
        context = {
            'name': name,
            'currencies': currencies,
        }
        return render(request=request, template_name='exchange_curr/index.html', context=context)

    if request.method == 'POST':
        print('post', request.POST)
        from_amount = float(request.POST.get('from-amount')) if request.POST.get('from-amount') else 1.0
        from_curr = request.POST.get('from-curr')
        to_curr = request.POST.get('to-curr')

        converted_amount = round((currencies[to_curr] / currencies[from_curr]) * from_amount, 2)

        context = {
            'name': name,
            'currencies': currencies,
            'from_curr': from_curr,
            'to_curr': to_curr,
            'from_amount': from_amount,
            'converted_amount': converted_amount
        }

        return render(request=request, template_name='exchange_curr/index.html', context=context)
