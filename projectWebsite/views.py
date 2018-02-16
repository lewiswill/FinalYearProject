from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from projectWebsite.forms import headline_form
from django.urls import reverse
from django.views.generic import TemplateView

class home_view(TemplateView):
    template_name = 'projectWebsite/index.html'
    
    def get(self, request):
       form = headline_form()
       return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = headline_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

        args = {'form': form}
        return render(request, self.template_name, args)

class about_view(TemplateView):
    template_name = 'projectWebsite/about.html'
    def about(request):
        return render (request,'about.html')

class features_view(TemplateView):
    template_name = 'projectWebsite/features.html'
    def about(request):
        return render (request,'features.html')

class fake_view(TemplateView):
    template_name = 'projectWebsite/fake.html'
    def about(request):
        return render (request,'fake.html')

class true_view(TemplateView):
    template_name = 'projectWebsite/true.html'
    def about(request):
        return render (request,'true.html')

        