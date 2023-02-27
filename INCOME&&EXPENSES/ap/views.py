from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView


from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


from django.urls import reverse_lazy
from .models import db

def home(request):
    return render(request,'tem/index.html')

# login

class custlogin(LoginView):
    template_name = 'reg/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('expenses')
# register 

class registeruser(FormView):
    template_name = 'reg/register.html'  
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('expenses') 
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(registeruser,self).form_valid(form)

    def get(self, *args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('expenses')
        return super(registeruser,self).get(*args,**kwargs)
# Create your views here.

# represting data in index.html

class expenses(ListView):
    model = db
    template_name = 'index.html'
    context_object_name = 'passing_data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['passing_data'] = context['passing_data'].filter(user=self.request.user)
        context['count'] = context['passing_data'].filter(complete=False).count()
        
        search_input = self.request.GET.get('search-area')or ''
        if search_input:
            context['passing_data'] = context['passing_data'].filter(product__icontains = search_input)
            context['search_input'] = search_input
        return context
    

## creating updating details and deleting

class details(DetailView):
    model = db
    template_name = 'detindex.html'
    context_object_name = 'details'


class create(CreateView):
    model = db
    template_name = 'create.html'
    fields = ['product','description','amount','complete']
    success_url = reverse_lazy('expenses') 

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(create,self).form_valid(form)

    
    
class update(UpdateView):
    model = db
    fields = ['product','description','amount','complete']
    template_name = 'create.html'
    success_url = reverse_lazy('expenses') 

class delete(DeleteView):
    model = db
    context_object_name = 'delete'
    template_name = 'delte.html'
    success_url = reverse_lazy('expenses')