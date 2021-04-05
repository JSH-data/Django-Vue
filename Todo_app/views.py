from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from Todo_app.models import Todo
from django.urls import reverse_lazy


class TodoVueOnlyTV(TemplateView) :
    template_name = 'Todo_app/todo_vue_only.html'

class TodoCV(CreateView) :
    model = Todo
    fields = '__all__'
    template_name = 'Todo_app/todo_form.html'
    success_url = reverse_lazy('Todo_app:list')

class TodoLV(ListView) :
    model = Todo
    template_name = 'Todo_app/todo_list.html'

class TodoDelV(DeleteView) :
    model = Todo
    template_name = 'Todo_app/todo_confirm_delete.html'
    success_url = reverse_lazy('Todo_app:list')