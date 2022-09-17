<template>

  <div class="row">
    <div class="col-lg-10 col-lg-offset-1">
      <div class="row">

        <div class="col-lg-9">
          <el-card class="box-card">

            <div slot="header" class="clearfix">
              <span style="font-size: 26px"> <b>作品评论区</b>  </span>
              &nbsp;<span>( 共 {{ count }} 条 )</span>
            </div>

            <div class="row container" v-for="obj,index in book_all">

              <div>
                <div class="col-lg-1" style="height: 150px">
                  <div id="img" style="position: relative;top:1px;">
                    <!--                                        <el-image-->
                    <!--                                                style="width: 80px;margin:0 calc(50% - 960px)"-->
                    <!--                                                :src="$settings.base_url+'/media/'+obj.user_img"-->
                    <!--                                                :fit="obj.username" :alt="obj.username">-->
                    <!--                                        </el-image>-->
<!--                    <img style="width: 80px;margin:0 calc(50% - 960px)"-->
<!--                         :src="'http://127.0.0.1:8000/media/' + obj.user_img" alt="">-->
                    <el-image
                        style="width: 100%; height: 100%;  border-radius: 50px"
                        :src="'http://127.0.0.1:8000/media/' + obj.user_img"
                        fit="cover"></el-image>

                  </div>
                </div>

                <div class="col-lg-6">

                  <p><b style=""> <i class="el-icon-user-solid" style="color:#606266"></i>
                    {{ obj.nickname }}</b></p>

                  <div>
                    <div v-if="obj.parent">
                      <p><span style="margin: 10px 0;color: #E6A23C "> @ {{ obj.parent_user }}</span></p>
                      <el-alert
                          :title="obj.context"
                          type="success"
                          :closable="false">
                      </el-alert>
                      <!--                                            <p> {{obj.context}} </p>-->
                    </div>
                    <div v-else>
                      <el-alert
                          :title="obj.context"
                          type="success"
                          :closable="false">
                      </el-alert>
                    </div>
                  </div>

                  <p><i style="color:#909399">{{ obj.create_time|dateFormat }}</i></p>
                  <!--                                    <hr>-->
                  <el-divider></el-divider>
                </div>

                <div class="col-lg-1">
                  <span @click="add_reply(obj.user,obj.nickname)"><el-tag>回复</el-tag></span>
                </div>

              </div>

            </div>

            <div id="user_comment">
              <!--                            <div>-->
              <!--                                <el-alert-->
              <!--                                        title="带辅助性文字介绍"-->
              <!--                                        type="success"-->
              <!--                                        :closable="false"-->
              <!--                                        description="这是一句绕口令：黑灰化肥会挥发发灰黑化肥挥发；灰黑化肥会挥发发黑灰化肥发挥。 黑灰化肥会挥发发灰黑化肥黑灰挥发化为灰……">-->
              <!--                                </el-alert>-->
              <!--                            </div>-->
              <!--                            <br>-->


            </div>

            <el-pagination
                @size-change="handleSizeChange"
                @current-change="handleCurrentChange"
                :current-page.sync="page"
                :page-sizes="[3 ,5,10,20]"
                :page-size="page_size"
                layout="sizes, prev, pager, next"
                :total="count">
            </el-pagination>


            <div>
              <p style="font-size: 18px">发表评论</p>

              <el-input
                  type="textarea"
                  :rows="8"
                  placeholder="请输入内容"
                  v-model="total_content"
                  maxlength="1000">

              </el-input>

              <p style="margin: 10px 5px;color:#909399;font-size: 10px">{{ textarea.length }} / 1000 字</p>

              <el-row style="position: relative;left: 85%">

                <el-button type="primary" round @click="sumbit_comment">发表评论</el-button>

              </el-row>

              <br>
            </div>

          </el-card>
        </div>

        <div class="col-lg-3">
          <el-card class="box-card">
            <div slot="header" class="clearfix">
              <span style="font-size: 20px"> <b>同类推荐</b>  </span>
            </div>

            <div class="row" v-for="obj,index in same_type" @click="pk = obj.id">
              <!--                            :src="obj.img.replace('http://127.0.0.1:8000/media/http%3A','http:/')"-->

              <router-link :to="'/index/detail/'+obj.id"
                           style="text-decoration: none">

                <!--                                                            <div @click="pk = obj.id">-->
                <div class="col-lg-3 col-lg-offset-1" style="margin: 10px">

                  <img height="85px"
                       :src="obj.img"
                       alt="">
                </div>
                <div class="col-lg-7 col-lg-offset-1">
                  <p style="font-size: 18px"><span><b>{{ obj.name }}</b></span></p>
                  <p><i>{{ obj.desc }}</i></p>
                  <br>
                  <br>
                </div>
                <!--                                                            </div>-->
              </router-link>
            </div>
          </el-card>
        </div>

      </div>

    </div>
  </div>

</template>

<script>
export default {
  name: "comment",
  data() {
    return {
      page: 1,
      count: 0,
      page_size: 3,
      book_all: '',
      same_type: '',
      reply_list: [],
      textarea: '',
      name_list: '',
      total_content: '',
      pk: '',
    }
  },
  methods: {

    handleSizeChange(args) {
      this.page = 1
      this.page_size = args
      this.fun_get()
      // console.log(args)

    },
    handleCurrentChange(args) {
      this.page = args
      this.fun_get()
      // console.log(args)
      // console.log(1)
    },

    fun_get() {
      let pk = this.$route.params.pk
      let url = this.$settings.base_url + '/api/home/comment'
      // console.log(url)
      this.$http.get(url, {
        params: {
          book: pk,
          page: this.page,
          page_size: this.page_size
        }
      }).then(res => {
        this.count = res.data.count
        this.book_all = res.data.results

        // console.log(this.book_all)

      })
      this.$http.get(this.$settings.base_url + '/api/home/allbook/' + pk).then(res => {

        this.same_type = JSON.parse(res.data.same_type)
      })
    },
    add_reply(id, name) {

      if (this.reply_list.indexOf(id) == -1) {
        this.reply_list.push(id)
        this.name_list = this.name_list + '@' + name + '\n'
        // console.log(this.name_list)
        this.total_content = this.name_list + this.textarea
        // let num = this.name_list.length
        // console.log(num)
        // console.log(this.total_content.slice(num))
        // this.textarea = this.total_content.slice(num)
      } else {
        this.$message('请不要在一条评论中重复艾特同一个人')
      }

    },
    sumbit_comment() {

      if (!this.$cookies.get('username')) {
        this.$message({
          message: '请先登录',
          type: 'warning'
        })
        return false
      }

      let url = this.$settings.base_url + '/api/home/comment/'
      if (this.textarea) {
        this.$http.post(this.$settings.base_url + '/api/home/comment/', {
          user_list: this.reply_list,
          book: this.$route.params.pk,
          context: this.textarea,
          user: this.$cookies.get('userid')
        },).then(res => {
          // console.log(res)
          if (res.data.code == 999) {
            this.$message.error(res.data.msg);
          } else {
            this.$message({
              message: '发表评论成功！',
              type: 'success',

            });
            let user = this.$cookies.get('username')
            let text = this.textarea
            this.textarea = ''
            this.total_content = ''
            this.fun_get()

            // let divEle = `
            // <div>
            //     <div style="margin: 5px 15px">${user}</div>
            //
            //     <div class="alert alert-success" role="alert">${text}</div>
            //     <br>
            // </div>
            // `
            // let div1 = document.createElement('div')
            // div1.innerHTML = divEle
            // let divE = document.getElementById('user_comment')
            // divE.append(div1)

          }
        })
      } else {
        this.$message({
          message: '评论内容不能为空！！！',
          type: 'warning'
        })
      }

    }
  },
  watch: {
    'total_content': function () {
      let num = this.name_list.length
      // console.log(num)
      // console.log(num)
      // console.log(this.total_content.slice(num))
      // console.log(this.total_content.indexOf(this.name_list))
      if (this.total_content.indexOf(this.name_list) == -1) {
        this.reply_list = []
        this.name_list = ''
        this.textarea = this.total_content
      } else {
        this.textarea = this.total_content.slice(num)
      }
      // console.log(this.textarea)
    },
    'pk': function () {
      // console.log(1)
      this.fun_get()
    },


  },

  created() {
    this.fun_get()
  },

}
</script>

<style scoped>
#img {
  height: 50px;
  width: 50px;
  margin: auto;
  text-align: center;
  overflow: hidden;
  border-radius: 50%;
}
</style>