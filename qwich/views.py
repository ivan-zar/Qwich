from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import math

from .models import Announcement


def index(request, card_batch=1):

    card_batch = int(card_batch)
    card_set = Announcement.objects.all()[5*(card_batch-1):(5*card_batch)]
    batches_number = range(1, min(math.ceil(Announcement.objects.all().count()/5) + 1, 7))

    context = {'card_set': card_set,
               'batches_number': batches_number,
               'card_batch': card_batch}

    return render(request, 'index.html', context)


def new_game(request):

    gtype_list = Announcement.objects.values_list('game_type', flat=True).distinct()
    context = {'gtype_list': gtype_list}
    return render(request, 'new_game.html', context)


def new_game_added(request):

    new_game_item = Announcement()
    new_game_item.game = request.POST['game']
    new_game_item.game_type = request.POST['game_type']
    new_game_item.place_name = request.POST['place_name']
    new_game_item.place_location = request.POST['place_location']
    new_game_item.metro = request.POST['metro']
    new_game_item.date_time = datetime.strptime(request.POST['date_time'], '%d.%m.%Y')
    new_game_item.reader = request.POST['reader']
    new_game_item.organizer = request.POST['organizer']
    new_game_item.save()

    card_set = Announcement.objects.all()[:5]
    context = {'card_set': card_set}

    return render(request, 'index.html', context)
