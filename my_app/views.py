from django.shortcuts import render

from my_app.models import Church
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView

def home(request):
    details = Church.objects.all()
    context = {
        'details':details
    }
    return render(request,'my_app/home.html',context)

class ChurchCreateView(LoginRequiredMixin,CreateView):
    model = Church
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ChurchUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Church
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.created_by:
            return True
        return False


class ChurchDetailView(LoginRequiredMixin,DetailView):
    model = Church

class ChurchDeleteView(LoginRequiredMixin,DeleteView):
    model = Church
    success_url = '/'

# class ChurchListView(ListView):
#     model = Church
#     template_name =