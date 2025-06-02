<script setup>
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';
import { Form, Field, ErrorMessage } from 'vee-validate'; //PARA EL FORMULARIO
import { ref } from 'vue'; //PARA LAS VARIABLES REACTIVAS
import { FormularioDeContactoSchema } from '@/schemas/FormularioDeContactoSchema'; //EL SCHEMA SON VALIDACIONES QUE SE HACEN PARA LOS FORMULARIOS
import { FormularioDeContactoComposable } from '@/composables/FormularioDeContactoComposable'

let boton = ref('block'); //ESTO Y LO DE ABAJO ES APRA LA ANIMACION DEL BOTON DE ENVIAR, PARA QUE APAREZCA EL CIRCULITO GIRANDO COMO DE PROCESANDO
let preloader = ref('none');

let nombre = ref('');
let correo = ref('');
let telefono = ref('');
let mensaje = ref('');



const { sendData } = FormularioDeContactoComposable();

let enviar = () => {
    boton.value = 'none';
    preloader.value = 'block';
    sendData({ nombre: nombre.value, correo: correo.value, telefono: telefono.value, mensaje: mensaje.value });
};

</script>

<template>
    <Header></Header>

    <div class="breadcumb-area bg-img bg-overlay" style="background-image: url(img/bg-img/breadcumb5.jpg)">
        <div class="container h-100">
            <div class="row h-100 align-items-center">
                <div class="col-12">
                    <div class="breadcumb-text text-center">
                        <h2>Contáctanos</h2>
                    </div>
                </div>
            </div>
        </div>
    </div>


    <div class="contact-information-area section-padding-80">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <div class="logo mb-80">
                        <img src="/img/core-img/logo2.png" alt="" style="width: 144px;height:65px" />
                    </div>
                </div>
            </div>

            <div class="row">


                <div class="col-12 col-lg-12">
                    <div class="row">
                        <div class="col-4">
                            <div class="single-contact-information mb-30">
                                <h6>Dirección:</h6>
                                <p>481 Creekside Lane Avila <br />Beach, CA 93424</p>
                            </div>
                        </div>
                        <div class="col-4">
                            <div class="single-contact-information mb-30">
                                <h6>Teléfonos:</h6>
                                <p>+53 345 7953 32453 <br />+53 345 7557 822112</p>
                            </div>
                        </div>
                        <div class="col-4">
                            <div class="single-contact-information mb-30">
                                <h6>E-Mail:</h6>
                                <p>{{ 'yourmail@gmail.com' }}</p>
                            </div>
                        </div>
                    </div>


                </div>


            </div>
        </div>
    </div>
    <div class="contact-area section-padding-0-80">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <div class="section-heading">
                        <h3>Cuéntanos en qué te podemos ayudar!!</h3>
                    </div>
                </div>
            </div>

            <div class="row">
                <div class="col-12">
                    <div class="contact-form-area">
                        <Form :validation-schema="FormularioDeContactoSchema" @submit="enviar()"> <!--CON EL :VALIDATION-SCHEMA USAS LAS VALIDACIONES DEL SCHEMA QUE HICISTE-->

                            <div class="row">

                                <div class="col-12 col-lg-6">
                                    <ErrorMessage name="nombre" class="text text-danger" />
                                    <Field type="text" name="nombre" class="form-control" v-model="nombre"
                                        placeholder="Nombre" />
                                </div>

                                <div class="col-12 col-lg-6">
                                    <ErrorMessage name="correo" class="text text-danger" />
                                    <Field type="text" name="correo" class="form-control" v-model="correo"
                                        placeholder="E-Mail" />
                                </div>


                                <div class="col-12">
                                    <ErrorMessage name="telefono" class="text text-danger" />
                                    <Field type="text" name="telefono" class="form-control" v-model="telefono"
                                        placeholder="Teléfono" />
                                </div>

                                <div class="col-12">
                                    <ErrorMessage name="mensaje" class="text text-danger" />
                                    <Field as="textarea" name="mensaje" class="form-control" v-model="mensaje"
                                        placeholder="Mensaje" cols="30" row="10" />
                                </div>

                                <!--CON ESTO DE ACA USAS LO DE LA ANIMACION DE ARIBA-->
                                <div class="col-12 text-center" :style="'display:' + boton">
                                    <button class="btn delicious-btn mt-30" type="submit" title="Enviar">
                                        Enviar
                                    </button>
                                </div>
                                <div class="col-12 text-center" :style="'display:' + preloader">
                                    <img src="/img/img/load.gif" />
                                </div>

                            </div>

                        </Form>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <Footer></Footer>

</template>