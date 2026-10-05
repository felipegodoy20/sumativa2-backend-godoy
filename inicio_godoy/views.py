from django.shortcuts import render

# Create your views here.

temas = [
    {
        'id': 1,
        'nombre': 'Labrador',
        'descripcion': 'El Labrador Retriever es una raza amigable, inteligente y muy activa, ideal para familias.',
        'imagenes': ['imagenes/Labrador_1.jpg', 'imagenes/Labrador_2.jpg'],
    },
    {
        'id': 2,
        'nombre': 'Pastor Suizo',
        'descripcion': 'El Pastor Suizo Blanco es una raza leal, enérgica y protectora, de gran tamaño y pelaje blanco.',
        'imagenes': ['imagenes/Pastor_suizo_1.jpg', 'imagenes/Pastor_suizo_2.jpg'],
    },
]

def inicio(request):
    return render(request, 'inicio_godoy/inicio.html', {'temas': temas})

def detalle_tema(request, tema_id):
    tema = next((t for t in temas if t['id'] == tema_id), None)
    return render(request, 'inicio_godoy/detalle.html', {'tema': tema})
