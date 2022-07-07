<template>

  <div class="register">
    <h2 >Registrate</h2>
    <input type="text" v-model="email" placeholder="E-mail" />
    <input type="text" v-model="username" placeholder="Username" />
    <input type="password" v-model="password1" placeholder="Password" />
    <input type="password" v-model="password2" placeholder="Enter Password Again" />
    <a v-on:click="signUp" href="#"><button>Sign Up</button></a>
    
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: "sign",
    data(){
      return {
            email: '',
            username: '',
            password1: '',
            password2: ''
        }
    },
    methods: {
      async signUp()
      {
        let result = await  axios.post("http://127.0.0.1:5000/signup",{
          email: this.email,
          username: this.username,
          password1: this.password1,
          password2: this.password2
        }) ;
        console.warn(result);
        if(result.data.success == true){
          localStorage.setItem("user-info",JSON.stringify(result.data.user));
          this.$router.push('/VerPost');
          location.reload()
        }

      }
    }
    ,
    mounted(){
      let user= localStorage.getItem("user-info");
      if(user){
        this.$router.push('/VerPost');
      }
    }
    }
  
</script>

<style>
h2{
  padding-top: 50px;
}
.register input {
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
.register button {
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
.register h2 {
    font-size: 32px;
    font-weight: 300;
    padding-left: 565px;
    display: block;
    margin-bottom: 30px;
    margin-right: auto;
    margin-left: auto;
    text-transform: uppercase;
    margin-botton: 24px;}
</style>