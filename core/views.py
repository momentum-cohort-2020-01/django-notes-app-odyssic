

from django.shortcuts import render, redirect

from .models import Note

from .forms import NoteForm

from django.http import HttpResponse, HttpResponseNotFound

from django.shortcuts import get_list_or_404, get_object_or_404


def notes_list(request):
    notes = Note.objects.all()

    return render(request, 'core/notes_list.html', {'notes': notes})
    # context items to be passed


def notes_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'core/notes_detail.html', {'note': note, "pk": pk})


def note_new(request):
    # breakpoint()
    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():
            note = form.save()
            return redirect('notes-detail', pk=note.pk)
    else:
        form = NoteForm()

    return render(request, 'core/note_edit.html', {'form': form})


def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)

        if form.is_valid():
            note = form.save()

            return redirect('notes-detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'core/note_edit.html', {'form': form})


def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)

        if form.is_valid():
            note = form.save()

            return redirect('notes-detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'core/note_edit.html', {'form': form})
