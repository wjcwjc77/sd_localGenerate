<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <input type="text" placeholder="Prompt:" v-model="prompt">    <br>
    <span>For example: a living room with a lot of furniture and decor on it's walls and flooring and a rug</span> <br> <br>
    <!-- <input type="text" placeholder="Neagtive Prompt:">    <br> <br> -->
    <button @click="fetchImages">Generate</button><br>
    <!-- <img src= "data:image/png;base64,图片的base64" /> -->
    <img
          :src="'data:image/png;base64,' + images"
        />
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data(){
    return{
      prompt:"",
      images: "",
    }
  },
  methods:{
    fetchImages() {
      const payload = {
            "prompt": this.prompt,
            "steps": 5
        }
      // Make an HTTP request to your Flask route to get the images
      // Example using Axios:
      axios.post('http://127.0.0.1:5000/test', { payload })
        .then((response) => {
          // Assuming the response contains the "images" field with base64 encoded image data
          this.images = response.data;
          console.log(response)
        })
        .catch((error) => {
          console.error('Error fetching images:', error);
        });
    },

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
