import * as yup from 'yup'
//npm i vee-validate --save Y npm i @vee-validate/yup

export const FormularioDeContactoSchema = yup.object(
    {
        nombre : yup.string().required('El campo nombre es obligatorio'),
        correo : yup.string().required('Debe ingresar correo').email('Error de email'), //VALIDA QUE EL CORREO SEA CORRECTO OSEA QUE SEA UN CORREO
        telefono : yup.string().required('Su telefono es obligatorio'),
        mensaje : yup.string().required('Debe especificar su mensaje')
    }
);