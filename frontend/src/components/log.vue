<template>

  <div class="register">
    <h2 >Log in</h2>
    <input type="text" v-model="username" placeholder="E-mail" />
    <input type="password" v-model="password" placeholder="Password" />
    <button v-on:click="log1">log in</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: "log",
    data(){
      return {
            username: '',
            password: '',
        }
    },
    methods: {


      async log1()
      {
        let result = await  axios.post("http://127.0.0.1:5000/login",{
          username: this.username,
          password: this.password,
        });
        console.warn(result);
        if(result.data.success == true){
          localStorage.setItem("user-info",JSON.stringify(result.data));
          
          this.$router.push('/VerPost');
          location.reload()
          
        }

      }
      
    },
    mounted(){
      let user= localStorage.getItem("user-info");
      if(user){
        this.$router.push('/VerPost');
        
      }
    }
};
</script>

<style>
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