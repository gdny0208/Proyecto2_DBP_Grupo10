<template>
    <div class="blog-wrapper">
        <div class="blog-content">
            <div>
                <h2 >{{post.title}}</h2>
                <p>{{ post.blogPost}}</p>

                <router-link class="link" to="#">
                    mira nuestros post<Arrow class="arrow" />
                </router-link>
            </div>
            <div class="blog-photo">
                <img :src="require(`../assets/blogPhotos/${post.photo}.jpg`)" alt="" />
            </div>
            <div>
                <p>""</p>
            </div>
        </div>
    </div>
</template>

<script>
import Arrow from "../assets/Icons/arrow-right-light.svg";
export default {
    name:"Inicio",
    props: ["post"],
    components: {Arrow,
    },
};
</script>

<style lang="scss" scoped>
    .blog-wrapper {
        
        display:flex;
        flex-direction: column;
        
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.6);
        @media (min-width: 700px){
            min-height: 350px;
            max-height: 700 px;
            flex-direction:row;
            }
    .blog-content {
        display:flex;
        flex-direction: column;
        
        align-items: center;
        flex: 4;
        order: 2;
        @media (min-width: 700px){
            order:1;    
        }
        @media (min-width: 800px){
            flex:3;
        }

        div {
            max-width: 400;
            
            
            

            h2 {
            
            font-size: 32px;
            font-weight: 300;
            text-transform: uppercase;
            margin-botton: 24px;
            @media (min-width: 700px){
                font-size: 40px;
                }
            }

            p {
                font-size: 15px;
                font-weight: 300;
                line-height: 1.7;
            }

            .content.preview {
                font-size: 13px;
                max-height: 24px;
                width:250px;
                white-space: newrap;
                overflow:hidden;
                text-overflow: ellipsis;
            }

            .link {
                display: inline-flex;
                align-items: center;
                margin-top: 32px;
                padding-button: 4px;
                border-bottom: 1px solid transparent;
                transition: .5s ease-in all;

                &:hover {
                    border-botton-color: #303030;
                }
            }

            .link-light {
                &:hover {
                    border-bottom-color: #ffff;
                }
            }
        }
    }

    .blog-photo {
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06);
        

        img {
            display: block;
            width: 100%;
            height: 100%;
            object-fit:cover;
            
        }
    }
}
</style>