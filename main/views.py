# views.py

from django.shortcuts import render
from django.http import HttpResponse
from .models import Message

def chat_view(request):
    """Представление для отображения чата (получение сообщений)."""
    return render(request, "chat.html")

def get_messages(request):
    """Представление для получения списка сообщений."""
    messages = Message.objects.order_by("timestamp")[:50]  # Получаем последние 50 сообщений
    return render(request, "partials/messages.html", {"messages": messages})


def send_message(request):
    """Представление для обработки отправки сообщений."""
    if request.method == "POST":
        username = request.POST.get("username", "Аноним")
        content = request.POST.get("content", "")

        # Сохраняем сообщение
        Message.objects.create(username=username, content=content)

        # Возвращаем обновленный список сообщений
        messages = Message.objects.order_by("timestamp")[:50]
        return render(request, "partials/messages.html", {"messages": messages})

    return HttpResponse(status=400)

