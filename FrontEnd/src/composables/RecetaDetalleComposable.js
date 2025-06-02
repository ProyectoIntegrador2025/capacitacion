import { readonly, ref } from "vue";

export function RecetaDetalleComposable(slug) {
    const dato = ref({});
    const result = ref(null);

    const getDatos = async () => {
        try {
            const response = await fetch(
                `${import.meta.env.VITE_API_URL}Recetas-Panel/Recetas-Por-Slug/${slug}`,
                {
                    headers: { 'content-type': 'application/json' }
                }
            );

            const json = await response.json();

            // Detecta errores por status HTTP
            if (!response.ok) {
                result.value = json.Mensaje || `Error ${response.status}`;
                return;
            }

            // Verifica si el backend devolvió error lógico con estado 200
            if (json.Estado === "Error") {
                result.value = json.Mensaje || "Error inesperado.";
                return;
            }

            // Si todo está bien
            dato.value = json;

        } catch (error) {
            // Errores de red, caídas del backend, CORS, etc.
            result.value = "Error de red o del servidor.";
        }
    };

    getDatos();

    return {
        dato: readonly(dato),
        result: readonly(result)
    };
}







/*import { readonly, ref } from "vue";

export function RecetaDetalleComposable (slug) {

    let dato = ref({});
    let result = ref(null);

    let getDatos = async ()=> {
        try {
            const data = await fetch(`${import.meta.env.VITE_API_URL}Recetas-Panel/Recetas-Por-Slug/${slug}`, {headers: {'content-type' : 'application/json'}});
            dato.value = await data.json();
        } catch (error) {
            result.value = error
        }
    };

    getDatos(slug);

    return {
        dato:readonly(dato),
        result:readonly(result)
    }

}*/