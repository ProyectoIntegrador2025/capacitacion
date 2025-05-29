import { readonly, ref } from "vue";



export function recetasComposable () {

    let datos = ref ([]);
    let result = ref (null);

    let getDatos = async ()=> {
        try {
            const data = await fetch(`${import.meta.env.VITE_API_URL}Recetas`, {headers: {'content-type' : 'application/json'}});
            datos.value = await data.json();
        } catch (error) {
            result.value = error
        }
    };

    getDatos();

    return {
        datos:readonly(datos),
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