<script setup>
//TODO LO DE PROGRAMACION VA ACA
    import Header from '@/components/Header.vue';
    import Footer from '@/components/Footer.vue';
    import { ref, onMounted } from 'vue';
    import { getDatosHome } from '@/services/homeServices';

    let datos = ref([]); //DECLARO UNA VARIABLE DE TIPO REACTIVA, LO CUAL ES QUE LA VARIABLE PUEDE TRABAJAR SEGUN LOS MANEJOS DE ESTADO, la inicializo como [] por que me viene un arreglo
    onMounted(async ()=> {
        datos.value = await getDatosHome()
    });

</script>

<template>
    <!--TODO LO QUE SE VA A VER EN EL NAVEGADOR VA ACA-->
    <Header></Header>

    <div class="breadcumb-area bg-img bg-overlay" style="background-image: url(img/bg-img/breadcumb3.jpg)">
        <div class="container h-100">
            <div class="row h-100 align-items-center">
                <div class="col-12">
                    <div class="breadcumb-text text-center">
                        <h2>Recetas flaites - Desarrollado con React 18</h2>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <section class="top-catagory-area section-padding-80-0">
        <div class="container">

        </div>
    </section>
    <section class="best-receipe-area">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <div class="section-heading">
                        <h3>Últimas recetas publicadas </h3>
                    </div>
                </div>
            </div>

            <div class="row">

                <div v-for="(dato, index) in datos.data" :key="index" class="col-12 col-sm-6 col-lg-4">
                    <div class="single-best-receipe-area mb-30">
                        <img :src="dato.foto" class="foto-mini" :alt="dato.nombre"> <!--LOS : ANTES DE SRC Y ALT SON PARA PODER ACCEDER A LOS DATOS DE LA VARIABLE AHI MISMO-->
                        <div class="receipe-content">
                            <RouterLink :to="{name:'RecetasDetalle', params:{slug : dato.slug}}">
                                <h5>{{ dato.nombre }}</h5>
                            </RouterLink>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <Footer></Footer>
</template>

<style scoped>
/*ACA VAN LOS ESTILOS CON CSS*/
</style>

<!--
ESTA ES LA ESTRUCTURA BASE DE UNA PLANTILLA EN VUE
<script setup>

</script>

<template>

</template>

<style scoped>

</style>
-->