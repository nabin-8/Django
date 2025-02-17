from django.shortcuts import render
from .models import Artist
from .forms import ArtistForm
from django.shortcuts import redirect

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'artists/artist_list.html', {'artists': artists})


def artist_create(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artist_list')
        else:
            form = ArtistForm()
        return render(request, 'artists/artist_form.html', {'form': form})


def artist_detail(request, pk):
    pass