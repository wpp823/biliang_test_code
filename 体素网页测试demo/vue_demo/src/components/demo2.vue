<template>
  <div>
    <input v-show="false" type="file" accept="image/*" @change="tirggerFile($event)" ref="input"/>
    <div style="width:200px;height:200px;border:1px solid;text-align:center;" @click="openImg">
      <span v-if="imgUrl===''">点击上传</span>
      <img style="height:100%;width:100%;" v-if="imgUrl!=''" :src="imgUrl"/>
    </div>
  </div>
</template>


<script>
export default {
  data() {
    return {
      isSelectFile: false,
      imgUrl: ""
    };
  },
  methods: {
    tirggerFile: function (event) {
      let file = event.target.files[0];
      let url = "";
      var reader = new FileReader();


      url = reader.readAsDataURL(file);
      console.log(url)
      let that = this;
      // console.log(this.result.indexOf(",") + 1)
      reader.onload = function (e) {
        url = this.result.substring(this.result.indexOf(",") + 1);
        that.imgUrl = "data:image/png;base64," + url;
        console.log(url)
        // that.$refs['imgimg'].setAttribute('src','data:image/png;base64,'+url);
      };
    },
    openImg() {
      this.$refs.input.click();
    }
  }
};
</script>


<style scoped>

</style>
