<script setup>
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';
import { useRoute } from 'vue-router';
import { watchEffect } from 'vue';
import { RecetaDetalleComposable } from '@/composables/RecetaDetalleComposable';
let route = useRoute();

const { dato: dato, result: result } = RecetaDetalleComposable(route.params.slug); //el .params te trae los parametros que vienen en el path

watchEffect(() => {
    if (result.value) {
        window.location = "/error";
    }
});
</script>

<template>
    <Header></Header>

    <div class="breadcumb-area bg-img bg-overlay" style="background-image: url(/img/bg-img/breadcumb4.jpg)">
        <div class="container h-100">
            <div class="row h-100 align-items-center">
                <div class="col-12">
                    <div class="breadcumb-text text-center">
                        <h2>{{ dato.data?.nombre }}</h2>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="receipe-post-area section-padding-80">


        <div class="container">
            <div class="row">
                <div class="col-12">
                    <img :src="dato.data?.foto" class="foto-mini" :alt="dato.data?.nombre" />
                </div>
            </div>
        </div>

        <div class="receipe-content-area">
            <div class="container">

                <div class="row">
                    <div class="col-12 col-md-8">
                        <div class="receipe-headline my-5">
                            <span>{{ dato.data?.fechaCreacion }}</span>
                            <h2>{{ dato.data?.nombre }}</h2>
                            <div class="receipe-duration">
                                <h6>Tiempo : {{ dato.data?.tiempo }}</h6>
                                <h6>Categoría: {{ dato.data?.categoria }}</h6>
                                <h6>Creada por: {{ dato.data?.user_nombre }}</h6>
                            </div>
                        </div>
                    </div>


                </div>

                <div class="row">
                    <div class="col-12 col-lg-12">
                        <div class="single-preparation-step d-flex">
                            <p> {{ dato.data?.descripcion }} </p>
                        </div>

                    </div>

                </div>


            </div>
        </div>
    </div>

    <Footer></Footer>
</template>