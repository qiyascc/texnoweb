from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from .models import CarouselImage, News, Project, Image, Startup
from .forms import UserMessageForm



def index(request):
    carousel_images = CarouselImage.objects.all().order_by('position')
    last_projects = Project.objects.all().order_by('-id')[:3]
    latest_news = News.objects.all().order_by('-id')[:3]
    context = {
        'last_projects': last_projects,
        'carousel_images': carousel_images,
        'latest_news': latest_news,
        
    }
    return render(request, 'index.html', context)


def news_view(request):
    news_list = News.objects.all()
    return render(request, 'new.html', {'news_list': news_list})

def news_detail(request, news_id):
    news_item = News.objects.get(id=news_id)
    return render(request, 'news_detail.html', {'news_item': news_item})

def projects_view(request):
    hardware_projects = Project.objects.filter(category='hardware')
    biology_projects = Project.objects.filter(category='biology')
    software_projects = Project.objects.filter(category='software')
    all_projects = Project.objects.all()
    last_projects = all_projects.order_by('-id')[:3]

    context = {
        'hardware_projects': hardware_projects,
        'biology_projects': biology_projects,
        'software_projects': software_projects,
        'all_projects': all_projects,
        'last_projects': last_projects,
    }

    return render(request, 'projects.html', context)


def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    all_projects = Project.objects.all()
    last_projects = all_projects.order_by('-id')[:3]
    context = {
        'last_projects': last_projects,
        'all_projects': all_projects,
        'project': project,
    }
    return render(request, 'projects_detail.html', context)


def startup_center(request):
    startups = Startup.objects.all()
    context = {
        'startups': startups,
    }
    return render(request, 'startup.html', context)

def startup_detail(request, startup_id):
    startup = Startup.objects.get(id=startup_id)
    last_startups = Startup.objects.all().order_by('-id')[:3]
    context = {
        'last_startups': last_startups,
        'startup': startup,
    }
    return render(request, 'startup_detail.html', context)


def all_startups(request):
    startup_list = Startup.objects.all()
    context = {
        'startup_list': startup_list,
    }
    return render(request, 'startup_gallery.html', context)



def contact(request):
    if request.method == 'POST':
        form = UserMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Uğurlu bir şəkildə göndərildi!')
            return redirect('contact')

    else:
        form = UserMessageForm()
        context = {
            'form': form
        }

    return render(request, 'contact.html', context)