from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView

from api_blog.models import Phrases


class List(ListView):
    model = Phrases


class Single(DetailView):
    model = Phrases


class Create(LoginRequiredMixin, CreateView):
    model = Phrases
    fields = ['title', 'content']
    success_url = reverse_lazy('list_phrase')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)


class Update(LoginRequiredMixin, UpdateView):
    model = Phrases
    fields = ['title', 'content']
    success_url = reverse_lazy('list_phrase')


class Delete(LoginRequiredMixin, DeleteView):
    model = Phrases
    success_url = reverse_lazy('list_phrase')

    # def get_success_url(self):
    #     # pode salvar informações como o a informação que vai ser excluida etc ..
    #     reverse_lazy('list_phrase')
