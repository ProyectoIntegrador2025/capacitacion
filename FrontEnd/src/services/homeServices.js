export async function getDatosHome () {
    let response = await fetch(`${import.meta.env.VITE_API_URL}recetas-panel/Home`, {headers: {'content-type' : 'application/json'}});
    return await response.json();
}