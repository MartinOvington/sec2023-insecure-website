from django.shortcuts import render, redirect
from django.db import transaction
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Account, Message


@login_required
def index(request):
    accounts = Account.objects.exclude(owner=request.user)
    return render(request, 'bank/index.html', {'accounts': accounts})


def balance(request):
    username = request.GET.get('user', '')
    user = User.objects.filter(username=username).first()
    if not user:
        return HttpResponseNotFound('<h1>User not found</h1>')
    account = Account.objects.filter(owner=user).first()
    if account:
        return render(request, 'bank/balance.html', {'account': account})
    return HttpResponseNotFound('<h1>Account not found</h1>')


@csrf_exempt
def send_money(request):
    receiver = request.GET.get('receiver', '')
    if request.method == 'POST':
        sender = request.user
        amount = int(request.POST.get('amount'))
        receiver_obj = User.objects.filter(username=receiver).first()
        transfer(sender, receiver_obj, amount)
        return redirect('/')
    return render(request, 'bank/send_money.html', {'receiver': receiver})


def messages(request):
    found_messages = [
        msg.message for msg in Message.objects.filter(user=request.user)]
    response = '<ul>'
    for msg in found_messages:
        response += f'<li>{msg}</li>'
    response += '</ul>'
    return HttpResponse(response)


"""
def messages(request):
    found_messages = [
        msg.message for msg in Message.objects.filter(user=request.user)]
    return render(request, 'bank/messages.html', {'messages': found_messages})
"""


def send_message(request):
    receiver = request.GET.get('receiver', '')
    if request.method == 'POST':
        receiver_obj = User.objects.filter(username=receiver).first()
        message = request.POST.get('message', '')
        Message.objects.create(user=receiver_obj, message=message)
        return redirect('/')
    return render(request, 'bank/send_message.html', {'receiver': receiver})


# @transaction.atomic#
def transfer(sender, receiver, amount):
    acc1 = Account.objects.get(owner=sender)
    acc2 = Account.objects.get(owner=receiver)
    # if amount < 0 or amount > acc1.balance or acc1 == acc2:
    #    return

    acc1.balance -= amount
    acc2.balance += amount

    acc1.save()
    acc2.save()
