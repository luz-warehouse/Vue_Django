<template>
  <div>
    <Header @go="book"></Header>
    <Navigator/>

    <div class="course">
      <div class="main">
        <!-- 筛选条件 -->
        <div class="condition">
          <ul class="cate-list">
            <li class="title">作品频道:</li>
            <li class="default " :class="{myhovera:result.gender_type == ''}" @click="result.gender_type = ''">
              不限
            </li>
            <li class="myhover" :class="{myhovera:result.gender_type == gender.id}" v-for="gender in gender"
                @click="result.gender_type = gender.id ">{{ gender.gender_name }}
            </li>
          </ul>
          <div class="ordering">
            <ul>
              <li class="title">作品分类:</li>
              <li class="default " :class="{myhovera:result.tag == ''}"
                  @click="result.tag=''">不限
              </li>
              <li class="myhover" :class="{myhovera:result.tag == tag.id}" @click="result.tag=tag.id"
                  v-for="tag in tag_list">{{ tag.name }}
              </li>
            </ul>

            <ul>
              <li class="title">作品章节:</li>
              <li class="default" :class="{myhovera:result.zhangjie == ''}" @click="result.zhangjie = ''">不限
              </li>
              <li class="myhover" @click="result.zhangjie = 499" :class="{myhovera:result.zhangjie == 499}">
                500章以下
              </li>
              <li class="myhover" @click="result.zhangjie = 501" :class="{myhovera:result.zhangjie == 501}">
                500-1000章
              </li>
              <li class="myhover" @click="result.zhangjie = 1001" :class="{myhovera:result.zhangjie == 1001}">
                1000章以上
              </li>
              <li class="">
                <input type="text" v-model="result.min_zj" style="width: 40px" @click="result.zhangjie=''">
                章 --
                <input type="text" v-model="result.max_zj" style="width: 40px" @click="result.zhangjie=''">
                章

              </li>
            </ul>
            <ul>
              <li class="title">排序方式:</li>
              <li class="default " :class="{myhovera:result.ordering == ''}"
                  @click="result.ordering=''">不限
              </li>
              <li class="myhover"
                  :class="{myhovera:result.ordering == 'zhangjie'||result.ordering == '-zhangjie'}"
                  @click="result.ordering  = (result.ordering == 'zhangjie'?'-zhangjie':'zhangjie')">章节数
              </li>
              <li class="myhover"
                  :class="{myhovera:result.ordering == 'click_num'||result.ordering == '-click_num'}"
                  @click="result.ordering  =(result.ordering == 'click_num'?'-click_num':'click_num')">点击量
                <!--                            @click="result.ordering=(filter.ordering=='-price'?'price':'-price')"-->
              </li>


              <li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</li>

            </ul>

          </div>
        </div>

        <div>
          <table class="table table-hover table-striped text-center">
            <thead>
            <tr style="color: grey">
              <td><b>序号</b></td>
              <td><b>类别</b></td>
              <td><b>书名</b></td>
              <td><b>作者</b></td>
              <td><b>章节数</b></td>
              <td><b>点击量</b></td>
            </tr>
            </thead>
            <tbody class="text-center">

            <tr v-for="(book,index) in book_list" style="color: grey">
              <td v-if="index==0" class="center-block rank"><i
                  style="background: #ff7b00;color: floralwhite">&nbsp;{{ index + 1 }}&nbsp;</i>
              </td>
              <td v-else-if="index==1" class="center-block rank"><i
                  style="background: #ffa92e;color: floralwhite">&nbsp;{{ index + 1 }}&nbsp;</i></td>
              <td v-else-if="index==2" class="center-block rank"><i
                  style="background: #ffd66c;color: floralwhite">&nbsp;{{ index + 1 }}&nbsp;</i></td>
              <td v-else class="center-block rank"><i
                  style="background: #90887d;color: floralwhite">&nbsp;{{ index + 1 }}&nbsp;</i>
              </td>
              <td>
                <router-link :to="'/index/detail/'+book.id" style="text-decoration: none"><span
                    class="myhoveraa">[{{ book.tag.name }}]</span></router-link>
              </td>

              <td>
                <router-link :to="'/index/detail/'+book.id" style="text-decoration: none"><span
                    class="myhoveraa">{{ book.name }}</span></router-link>
              </td>
              <td>{{ book.author.name }}</td>
              <td>{{ book.zhangjie }}</td>
              <td>{{ book.click_num }}</td>

            </tr>
            </tbody>
          </table>

        </div>

        <div class="course_pagination block">
          <el-pagination
              @size-change="handleSizeChange"
              @current-change="handleCurrentChange"
              :current-page.sync="result.page"
              :page-sizes="[10 ,20,30,50]"
              :page-size="result.page_size"
              layout="sizes, prev, pager, next"
              :total="course_total">
          </el-pagination>
        </div>
      </div>

    </div>

    <Footer/>
  </div>
</template>

<script>
import Header from '../components/Header'
import Footer from '../components/Footer'
import Navigator from '../components/Navigator'
// import Booklist from "../components/booklist/booklist";

export default {
  name: "allbook",
  components: {
    Header,
    Footer,
    Navigator,
    // Booklist,
  },
  data() {
    return {
      gender: '',
      tag_list: [],
      book_list: '',
      course_total: 0,
      sousuoneirong:'',
      result: {
        gender_type: '',
        zhangjie: '',
        tag: '',
        min_zj: '',
        max_zj: '',
        ordering: '',
        page_size: 10,       // 单页数据量
        page: 1,
      }
    }
  },
  created() {
    this.get_gender();
    this.get_tag();
    this.get_booklist();


  },
  watch: {
    'result.gender_type': function () {
      this.result.page = 1
      this.get_booklist()
    },
    'result.min_zj': function () {
      this.result.page = 1
      this.get_booklist()
    },
    'result.tag': function () {
      this.result.page = 1
      this.get_booklist()
    },
    'result.zhangjie': function () {
      this.result.page = 1
      this.get_booklist()
    },
    'result.max_zj': function () {
      this.result.page = 1
      this.get_booklist()
    },
    'result.page_size': function () {
      console.log(this.page_size)
      this.result.page = 1
      this.get_booklist()
    },
    'result.page': function () {

      this.get_booklist()
    },
    'result.ordering': function () {
      console.log(this.result.ordering)
      this.result.page = 1
      this.get_booklist()
    }

  },
  methods: {
    book(booklist, bookname) {

      if (booklist.length == 0) {
        this.sousuoneirong = bookname
        // console.log('没搜到东西，好难过', bookname)
      }

      this.book_list = booklist

    },
    handleSizeChange(val) {
      console.log(this.page_size)
      this.result.page_size = val
      // console.log(`每页 ${val} 条`);
    },
    handleCurrentChange(val) {
      this.result.page = val
      // console.log(`当前页: ${val}`);
    },
    get_gender() {
      this.$http.get(this.$settings.base_url + '/api/home/gender/').then(
          response => {
            this.gender = response.data
          }).catch(() => {
        this.$message({
          message: "获取频道信息有误，请联系客服工作人员"
        })
      })
    },
    get_tag() {
      this.$http.get(this.$settings.base_url + '/api/home/tag/').then(
          response => {
            // console.log(response.data)
            this.tag_list = response.data
          }).catch(() => {
        this.$message({
          message: "获取分类信息有误，请联系客服工作人员"
        })
      })

    },
    get_booklist() {
      this.$http.get(this.$settings.base_url + '/api/home/allbook/', {params: this.result}).then(
          response => {
            // console.log(response.data.results)
            this.book_list = response.data.results

            this.course_total = response.data.count
            // console.log(this.course_total)
            // console.log(this.book_list)
          }).catch(() => {
        this.$message({
          message: "获取书籍信息有误，请联系客服工作人员"
        })
      })
    }
  }


}
</script>

<style scoped>
.course {
  background: #f6f6f6;
}

.course .main {
  width: 1100px;
  margin: 35px auto 0;
}

.course .condition {
  margin-bottom: 35px;
  padding: 25px 30px 25px 20px;
  background: #fff;
  border-radius: 4px;
  box-shadow: 0 2px 4px 0 #f0f0f0;
}

.course .cate-list {
  border-bottom: 1px solid #333;
  border-bottom-color: rgba(51, 51, 51, .05);
  padding-bottom: 18px;
  margin-bottom: 17px;
}

.course .cate-list::after {
  content: "";
  display: block;
  clear: both;
}

.course .cate-list li {
  float: left;
  font-size: 16px;
  padding: 6px 15px;
  line-height: 16px;
  margin-left: 14px;
  position: relative;
  transition: all .3s ease;
  cursor: pointer;
  color: #4a4a4a;
  border: 1px solid transparent; /* transparent 透明 */
}

.course .cate-list .title {
  color: #888;
  margin-left: 0;
  letter-spacing: .36px;
  padding: 0;
  line-height: 28px;
}

.course .cate-list .this {
  color: #ffc210;
  border: 1px solid #ffc210 !important;
  border-radius: 30px;
}

.course .ordering::after {
  content: "";
  display: block;
  clear: both;
}

.course .ordering ul {
  float: left;
}

.course .ordering ul::after {
  content: "";
  display: block;
  clear: both;
}

.course .ordering .condition-result {
  float: right;
  font-size: 14px;
  color: #9b9b9b;
  line-height: 28px;
}

.course .ordering ul li {
  float: left;
  padding: 6px 15px;
  line-height: 16px;
  margin-left: 14px;
  position: relative;
  transition: all .3s ease;
  cursor: pointer;
  color: #4a4a4a;
}

.course .ordering .title {
  font-size: 16px;
  color: #888;
  letter-spacing: .36px;
  margin-left: 0;
  padding: 0;
  line-height: 28px;
}

.course .ordering .this {
  color: #ffc210;
}

.course .ordering .price {
  position: relative;
}

.course .ordering .price::before,
.course .ordering .price::after {
  cursor: pointer;
  content: "";
  display: block;
  width: 0px;
  height: 0px;
  border: 5px solid transparent;
  position: absolute;
  right: 0;
}

.course .ordering .price::before {
  border-bottom: 5px solid #aaa;
  margin-bottom: 2px;
  top: 2px;
}

.course .ordering .price::after {
  border-top: 5px solid #aaa;
  bottom: 2px;
}

.course .ordering .price_up::before {
  border-bottom-color: #ffc210;
}

.course .ordering .price_down::after {
  border-top-color: #ffc210;
}

.course .course-item:hover {
  box-shadow: 4px 6px 16px rgba(0, 0, 0, .5);
}

.course .course-item {
  width: 1100px;
  background: #fff;
  padding: 20px 30px 20px 20px;
  margin-bottom: 35px;
  border-radius: 2px;
  cursor: pointer;
  box-shadow: 2px 3px 16px rgba(0, 0, 0, .1);
  /* css3.0 过渡动画 hover 事件操作 */
  transition: all .2s ease;
}

.course .course-item::after {
  content: "";
  display: block;
  clear: both;
}

/* 顶级元素 父级元素  当前元素{} */
.course .course-item .course-image {
  float: left;
  width: 423px;
  height: 210px;
  margin-right: 30px;
}

.course .course-item .course-image img {
  max-width: 100%;
  max-height: 210px;
}

.course .course-item .course-info {
  float: left;
  width: 596px;
}

.course-item .course-info h3 a {
  font-size: 26px;
  color: #333;
  font-weight: normal;
  margin-bottom: 8px;
}

.course-item .course-info h3 span {
  font-size: 14px;
  color: #9b9b9b;
  float: right;
  margin-top: 14px;
}

.course-item .course-info h3 span img {
  width: 11px;
  height: auto;
  margin-right: 7px;
}

.course-item .course-info .teather-info {
  font-size: 14px;
  color: #9b9b9b;
  margin-bottom: 14px;
  padding-bottom: 14px;
  border-bottom: 1px solid #333;
  border-bottom-color: rgba(51, 51, 51, .05);
}

.course-item .course-info .teather-info span {
  float: right;
}

.course-item .section-list::after {
  content: "";
  display: block;
  clear: both;
}

.course-item .section-list li {
  float: left;
  width: 44%;
  font-size: 14px;
  color: #666;
  padding-left: 22px;
  /* background: url("路径") 是否平铺 x轴位置 y轴位置 */
  background: url("/src/assets/img/play-icon-gray.svg") no-repeat left 4px;
  margin-bottom: 15px;
}

.course-item .section-list li .section-title {
  /* 以下3句，文本内容过多，会自动隐藏，并显示省略符号 */
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
  display: inline-block;
  max-width: 200px;
}

.course-item .section-list li:hover {
  /*background-image: url("/src/assets/img/play-icon-yellow.svg");*/
  color: #ffc210;
}

.course-item .section-list li .free {
  width: 34px;
  height: 20px;
  color: #fd7b4d;
  vertical-align: super;
  margin-left: 10px;
  border: 1px solid #fd7b4d;
  border-radius: 2px;
  text-align: center;
  font-size: 13px;
  white-space: nowrap;
}

.course-item .section-list li:hover .free {
  color: #ffc210;
  border-color: #ffc210;
}

.course-item {
  position: relative;
}

.course-item .pay-box {
  position: absolute;
  bottom: 20px;
  width: 600px;
}

.course-item .pay-box::after {
  content: "";
  display: block;
  clear: both;
}

.course-item .pay-box .discount-type {
  padding: 6px 10px;
  font-size: 16px;
  color: #fff;
  text-align: center;
  margin-right: 8px;
  background: #fa6240;
  border: 1px solid #fa6240;
  border-radius: 10px 0 10px 0;
  float: left;
}

.course-item .pay-box .discount-price {
  font-size: 24px;
  color: #fa6240;
  float: left;
}

.course-item .pay-box .original-price {
  text-decoration: line-through;
  font-size: 14px;
  color: #9b9b9b;
  margin-left: 10px;
  float: left;
  margin-top: 10px;
}

.course-item .pay-box .buy-now {
  width: 120px;
  height: 38px;
  background: transparent;
  color: #fa6240;
  font-size: 16px;
  border: 1px solid #fd7b4d;
  border-radius: 3px;
  transition: all .2s ease-in-out;
  float: right;
  text-align: center;
  line-height: 38px;
  position: absolute;
  right: 0;
  bottom: 5px;
}

.course-item .pay-box .buy-now:hover {
  color: #fff;
  background: #ffc210;
  border: 1px solid #ffc210;
}

.course .course_pagination {
  margin-bottom: 60px;
  text-align: center;
}

.myhover:hover {

  background: #ffa60c;
  border-radius: 10%;

}

.myhovera {
  background: #ffa60c;
  border-radius: 10%;

}

.myhoveraa {
  color: #a4a4a4;

}

.myhoveraa:hover {
  color: #ffa60c;

}

</style>