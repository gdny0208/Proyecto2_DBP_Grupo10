<template>
  <div>
    <post/>
  </div>
</template>

<script>
import post from "../components/Post"
export default {
  name:"blog",
  components: {post},
  mounted(){
      let user= localStorage.getItem("user-info");
      if(!user){
        this.$router.push('/signup');
      }
    }
};
</script>