from django.shortcuts import render, redirect
from .models import Room, Message

# Create your views here.
def CreateRoom(request):
    if(request.method == "POST"):
        username = request.POST['username']
        room = request.POST["room"]

        #if room doesn't exist, create it
        try:
            get_room = Room.objects.get(room_name = room)
        except Room.DoesNotExist:
            new_room = Room()
            new_room.room_name = room
            new_room.save()
        
        #now redirect to the chatroom
        return redirect('room', room_name = room, username = username)

    return render(request, 'index.html')

def MessageView(request, room_name, username):
    #fetch messages for the given room
    get_room = Room.objects.get(room_name = room_name)
    get_messages = Message.objects.filter(room = get_room)

    return render(request, 'message.html', {
        'messages' : get_messages,
        'user' : username,
        'room_name' : room_name
    })