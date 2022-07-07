<template>
  <div class="home">
    <Inicio :post="welcomeScreen" />
    <Inicio :post="hola12"/>
  </div>
</template>

<script>
import Inicio from "../components/Inicio"
export default {
  name: "Home",
  components: {Inicio},
  data() {
    return {
      welcomeScreen: {
        title: "Bienvenido",
        blogPost:
          "Pon tus ideas en nuestro blog de comida",
        photo:"comida2",
      },
    };
  },
};
</script>
