import * as yup from 'yup'
//npm i vee-validate --save Y npm i @vee-validate/yup

export const RegistroSchema = yup.object(
    {
        nombre : yup.string().required('El campo nombre es obligatorio'),
        correo : yup.string().required('Debe ingresar correo').email('Error de email'), //VALIDA QUE EL CORREO SEA CORRECTO OSEA QUE SEA UN CORREO
        password : yup.string().required('Su contraseña es obligatorio')
    }
);

export const LogInSchema = yup.object(
    {
        correo : yup.string().required('Debe ingresar correo').email('Error de email'), //VALIDA QUE EL CORREO SEA CORRECTO OSEA QUE SEA UN CORREO
        password : yup.string().required('Su contraseña es obligatorio')
    }
);