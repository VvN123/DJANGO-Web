from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Game
from .forms import NewItemForm,EditItemForm

def detail(request, pk):
    game = get_object_or_404(Game, pk=pk)

    return render(request, 'game/detail.html', {
        'game' : game
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            game = form.save(commit=False)
            game.save()

            return redirect('game:detail', pk=game.id)

    else:
        form = NewItemForm()

    return render(request, 'game/form.html', {
        'form':form
    })



@login_required
def edit(request, pk):
    game = get_object_or_404(Game, pk=pk)
    
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=game)

        if form.is_valid():
            form.save()

            return redirect('game:detail', pk=game.id)

    else:
        form = EditItemForm(instance=game)

    return render(request, 'game/form.html', {
        'form':form
    })


@login_required
def delete(request,pk):
    game = get_object_or_404(Game, pk=pk)
    game.delete()

    return redirect('dashboard:index')

