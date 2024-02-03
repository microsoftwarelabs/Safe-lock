from django.shortcuts import render

def detail(request):
    return render(request, "./templates/index.html",)


def chat(request):
    user = 'Alice'
    messages = [
        {'sender': 'Alice', 'content': 'Bom dia', 'time': '09:54'},
        {'sender': 'Bob', 'content': 'Bom dia! Tudo certo?', 'time': '09:55'},
        {'sender': 'Alice', 'content': 'Sim, e com você?', 'time': '09:57'},
        {'sender': 'Bob', 'content': 'Sim, quero comprar 0.3 bitcoins', 'time': '10:01'},
        {'sender': 'Alice', 'content': 'Beleza', 'time': '10:17'},
    ]
    for i in range(len(messages)):
        if(messages[i]['sender'] == user):
            messages[i]['style'] = 'user'
        else:
            messages[i]['style'] = 'other'

    return render(request, "./templates/chat.html",{'messages': messages})