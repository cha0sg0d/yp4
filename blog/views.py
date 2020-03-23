from django.shortcuts import render
from django.utils import timezone
from .models import Post, Alumni
from .forms import AlumniForm


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def alum_list(request):
    people = Alumni.objects.all()
    return render(request, 'blog/alum_list.html', {'people': people})

def alumni_new(request):
    if request.method == 'POST':
        form = AlumniForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.date = timezone.now()
            person.save()
    else:
        form = AlumniForm()
    return render(request, 'blog/alum_edit.html', {'form': form})

def home(request):
    return render(request, 'blog/home.html')

