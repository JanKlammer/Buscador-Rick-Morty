# 🔍 Buscador Rick & Morty

Aplicación web construida con Django que permite buscar personajes de la serie **Rick & Morty** utilizando la API oficial.

## 🚀 Funcionalidades implementadas

- 🔎 Buscador: Permite buscar personajes escribiendo una palabra clave (por ejemplo, parte del nombre).
- 🧍 Visualización de resultados:
  - Se muestran en tarjetas con información relevante del personaje: nombre, estado, última ubicación, y episodio inicial.
  - El borde de la tarjeta cambia de color según el estado del personaje:
    - 🟢 Verde: Alive
    - 🔴 Rojo: Dead
    - 🟠 Naranja: Unknown
- ✅ Control de acceso:
  - Si el usuario está autenticado, puede agregar personajes a su lista de favoritos.
  - Si el personaje ya fue agregado, se desactiva el botón con un mensaje de confirmación.
- 🔐 Protección CSRF incluida en los formularios.
- 📃 Plantillas Django (HTML) con extensión de base (`header.html`).


Se uso:
- Python + Django
- HTML + Bootstrap (para estilos y maquetado)
- API pública de Rick & Morty






