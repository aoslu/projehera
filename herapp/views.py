from herapp.forms import MessageForm
from django.shortcuts import render
from herapp.models import NargileKomuru, Photo,BriketKomur,PresSosisMangalKuru, NakliyeFoto,MeseKomur, Urunler
from django.core.paginator import Paginator
def anasayfa(request):
    foto = Photo.objects.all()

    sayfa = request.GET.get('sayfa')
    paginator = Paginator(foto, 6) # Sayfalama Kısmı


    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            form = MessageForm()
    else:
        form = MessageForm()
    
    context= {
        'form':form,
        'foto':paginator.get_page(sayfa),
    }
    return render(request, "ev/anasayfa.html", context)

#def contak(request):
#    return render(request, "ev/contak.html")

def brand(request):

    urunler = Urunler.objects.all()
    context= {
        'urunler':urunler
    }
    return render(request, "ev/brand.html",context)

def about(request):
    return render(request, "ev/about.html")

def contact(request):
    if request.method == 'POST':
        xd = MessageForm(request.POST)
        if xd.is_valid():
            xd.save()
            xd = MessageForm()
    else:
        xd = MessageForm()
    
    context = {
        'xd': xd
    }
    return render(request, "ev/contact.html",context)

def briket(request):
    fotoo = BriketKomur.objects.all()
    context= {
        'fotoo':fotoo 
    }
    return render(request, "ev/briket.html", context)

def mese(request):
    fotooo = MeseKomur.objects.all()
    context= {
        'fotooo':fotooo 
    }
    return render(request, "ev/mese.html",context)

def sosis(request):
    fotoooo = PresSosisMangalKuru.objects.all()
    context= {
        'fotoooo':fotoooo 
    }
    return render(request, "ev/sosis.html",context)

def special(request):
    fotooooo = NakliyeFoto.objects.all()
    context= {
        'fotooooo':fotooooo 
    }
    return render(request, "ev/special.html",context)
    
def nargile(request):
    fotoooooo = NargileKomuru.objects.all()
    context= {
        'fotoooooo':fotoooooo 
    }
    return render(request, "ev/nargile.html",context)


