from django.shortcuts import render

# Create your views here.
def alerts(request):
    return render(request,'alerts.html')


def badge(request):
    return render(request,'badge.html')



def breadcrumb(request):
    return render(request,'breadcrumb.html')


def buttons(request):
    return render(request,'buttons.html')

def buttongroup(request):
    return render(request,'buttongroup.html')


def card(request):
    return render(request,'card.html')

def carousel(request):
    return render(request,'carousel.html')


def collapse(request):
    return render(request,'collapse.html')


def dropdown(request):
    return render(request,'dropdown.html')


def forms(request):
    return render(request,'forms.html')

def inputgroup(request):
    return render(request,'inputgroup.html')


def jumpbortron(request):
    return render(request,'jumpbortron.html')


def list(request):
    return render(request,'list.html')

def mediaobject(request):
    return render(request,'mediaobject.html')

def modal(request):
    return render(request,'modal.html')


def navs(request):
    return render(request,'navs.html')


def navbar(request):
    return render(request,'navbar.html')

def pagination(request):
    return render(request,'pagination.html')

def popovers(request):
    return render(request,'popovers.html')

def progress(request):
    return render(request,'progress.html')

def scrollspy(request):
    return render(request,'scrollspy.html')

def spinners(request):
    return render(request,'spinners.html')


def toasts(request):
    return render(request,'toasts.html')

def tooltips(request):
    return render(request,'tooltips.html')