from django.shortcuts import render, redirect
from .models import PostModel
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
#from .forms import PostModelForm

@csrf_exempt
def home(request):
    posts = PostModel.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'home.html', context)

@csrf_exempt
def create_post(request):
    
    CATEGORY_CHOICES = PostModel._meta.get_field('categoria').choices
    AYUDANTE_CHOICES = PostModel._meta.get_field('ayudante').choices
    context = {
        'CATEGORY_CHOICES': CATEGORY_CHOICES,
        'AYUDANTE_CHOICES': AYUDANTE_CHOICES,
    }

    if request.method == 'POST':
        profe = request.POST['profe']
        imagen = request.FILES['imagen']
        contenido = request.POST['contenido']
        categoria = request.POST['categoria']
        ayudante = request.POST['ayudante']

        # Crea un nuevo objeto PostModel
        if PostModel.objects.filter(profe=profe).exists():
            messages.error(request, 'El nombre del profesor ya está ocupado. Por favor, elige otro nombre.')
        else:
            # Crea un nuevo objeto PostModel
            post = PostModel(profe=profe, imagen=imagen, contenido=contenido, categoria=categoria, ayudante=ayudante)
            post.save()
            messages.success(request, 'El post se ha creado correctamente.')

        #post = PostModel(profe=profe, imagen=imagen, contenido=contenido, categoria=categoria, ayudante=ayudante)
        #post.save()

        return redirect('home')
    else:
        return render(request, 'blog/create_post.html', context)


@csrf_exempt
def post_detail(request, pk):
    post = PostModel.objects.get(id=pk)
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)
    
@csrf_exempt    
def edit_post(request, pk):
    post = PostModel.objects.get(id=pk)

    if request.method == 'POST':
        post.profe = request.POST['profe']
        
        if 'imagen' in request.FILES:
            imagen = request.FILES['imagen']
        else:
            imagen = post.imagen

        post.contenido = request.POST['contenido']
        post.categoria = request.POST['categoria']
        post.ayudante = request.POST['ayudante']
        post.imagen = imagen
        post.save()

        return redirect('blog-post-detail', pk=post.pk)
        #return redirect('home')
    else:
        CATEGORY_CHOICES = PostModel._meta.get_field('categoria').choices
        AYUDANTE_CHOICES = PostModel._meta.get_field('ayudante').choices

        context = {
            'post': post,
            'CATEGORY_CHOICES': CATEGORY_CHOICES,
            'AYUDANTE_CHOICES': AYUDANTE_CHOICES
        }

        return render(request, 'blog/edit_post.html', context)

def terms_of_use(request):
    return render(request, 'terms_of_use.html')