from django.forms import BaseModelForm
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .models import Notes
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.views.generic.edit import DeleteView
from .forms import NotesForm
from django.contrib.auth.mixins import LoginRequiredMixin

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request,'notes/notes_list.html',{'notes':all_notes})


class NotesListView(LoginRequiredMixin,ListView):
    model = Notes
    # template_name = 'notes/notes_list.html'
    context_object_name = 'notes'
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.notes.all()

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

class NoteCreateView(LoginRequiredMixin,CreateView):
    model = Notes
    # fields = ['title','content']
    form_class = NotesForm
    success_url ="/smart/notes"
    def form_valid(self, form: BaseModelForm):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
        

class NoteUpdateView(LoginRequiredMixin,UpdateView):
    model = Notes
    # fields = ['title','content']
    form_class = NotesForm
    success_url ="/smart/notes"
class NoteDeleteView(LoginRequiredMixin,DeleteView):
    model = Notes
    success_url ="/smart/notes"
    template_name= 'notes/notes_delete.html' 