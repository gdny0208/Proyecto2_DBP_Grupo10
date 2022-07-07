<template>
    <div class="create">
        <h1>Crear Post</h1>
        <input type="text" v-model="textx" placeholder="Post" /><br>
        <button v-on:click="post1">Post</button>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: "post",
    data(){
      return {
            textx: '',
        }
    },
    methods: {
      async post1()
      { let pos= localStorage.getItem("user-info")
        let result = await  axios.post("http://127.0.0.1:5000/create_post",{
          text: this.textx,
          id1: JSON.parse(pos).id,
          
        }) ;
        console.warn(result);
        if(result.data.success == true){
          this.$router.push('/VerPost');
          location.reload()
        }
      }
    }
};
</script>

<style>
    .create{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background-color: rgb(81, 105, 224);
    }
    .create h1{
      color: rgb(4, 3, 1);
      padding-top: 60px;
      padding-bottom: 15px;
      font-family: 'Raleway',sans-serif;
      font-size: 2.5em;
    }
    .create input {
        height:300px;
        width:500px;
        padding-left: 20px;
        display: block;
        margin: 20px;
        margin-bottom: 30px;
        margin-right: auto;
        margin-left: auto;
        border: 3px solid #2011ef;
        border-radius: 5px;
        font-size: 16px;
    }
    .create button {
        width: 300px;
        height: 40px;
        padding-left: 20px;
        display: block;
        margin-bottom: 30px;
        margin-right: auto;
        margin-left: auto;
        background-color: #2011ef;
        color: #fff;
        border: none;
        border-radius: 80px;
    }
</style>