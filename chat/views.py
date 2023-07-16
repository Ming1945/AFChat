from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.
# def error_404_view(request, exception):
#     data = {"name": "AFChat.com"}
#     return render(request,'../templates/404.html', data)

def home(request):
    return render(request, 'home.html')

def room(request, room): #stelah request harus collect variable room yg di parsing dari dynamic url
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

#to create new room in db if it's not exist, else redirect
def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if not Room.objects.filter(name=room).exists():
        new_room = Room.objects.create(name=room)
        new_room.save()
    return redirect(f'/{room}/?username={username}')


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    messages = [message.to_dict() for message in messages]
    print(messages)
    return JsonResponse({"messages":messages})