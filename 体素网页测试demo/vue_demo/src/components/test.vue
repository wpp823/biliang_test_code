<template>
  <div class="form-list">
    <label class="label-one">商品图片</label>
    <div class="add-picture">
      <ul>
        <li v-if="img_li1">
          <!-- 展示图片 -->
          <div class="hasPic" v-if="img_1">
            <img class="seledPic" :src="this.imgdata.seledPic_1"/>
            <img
              class="closepic"
              src=""
              @click="pichide('seledPic_1')"
            />
          </div>
          <div class="selPic" v-else>
            <label for="picadd" class="picadd"></label>
            <input
              id="picadd"
              type="file"
              maxlength
              class="input-file"
              multiple="multiple"
              @change="onUpload($event,'seledPic_1')"
              accept="image/*"
            />
          </div>
        </li>
      </ul>
      <p class="prompt">提示：最多添加3张图片，格式为jpg或png</p>
      <p class="prompt" v-if="tips">店铺照片不能为空</p>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      //  上传图片标识
      img_1: false,
      img_2: false,
      img_3: false,
      imgdata: {
        seledPic_1: "",
        seledPic_2: "",
        seledPic_3: ""
      },
      img_li1: true,
      img_li2: false,
      img_li3: false,
    }
  },
  methods: {
    // 判断图片上传类型
    produceImg(type, url) {
      let that = this;
      if (type == "seledPic_1") {
        that.img_1 = true;
        that.img_li2 = true;
        that.$set(that.imgdata, "seledPic_1", url);
      } else if (type == "seledPic_2") {
        that.img_2 = true;
        that.img_li3 = true;
        that.$set(that.imgdata, "seledPic_2", url);
      } else if (type == "seledPic_3") {
        that.img_3 = true;
        that.$set(that.imgdata, "seledPic_3", url);
      }
    },
    // 点击关闭按钮图片隐藏
    pichide(type) {
      let that = this;
      if (type == "seledPic_1") {
        if (that.imgdata.seledPic_1 != "") {
          that.img_1 = false;
          that.img_li2 = false;
        }
        if (that.imgdata.seledPic_2 != "") {
          that.img_1 = false;
          that.img_li2 = true;
        }
        if (that.imgdata.seledPic_3 != "") {
          that.img_1 = false;
          that.img_li2 = true;
          that.img_li3 = true;
        }
      } else if (type == "seledPic_2") {
        if (that.imgdata.seledPic_1 != "") {
          that.img_2 = false;
        }
        if (that.imgdata.seledPic_2 != "") {
          that.img_2 = false;
          that.img_li3 = false;
        }
        if (that.imgdata.seledPic_3 != "") {
          that.img_2 = false;
          that.img_li3 = true;
        }
      } else if (type == "seledPic_3") {
        that.img_3 = false;
      }
    },
    //start 上传图片
    onUpload(e, type) {
      let file = e.target.files[0];
      let filesize = file.size;
      let filename = file.name;
      if (filesize > 10485760) {
        alert("图片太大，无法上传");
      } else {
        let reader = new FileReader();
        // 将图片转为base64位
        reader.readAsDataURL(file);
        reader.onload = function (k) {
          // 读取到的图片base64 数据编码
          var imgcode = k.target.result;
          let data = {
            image: imgcode
          };
          axios({
            url: "http://………………………………",//url地址
            method: "POST",
            data: qs.stringify(data)
          })
            .then(res => {
              let resdata = res.data;
              if (resdata.code == 200) {
                let url = resdata.info;
                this.produceImg(type, url);
              } else {
                alert(resdata.msg);
              }
            })
            .catch(err => {
              console.log(err);
            });
        }.bind(this);
      }
    },
  }
}

</script>
<style>
.form-list {
  width: 100%;
  color: #666;
  font-size: 16px;
  margin: 0 0 20px 0;
}

.add-picture {
  overflow: hidden;
}

.add-picture ul li {
  float: left;
  margin: 0 20px 10px 0;
}

.add-picture .hasPic,
.add-picture .selPic {
  overflow: hidden;
  width: 86px;
  height: 86px;
  border-radius: 4px;
}

.add-picture .hasPic {
  position: relative;
}

.add-picture .hasPic img {
  display: block;
  width: 100%;
  height: 100%;
}

.add-picture .hasPic img.closepic {
  position: absolute;
  top: 0;
  right: 0;
  display: block;
  width: 25px;
  height: 25px;
}

.add-picture .selPic .picadd {
  display: block;
  width: 100%;
  height: 100%;
  /*background: #ff0000;*/
  background-size: 100% 100%;
}

.add-picture .selPic input {
  display: none;
}

.add-picture .prompt {
  clear: both;
  margin: 0;
  font-size: 14px;
  color: #ff0000;
}
</style>
