from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from catalogo.models import Juego

def lista_juegos(request):
    juegos = Juego.objects.all().order_by('id')  # mantenemos un orden consistente
    paginator = Paginator(juegos, 6)  # mostramos 6 juegos por página

    # Obtenemos el número de página desde la URL (?page=2)
    page_number = request.GET.get('page')

    # Obtenemos los objetos de esa página
    page_obj = paginator.get_page(page_number)

    # Pasamos a la plantilla como 'lista_juegos'
    contexto_catalogo_juegos = {'lista_juegos': page_obj}
    return render(request, 'catalogo/lista_juegos.html', contexto_catalogo_juegos)

def detalle_juego(request, pk):
    # Obtenemos el juego concreto o mostramos un 404 si no existe
    juego = get_object_or_404(Juego, pk=pk)

    # Creamos el contexto que pasaremos a la plantilla
    contexto = {'juego': juego}

    # Renderizamos la plantilla de detalle
    return render(request, 'catalogo/detalle_juego.html', contexto)