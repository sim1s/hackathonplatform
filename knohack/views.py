from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Event
from .forms import EventForm
from django.contrib.auth.decorators import login_required

def event_list(request):
    events = Event.objects.order_by('start_time')
    return render(request, 'knohack/event_list.html', {'events': events})

def event_detail(request, pk):
	event = get_object_or_404(Event, pk=pk)
	return render(request, 'knohack/event_detail.html', {'event':event})

def create_new_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.host = request.user
            event.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm()
    return render(request, 'knohack/event_edit.html', {'form': form})

def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.host = request.user
            event.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'knohack/event_edit.html', {'form': form})

def event_draft_list(request):
    events = Event.objects.filter(created_date__isnull=True).order_by('start_time')
    return render(request, 'knohack/event_draft_list.html', {'events': events})

def event_create(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.create()
    return redirect('event_detail', pk=pk)

def event_remove(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return redirect('event_list')
