from django.shortcuts import render, get_object_or_404, redirect
from .models import Note


#Landing Page
def main(request):
    return render(request, "note.html")

#View All Notes
def all(request):
    notes = Note.objects.all() # Fetch all notes from the database
    return render(request, "note.html", {"notes": notes})

#Vieww Note Deatils
def detail(request, note_id):
    note = get_object_or_404(Note, id=note_id) # Fetch note by ID
    return render(request, "noteedit.html", {"note": note})

#Create New Note
def create_note(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Note.objects.create(title=title, content=content)
        return redirect("all") #Ensure 'all_note' is a valid URL name
    return render(request, "notecreate.html")

#Edit Note
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        note.title = title
        note.content = content
        note.save()
        return redirect("all")
    return render(request, "noteedit.html", {"note": note})


def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect("all")