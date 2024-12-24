from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room, Message
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)

    messages = Message.objects.filter(room = room)#[0:25]

    User = get_user_model()
    users = User.objects.all()

    return render(request, 'room/room.html', {'room': room, 'messages': messages, 'users': users})

#@login_required
#def deleteMessage(request, pk):
#    message = Message.object.get(id = pk)
#    message.delete()
#    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def deleteMessage(request, message_id):
    message = Message.objects.get(pk=message_id)
    message.delete()
    #return redirect('room/' + room)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
