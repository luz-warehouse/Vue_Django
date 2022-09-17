<template>
    <div>
        <Header></Header>
        <Navigator></Navigator>
        <div class="container">
            <div class="row">
                <div class="col-lg-offset-2 col-lg-8 text-center">

                    <el-steps :active="active" finish-status="success" simple style="margin-top: 20px">
                        <el-step title="步骤 1">
                        </el-step>
                        <el-step title="步骤 2"></el-step>
                        <el-step title="步骤 3"></el-step>
                    </el-steps>

                    <el-row v-if="active == 0" style="margin-top: 33px">
                        <h5>您的邮箱注册邮箱:</h5>
                        <el-col :span="6" :offset="9" style="margin-top: 30px">
                            <el-input
                                    placeholder="请输入邮箱"
                                    prefix-icon="el-icon-s-comment"
                                    v-model="result.email"
                                    clearable>
                            </el-input>
                            <br>
                            <br>
                            <br>
                            <!--                            <el-button style="width:100%" @click="send_email_pwd" type="success">-->
                            <el-button style="margin-top: 12px;" @click="next">发送验证邮件</el-button>
                            <br>
                            <br>
                            <br>
                        </el-col>


                    </el-row>

                    <el-row v-if="active == 1" style="margin-top: 33px">
                        <h5>请输入你收到的验证码</h5>
                        <el-col :span="6" :offset="9" style="margin-top: 30px">
                            <el-input
                                    placeholder="请输入验证码"
                                    prefix-icon="el-icon-s-comment"
                                    v-model="result.code"
                                    clearable>
                            </el-input>
                            <br>
                            <br>
                            <br>
                            <!--                            <el-button style="width:100%" @click="send_email_pwd" type="success">-->
                            <el-button style="margin-top: 12px;" @click="next">下一步</el-button>
                            <br>
                            <br>
                            <br>
                        </el-col>

                    </el-row>

                    <el-row v-if="active == 2" style="margin-top: 33px">
                        <h5>请输入新的密码</h5>
                        <el-col :span="6" :offset="9" style="margin-top: 30px">
                            <el-input
                                    placeholder="请输入新密码"
                                    prefix-icon="el-icon-s-comment"
                                    v-model="result.newpwd"
                                    clearable
                                    show-password>
                            </el-input>
                            <br>
                            <br>
                            <el-input
                                    placeholder="请再次确认密码"
                                    prefix-icon="el-icon-s-comment"
                                    v-model="result.repwd"
                                    clearable
                                    show-password>
                            </el-input>
                            <br>
                            <br>
                            <br>
                            <!--                            <el-button style="width:100%" @click="send_email_pwd" type="success">-->
                            <el-button style="margin-top: 12px;" @click="next">下一步</el-button>
                            <br>
                            <br>
                            <br>
                        </el-col>

                    </el-row>

                    <br>
                    <br>
                    <br>


                </div>
            </div>
        </div>
        <Footer></Footer>
    </div>
</template>

<script>
    import Header from './Header'
    import Footer from '../components/Footer'
    import Navigator from '../components/Navigator'

    export default {
        name: "Reset_pwd",
        components: {
            Header,
            Footer,
            Navigator
        },
        data() {

            return {

                active: 0,
                result: {
                    email:'',
                    code: '',
                    newpwd: '',
                    repwd: ''
                }
            };
        },
        methods: {
            next() {
                // if (this.active++ > 2) this.active = 0;
                // console.log(this.active)

                // 第一步判断邮箱
                if (this.active == 0) {
                    // console.log('1')
                    this.$http.post(this.$settings.base_url + '/api/user/email_pwd/', this.result).then(res => {
                        if (res.data.code == 100) {

                            console.log(this.active)
                            // if (this.active++ > 2) this.active = 0;
                            this.active++
                            console.log(this.active)
                        } else {
                            this.$message(res.data.msg)
                        }

                    })

                }

                // 第二步判断验证码
                if (this.active == 1) {
                    if (this.result.code) {
                        this.$http.post(this.$settings.base_url + '/api/user/check_code/', this.result).then(res => {
                            if (res.data.code == 100) {
                                // if (this.active++ > 2) this.active = 0;
                                // console.log(this.active)
                                this.active++
                                // console.log(this.active)

                            } else {
                                this.$message(res.data.msg)
                            }
                        })
                    } else {
                        this.$message('请输入验证码，再继续下一步校验')
                    }
                }

                if (this.active == 2){
                    if ( !this.result.newpwd ){
                        this.$message('新密码不能为空')
                    }else if(!this.result.repwd){
                         this.$message('确认密码不能为空')
                    }else if(this.result.newpwd != this.result.repwd){
                        this.$message('两次密码不一致')
                    }else{
                        this.$http.post(this.$settings.base_url + '/api/user/eamil_edit_pwd/',this.result).then(res=>{
                            if(res.data.code == 100){
                                // this.$emit('go')
                                // this.$router.push('/')
                              this.$message({
                                type:"success",
                                message:'密码修改成功！'
                              })
                                this.$router.push('/')

                            }else{
                                this.$message(res.data.msg)
                            }
                        })
                    }

                }

            }
        }
    }


</script>

<style scoped>

</style>