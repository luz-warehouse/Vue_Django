<template>
    <div class="register">
        <div class="box">
            <i class="el-icon-close" @click="close_register"></i>
            <div class="content">
                <div class="nav">
                    <span class="active">新用户注册</span>
                </div>
                <el-form>
                    <el-input
                            placeholder="用户名(非必填)"
                            prefix-icon="el-icon-user-solid"
                            v-model="username"
                            clearable
                            @blur="check_username">
                    </el-input>
                    <el-input
                            placeholder="手机号"
                            prefix-icon="el-icon-phone-outline"
                            v-model="mobile"
                            clearable
                            @blur="check_mobile">
                    </el-input>
                    <el-input
                            placeholder="邮箱"
                            prefix-icon="el-icon-platform-eleme"
                            v-model="email"
                            clearable
                            @blur="check_email">
                    </el-input>
                    <el-input
                            placeholder="密码"
                            prefix-icon="el-icon-key"
                            v-model="password"
                            clearable
                            show-password>
                    </el-input>
                    <el-input
                            placeholder="验证码"
                            prefix-icon="el-icon-chat-line-round"
                            v-model="sms"
                            clearable>
                        <template slot="append">
                            <span class="sms" @click="send_sms">{{ sms_interval }}</span>
                        </template>
                    </el-input>
                    <el-button type="primary" @click="register">注册</el-button>
                </el-form>
                <div class="foot">
                    <span @click="go_login">立即登录</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Register",
        data() {
            return {
                mobile: '',
                password: '',
                sms: '',
                sms_interval: '获取验证码',
                is_send: false,
                email: '',
                username: ''
            }
        },
        methods: {
            // 校验用户名是否存在
            check_username() {
                if (this.username) {
                    this.$http.post(this.$settings.base_url + '/api/user/check_username/', {username: this.username}).then(res => {
                        if (res.data.code != 100) {
                            this.username = ''
                            this.$message(res.data.msg)
                        }
                    })
                }

            },
            check_email() {
                if (this.email) {
                    this.$http.post(this.$settings.base_url + '/api/user/check_email/',{email:this.email}).then(res=>{
                        if (res.data.code!=100){
                            this.email = ''
                            this.$message(res.data.msg)
                        }
                    })
                }
            },
            close_register() {
                this.$emit('close', false)
            },
            go_login() {
                this.$emit('go')
            },
            check_mobile() {
                if (!this.mobile) return;
                if (!this.mobile.match(/^1[3-9][0-9]{9}$/)) {
                    this.$message({
                        message: '手机号有误',
                        type: 'warning',
                        duration: 1000,
                        onClose: () => {
                            this.mobile = '';
                        }
                    });
                    return false;
                }
                //校验手机号是否注册过，如果注册过，就不能再发短信了
                this.$http.get(this.$settings.base_url + '/api/user/check_mobile/?mobile=' + this.mobile).then(res => {
                    if (res.data.code == 100 && res.data.exisit) {
                        this.$message('该手机号已经注册，请先去直接登录')
                        // this.mobile=''
                        this.$emit('go')
                    } else {
                        this.is_send = true;

                    }
                })

            },
            send_sms() {
                if (!this.is_send) return;
                this.is_send = false;
                let sms_interval_time = 60;
                this.sms_interval = "发送中...";
                let timer = setInterval(() => {
                    if (sms_interval_time <= 1) {
                        clearInterval(timer);
                        this.sms_interval = "获取验证码";
                        this.is_send = true; // 重新回复点击发送功能的条件
                    } else {
                        sms_interval_time -= 1;
                        this.sms_interval = `${sms_interval_time}秒后再发`;
                    }
                }, 1000);
                // 发送请求，获取验证码
                this.$http.get(this.$settings.base_url + '/api/user/send_sms/?mobile=' + this.mobile).then(res => {
                    this.$message(res.data.msg)
                })
            },
            register() {
                // if (!this.email) {
                //     this.$message('邮箱不能为空')
                // }
                if (this.mobile && this.sms && this.password && this.email) {

                    this.$http.post(this.$settings.base_url + '/api/user/register/', {
                        mobile: this.mobile,
                        code: this.sms,
                        password: this.password,
                        email:this.email,
                        username:this.username
                    }).then(res => {
                        if (res.data.code == 100) {
                            this.$message('恭喜你,注册成功')
                            //跳转到登录页面
                            this.$emit('go')

                        } else {
                            this.$message({
                                message: res.data.msg[0],
                                type: 'error'
                            })
                        }
                    })

                } else {
                    this.$message({
                        message: '邮箱、手机号、验证码都不能为空',
                        type: 'warning'
                    })
                }
            }
        }
    }
</script>

<style scoped>
    .register {
        width: 100vw;
        height: 100vh;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 10;
        background-color: rgba(0, 0, 0, 0.3);
    }

    .box {
        width: 400px;
        height: 480px;
        background-color: white;
        border-radius: 10px;
        position: relative;
        top: calc(50vh - 240px);
        left: calc(50vw - 200px);
    }

    .el-icon-close {
        position: absolute;
        font-weight: bold;
        font-size: 20px;
        top: 10px;
        right: 10px;
        cursor: pointer;
    }

    .el-icon-close:hover {
        color: darkred;
    }

    .content {
        position: absolute;
        top: 40px;
        width: 280px;
        left: 60px;
    }

    .nav {
        font-size: 20px;
        height: 38px;
        border-bottom: 2px solid darkgrey;
    }

    .nav > span {
        margin-left: 90px;
        color: darkgrey;
        user-select: none;
        cursor: pointer;
        padding-bottom: 10px;
        border-bottom: 2px solid darkgrey;
    }

    .nav > span.active {
        color: black;
        border-bottom: 3px solid black;
        padding-bottom: 9px;
    }

    .el-input, .el-button {
        margin-top: 15px;
    }

    .el-button {
        width: 100%;
        font-size: 18px;
    }

    .foot > span {
        float: right;
        margin-top: 20px;
        color: orange;
        cursor: pointer;
    }

    .sms {
        color: orange;
        cursor: pointer;
        display: inline-block;
        width: 70px;
        text-align: center;
        user-select: none;
    }
</style>