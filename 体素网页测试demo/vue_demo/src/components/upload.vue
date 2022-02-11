<template>
  <div id="app">
    <img :src="imgUrl" width="400" height="300"/><br/>
    <input type="file" @change="tirggerFile($event)" ref="inputer" accept="image/jpeg,image/jpg"/><br/>
    <input type="button" value="上传" @click="uploadpic()"/><br/>
<!--    <button @click="get_img_info">获取图片</button>-->
    <json-viewer :value="showtext" :expand-depth=4 copyable sort></json-viewer>

  </div>
</template>

<script>
export default {
  // el: '#app',
  data() {
    return {
      imgUrl: '',
      filem: '',
      showtext: '返回内容',
    }
  },
  methods: {
    tirggerFile(event) {

      let file = event.target.files[0];
      console.log(24, file)
      var reader = new FileReader();
      let that = this;
      let url
      url = reader.readAsDataURL(file);
      reader.onload = function (e) {
        url = this.result.substring(this.result.indexOf(",") + 1);
        that.imgUrl = "data:image/png;base64," + url;
        console.log(url)
        // that.$refs['imgimg'].setAttribute('src','data:image/png;base64,'+url);
      };
      console.log(32, url)

    },
    // get_img_info() {
    //   console.log(this.$refs.inputer.files)
    // },
    // 上传图片成功
    uploadpic() {
      let inputDOM = this.$refs.inputer;
      this.filem = inputDOM.files[0];
      let formData = new FormData();
      // console.log(this.filem)
      // url = this.result.substring(this.result.indexOf(",") + 1);
      formData.append("file", this.filem);

      // this.imgUrl = formData.url
      this.$axios({
        method: "post",
        url: "http://localhost:8888/upload",
        data: formData,
        headers: {'Content-Type': undefined}
      })
        .then(successResponse => {
          // console.log( successResponse.data.message);
          this.showtext = JSON.stringify(successResponse.data, null, "\t");
        })
    }
  }
}
</script>
