<template>

  <div>
    <Header></Header>
    <Navigator></Navigator>

    <el-row>
      <br>
      <el-col :span="18" :offset="3">


        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span> <h3><b>{{ zj_name }}</b></h3></span>
            <!--                        <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>-->
          </div>
          <div>
            <div class="text item" id="content" style="margin: 20px 50px" v-html="content">
              <!--                        {{content|safe}}-->

            </div>
          </div>
        </el-card>

        <el-row style="position: fixed;left: 90%;top: 60%" class="text-center">

          <div>
            <el-button round @click="zj_id--">上一章</el-button>
          </div>
          <br>
          <div>
            <el-button round @click="zj_id++">下一章</el-button>
          </div>

        </el-row>

        </el-col>

    </el-row>

    <div style="position: fixed;left: 92%;top: 40%">
      <div v-if="is_bofang_show=='kaishi'">
        <el-button type="success" icon="el-icon-caret-right" circle @click="bofang"></el-button>
      </div>
      <div v-if="is_bofang_show=='huifu'">
        <el-button type="primary" icon="el-icon-caret-right" circle @click="huifu"></el-button>
      </div>
      <div v-if="is_bofang_show=='zanting'">
        <el-button type="warning" icon="el-icon-loading" circle @click="zanting"></el-button>
      </div>
      <br>
      <div>
        <el-button type="danger" icon="el-icon-error" circle @click="handleStop"></el-button>
      </div>
    </div>

    <Footer></Footer>
  </div>

</template>

<script>
import Header from '../components/Header'
import Footer from '../components/Footer'
import Navigator from '../components/Navigator'
import Zhangjie from "../components/Zhangjie";
import comment from "../components/comment";

const synth = window.speechSynthesis;
const msg = new SpeechSynthesisUtterance();

msg.lang = "zh-CN";  // 使用的语言:中文


export default {
  name: "zhangjiedetail",
  data() {
    return {
      book_id: '',
      zj_id: '',
      page: '',
      content: '',
      zj_name: '',
      zhangjie_id: '',
      yinliang: 1,
      yusu: 1.2,
      yingao: 2,
      is_bofang_show: 'kaishi',
    }
  },
  watch: {
    'zj_id': function () {
      this.get_zj()
    },
    'content': function () {
      this.handleStop()
    }
  },
  methods: {


    // 阅读播放
    bofang() {
      this.handleSpeak(this.content)
      this.is_bofang_show = 'zanting'
    },
    // 暂停
    zanting() {
      this.is_bofang_show = 'huifu'
      msg.volume = this.yinliang;      // 声音音量：1
      msg.rate = this.yusu;        // 语速：1
      msg.pitch = this.yingao;       // 音高：1
      synth.pause()
    },
    huifu() {
      this.is_bofang_show = 'zanting'
      msg.volume = this.yinliang;      // 声音音量：1
      msg.rate = this.yusu;      // 语速：1
      msg.pitch = this.yingao;       // 音高：1
      synth.resume()
    },

    // 语音播报的函数
    handleSpeak(text) {
      msg.text = text;     // 文字内容: 小朋友，你是否有很多问号
      // msg.lang = "zh-CN";  // 使用的语言:中文
      msg.volume = this.yinliang;      // 声音音量：1
      msg.rate = this.yusu;     // 语速：1
      msg.pitch = this.yingao;        // 音高：1
      synth.speak(msg);    // 播放
    },
    // 语音停止
    handleStop(e) {
      this.is_bofang_show = 'kaishi'
      msg.text = e;
      msg.lang = "zh-CN";
      synth.cancel(msg);
    },
    // get_data() {
    //   this.$http.get(this.$settings.base_url + '/api/home/zjdetail/', {
    //     params: {
    //       book: this.book_id,
    //     }
    //   }).then(res => {
    //     // console.log(res.data)
    //   })
    // },
    get_zj() {
      this.$http.get(this.$settings.base_url + '/api/home/zhangjiedeaile/' + this.zj_id + '?book=' + this.book_id).then(res => {

        if (res.data.code == 999) {
          this.$message('章节内容不存在')
          this.zj_id = this.zhangjie_id
        } else {
          // console.log(res.data.content)
          // console.log(res.data.content.replace('','<br>'))
          // this.content = res.data.content.replace(' ','<br>')
          // aaa
          this.content = res.data.content
          this.zj_name = res.data.zj_name
          this.zhangjie_id = this.zj_id
        }


      })
    }
  },
  components: {
    // cCommentList, cAuthorShow
    Header,
    Footer,
    Navigator,
    Zhangjie,
    comment
  },
  created() {
    // console.log(this.$route.params)
    this.book_id = this.$route.params.pk
    this.zj_id = this.$route.params.id
    this.zhangjie_id = this.$route.params.id
    // this.get_data()
    this.get_zj()
  },
  beforeDestroy() {
    this.handleStop()
  },
  // destroyed() {
  //   this.handleStop()
  // }

}
</script>

<style scoped>


</style>