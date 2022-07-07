<template>
    <div>
        <input type="text" v-model="textx" placeholder="post" />
        <button v-on:click="post1">Post</button>
    </div>
    <!--<div>
        <div class="Post">
            <h1 align="center">Publicaciones</h1>
            <form>
                <div align="center">
                    <textarea name="text1" id="text" class="form-control" v-model="text1"></textarea>
                </div >
                <br />
                <div align="center">
                    <button v-on:click="post1">Publicar</button>
                </div>
            </form>
            <br />
            <div align="center">
                <router-link :to="{name:'Home'}" tag="button">Atrás</router-link>
            </div>
        </div>
    </div>-->
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
    .Post{
      background: rgba(0, 0, 0, 0.7) url('https://wallpaperstock.net/libro-de-recetas-wallpapers_53636_1920x1200.jpg');
      height: 100%;
      background-position: auto;
      background-repeat: no-repeat;
      background-size: cover;
      background-blend-mode: darken;
    }
    .Post h1{
      color: rgb(228, 218, 197);
      padding-top: 50px;
      padding-bottom: 50px;
      font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
      font-size: 2.5em;
    }
    .Post textarea{
     height: 250px;
    }
    .Post.form-control{
      box-sizing: border-box;
      border: 3px solid rgb(72, 71, 71);
      border-radius: 8px;
      background-color: #f8f8f8;
      font-size: 16px;
      resize: none;
    }
    .Post input {
        width: 300px;
        height: 40px;
        padding-left: 20px;
        display: block;
        margin: 20px;
        margin-bottom: 30px;
        margin-right: auto;
        margin-left: auto;
        border: 1px solid #42b983;
        border-radius: 5px;
    }
    .Post button {
        width: 300px;
        height: 40px;
        padding-left: 20px;
        display: block;
        margin-bottom: 30px;
        margin-right: auto;
        margin-left: auto;
        background-color: #42b983;
        color: #fff;
        border: none;
        border-radius: 5px;
    }
</style>