

from django.shortcuts import render

import data


def notes_list(request):
    notes = data.NOTES

    return render(request, 'base.html', {'notes': notes})
    # context items to be passed


def notes_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return rende(request, 'core/notes_detail.html', {'note': note, "pk": pk})
