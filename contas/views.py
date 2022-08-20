from django.shortcuts import redirect, render
from django.http import HttpResponse
import datetime
from .models import Transacao
from .forms import TransacaoForm


def teste(request):
    data = {}
    data['now'] = datetime.datetime.now()
    data['transacoes'] = ['t1','t2','t3']

    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)

    return render(request, 'contas/teste.html', data)


def read(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/read.html', data)


def create(request):
    form = TransacaoForm(request.POST or None)
    data = {}
    data['form'] = form

    if form.is_valid():
        form.save()
        return redirect('read')

    return render(request, 'contas/create.html', data)


def update(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)
    data = {}
    data['form'] = form
    data['transacao'] = transacao

    if form.is_valid():
        form.save()
        return redirect('read')
    
    return render(request, 'contas/update.html', data)


def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('read')