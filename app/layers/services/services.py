# capa de servicio/lógica de negocio


from ..persistence import repositories
from ..utilities import translator
from django.contrib.auth import get_user
from ..transport import transport


def getAllImages(input=None):
    # obtiene un listado de datos "crudos" desde la API, usando a transport.py.
    images = []
    json_collection = transport.getAllImages()
    # json_collection = [] # Guardo aca el json en crudo que es el que estamos ahora renderizando y por eso las cards se ven medio mal
    # Falta el codigo que itera sobre el json y lo convierte en las cards para que use el home
    # Fijarse en el home que datos son los que se usan de la card
    for element in json_collection:
        # Extraemos la información que necesitamos de cada personaje
       
        #1. Nombre del personaje.
        name = element.get('name', 'Nombre no disponible')  
        
        #2. Estado del personaje (vivo, muerto o desconocido)
        status = element.get('status', 'Estado no disponible')  
       
        #3. Ultima ubicación del personaje
        last_location = element.get('location', {}).get('name', 'Ubicación no disponible') 
        
        #4. Ubicación de la primera aparición del personaje.
        first_seen = element.get('origin', {}).get('name', 'unknown')
       
        #5. Imagen del personaje.
        image = element.get("image", "Imagen no disponible")
       
        # Creamos una "card" con los datos obtenidos
        images.append({
            'name': name,
            'status': status,
            'last_location': last_location,
            "first_seen": first_seen,
            'url': image #esto era "image" : image y no salia nada, al cambiarlo a "url":image se corrigio.
            })

    return images


# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    fav = '' # transformamos un request del template en una Card.
    fav.user = '' # le asignamos el usuario correspondiente.


    return repositories.saveFavourite(fav) # lo guardamos en la base.


# usados desde el template 'favourites.html'
def getAllFavourites(request):
    if not request.user.is_authenticated:
        return []
    else:
        user = get_user(request)


        favourite_list = [] # buscamos desde el repositories.py TODOS los favoritos del usuario (variable 'user').
        mapped_favourites = []


        for favourite in favourite_list:
            card = '' # transformamos cada favorito en una Card, y lo almacenamos en card.
            mapped_favourites.append(card)


        return mapped_favourites


def deleteFavourite(request):
    favId = request.POST.get('id')
    return repositories.deleteFavourite(favId) # borramos un favorito por su ID.

