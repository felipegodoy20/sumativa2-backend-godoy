from django.shortcuts import render

# Create your views here.

temas = [
    {
        'id': 1,
        'nombre': 'Labrador Retriever',
        'descripcion': 'El Labrador Retriever es una de las razas de perros más populares y queridas en todo el mundo. Conocidos por su carácter amigable, inteligencia y adaptabilidad, los Labradores son compañeros ideales para familias, profesionales y personas activas. Esta raza es especialmente reconocida por su lealtad y disposición para complacer. Son perros que suelen ser muy sociables, que disfrutan de la compañía tanto de humanos como de otros animales, y tienen una naturaleza equilibrada y confiable. Además de ser excelentes compañeros, los Labradores Retriever son ampliamente utilizados en roles como perros guía, de rescate y de trabajo, gracias a su inteligencia y versatilidad. Su personalidad afectuosa y juguetona los convierte en una elección perfecta para cualquier hogar.',
        'imagenes': ['imagenes/Labrador_1.jpg', 'imagenes/Labrador_2.jpg'],
    },
    {
        'id': 2,
        'nombre': 'Pastor Suizo',
        'descripcion': 'El Pastor Suizo es una raza de perro conocida por su elegante pelaje blanco, su carácter noble y su inteligencia excepcional. Aunque comparte muchas características con el Pastor Alemán, el Pastor Suizo suele tener una personalidad más tranquila y adaptable. Es un perro leal, protector y afectuoso, lo que lo convierte en un compañero ideal para familias. Además, es versátil en sus capacidades, siendo apto tanto para la vida en el hogar como para actividades de trabajo o deportes caninos. Con un temperamento equilibrado, esta raza se destaca por su capacidad para aprender rápidamente y su disposición para complacer a su tutor. El Pastor Suizo requiere ejercicio diario y estímulos mentales para mantenerse feliz y saludable.',
        'imagenes': ['imagenes/Pastor_suizo_1.jpg', 'imagenes/Pastor_suizo_2.jpg'],
    },
]

def inicio(request):
    return render(request, 'inicio_godoy/inicio.html', {'temas': temas})

def detalle_tema(request, tema_id):
    tema = next((t for t in temas if t['id'] == tema_id), None)
    return render(request, 'inicio_godoy/detalle.html', {'tema': tema})
