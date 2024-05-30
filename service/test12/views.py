from django.shortcuts import render
from test12.models import *
from test12.forms import *

# Create your views here.


from django.http import HttpResponse, HttpResponseRedirect
import datetime


def list_orders(request):
    now = datetime.datetime.now()
    
    report = ''
    for order in Order.objects.all().prefetch_related('attached_files'):
        report += '<p>order %s files are[%s]</p>' % (order.pk, ','.join(map(lambda x: str(x), order.all_ataches)))        
    
    html = '<html><body>It is now %s.<p> %s </p></body></html>' % (now, report)
    return HttpResponse(html)

def order(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = OrderForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            order: Order = form.save()
            # order.attached_files
            for file in request.FILES:
                AttachedFile.objects.create(
                    order=order,
                    attached_file=file,
                )            

            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = OrderForm()

    # return render(request, 'test12/order.html', {'form': form})
    return render(request, 'order.html', {'form': form})
