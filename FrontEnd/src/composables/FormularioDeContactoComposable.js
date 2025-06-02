


export function FormularioDeContactoComposable(body) {



    let sendData = async (body) => {
        try {
            let respuesta = await fetch(`${import.meta.env.VITE_API_URL}Contacto`,
                {
                    method: 'POST',
                    body: JSON.stringify(body),
                    headers: { 'content-type': 'application/json' }
                }
            );
            if (respuesta.status == 200) {
                alert('Mensaje enviado exitosamente!');
                window.location = '/'; //CON LOCATION.HREF; SE REFRESCARIA LA APGINA NOMAS
            }
        } catch (error) {
            throw new Error ('Error al enviar el correo')
        }
    };

    return {
        sendData
    };

}