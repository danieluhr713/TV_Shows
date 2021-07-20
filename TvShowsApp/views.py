from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

# Create your views here.
def shows(request):
    # context = {
    #     'shows': Show.objects.all()
    # }
    return render(request, 'show.html')

def create_show(request):

    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:

        for key, value in errors.items():
            messages.error(request, value)

        return redirect('/shows/new')
    else:

        one_show = Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            releaseDate = request.POST['releaseDate'],
            description = request.POST['description']
        )
        return redirect(f'/shows/{one_show.id}')

def one_show(request, id):
    one_show = Show.objects.get(id=id)
    context = {
        'show': one_show
    }
    return render(request, 'one_show.html', context)

def all_shows(request):
    show = Show.objects.all()
    context = {
        'show':show
    }
    return render(request, 'all_shows.html', context)

def delete_show(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows/new')


def edit(request, id):
    show = Show.objects.get(id=id)
    context = {
        'show': show
    }
    return render(request, 'edit_show.html', context)

def update_shows(request, id):
    to_update = Show.objects.get(id=id)

    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:

        for key, value in errors.items():
            messages.error(request, value)

        return redirect(f'/shows/{to_update.id}/edit')
    else:
        to_update.title = request.POST['title']
        to_update.network = request.POST['network']
        to_update.releaseDate = request.POST['releaseDate']
        to_update.description = request.POST['description']
        to_update.save()
        return redirect('/shows/shows')
