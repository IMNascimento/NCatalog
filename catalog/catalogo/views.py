from django.shortcuts import redirect, render
from .models import Photography
from .forms import PhotographyForm, PhotographyDisplayForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def index(request):
    fotografias = Photography.objects.order_by("date_photography").filter(published=True)
    return render(request, 'catalogo/index.html',{"fotos":fotografias})


def sobre(request):
    return render(request, "catalogo/about.html")

def jobs(request):
    return render(request,"catalogo/services.html")

def buscar(reuqest):
    pass

@login_required
def register_photography(request):
    forms = PhotographyForm
    if request.method == "POST":
        form = PhotographyForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'imagem cadastrada com sucesso!')
            return redirect('all_foto')
        
    return render(request, "catalogo/create.html",{"form":forms})




@login_required
def delete_photography(request, id):
    photo = Photography.objects.get(pk=id)
    photo.delete()
    messages.success(request, 'imagem foi deletada com sucesso!')
    return redirect('all_foto')

@login_required
def read_photography(request, id):
    photo = Photography.objects.get(pk=id)
    print(photo)
    form = PhotographyDisplayForm(instance=photo)
    return render(request, "catalogo/show.html",{"form":form, "photo":photo})

@login_required
def edit_photography(request, id):
    photo = Photography.objects.get(pk=id)
    form = PhotographyForm(instance=photo)
    return render(request, "catalogo/edit.html",{"form":form, "photo":photo})

@login_required
def update_photography(request, id):
    try:
        if request.method == "POST":
            photo = Photography.objects.get(pk=id)
            form = PhotographyForm(request.POST, request.FILES, instance=photo)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'imagem foi alterada com sucesso!')
                return redirect('all_foto')
    except Exception as e:
        messages.error(request, e)
        return redirect('all_foto')
            


@login_required
def all_photography(request):
    photos = Photography.objects.all()
    return render(request, 'dashboard/photo.html', {'photos': photos})