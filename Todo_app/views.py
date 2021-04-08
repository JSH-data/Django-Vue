from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from django.views.generic.list import MultipleObjectMixin
from Todo_app.models import Todo
from django.urls import reverse_lazy

class TodoMOMCV(MultipleObjectMixin, CreateView):
    model = Todo
    fields = '__all__'
    template_name = 'Todo_app/todo_mixin.html'
    success_url = reverse_lazy('Todo_app:mixin') 

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset() 
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().post(request, *args, **kwargs)

class TodoVueOnlyTV(TemplateView) :
    template_name = 'Todo_app/todo_vue_only.html'

class TodoCV(CreateView) :
    model = Todo
    fields = '__all__'
    template_name = 'Todo_app/todo_form.html'
    success_url = reverse_lazy('Todo_app:list')

class TodoLV(ListView) :
    model = Todo # 리스트 뷰를 사용함으로서 Todo라는 데이터베이스의 자료를 자동으로 템플릿에게 넘겨주게 됩니다. 
    template_name = 'Todo_app/todo_list.html'

class TodoDelV(DeleteView) :
    model = Todo
    template_name = 'Todo_app/todo_confirm_delete.html'
    success_url = reverse_lazy('Todo_app:list')

class TodoDelv2(DeleteView) :
    model = Todo
    # template_name = 'Todo_app/todo_confirm_delete.html'
    success_url = reverse_lazy('Todo_app:mixin')

    def get(self, request, *args, **kwargs) :
        return self.delete(request, *args, **kwargs)