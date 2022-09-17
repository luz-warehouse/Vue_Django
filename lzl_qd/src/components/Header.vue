<template>
  <div :class="['header', showHeader?'header-oneline':'header-moreline']">
    <div class="logo">
      <router-link to="/">
        <img class="logo-img" src="../assets/img/logo.png" alt=""/>
      </router-link>
    </div>
    <div class="search">
      <input @click="funname" v-model="name" class="search-input" placeholder="书名、作者、关键字"/>
      <div class="search-btn" @click="searchbook">
        <i class='glyphicon glyphicon-search' style="color: cornsilk"></i>
      </div>
    </div>
    <div class="info">

      <!-- <span class="info-divider"></span> -->

      <br>
      <div class="right-part">
        <div v-if="!username">
          <span @click="put_login" class="info-login">登录</span>
          <span @click="put_register" class="info-login">注册</span>

          <router-link to="/Password">
            <span class="info-login">&nbsp;忘记密码</span>
          </router-link>
          <!--                    <span @click="reset_pwd">忘记密码</span>-->
        </div>
        <div v-else>
          <router-link to="">
            <span class="el-icon-notebook-2" style="color: coral">&nbsp;我的书架</span>
          </router-link>
          <router-link to="/personage" style="text-decoration:none;">
            <span class="info-login">{{ this.nickname }}</span>
          </router-link>
          <!--                    <span class="line"> |&nbsp; </span>-->
          <span @click="logout" class="info-login">注销</span>
        </div>
      </div>
    </div>
    <Login v-if="is_login" @close="close_login" @go="put_register"/>
    <!--        <Login v-if="is_login" @close="close" @go="put_register"/>-->
    <Register v-if="is_register" @close="close_register" @go="put_login"/>
  </div>
</template>

<script>
import cDivider from './Divider';
import Login from "./Login";
import Register from "./Register";

export default {
  data() {
    return {
      input: "",
      login: false,
      nickname: '',
      showHeader: false,
      username: '',
      url_path: sessionStorage.url_path || '/',
      is_login: false,
      is_register: false,
      // 搜索相关
      is_search_tip: true,
      search_placeholder: '',
      search_word: '',
      name: '',
      book_list: ''

    };
  },
  components: {
    cDivider,
    Login,
    Register,
  },
  created() {
    this.refreshLoginStatus();
    this.username = this.$cookies.get('username')
    this.nickname = this.$cookies.get('nickname')
    // console.log(this.$cookies.get('nickname'))
    // console.log(this.nickname)
  },
  methods: {

    funname() {
      // console.log(this.$route.path)
      if (this.$route.path != '/allBook') {
        this.$router.push('/allBook')
      }
    },

    searchbook() {
      if (this.$route.path == '/allBook') {
        this.$http.get(this.$settings.base_url + '/api/home/searchbook/?name=' + this.name).then(
            response => {
              // console.log(response.data.results)
              this.book_list = response.data.results

              this.$emit('go', this.book_list,this.name)
            }
        )
      } else {
        var namea = this.name
        this.$router.push('/allBook')

        this.name = namea
        this.$http.get(this.$settings.base_url + '/api/home/searchbook/?name=' + this.name).then(
            response => {
              // console.log(response.data.results)
              this.book_list = response.data.results

              this.$emit('go', this.book_list,this.name)
            }
        )
      }

    },
    put_login() {

      this.is_login = true;
      this.is_register = false;
    },
    put_register() {
      this.is_login = false;
      this.is_register = true;
    },
    close_login() {
      this.is_login = false;
      // 只要关闭登录框，去cookie中取username，如果在，就放到头部，不在，就不做处理
      this.username = this.$cookies.get('username')

    },
    close_register() {
      this.is_register = false;
    },
    logout() {
      // 退出登录不需要跟后端交互，本地的cookie删除即可
      this.$cookies.remove('username')
      this.$cookies.remove('token')
      this.$cookies.remove('userid')
      //username也要值为空
      this.username = ''
      this.$router.push('/')
    },

    refreshLoginStatus() {
      if (this.$route.query.modelType != "mobile") {
        this.showHeader = true;
      }
      // console.log(localStorage);
      // console.log(this.$cookies.keys());
      // this.$cookies.keys().forEach(key => {
      //   console.log(key+':'+this.$cookies.get(key));
      // });
      if (this.$cookies.get('Authorization') != null) {
        this.login = true;
        this.nickname = this.$cookies.get('nickname');
      } else if (localStorage.getItem('Authorization') != null) {
        this.$cookies.set("Authorization", localStorage.getItem('Authorization'), 0);
        //刷新token
        this.$http.postForm('/user/refreshToken', {}, res => {
          localStorage.setItem('Authorization', res.token);
          this.$cookies.set("Authorization", res.token, 0);
          this.$cookies.set("nickname", res.nickName, 0);

          this.login = true;
          this.nickname = res.nickName;
        }, () => {
          //访问有误如token失效不处理,清理本地token
          localStorage.removeItem('Authorization');
          this.login = false;
        });
      } else {
        this.login = false;
      }
    },
  },

  watch: {
    '$route.path': function () {
      //路由有变化就检查登录状态
      this.refreshLoginStatus();
    },
    '$store.state.loginStatus': function () {
      this.refreshLoginStatus();
    },
    '$store.state.searchKey': function (newVal) {
      this.input = newVal;
    },
    'name': function () {
      this.searchbook()
    }
  },
  mounted() {
    // Vue.$on('refreshloginstatus', () => {
    //     console.log('refresh...');
    //     // this.refreshLoginStatus();
    // });
  }

}

</script>

<style lang="scss" scope>
//这种东西，正式项目应该是手机和pc不同的地方各一套，就不要写在一起了
.header-oneline {
  height: 92px;
  display: flex;
}

.header-moreline {
  height: 120px;
}

.header {
  background-color: #fff;
  width: 100%;
}

.logo {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;

  .logo-img {
    margin-left: 50px;
    height: 48px;
  }
}

.search {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;

  .search-input {
    outline: none;
    padding-left: 19px;
    border: 1px solid #e97e04;
    border-radius: 19px 0 0 19px;
    width: 270px;
    height: 34px;
    font-size: 14px;
  }

  .search-btn {
    cursor: pointer;
    height: 38px;
    width: 60px;
    border-radius: 0 19px 19px 0;
    background-color: #FF8800;
    display: flex;
    justify-content: center;
    align-items: center;

    .search-icon {
      width: 19px;
      height: 19px;
      background: url('../assets/img/logo@2x.png');
      background-repeat: no-repeat;
      background-size: cover;
    }
  }
}

.info {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;

  .info-bookshelf {
    padding-left: 25px;
    background-image: url("../assets/img/Logotitle.png");
    background-size: contain;
    background-repeat: no-repeat;
    height: 20px;
    line-height: 20px;
    margin-right: 20px;
  }

  .info-divider {
    height: 20px;
    border-style: solid;
    border-color: #FF8800;
    border-width: 0 0 0 1px;
  }

  .info-login {
    color: #333;
    cursor: pointer;
    line-height: 20px;
    height: 20px;
    margin-left: 15px;
  }

  .info-login:hover {
    color: #FF8800;
  }

  .info-logout {
    cursor: pointer;
  }

  .info-regist {
    height: 30px;
    width: 40px;
  }
}
</style>