from django.shortcuts import render

# Create your views here.
def ProductView(request):
    return render(request,'product.html')


#CRUD
def CreateView(request):
    if request.method == 'POST':
        # process the form data
        # create a new product
        pass
    else:
        # display the form
        return render(request, 'create.html')
    