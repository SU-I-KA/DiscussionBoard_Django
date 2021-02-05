from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Board, Topic, Post
from .form import *

# Create your views here.

def index(request):
    boards = Board.objects.all()
    return render(request, 'boards/index.html', {'boards':boards})

def board_topics(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    return render(request, 'boards/topics.html', {'board':board})

def new_topic(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    user = User.objects.first()
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.author=user
            topic.save()
            
            # subject = form.cleaned_data.get('subject')
            # message = form.cleaned_data.get('message')
            

            """ topic = Topic.objects.create(
                subject=subject,
                author=user,
                board=board
            ) """
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                author=user
            )
            return redirect('board_topics', board_id=board.pk)
    else:
        form = NewTopicForm()

    return render(request, 'boards/new_topic.html', {'form':form, 'board':board})
