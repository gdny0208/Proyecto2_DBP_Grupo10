<template>
<div class="Ver">
    <h1 align="center">Publicaciones</h1>
    <div align="center">
        <router-link class="link" :to="{name:'Blog'}"><button>Crear Post</button> </router-link>
    </div>
    <div>
      <div class="post"  v-for="item in posts.users" :key="item">  
        <div class="post-body">
          <p>{{item.text}}</p>
        </div>
         <button v-on:click ="delete2(item.id)">
               Delete
            </button>
            <ul class="dropdown-menu">
              <li>
                
              </li>
            </ul>
      
      </div>
      
      <br>
    </div>
</div>
</template>

<script>
import axios from 'axios'
export default {
    name: "ver",
    data(){
      return {
            posts: [],
            delete1: 30,
            f : false,
        }
    },
    methods: {
      
        async delete2(info1) {
            let pos= localStorage.getItem("user-info")
            await  axios.post("http://127.0.0.1:5000/delete",{
            id: info1,
            id2: JSON.parse(pos).id,
            
        }) 
                let vue = this;
        axios.get('http://localhost:5000/Post').then(function(response){
            vue.posts = response.data;
            console.log(vue.posts);
            
        })

        },
    },
    mounted(){
        let vue = this;
        axios.get('http://localhost:5000/Post').then(function(response){
            vue.posts = response.data;
            console.log(vue.posts);
            
        })
    },
};
</script>


  <style>
    .Ver{
        background-color: rgb(81, 105, 224);
    }
    .Ver body{
      background: rgba(0, 0, 0, 0.7) url('https://i.pinimg.com/originals/af/db/30/afdb30e83d6ca64eb482a6b40c295e08.jpg');
      height: 100%;
      background-position: auto;
      background-repeat: no-repeat;
      background-size: cover;
      background-blend-mode: darken;
    }
    .Ver h1{
      text-align: center;
      color: black;
      font-weight: bold;
      padding-top: 50px;
      padding-bottom: 20px;
      font-size: 70px;
      font-weight: 600;
      color: white;
      background-clip: text;
      -webkit-background-clip: text;
      font-family: 'Raleway',sans-serif;
    }
    .Ver button{
      background-color: #2011ef;
      border: none;
      color: white;
      padding: 15px 32px;
      padding-bottom: 15px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      margin: 4px 2px;
      cursor: pointer;
      border-radius: 8px;
    }
    .post {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      margin-top: 5px;
    }
    .post-body {
      width: 900px;
      height: auto;
      display: flex;
      flex-direction: column;
      align-items: center;
      margin-top: 50px;
      border: 4px solid #2011ef;
      border-radius: 8px;
      padding-top: 10px;
      padding-left: 5px;
      padding-right: 5px;
      background-color: white;
      text-align: left;
      color: black;
    }
    
  </style>