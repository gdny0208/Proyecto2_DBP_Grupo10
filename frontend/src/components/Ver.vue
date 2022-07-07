<template>
<div class="Ver">
    <h1 align="center">Publicaciones</h1>
    <div align="center">
        <router-link class="link" :to="{name:'Blog'}"><button>Create a Post</button> </router-link>
    </div>
    <div>
      <li  v-for="item in posts.users" :key="item">      
      {{ item }}
         <button>
               <a  v-on:click="delete2" class="dropdown-item" >Delete {{delete1 = item.id}} </a>
            </button>
            <ul class="dropdown-menu">
              <li>
                
              </li>
            </ul>
      
      </li>
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
        async delete2() {
            let pos= localStorage.getItem("user-info")
            await  axios.post("http://127.0.0.1:5000/delete",{
            id: this.delete1,
            id2: JSON.parse(pos).id,
          
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
    }
    .card {
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    transition: 0.3s;
    border-radius: 5px; /* 5px rounded corners */
    }
    /* Add rounded corners to the top left and the top right corner of the image */
    img {
    border-radius: 5px 5px 0 0;
    }
  </style>