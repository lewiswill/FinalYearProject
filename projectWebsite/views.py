from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from projectWebsite.forms import HeadlineForm

def get_headline(request):
   if request.method == 'POST':
      form = HeadlineForm(request.POST)
      if form.is_valid():
          return HttpResponseRedirect('')

   else:
      form = HeadlineForm()

   return render(request, 'projectWebsite/index.html', {'form': form})