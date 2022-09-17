<template>
  <div>
    <Header></Header>
    <Navigator></Navigator>
    <el-row :gutter="20">
      <el-col :span="20" :offset="2">
        <div class="grid-content bg-purple">
          <el-radio-group v-model="tabPosition" style="margin-bottom: 30px;">
          </el-radio-group>
          <el-tabs :tab-position="tabPosition" style="height: 600px;margin-right: 100px">
            <el-tab-pane label="热度榜">
              <div class="book_tit" style="margin-left: 60px;margin-top: 30px">
                <div class="fl">
                  <h2 class="font26 mt5 mb5" id="rankName">
                    <b>热度榜</b>
                  </h2>
                  <hr>
                  <table class="table table-hover table-striped">
                    <thead>
                    <tr>
                      <td><b>排名</b></td>
                      <td><b>分类</b></td>
                      <td><b>书名</b></td>

                      <td><b>作者</b></td>
                      <td><b>热度值</b></td>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="book,index in click_a" style="color: grey">

                      <td v-if="index==0" class="center-block rank">
                        <i style="background: #ff7b00;color: floralwhite">&nbsp;{{ index + 1 }}&nbsp;</i>
                      </td>

                      <td v-else-if="index==1" class="center-block rank"><i
                          style="background: #ffa92e;color: floralwhite">&nbsp;{{ index + 1 }}&nbsp;</i>
                      </td>
                      <td v-else-if="index==2" class="center-block rank"><i
                          style="background: #ffd66c;color: floralwhite">&nbsp;{{ index + 1 }}&nbsp;</i>
                      </td>
                      <td v-else class="center-block rank"><i
                          style="background: #90887d;color: floralwhite">&nbsp;{{ index + 1 }}&nbsp;</i>
                      </td>
                      <td>
                        <router-link :to="'/index/detail/'+book.id"
                                     style="text-decoration: none">

                          <span class="myhover">[{{ book.tag.name }}]</span>
                        </router-link>

                      </td>
                      <td>
                        <router-link :to="'/index/detail/'+book.id"
                                     style="text-decoration: none">
                          <span class="myhover">{{ book.name }}</span>
                        </router-link>
                      </td>
                      <td>{{ book.author.name }}</td>
                      <td>{{ book.click_num }}</td>

                    </tr>
                    </tbody>
                  </table>
                </div>

              </div>

            </el-tab-pane>

            <el-tab-pane label="章节榜">
              <div class="book_tit" style="margin-left: 60px;margin-top: 30px">
                <div class="fl">
                  <h2 class="font26 mt5 mb5" id="rankNamea">
                    <b>章节榜</b>
                  </h2>
                  <hr>
                  <table class="table table-hover table-striped">
                    <thead>
                    <tr>
                      <td><b>排名</b></td>
                      <td><b>分类</b></td>
                      <td><b>书名</b></td>

                      <td><b>作者</b></td>
                      <td><b>章节数</b></td>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="book,index in zhangjie_a" style="color: grey">
                      <td v-if="index==0" class="center-block rank"><i
                          style="background: #ff7b00;color: floralwhite">&nbsp;{{ index + 1 }}&nbsp;</i>
                      </td>
                      <td v-else-if="index==1" class="center-block rank"><i
                          style="background: #ffa92e;color: floralwhite">&nbsp;{{ index + 1 }}&nbsp;</i>
                      </td>
                      <td v-else-if="index==2" class="center-block rank"><i
                          style="background: #ffd66c;color: floralwhite">&nbsp;{{ index + 1 }}&nbsp;</i>
                      </td>
                      <td v-else class="center-block rank"><i
                          style="background: #90887d;color: floralwhite">&nbsp;{{ index + 1 }}&nbsp;</i>
                      </td>
                      <td>
                        <router-link :to="'/index/detail/'+book.id"
                                     style="text-decoration: none">
                          <span class="myhover">[{{ book.tag.name }}]</span>
                        </router-link>
                      </td>
                      <td>
                        <router-link :to="'/index/detail/'+book.id"
                                     style="text-decoration: none">
                          <span class="myhover">{{ book.name }}</span>
                        </router-link>
                      </td>
                      <td>{{ book.author.name }}</td>
                      <td>{{ book.zhangjie }}</td>

                    </tr>
                    </tbody>
                  </table>
                </div>

              </div>

            </el-tab-pane>

            <el-tab-pane label="更新榜">

              <div class="book_tit" style="margin-left: 60px;margin-top: 30px">
                <div class="fl">
                  <h2 class="font26 mt5 mb5" id="rankNameaa">
                    <b>更新榜</b>
                  </h2>
                  <hr>
                  <table class="table table-hover table-striped">
                    <thead>
                    <tr>
                      <td><b>排名</b></td>
                      <td><b>分类</b></td>
                      <td><b>书名</b></td>

                      <td><b>作者</b></td>
                      <td><b>更新时间</b></td>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="book,index in create_time" style="color: grey">
                      <td v-if="index==0" class="center-block rank"><i
                          style="background: #ff7b00;color: floralwhite">&nbsp;{{ index + 1 }}&nbsp;</i>
                      </td>
                      <td v-else-if="index==1" class="center-block rank"><i
                          style="background: #ffa92e;color: floralwhite">&nbsp;{{ index + 1 }}&nbsp;</i>
                      </td>
                      <td v-else-if="index==2" class="center-block rank"><i
                          style="background: #ffd66c;color: floralwhite">&nbsp;{{ index + 1 }}&nbsp;</i>
                      </td>
                      <td v-else class="center-block rank"><i
                          style="background: #90887d;color: floralwhite">&nbsp;{{ index + 1 }}&nbsp;</i>
                      </td>
                      <td>
                        <router-link :to="'/index/detail/'+book.id"
                                     style="text-decoration: none">
                          <span class="myhover">[{{ book.tag.name }}]</span>
                        </router-link>
                      </td>
                      <td>
                        <router-link :to="'/index/detail/'+book.id"
                                     style="text-decoration: none">
                          <span class="myhover">{{ book.name }}</span>
                        </router-link>
                      </td>
                      <td>{{ book.author.name }}</td>
                      <td>{{ book.create_time| dateFormat }}</td>

                    </tr>
                    </tbody>
                  </table>
                </div>

              </div>

            </el-tab-pane>

            <el-tab-pane label="评论榜">

              <div class="book_tit" style="margin-left: 60px;margin-top: 30px">
                <div class="fl">
                  <h2 class="font26 mt5 mb5" id="rankNameaa">
                    <b>更新榜</b>
                  </h2>
                  <hr>
                  <table class="table table-hover table-striped">
                    <thead>
                    <tr>
                      <td><b>排名</b></td>
                      <td><b>分类</b></td>
                      <td><b>书名</b></td>

                      <td><b>作者</b></td>
                      <td><b>评论数</b></td>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="book,index in comment_list" style="color: grey">
                      <td v-if="index==0" class="center-block rank"><i
                          style="background: #ff7b00;color: floralwhite">&nbsp;{{ index + 1 }}&nbsp;</i>
                      </td>
                      <td v-else-if="index==1" class="center-block rank"><i
                          style="background: #ffa92e;color: floralwhite">&nbsp;{{ index + 1 }}&nbsp;</i>
                      </td>
                      <td v-else-if="index==2" class="center-block rank"><i
                          style="background: #ffd66c;color: floralwhite">&nbsp;{{ index + 1 }}&nbsp;</i>
                      </td>
                      <td v-else class="center-block rank"><i
                          style="background: #90887d;color: floralwhite">&nbsp;{{ index + 1 }}&nbsp;</i>
                      </td>
                      <td>
                        <router-link :to="'/index/detail/'+book.id"
                                     style="text-decoration: none">
                          <span class="myhover">[{{ book.tag.name }}]</span>
                        </router-link>
                      </td>
                      <td>
                        <router-link :to="'/index/detail/'+book.id"
                                     style="text-decoration: none">
                          <span class="myhover">{{ book.name }}</span>
                        </router-link>
                      </td>
                      <td>{{ book.author.name }}</td>
                      <td>{{ book.comment_num }}</td>
<!--                      <td>{{ book.create_time| dateFormat }}</td>-->

                    </tr>
                    </tbody>
                  </table>
                </div>

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
import Header from './Header'
import Navigator from './Navigator'
import Footer from "@/components/Footer";

export default {
  data() {
    return {
      activeName: 'second',
      tabPosition: 'right',
      click_a: [],
      zhangjie_a: [],
      create_time: [],
      ordering: '-zhangjie',
      filter: {ordering: '-click_num'},
      aaa: '',
      comment_list: '',
    };
  },
  components: {
    Header,
    Footer,
    Navigator
  },
  created() {
    this.get_clicks();
    this.get_clickss();
    this.get_time();
    this.getComment_listnum()
  },
  methods: {
    getComment_listnum() {
      this.$http.get(this.$settings.base_url + '/api/home/allbook/', {
        params: {ordering: '-comment_num'}
      }).then( res => {
        console.log(res.data)
        this.comment_list = res.data.results
      })
    },
    handleClick(tab, event) {
      console.log(tab, event);
    },

    get_clicks() {
      this.$http.get(this.$settings.base_url + '/api/home/allbook/', {
        params: this.filter
      }).then(response => {
        // console.log(response.data)
        this.click_a = response.data.results
      }).catch(() => {
        this.$message({
          message: "获取书籍信息有误，请联系客服工作人员"
        })
      })
    },
    get_clickss() {
      this.$http.get(this.$settings.base_url + '/api/home/allbook/?ordering=' + this.ordering).then(response => {
        // console.log(response.data)
        this.zhangjie_a = response.data.results
      }).catch(() => {
        this.$message({
          message: "获取书籍信息有误，请联系客服工作人员"
        })
      })
    },
    get_time() {
      this.$http.get(this.$settings.base_url + '/api/home/allbook/?ordering=-create_time').then(response => {
        // console.log(response.data)
        this.create_time = response.data.results
      }).catch(() => {
        this.$message({
          message: "获取书籍信息有误，请联系客服工作人员"
        })
      })

    }

  },
  watch: {
    'filter.ordering': function () {
      this.get_clicks()
    }

  }
};
</script>
<style>
.myhover:hover {
  color: #ff7b00;
}

.myhover {
  color: darkgrey;
}

a:hover {
  color: #f70;
}

h3 {
  display: block;
  font-size: 1.17em;
  margin-block-start: 1em;
  margin-block-end: 1em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
  font-weight: bold;
}

.book_tit {
  border-bottom: 1px solid #eee;
  overflow: hidden;
  padding-bottom: 14px;
  line-height: 1.2;
}

.mb5 {
  margin-bottom: 5px;
}

.mt5 {
  margin-top: 5px;
}

.font26 {
  font-size: 26px !important;
}
</style>
