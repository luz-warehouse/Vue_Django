<template>
    <div class="home">
        <Header/>
        <Navigator/>
        <br>
        <div class="container">
            <!--            第一行-->
            <el-row :gutter="20">

                <div>
                    <el-col :span="16">
                        <div class="grid-content bg-purple" style="height: 300px">

                            <!--                            <template >-->
                            <br>
                            <br>
                            <el-carousel indicator-position="outside">
                                <el-carousel-item v-for="item in this.banner_list"><br>
                                    <!--                                     <router-link :to="item.link" style="text-decoration: none">-->
                                    <img width="100%"
                                         height="100%"
                                         :src="item.image"
                                         alt="">
                                    <!--                                     </router-link>-->
                                </el-carousel-item>
                            </el-carousel>
                            <!--                            </template>-->

                        </div>
                    </el-col>
                </div>
                <br>
                <el-col :span="7" :offset="1">
                    <div class="grid-content bg-purple">
                        <el-card class="box-card">
                            <div slot="header" class="clearfix">

                                <span> <h2><b>本周强推</b></h2></span>
                                <!--                                <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>-->
                            </div>
                            <div v-for=" index in 5" :key="index" class="text item">
                                <!--                                {{index}}-->
                                <div v-if="index==1">
                                    <router-link :to="'/index/detail/'+ gengxin_list[index].id"
                                                 style="text-decoration: none">
                                        <span><i
                                                style="background: #ff7b00;color: floralwhite; height: 20px;width: 20px">&nbsp;{{index}}&nbsp;</i> <span
                                                class="myhover">{{gengxin_list[index].name}}</span></span>
                                        <div>
                                            <div class="row">
                                                <br>
                                                <div class="col-lg-3 col-lg-offset-1">
                                                    <img height="80px"
                                                         :src="gengxin_list[index].book_img.replace('http://127.0.0.1:8000/media/http%3A','http:/')"
                                                         alt="">
                                                </div>
                                                <div class="col-lg-8">
                                                    <span class="myhover">{{gengxin_list[index].desc}}</span>
                                                </div>

                                            </div>
                                        </div>
                                    </router-link>
                                    <br>
                                </div>
                                <div v-else-if="index==2">
                                    <div>
                                        <span><i
                                                style="background: #ffa92e;color: floralwhite; height: 20px;width: 20px">&nbsp;{{index}}&nbsp;</i>  <router-link
                                                :to="'/index/detail/'+gengxin_list[index].id"
                                                style="text-decoration: none"><span class="myhover">{{gengxin_list[index].name}}</span></router-link></span>

                                    </div>
                                    <br>
                                </div>
                                <div v-else-if="index==3">
                                    <div>
                                        <span><i
                                                style="background: #ffd66c;color: floralwhite; height: 20px;width: 20px">&nbsp;{{index}}&nbsp;</i>  <router-link
                                                :to="'/index/detail/'+gengxin_list[index].id"
                                                style="text-decoration: none"><span class="myhover">{{gengxin_list[index].name}}</span></router-link></span>

                                    </div>
                                    <br>
                                </div>
                                <div v-else>
                                    <div>
                                        <div>
                                        <span><i
                                                style="background: #90887d;color: floralwhite; height: 20px;width: 20px">&nbsp;{{index}}&nbsp;</i> <router-link
                                                :to="'/index/detail/'+gengxin_list[index].id"
                                                style="text-decoration: none"> <span class="myhover">{{gengxin_list[index].name}}</span></router-link></span>

                                        </div>
                                    </div>
                                    <br>
                                </div>
                                <!--                                <span v-if="o=1">{{'列表内容 ' + o }}</span>-->
                                <!--                                <span v-else>{{'列表内容 ' + o }}</span>-->
                            </div>
                        </el-card>
                    </div>
                </el-col>
            </el-row>

            <!--            第二行-->
            <el-row :gutter="20">

                <el-col :span="16">
                    <h2><b>热门推荐</b></h2>
                    <br>
                    <div class="grid-content bg-purple">
                        <el-row>
                            <!--                            <el-col :span="5" v-for="(o, index) in 3" :key="o" :offset="index > 0 ? 2 : 0">-->
                            <el-col :span="5" v-for="index in 6" :key="index" :offset="2">
                                <router-link :to="'/index/detail/'+click_list[index].id" style="text-decoration: none">

                                    <el-card :body-style="{ padding: '0px' }" style="width: 180px">
                                        <img :src="click_list[index].book_img.replace('http://127.0.0.1:8000/media/http%3A','http:/')"
                                             class="image">
                                        <div style="padding: 14px;">
                                            <div style="height: 30px">
                                                <span class="myhover">{{click_list[index].name}}</span>
                                            </div>
                                            <div class="bottom clearfix" style="height: 30px">
                                                <time class="time">{{ click_list[index].desc }}</time>
                                                <!--                                            <el-button type="text" class="button">操作按钮</el-button>-->
                                            </div>
                                        </div>
                                    </el-card>
                                </router-link>
                                <br>
                            </el-col>
                        </el-row>

                    </div>
                </el-col>

                <el-col :span="7" :offset="1">
                    <div class="grid-content bg-purple">
                        <el-card class="box-card">
                            <div slot="header" class="clearfix">

                                <span> <h2><b>点击榜单</b></h2></span>
                                <!--                                <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>-->
                            </div>
                            <div v-for=" book,o in click_list" :key="o" class="text item">
                                <div v-if="o==0">
                                    <router-link :to="'/index/detail/'+book.id" style="text-decoration: none">
                                        <span><i
                                                style="background: #ff7b00;color: floralwhite; height: 20px;width: 20px">&nbsp;{{o+1}}&nbsp;</i><span
                                                class="myhover"> {{book.name}}</span></span>
                                        <div>
                                            <div class="row">
                                                <br>
                                                <div class="col-lg-3 col-lg-offset-1">
                                                    <img height="80px"
                                                         :src="book.book_img.replace('http://127.0.0.1:8000/media/http%3A','http:/')"
                                                         alt="">
                                                </div>
                                                <div class="col-lg-8">
                                                    <span class="myhover">{{book.desc}}</span>
                                                </div>
                                            </div>
                                        </div>
                                    </router-link>
                                    <br>
                                </div>

                                <div v-else-if="o==1">
                                    <div>
                                        <router-link :to="'/index/detail/'+book.id" style="text-decoration: none">
                                        <span class="myhover"><i
                                                style="background: #ffa92e;color: floralwhite; height: 20px;width: 20px">&nbsp;{{o+1}}&nbsp;</i>  {{book.name}}</span>
                                        </router-link>
                                    </div>
                                    <br>
                                </div>
                                <div v-else-if="o==2">
                                    <div>
                                        <router-link :to="'/index/detail/'+book.id" style="text-decoration: none">
                                        <span class="myhover"><i
                                                style="background: #ffd66c;color: floralwhite; height: 20px;width: 20px">&nbsp;{{o+1}}&nbsp;</i> {{book.name}}</span>
                                        </router-link>
                                    </div>
                                    <br>
                                </div>
                                <div v-else>
                                    <div>
                                        <div>
                                            <router-link :to="'/index/detail/'+book.id" style="text-decoration: none">
                                        <span class="myhover"><i
                                                style="background: #90887d;color: floralwhite; height: 20px;width: 20px">&nbsp;{{o+1}}&nbsp;</i>  {{book.name}}</span>
                                            </router-link>
                                        </div>
                                    </div>
                                    <br>
                                </div>
                                <!--                                <span v-if="o=1">{{'列表内容 ' + o }}</span>-->
                                <!--                                <span v-else>{{'列表内容 ' + o }}</span>-->
                            </div>
                        </el-card>
                    </div>
                </el-col>
            </el-row>

            <!--            第三行-->
            <el-row :gutter="20">

                <el-col :span="16">
                    <h2><b>精品推荐</b></h2>
                    <br>
                    <div class="grid-content bg-purple">
                        <el-row>
                            <!--                            <el-col :span="5" v-for="(o, index) in 3" :key="o" :offset="index > 0 ? 2 : 0">-->
                            <el-col :span="5" v-for="index in 6" :key="index" :offset="2">
                                <router-link :to="'/index/detail/'+zhangjie_list[index].id"
                                             style="text-decoration: none">
                                    <el-card :body-style="{ padding: '0px' }" style="width: 180px">
                                        <img :src="zhangjie_list[index].book_img.replace('http://127.0.0.1:8000/media/http%3A','http:/')"
                                             class="image">
                                        <div style="padding: 14px;">
                                            <div style="height: 30px">
                                                <span class="myhover">{{zhangjie_list[index].name}}</span>
                                            </div>
                                            <div class="bottom clearfix" style="height: 35px">
                                                <time class="time">{{ zhangjie_list[index].desc }}</time>
                                                <!--                                            <el-button type="text" class="button">操作按钮</el-button>-->
                                            </div>
                                        </div>
                                    </el-card>
                                    <br>
                                </router-link>
                            </el-col>
                        </el-row>

                    </div>
                </el-col>

                <el-col :span="7" :offset="1">
                    <div class="grid-content bg-purple">
                        <el-card class="box-card">
                            <div slot="header" class="clearfix">
                                <span> <h2><b>达人榜单</b></h2></span>
                                <!--                                <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>-->
                            </div>
                            <div v-for=" book,o in zhangjie_list" :key="o" class="text item">
                                <div v-if="o==0">
                                    <router-link :to="'/index/detail/'+book.id" style="text-decoration: none">
                                        <span class="myhover"><i
                                                style="background: #ff7b00;color: floralwhite; height: 20px;width: 20px">&nbsp;{{o+1}}&nbsp;</i>  {{book.name}}</span>
                                        <div>
                                            <div class="row">
                                                <br>
                                                <div class="col-lg-3 col-lg-offset-1">
                                                    <img height="80px"
                                                         :src="book.book_img.replace('http://127.0.0.1:8000/media/http%3A','http:/')"
                                                         alt="">
                                                </div>
                                                <div class="col-lg-8">
                                                    <span class="myhover">{{book.desc}}</span>
                                                </div>
                                            </div>
                                        </div>
                                        <br>
                                    </router-link>
                                </div>

                                <div v-else-if="o==1">
                                    <router-link :to="'/index/detail/'+book.id" style="text-decoration: none">

                                        <div>
                                        <span class="myhover"><i
                                                style="background: #ffa92e;color: floralwhite; height: 20px;width: 20px">&nbsp;{{o+1}}&nbsp;</i>  {{book.name}}</span>

                                        </div>
                                        <br>
                                    </router-link>
                                </div>
                                <div v-else-if="o==2">
                                    <router-link :to="'/index/detail/'+book.id" style="text-decoration: none">

                                        <div>
                                        <span class="myhover"><i
                                                style="background: #ffd66c;color: floralwhite; height: 20px;width: 20px">&nbsp;{{o+1}}&nbsp;</i>  {{book.name}}</span>

                                        </div>
                                        <br>
                                    </router-link>
                                </div>
                                <div v-else>
                                    <router-link :to="'/index/detail/'+book.id" style="text-decoration: none">

                                        <div>
                                            <div>
                                        <span class="myhover"><i
                                                style="background: #90887d;color: floralwhite; height: 20px;width: 20px">&nbsp;{{o+1}}&nbsp;</i>  {{book.name}}</span>

                                            </div>
                                        </div>
                                        <br>
                                    </router-link>
                                </div>
                                <!--                                <span v-if="o=1">{{'列表内容 ' + o }}</span>-->
                                <!--                                <span v-else>{{'列表内容 ' + o }}</span>-->
                            </div>
                        </el-card>
                    </div>
                </el-col>
            </el-row>

            <!--            第四行-->
            <el-row :gutter="20">

                <el-col :span="16">
                    <h2><b>最近更新</b></h2>
                    <br>
                    <div class="grid-content bg-purple">
                        <el-row>
                            <!--                            <el-col :span="5" v-for="(o, index) in 3" :key="o" :offset="index > 0 ? 2 : 0">-->
                            <!--                            这是更新版本内容-->
                            <div class="text-center">
                                <table class="table table-hover table-striped">
                                    <thead>
                                    <tr>
                                        <!--                                        <td><b>排名</b></td>-->
                                        <td><b>分类</b></td>
                                        <td><b>书名</b></td>

                                        <td><b>作者</b></td>
                                        <td><b>更新时间</b></td>
                                    </tr>
                                    </thead>
                                    <tbody>
                                    <tr v-for="book,index in gengxin_list" style="color: grey">
                                        <!--                                        <td v-if="index==0" class="center-block rank"><i-->
                                        <!--                                                style="background: #ff7b00;color: floralwhite">&nbsp;{{index+1}}&nbsp;</i>-->
                                        <!--                                        </td>-->
                                        <!--                                        <td v-else-if="index==1" class="center-block rank"><i-->
                                        <!--                                                style="background: #ffa92e;color: floralwhite">&nbsp;{{index+1}}&nbsp;</i>-->
                                        <!--                                        </td>-->
                                        <!--                                        <td v-else-if="index==2" class="center-block rank"><i-->
                                        <!--                                                style="background: #ffd66c;color: floralwhite">&nbsp;{{index+1}}&nbsp;</i>-->
                                        <!--                                        </td>-->
                                        <!--                                        <td v-else class="center-block rank"><i-->
                                        <!--                                                style="background: #90887d;color: floralwhite">&nbsp;{{index+1}}&nbsp;</i>-->
                                        <!--                                        </td>-->
                                        <td>
                                            <router-link :to="'/index/detail/'+book.id" style="text-decoration: none">

                                                <span class="myhover">[{{book.tag.name}}]</span>
                                            </router-link>
                                        </td>
                                        <td>
                                            <router-link :to="'/index/detail/'+book.id" style="text-decoration: none">

                                                <span class="myhover">{{book.name}}</span>
                                            </router-link>
                                        </td>
                                        <td>{{book.author.name}}</td>
                                        <td>{{book.create_time| dateFormat }}</td>

                                    </tr>
                                    </tbody>
                                </table>
                            </div>

                        </el-row>

                    </div>
                </el-col>

                <el-col :span="7" :offset="1">
                    <div class="grid-content bg-purple">
                        <el-card class="box-card">
                            <div slot="header" class="clearfix">
                                <span> <h2><b>更新榜单</b></h2></span>
                                <!--                                <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>-->
                            </div>
                            <div v-for=" book,o in zhangjie_a " :key="o" class="text item">

                                <div v-if="o==0">
                                    <router-link :to="'/index/detail/'+book.id" style="text-decoration: none">

                                        <span class="myhover"><i
                                                style="background: #ff7b00;color: floralwhite; height: 20px;width: 20px">&nbsp;{{o+1}}&nbsp;</i>  {{book.name}}</span>
                                        <div>
                                            <div class="row">
                                                <br>
                                                <div class="col-lg-3 col-lg-offset-1">
                                                    <img height="80px"
                                                         :src="book.book_img.replace('http://127.0.0.1:8000/media/http%3A','http:/')"
                                                         alt="">
                                                </div>
                                                <div class="col-lg-8">
                                                    <span class="myhover">{{book.desc}}</span>
                                                </div>

                                            </div>
                                        </div>
                                        <br>
                                    </router-link>
                                </div>

                                <div v-else-if="o==1">
                                    <router-link :to="'/index/detail/'+book.id" style="text-decoration: none">

                                        <div>
                                        <span class="myhover"><i
                                                style="background: #ffa92e;color: floralwhite; height: 20px;width: 20px">&nbsp;{{o+1}}&nbsp;</i>  {{book.name}}</span>

                                        </div>
                                        <br>
                                    </router-link>
                                </div>
                                <div v-else-if="o==2">
                                    <router-link :to="'/index/detail/'+book.id" style="text-decoration: none">

                                        <div>
                                        <span class="myhover"><i
                                                style="background: #ffd66c;color: floralwhite; height: 20px;width: 20px">&nbsp;{{o+1}}&nbsp;</i>  {{book.name}}</span>

                                        </div>
                                        <br>
                                    </router-link>
                                </div>
                                <div v-else>
                                    <router-link :to="'/index/detail/'+book.id" style="text-decoration: none">

                                        <div>
                                            <div>
                                        <span class="myhover"><i
                                                style="background: #90887d;color: floralwhite; height: 20px;width: 20px">&nbsp;{{o+1}}&nbsp;</i>  {{book.name}}</span>

                                            </div>
                                        </div>
                                        <br>
                                    </router-link>
                                </div>
                                <!--                                <span v-if="o=1">{{'列表内容 ' + o }}</span>-->
                                <!--                                <span v-else>{{'列表内容 ' + o }}</span>-->
                            </div>
                        </el-card>
                    </div>
                </el-col>
            </el-row>

        </div>
        <!--<img height="50px" width="50px" src="http://static.zongheng.com/upload/recommend/5a/db/5adb754532b692993f82b4f2a0dca353.jpeg" alt="">-->
        <br>
        <br>
        <br>
        <!--        <button class="btn btn-success">??????</button>-->
        <Footer/>
    </div>
</template>

<script>


    import Header from '../components/Header'
    import Footer from '../components/Footer'
    import Navigator from '../components/Navigator'


    export default {
        name: 'Home',
        data() {
            return {
                currentDate: new Date(),
                lunboheight: 50,
                zhangjie_a: '',
                zhangjie_list: '',
                gengxin_list: '',
                click_list: '',
                banner_list: '',

            };
        },
        methods: {
            _get_banner() {
                this.$http.get(this.$settings.base_url + '/api/home/banner').then(
                    response => {
                        if (response.data.code === 100) {
                            // console.log(response.data.data)
                            this.banner_list = response.data.data
                          // console.log(this.banner_list)
                        } else {
                            this.$message({
                                message: "获取轮播图信息有误，请联系客服工作人员"
                            })
                        }
                    }
                ).catch(() => {
                    this.$message({
                        message: "获取轮播图信息有误，请联系客服工作人员"
                    })
                })

            }
        },

        created() {
            this._get_banner();

            this.$http.get(this.$settings.base_url + '/api/home/allbook/', {
                params: {
                    ordering: '-create_time'
                }
            }).then(res => {
                // console.log(res.data)
                this.zhangjie_a = res.data.results
            })

            this.$http.get(this.$settings.base_url + '/api/home/allbook/?ordering=' + 'zhangjie').then(res => {
                // console.log(res.data.results)
                this.zhangjie_list = res.data.results
            })
            this.$http.get(this.$settings.base_url + '/api/home/allbook/?ordering=' + '-create_time&page_size=20').then(res => {
                // console.log(res.data.results)
                this.gengxin_list = res.data.results
            })
            this.$http.get(this.$settings.base_url + '/api/home/allbook/?ordering=' + '-click_num').then(res => {
                // console.log(res.data.results)
                this.click_list = res.data.results
            })
        },
        components: {
            Header,
            Footer,
            Navigator
        },

    }
</script>

<style>
    .time {
        font-size: 13px;
        color: #999;
    }

    .bottom {
        margin-top: 13px;
        line-height: 12px;
    }

    .button {
        padding: 0;
        float: right;
    }

    .image {
        width: 100%;
        display: block;
    }

    .clearfix:before,
    .clearfix:after {
        display: table;
        content: "";
    }

    .clearfix:after {
        clear: both
    }

    .el-row {
        margin-bottom: 20px;
    }

    :last-child {
        margin-bottom: 0;
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

    .el-carousel__item h3 {
        color: #475669;
        font-size: 14px;
        opacity: 0.75;
        line-height: 200px;
        margin: 0;
    }

    .el-carousel__item:nth-child(2n) {
        /*background-color: #99a9bf;*/
    }

    .el-carousel__item:nth-child(2n+1) {
        /*background-color: #d3dce6;*/
    }

    .myhover:hover {
        color: #ff7b00;
    }

    .myhover {
        color: #7c7c7c;
    }
</style>