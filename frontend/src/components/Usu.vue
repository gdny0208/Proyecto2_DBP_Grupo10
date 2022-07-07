<template>
<div>
    <h1>Mis Post</h1>
    {{posts}}

</div>
</template>

<script>
import axios from 'axios'
export default {
    name: "Usu",
    data(){
      return {posts:[],
            id2: '',
        }
    },
   mounted(){
        let vue = this;
        axios.post('http://localhost:5000/postuser'),{id2: "ALEJANDRO"}.then(function(response){
            vue.posts = response.data;
            console.log(vue.posts);
        })
    },
    
};
</script>