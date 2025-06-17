// Mostrar mensaje al guardar
if (window.location.search.includes("agregado=ok")) {
    document.getElementById("mensaje").innerHTML = `
        <div class="alert alert-success alert-dismissible fade show" role="alert">
            ✅ Tu usuario se agendó correctamente.
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>`;
}
// Mostrar mensaje al eliminar
if (window.location.search.includes("eliminado=ok")) {
    document.getElementById("mensaje").innerHTML = `
        <div class="alert alert-warning alert-dismissible fade show" role="alert">
            🗑 Tu usuario se eliminó correctamente.
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>`;
}
