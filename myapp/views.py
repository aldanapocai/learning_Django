from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import School, Link
import uuid


# Create your views here.
""" def index(request):
    if request.method == 'POST':
        sentence = request.POST['sentence']

        amount_of_words = sentence.split()
        amount_of_words = len(amount_of_words)
        return render(request, 'index.html', {'amount_of_words': amount_of_words})

    return render(request, 'index.html')    """  

def index(request):
    if request.method == 'POST':
        link = request.POST['link']
        unique_id = str(uuid.uuid4())[:5]
        new_link = Link(link= link, uuid=unique_id)
        new_link.save() 
        return render(request, 'index.html', {'unique_id': unique_id})
    
    return render(request, 'index.html')

#Dinamic request page
def return_url(request, pk):
    link_details  = Link.objects.get(uuid=pk)
    link_url = link_details.link
    return redirect(link_url)