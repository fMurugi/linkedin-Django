from django.shortcuts import render
from django.http import Http404
from .models import Notes
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.views.generic.edit import DeleteView
from .forms import NotesForm

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request,'notes/notes_list.html',{'notes':all_notes})

class NotesListView(ListView):
    model = Notes
    # template_name = 'notes/notes_list.html'
    context_object_name = 'notes'

# def note_detail(request,pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404('Note does not exist')
#     return render(request,'notes/notes_details.html',{'note':note})
    
class NoteDetailView(DetailView):
    model = Notes
    template_name = 'notes/notes_details.html'
    context_object_name = 'note'

class NoteCreateView(CreateView):
    model = Notes
    # fields = ['title','content']
    form_class = NotesForm
    success_url ="/smart/notes"
class NoteUpdateView(UpdateView):
    model = Notes
    # fields = ['title','content']
    form_class = NotesForm
    success_url ="/smart/notes"
class NoteDeleteView(DeleteView):
    model = Notes
    success_url ="/smart/notes"
    template_name= 'notes/notes_delete.html'