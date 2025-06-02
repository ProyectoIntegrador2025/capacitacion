import { readonly, ref } from "vue";
import axios from "axios";

export function RegistroComposable(body) {

    let sendData = async (body) => {
        axios.post(`${import.meta.env.VITE_API_URL}Seguridad/Registro`, body, { headers: { 'content-type': 'application/json' } })
            .then( //IMPORTANTE, EL .THEN ESPERA SIEMPRE UN 200 O 201, SINO TE MANDA DE UNA AL CATCH
                (response) => {
                    alert('¡Registro Existoso, verifica tu mail para activar tu cuenta!');
                    window.location = '/'
                }
            )
            .catch(
                (error) => {
                    alert(error);
                    window.location = '/'
                }
            );
        //PARA METODOS PUT, POST Y DELETE SE PASA EL BODY TAMBIEN, PARA EL GET SOLO EL DICCIONARIO
    }

    return {
        sendData
    };

}

export function LogInComposable() {

    let sendData = async (body) => {
        axios.post(`${import.meta.env.VITE_API_URL}Seguridad/LogIn`, body, { headers: { 'content-type': 'application/json' } })
            .then(
                (response) => {
                    alert('¡LogIn Exitoso!');
                    window.location = '/'
                }
            )
            .catch(
                (error) => {
                    alert(error);
                    window.location = '/'
                }
            );
    }

    return {
        sendData
    };

}