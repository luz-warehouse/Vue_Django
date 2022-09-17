<template>
  <div class="bbb">
    <Header/>
    <Navigator/>
    <br>
    <el-row :gutter="20">
      <el-col :span="20" :offset="2">
        <div class="aaa">
          <br>
          <el-tabs :tab-position="tabPosition" style="height: 100%;">

            <el-tab-pane label="　　个 　人 　中　 心　">
              <div class="avataraa">
                <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

                <!--                <el-image-->
                <!--                    style="width: 120px; height: 120px; border-radius: 50%"-->
                <!--                    :src="GRZX.icon"-->
                <!--                ></el-image>-->
                <el-image
                    style="width: 120px; height: 120px;  border-radius: 50px"
                    :src="GRZX.icon"
                    fit="cover"></el-image>
                <!--                <img style="width: 120px; height: 120px; border-radius: 50%" :src="GRZX.icon" alt="">-->


              </div>
              <div class="text-center">
                <span>账户余额:&nbsp;&nbsp;</span>
                <span>{{ GRZX.coin }}</span>
                <span>&nbsp;屋币</span>
                <router-link to="/index/recharge">
                  <span class="info-recharge">立即充值</span>
                </router-link>
              </div>

              <br>
              <hr>
              <hr>

            </el-tab-pane>

            <el-tab-pane label="　　我 　的 　书　 架　">
              <div>
                <div class="container" style="margin: 20px">
                  <div><h3>我的书架</h3></div>
                  <hr>
                  <div class="row ">
                    <table class="table table-hover table-striped">
                      <thead>
                      <tr>
                        <td><b>序号</b></td>
                        <td><b>书名</b></td>
                        <td><b>更新时间</b></td>
                        <td><b>从书架中删除</b></td>
                      </tr>
                      </thead>
                      <tbody>

                      <tr v-for="obj,index in shujia_list" v-if="obj.id">

                        <td style="width: 10%">
                          <router-link :to="'/index/detail/'+obj.book"
                                       style="text-decoration: none">{{ index + 1 }}
                          </router-link>
                        </td>
                        <td style="width: 25%">
                          <router-link :to="'/index/detail/'+obj.book"
                                       style="text-decoration: none">
                            <span class="abc">{{ obj.bookname }}</span>
                          </router-link>
                        </td>
                        <td style="width: 25%">
                          <span class="abc">{{ obj.book.updated_time| dateFormat }}</span>
                        </td>
                        <td>
                          <el-button size="mini" type="danger" icon="el-icon-delete" circle
                                     @click="delete_shujia(obj)"></el-button>
                        </td>


                      </tr>
                      </tbody>

                    </table>
                  </div>
                </div>
              </div>

            </el-tab-pane>

            <el-tab-pane label="　　我　 的 　书　 评　">

              <div>

                <div class="container">
                  <div><h3>我的书评</h3></div>


                  <div class="row">

                    <div v-for=" (obj,index) in comment_list">
                      <el-card class="box-card">
                        <div slot="header" class="clearfix">
                          <router-link :to="'/index/detail/'+obj.book"
                                       style="text-decoration: none">
                            <span>{{ obj.bookname }}</span>
                          </router-link>
                        </div>
                        <div class="text item">

                          <div v-if="obj.parent">
                            <p>@{{ obj.nickname }}</p>

                            <div>
                              <el-alert
                                  :title="obj.context"
                                  type="warning"
                                  effect="dark">
                              </el-alert>
                            </div>

                          </div>

                          <div v-else>
                            <el-alert
                                :title="obj.context"
                                type="warning"
                                effect="dark">
                            </el-alert>
                          </div>

                        </div>
                      </el-card>
                    </div>


                  </div>


                </div>

                <div style="position: relative;bottom: 10%">
                  <el-pagination
                      @size-change="handleSizeChange"
                      @current-change="handleCurrentChange"
                      :current-page.sync="page"
                      :page-sizes="[1 ,2,3]"
                      :page-size="page_size"
                      layout="sizes, prev, pager, next"
                      :total="count">
                  </el-pagination>
                </div>

              </div>

            </el-tab-pane>

            <el-tab-pane label="　　我　 的 　反　 馈　">
              <h1 class="text-center">即将上线!!!</h1>
              <h1 class="text-center">即将上线!!!</h1>
              <h1 class="text-center">即将上线!!!</h1>
              <h1 class="text-center">即将上线!!!</h1>
              <h1 class="text-center">即将上线!!!</h1>
              <h1 class="text-center">即将上线!!!</h1>
              <h1 class="text-center">即将上线!!!</h1>
              <h1 class="text-center">即将上线!!!</h1>
              <h1 class="text-center">即将上线!!!</h1>
            </el-tab-pane>

            <el-tab-pane label="　　账　 号　 设 　置　">
              <div>
                <ul>
                  <li>
                    <div class="avatara">
                      <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
                      <p class="ccc">我的头像&nbsp;&nbsp;&nbsp;&nbsp;</p>
                      <label for="avatarFile">

                        <div class="item_bock head_p">

                          <div class="head_img">
                            <el-image
                                style="width: 100px; height: 100px;  border-radius: 50px"
                                :src="GRZX.icon"
                                fit="cover"></el-image>
                            <!--                            <img :src="GRZX.icon" alt="">-->
                          </div>

                        </div>
                        <!--                        <el-image-->
                        <!--                            style="width: 80px; height: 80px; border-radius: 50%"-->
                        <!--                            :src="GRZX.icon"-->
                        <!--                        ></el-image>-->
                      </label>
                      <input type="file" id="avatarFile" v-show="false" @change="set_ico">
                    </div>
                  </li>
                  <br>
                  <li>
                    <div>
                      <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

                      <span class="ccc">我的昵称&nbsp;&nbsp;&nbsp;&nbsp;</span>

                      <span class="ddd" @click="name = true">{{ this.GRZX.nickname }} [修改]</span>
                      <el-dialog
                          title="修改昵称"
                          :visible.sync="name"
                          width="30%"
                          center>
                                                <span>
                                                    昵称：<el-input v-model="nickname"
                                                                 placeholder="请输入新昵称"></el-input>
                                                    <p class="nick-hint">用户名只能包括汉字、英文字母、数字和下划线</p>
                                                </span>
                        <span slot="footer" class="dialog-footer">
                                                <el-button @click="name = false">取 消</el-button>
                                                    <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
                                                <el-button type="primary" @click="set_nickname">修改</el-button>
                                              </span>
                      </el-dialog>
                    </div>
                  </li>
                  <br>
                  <li>
                    <div>
                      <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

                      <span class="ccc">我的性别&nbsp;&nbsp;&nbsp;&nbsp;</span>
                      <span class="ddd" @click="centerDialogVisible = true">{{ this.GRZX.gender }} [修改]</span>
                      <el-dialog
                          title="修改性别"
                          :visible.sync="centerDialogVisible"
                          width="30%"
                          center>
                                                <span class="text-center">
                                                        <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
                                                        <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

                                                      <el-radio v-model="sex" label="0">男</el-radio>
                                                      <el-radio v-model="sex" label="1">女</el-radio>
                                                </span>
                        <span slot="footer" class="dialog-footer">
                                                <el-button @click="centerDialogVisible = false">取 消</el-button>
                                                 <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

                                                <el-button type="primary"
                                                           @click="set_sex">修 改</el-button>
                                              </span>
                      </el-dialog>
                    </div>
                  </li>
                  <br>
                  <li>
                    <div>
                      <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

                      <span class="ccc">我的密码&nbsp;&nbsp;&nbsp;&nbsp;</span>
                      <span class="ddd" @click="pwd = true">修改密码</span>
                      <el-dialog
                          title="修改密码"
                          :visible.sync="pwd"
                          width="30%"
                          center>
                                                <span>
                                                    <p></p>原密码：
                                                    <el-input v-model="s_pwd.password" placeholder="请输入原密码"
                                                              type="password"></el-input>
                                                    <p></p>新密码：
                                                    <el-input v-model="s_pwd.new_password"
                                                              placeholder="请输入新密码" type="password"></el-input>
                                                    <p></p>确认新密码：
                                                    <el-input v-model="s_pwd.re_password"
                                                              placeholder="请确认新密码" type="password"></el-input>
                                                </span>
                        <span slot="footer" class="dialog-footer">
                                                <el-button @click="pwd = false">取 消</el-button>
                                                    <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
                                                <el-button type="primary" @click="set_pwd">修改</el-button>
                                              </span>
                      </el-dialog>

                    </div>
                  </li>
                  <br>
                  <li>
                    <div>
                      <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

                      <span class="ccc">当前状态&nbsp;&nbsp;&nbsp;&nbsp;</span>
                      <span class="ddd" @click="logout">退出登录</span>
                    </div>
                  </li>
                </ul>
              </div>

            </el-tab-pane>

          </el-tabs>
        </div>
      </el-col>
    </el-row>
    <Footer/>
  </div>
</template>

<script>
import Header from '../components/Header'
import Footer from '../components/Footer'
import Navigator from '../components/Navigator'

export default {

  name: "personage",
  data() {
    return {
      myfile: '',
      page: 1,
      count: 0,
      page_size: 3,
      comment_list: '',
      shujia_list: '',
      tabPosition: 'left',
      centerDialogVisible: false,
      name: false,
      pwd: false,
      myavatar: false,
      GRZX: '',
      user_id: '',
      //提交的数据
      avatar: '',
      nickname: '',
      sex: '',
      imageUrl: '',
      s_pwd: {
        password: '',
        new_password: '',
        re_password: '',
      }


    }
  },
  created() {
    // 个人中心
    this.account()
    this.get_shujia()
    this.get_comment()
    if (this.$cookies.get('userid')) {
      // 个人中心
      this.account()
    } else {
      this.$message({
        message: "请先登录~"
      })
      this.$router.push('/')
    }
  },

  methods: {
    // 删书架
    delete_shujia(pk) {
      // let obj = pk
      this.$http.delete(this.$settings.base_url + '/api/home/shujia/' + pk.id + '/').then(res => {
        // console.log('这是删除之后的',res)
        if (res.data.code == 100) {
          this.$message({
            message: '删除成功',
            type: 'success'
          })
          pk.id = 0
        }
      })
    },
    // 修改头像
    set_ico() {

      let img_obj = new FormData()

      if ( !document.getElementById('avatarFile').files[0]){
        return false
      }

      this.myfile = document.getElementById('avatarFile').files[0]

      img_obj.append('file', this.myfile)
      img_obj.append('pk', this.$cookies.get('userid'))


      this.$http.put(this.$settings.base_url + '/api/user/seticon/' + this.$cookies.get('userid') + '/',
          img_obj,
          {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          }).then(res => {
        if (res.data.code == 100) {
          // console.log(res.data)
          // console.log(this.GRZX.icon)
          this.GRZX.icon = 'http://127.0.0.1:8000/media/' + res.data.icon
          // console.log(this.GRZX.icon)
        }
      })

    },
    handleSizeChange(args) {
      this.page = 1
      this.page_size = args
      this.get_comment()
      // console.log(args)

    },
    handleCurrentChange(args) {
      this.page = args
      this.get_comment()
      // console.log(args)
      // console.log(1)
    },
    get_comment() {
      let userid = this.$cookies.get('userid')
      if (userid) {
        this.$http.get(this.$settings.base_url + '/api/home/comment', {
          params: {
            user: userid,
            page: this.page,
            page_size: this.page_size
          }
        }).then(res => {
          // console.log(res.data)
          this.count = res.data.count

          // console.log(res.data.results)
          this.comment_list = res.data.results
        })
      } else {
        this.$message(
            '请先登录！！！'
        )
      }
    },

    get_shujia() {
      let userid = this.$cookies.get('userid')
      if (userid) {
        this.$http.get(this.$settings.base_url + '/api/home/shujia?user=' + userid).then(res => {
          // console.log(res.data)
          if (res.data.code == 999) {
            this.$message(res.data.msg)
          } else {
            this.shujia_list = res.data
            // console.log('书架的',this.shujia_list)
          }

        })
      } else {
        this.$message(
            '请先登录！！！'
        )
      }
    },

    account() {
      let token = this.$cookies.get('token')
      let User_id = this.$cookies.get('userid');
      this.user_id = User_id;
      this.$http.get(this.$settings.base_url + '/api/user/personal/' + this.user_id, {
        headers: {'Authorization': token}
      }).then(response => {
        // console.log(response.data)
        this.GRZX = response.data
        // console.log('这是刘鹏飞',response.data)
      }).catch(() => {
        this.$message({
          message: "获取个人信息有误，请联系客服工作人员"
        })
      })
    },
    //修改昵称
    set_nickname() {

      if (this.nickname) {
        this.name = false;
        let token = this.$cookies.get('token')
        let User_id = this.$cookies.get('userid');
        this.user_id = User_id;
        this.$http.put(this.$settings.base_url + '/api/user/personal/' + this.user_id + '/',
            {
              nickname: this.nickname
            }, {
              headers: {'Authorization': token},
            },).then(response => {
          this.GRZX = response.data
          this.$cookies.set('nickname', this.GRZX.nickname)
          // console.log(this.GRZX)
        })

      } else {
        this.$message({
          message: '输入的昵称不能为空'
        })

      }


    },
    //修改性别
    set_sex() {
      this.centerDialogVisible = false;
      let token = this.$cookies.get('token')
      let User_id = this.$cookies.get('userid');
      this.user_id = User_id;
      this.$http.put(this.$settings.base_url + '/api/user/personal/' + this.user_id + '/',
          {
            sex: this.sex
          }, {
            headers: {'Authorization': token},
          },).then(response => {
        this.GRZX = response.data
      })

    },
    //修改密码
    set_pwd() {

      if (this.s_pwd.password && this.s_pwd.new_password && this.s_pwd.re_password) {
        this.pwd = false;
        let token = this.$cookies.get('token')
        let User_id = this.$cookies.get('userid');
        this.user_id = User_id;
        this.$http.put(this.$settings.base_url + '/api/user/check_pwd/' + this.user_id + '/', this.s_pwd,
            {headers: {'Authorization': token},}
        ).then(response => {
          if (response.data.code === 100) {
            this.$message({
              message: response.data.msg,
              type: "success"
            })
          } else {
            this.$message({
              message: response.data.msg[0]
            })
          }
        })

      } else {
        this.$message({
          message: '输入的密码不能为空'
        })
      }
    },
    //退出登录
    logout() {
      this.$cookies.remove('username')
      this.$cookies.remove('token')
      this.$cookies.remove('userid')
      this.$router.push('/')
    },

  },

  components: {
    Header,
    Footer,
    Navigator
  }
}

</script>

<style scoped>

.item_bock {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 94px;
  width: 300px;
  padding: 0px 24px 0px 38px;
  border-bottom: 1px solid #f7f7f7;
  background: #fff;
}

.head_p {
  height: 132px;
}

.head_img {
  height: 90px;
  border-radius: 50px
}


.head_img img {
  width: 90px;
  height: 90px;
  border-radius: 50px
}

.grid-content {
  width: 80%;
  /*background: #e5efe7;*/
}

.bbb {
  background: rgba(0, 0, 0, 0.1);
}

.aaa {
  height: 600px;
  background: #ffffff;
  border-radius: 2%;

}

.ccc {
  color: #cbcbcb;

}

.ddd:hover {
  color: #ff7b00;
}

.nick-hint {
  font-size: 13px;
  margin: 20px 0;
}

.avatara {
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  /*-webkit-box-pack: center;*/
  -webkit-box-align: center;
}

.abc:hover {
  color: #ff7b00;
}

.abc {
  color: darkgrey
}

.avataraa {
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-pack: center;
  -webkit-box-align: center;
}

.info-recharge {
  display: inline-block;
  border-radius: 3px;
  width: 60px;
  line-height: 20px;
  margin-left: 10px;
  background-color: #ff7b00;
  color: #fff;
  text-align: center;
}


</style>