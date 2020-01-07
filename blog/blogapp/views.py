from django.shortcuts import render
from django.utils import timezone
from .models import BlogEntries


def index(request):
    if request.method == "POST":
        entry_text = request.POST['message']
        date_published = timezone.now()
        new_entry = BlogEntries(date_published=date_published, entry_text=entry_text)
        new_entry.save()

    entries_list = BlogEntries.objects.order_by('-date_published')
    return render(request,
                  'blogapp/index.html',
                  {'entries_list': entries_list})

