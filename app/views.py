from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
from app.forms import CommentCreateForm
from app.models import App, Comment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

# Create your views here.
class HelloClass(TemplateView):
    template_name='index.html'

class AppList(ListView):
    template_name='app/app_list.html'
    model=App

class AppDetail(LoginRequiredMixin,DetailView):
    template_name='app/app_detail.html'
    model=App


class AppCreate(LoginRequiredMixin,CreateView):
    template_name='app/app_create.html'
    model=App
    fields=('title','text','degree')
    success_url=reverse_lazy('app:app-list')

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)



class AppDelete(LoginRequiredMixin,DeleteView):
    template_name='app/app_delete.html'
    model=App
    success_url=reverse_lazy('app:app-list')

    def get_object(self,queryset=None):
        data=super().get_object(queryset)

        if data.user != self.request.user:
            raise PermissionDenied
        return data


        

class AppUpdate(LoginRequiredMixin,UpdateView):
    template_name='app/app_update.html'
    model=App
    fields=('title','text','degree')
    success_url=reverse_lazy('app:app-list')

    def get_object(self,queryset=None):
        data=super().get_object(queryset)

        if data.user != self.request.user:
            raise PermissionDenied
        return data

class CommentCreate(CreateView):
    template_name='app/comment_create.html'
    model=Comment
    form_class=CommentCreateForm
    def form_valid(self,form):
        post_pk=self.kwargs['key']
        post=get_object_or_404(App,pk=post_pk)
        comment=form.save(commit=False)
        comment.target=post
        comment.username=self.request.user
        comment.save()
        return redirect('app:app-detail',pk=post_pk)
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['app']=get_object_or_404(App,pk=self.kwargs['key'])
        return context

    
