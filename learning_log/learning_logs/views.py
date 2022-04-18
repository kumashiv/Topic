from django.shortcuts import render

from .models import Topic, Entry

from django.contrib.auth.decorators import login_required
from django.http import Http404

# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    """The HomePage for learning_log"""
    return render(request, 'learning_logs/index.html')

@login_required
def topic(request, topic_id):
    """Show topic and all its entries"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')

    context = {
        'topic':topic,
        'entries':entries,
        }
    return render(request, 'learning_logs/topic.html', context)
