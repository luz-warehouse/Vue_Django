<template>

    <div class="row">
        <div class="col-lg-10 col-lg-offset-1">
            <el-card class="box-card">
                <div slot="header" class="clearfix">
                    <h3>所有目录</h3>
                </div>

                <div>
                    <el-row :gutter="20" class="text-center">

                        <el-col :span="6" style="width: 33%" v-for=" obj,index in zhangjie_list.bookzj ">

                            <router-link :to="'/index/detail/'+ zhangjie_list.id + '/' + obj.id"
                                         style="text-decoration: none">
                                <div class="grid-content bg-purple"><span class="hovera">{{obj.name}}</span></div>
                            </router-link>

                        </el-col>

                    </el-row>
                </div>

            </el-card>
        </div>

    </div>

</template>

<script>
    export default {
        name: "Zhangjie",
        watch: {
            '$route.params.pk': function () {
                console.log(this.$route.params.pk)
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
                    // console.log(res.data)
                    this.zhangjie_list = res.data
                    // console.log(res.data)
                })
            }
        },
        mounted() {
            this.pk = this.$route.params.pk
            this.get_data()

        },
        data() {
            return {
                zhangjie_list: '',
                pk: ''
            }
        }

    }
</script>

<style scoped>
    .hovera:hover {
        color: #ff7b00
    }

    .el-row {
        margin-bottom: 30px;

    }

    .el-col {
        border-radius: 5px;
    }

    .bg-purple-dark {
        /*background: #99a9bf;*/
    }

    .bg-purple {
        /*background: #d3dce6;*/
    }

    .bg-purple-light {
        background: #e5e9f2;
    }

    .grid-content {
        border-radius: 4px;
        min-height: 40px;
    }

    .row-bg {
        padding: 20px 0;
        background-color: #f9fafc;
    }
</style>