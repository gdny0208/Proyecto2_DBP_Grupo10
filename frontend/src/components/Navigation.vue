<template> 
  <header>
    <nav class="container">
        <div class="branding">
            <router-link class="header" :to="{name:'Home'}">Blog</router-link>
        </div>
        <div class="nav-links">
            <ul>
                <router-link v-if="imagen" class="link" :to="{name:'Login'}">Login</router-link>
                <router-link v-if= "imagen" class="link" :to="{name:'SignUp'}">Registrar</router-link>
                <router-link v-if= "!imagen" class="link" :to="{name:'Blog'}">Crear Post</router-link>
                <router-link v-if= "!imagen" class="link" :to="{name:'VerPost'}">Blog</router-link>
                <router-link v-if= "!imagen" class="link" :to="{name:'Usuario'}">Usuario</router-link>
                <a v-if= "!imagen" v-on:click="logout1" class="link" href="/">Logout</a>
               
            </ul>
        </div>
    </nav>
  </header>
</template>

<script>

export default {
    name: "navigation",
    components:{
    },
    data() {let user= localStorage.getItem("user-info");
            if(!user){
               return{ imagen:true
                } 
            }
            else{
                return{
                    imagen:false
                }
            }

    },
    created() {
    },
    methods: {
        logout1() {
            localStorage.clear();
        },
    },
    
};
</script>

<style lang="scss" scoped>
header {
    background-color: #fff;
    padding: 0 25px;
    box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.6);
    z-index:99;

    .link {
        font-weight: 500;
        padding: 0 8px;
        transition: 0.3s color ease;

        &:hover {
            color: #1eb8b8;
        }
    }

    nav {
        display: flex;
        padding: 25px 0;

        .branding {
            display: flex;
            align-items: center;

            .header {
                font-weight:600;
                font-size:24px;
                color: #000;
                text-decoration: none;
            }
        }
    
        .nav-links {
            position: relative;
            display:flex;
            flex: 1;
            align-items: center;
            justify-content: flex-end;

            ul {
                margin-right:32px;

                .link{
                    margin-right:32px;
                }

                .link:last-child {
                    margin-right:0;
                }
            }
        }

    }
}
</style>