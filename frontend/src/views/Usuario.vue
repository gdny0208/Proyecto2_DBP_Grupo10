<template>
  <div>
    <Usu/>
  </div>
</template>

<script>
import Usu from "../components/Usu"
export default {
  name:"Usuario",
  components: {Usu},
  mounted(){
    let user= localStorage.getItem("user-info");
    if(!user){
      this.$router.push('/');
      }
    }

};
</script>
