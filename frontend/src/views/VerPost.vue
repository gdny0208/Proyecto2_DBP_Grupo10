<template>
  <div>
    <ver/>
  </div>
</template>

<script>
import ver from "../components/Ver"
export default {
  name:"Verpost",
  components: {ver},
  mounted(){
      let user= localStorage.getItem("user-info");
      if(!user){
        this.$router.push('/login');
      }
    }
  

};
</script>
