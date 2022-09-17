<template>
  <div class="background">
    <Header></Header>
    <Navigator></Navigator>
    <br>

    <el-row :gutter="24">

      <el-col :span="20" :offset="2">

        <el-breadcrumb separator=">">
          <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/allBook' }">{{ zhangjie_list.tag.name }}</el-breadcrumb-item>
          <el-breadcrumb-item>{{ zhangjie_list.name }}</el-breadcrumb-item>
        </el-breadcrumb>
        <br>
        <div class="grid-content bg-purple">
          <el-container>
            <!--                        :src="zhangjie_list.book_img.replace('http://127.0.0.1:8000/media/http%3A','http:/')"-->
            <el-aside width="240px">
              <img :height="height" @mouseleave="funclittle" @mouseenter="funcbig"

                   :src="zhangjie_list.book_img.replace('http://127.0.0.1:8000/media/http%3A','http:/')"
                   alt="">
            </el-aside>
            <el-card class="box-card" style="width: 100%;margin: 0 10px">
              <div style="margin: 10px">
                <p> &nbsp;<b style="font-size: 30px">{{ zhangjie_list.name }}</b>&nbsp;&nbsp;&nbsp;&nbsp;
                  {{ zhangjie_list.author.name }}&nbsp; 著</p>
                <br>
                <p> &nbsp;类别：{{ zhangjie_list.tag.name }} &nbsp;&nbsp;&nbsp;&nbsp;
                  总点击：{{ zhangjie_list.click_num }}
                  &nbsp;&nbsp;&nbsp;最后更新时间：{{ zhangjie_list.create_time|dateFormat }}</p>
                <br>
                <p style="width: 70%">&nbsp;<i>{{ zhangjie_list.desc }} </i></p>
                <br>
                <br>

                <router-link :to="'/index/detail/'+ zhangjie_list.id + '/' + zhangjie_list.bookzj[0].id"
                             style="text-decoration: none">
                  <el-button type="success" round style="width: 20%">开始阅读</el-button>
                </router-link>

                &nbsp;
                <el-button type="warning" round style="width: 20%" @click="funcone(zhangjie_list.id)">
                  加入书架
                </el-button>

                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

              </div>

            </el-card>

            <el-card class="box-card text-center" style="width: 28%;position: relative;left: 0">
              <br>
              <div class="block">
                <el-image
                    style="width: 100px; height: 100px; border-radius: 50%"
                    :src="zhangjie_list.author.author_img"
                    fit="cover"
                    ></el-image>

              </div>
              <span class="title"><b>{{ zhangjie_list.author.name }}</b></span>
              <hr>
              <p class="text-left" style="font-size: 16px">作者有话说</p>
              <p style="font-size: 18px;font-family: 楷体">阿巴阿巴阿巴阿巴阿巴阿巴阿巴阿巴阿巴阿巴阿巴</p>
            </el-card>

          </el-container>

        </div>
      </el-col>

    </el-row>

    <br>

    <Zhangjie></Zhangjie>

    <br>

    <comment></comment>

    <Footer></Footer>
  </div>
</template>

<script>
import Header from '../components/Header'
import Footer from '../components/Footer'
import Navigator from '../components/Navigator'
import Zhangjie from "../components/Zhangjie";
import comment from "../components/comment";



export default {
  name: "BookShow",
  components: {
    // cCommentList, cAuthorShow
    Header,
    Footer,
    Navigator,
    Zhangjie,
    comment
  },
  created() {
    this.pk = this.$route.params.pk
  },
  data() {
    return {
      zhangjie_list: '',
      height: '99%',
      pk: '',
      read_text:'',
    }
  },
  watch: {
    '$route.params.pk': function () {
      // console.log(this.$route.params.pk)
      this.pk = this.$route.params.pk
    },
    'pk': function () {
      this.get_data()
    }
  },
  methods: {

    get_data() {
      // var pk = this.$route.params.pk
      // console.log(pk)
      this.$http.get(this.$settings.base_url + '/api/home/allbook/' + this.pk).then(res => {

        this.zhangjie_list = res.data
        // console.log(this.zhangjie_list)
      })
    },
    funcbig() {
      this.height = '100%'
    },
    funclittle() {
      this.height = '99%'
    },
    funcone(args) {
      // console.log(args)
      // console.log($cookies.get('userid'))

      if (!(this.$cookies.get('userid'))) {
        this.$message({
          type: 'warning',
          message: '请登录之后添加！',
        })
        return false
      }


      this.$http.post(this.$settings.base_url + '/api/home/shujia/', {
        user: this.$cookies.get('userid'),
        book: args
      }).then(res => {
        if (res.data.code == 999) {
          this.$message(res.data.msg)
        } else {
          this.$message({
            type: 'success',
            message: '添加书架成功',
          })
        }
      })

    }
  }

}
</script>

<style scoped>
.el-row {
  margin-bottom: 20px;
}


.el-col {
  border-radius: 4px;
}

.bg-purple-dark {
  background: #99a9bf;
}

.bg-purple {
  /*background: #d3dce6;*/
}

.bg-purple-light {
  background: #e5e9f2;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}

.background {
  background: #fff;
}

.el-header, .el-footer {
  background-color: #B3C0D1;
  color: #333;
  text-align: center;
  line-height: 60px;
}

.el-aside {
  /*background-color: #D3DCE6;*/
  color: #333;
  text-align: center;
  line-height: 300px;

}

.el-main {
  background-color: #E9EEF3;
  color: #333;
  text-align: center;
  line-height: 160px;
}

body > .el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
</style>