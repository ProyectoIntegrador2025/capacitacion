import { readonly, ref } from "vue";
import { useRoute } from "vue-router";



export function recetasComposable () {

    let datos = ref ([]);
    let categorias = ref([]);
    let result = ref (null);

    let getDatos = async ()=> {
        let route = useRoute();
        let url;

        if (route.query.categoria_id) {
            url = `${import.meta.env.VITE_API_URL}Recetas-Panel/Buscador?categoria_id=${route.query.categoria_id}&search=${route.query.search}`
        } else {
            url = `${import.meta.env.VITE_API_URL}Recetas`
        }

        try {
            const data = await fetch(url, {headers: {'content-type' : 'application/json'}});
            datos.value = await data.json();
        } catch (error) {
            result.value = error
        }
    };

    let getCategorias = async ()=> {
        try {
            const data = await fetch(`${import.meta.env.VITE_API_URL}Categorias`, {headers: {'content-type' : 'application/json'}});
            categorias.value = await data.json();
        } catch (error) {
            result.value = error
        }
    };

    getDatos();
    getCategorias();

    return {
        datos:readonly(datos),
        categorias:readonly(categorias),
        result:readonly(result)
    }

}

/*
ESTA ES LA ESTRUCTURA BASICA DE UN COMPOSABLE:
export function recetasComposable () {

    let datos = ref ([]);
    let result = ref (null);

    let getDatos = async ()=> {

    };

    getDatos();

    return {
        datos:readonly(datos),
        result:readonly(result)
    }

}
*/