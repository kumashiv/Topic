from django.shortcuts import render

# Create your views here.
def index(request):
    """The HomePage for learning_log"""
    return render(request, 'learning_logs/index.html')

def topic(request, topic_id):
    """Show topic and all its entries"""
    topic = Topics.objects.get(topic_id)
    entries = topic.entry_set.order_by('-date_added')

    context = {
        'topic':topic,
        'entries':entries,
        }
    return render(request, 'learning_logs/topic.html', context)
