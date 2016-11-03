from django.shortcuts import render

def event_list(request):
    return render(request, 'knohack/event_list.html', {})
