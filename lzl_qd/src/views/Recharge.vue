<template>
    <div>

        <Header></Header>
        <Navigator></Navigator>

        <div class="user-recharge">
            <div class="recharge-user">
                <span class="title">充值账号：</span>
                <span class="nickname">{{ userInfo.nickname }}</span>
                <span class="title">余额：</span>
                <span class="balace">{{ userInfo.coin }}</span>屋币
            </div>
            <div class="recharge-type">
                <p class="title">选择充值方式</p>
                <div :class="['pay-box', payType==0?'pay-box-on':'']" @click="changePayType(0)">
                    <img src="../assets/img/pay_zfb.png" alt="" class="alipay-img">
                </div>
                <div :class="['pay-box', payType==1?'pay-box-on':'']" @click="changePayType(1)">
                    <img src="../assets/img/pay_wx.png" alt="" class="wechatpay-img">
                </div>
            </div>
            <div class="recharte-amount">
                <p class="amount-title">选择充值金额</p>

                <div class="amount-select">
                    <div class="amount-item" v-for="item in rechargeList" :key="item.rmb" @click="goPay(item)">
                        <p class="amount-rmb">{{ item.rmb }}元</p>
                        <p class="amount-gold">{{ item.rmb * proportion }}屋币</p>
                    </div>
                </div>

                <p class="amount-proportion">当前比例：1元={{ proportion }}屋币</p>

            </div>
            <div class="hint">
                <p class="title">温馨提示</p>
                <p class="hint-item">1. 充值阅读权限仅限本书城使用</p>
                <p class="hint-item">2. 充值支持支付宝、微信支付</p>
                <p class="hint-item">3. 若充值遇到问题，
                    <router-link to="/index/user/feedback" class="feed-back">点此留言</router-link>
                </p>
            </div>
        </div>
        <Footer></Footer>
    </div>
</template>

<script>

    import Header from '../components/Header'
    import Footer from '../components/Footer'
    import Navigator from '../components/Navigator'


    export default {
      name:'Recharge',
      data() {
        return {
          userInfo: '',
          proportion: 100,
          rechargeList: [
            {rmb: 10},
            {rmb: 50},
            {rmb: 100},
            {rmb: 200},
            {rmb: 500},
            {rmb: 1000},
          ],
          payType: 0, //0-alipay 1-wechatpay
        }
      },
      created() {
        this.getUserInfo();
      },
      components: {
        // cCommentList, cAuthorShow
        Header,
        Footer,
        Navigator,
      },
      methods: {

        getUserInfo(){
          let userid = this.$cookies.get('userid');
          this.$http.get(this.$settings.base_url+'/api/user/super/'+userid+'/').then(response=>{
            console.log(response.data)
            this.userInfo = response.data
          })

        },

        changePayType(payType) {
          if (payType == this.payType) {
            return;
          }
          if (payType != 0) {
            this.$message('功能即将上线');
            return;
          }
          this.payType = payType;
        },
        goPay(item) {
          if (this.payType == 0) {
            //alipay
            // this.$http.postForm('/pay/aliPay', {payAmount:item.rmb}, res=>{
            //   console.log(res);
            // })
            // window.open(this.$router.resolve('/index/rechargeForm?payAmount=' + item.rmb + '&gold=' + item.rmb * this.proportion).href, '_blank');
            let token = this.$cookies.get('token');
            let userid = this.$cookies.get('userid');
            if (token) {
              this.$http.put(`${this.$settings.base_url}/api/user/setcoin/` + userid +'/', {
                'coin': item.rmb * this.proportion,
              }, {
                headers: {
                  'Authorization': token
                }
              }).then(res => {
                if (res.data.code === 100) {
                  //打开一个新连接，支付
                  open(res.data.pay_url, '_self')
                } else {
                  this.$message({
                    message: res.data.msg
                  });
                }
              })
            } else {
              this.$message({
                message: "您没有登录，请先登录"
              });
            }
          }
        }
      }
    }





</script>

<style lang='scss' scoped>
    .user-recharge {
        width: 70%;
        margin: 20px auto;
        background-color: #fff;
        border-radius: 10px;
        padding: 40px;

        .recharge-user {
            border: 1px solid #EAEAEA;
            border-width: 0 0 1px 0;
            font-size: 16px;
            height: 40px;
            // .title {

            // }
            .nickname {
                margin-right: 30px;
            }

            .balace {
                color: #ff7b00;
            }
        }

        .recharge-type {
            .title {
                margin: 30px 0 0 0;
                font-size: 16px;
            }

            .pay-box {
                cursor: pointer;
                display: inline-block;
                margin: 20px 20px 0 0;
                width: 200px;
                /*height: 80px;*/
                line-height: 80px;
                text-align: center;
                border: 2px solid #eee;
                border-radius: 5px;

                .alipay-img {
                    vertical-align: middle;
                }

                .wechatpay-img {
                    vertical-align: middle;
                }
            }

            .pay-box-on {
                border-color: #ff7b00;
            }
        }

        .recharte-amount {
            border: 1px solid #eaeaea;
            border-width: 0 0 1px 0;

            .amount-title {
                margin: 30px 0 0 0;
                font-size: 16px;
            }

            .amount-select {
                display: flex;
                flex-wrap: wrap;

                .amount-item {
                    //只有在设置比例后单一需要固定的元素才需要
                    /*flex-shrink: 0;*/
                    cursor: pointer;
                    border: 2px solid #eee;
                    border-radius: 5px;
                    text-align: center;
                    margin: 20px 20px 0 0;
                    width: 200px;
                    height: 90px;
                    padding: 10px 0;

                    .amount-rmb {
                        margin: 0;
                        font-size: 20px;
                        font-weight: bold;
                        line-height: 40px;
                    }

                    .amount-gold {
                        margin: 0;
                        line-height: 30px;
                    }
                }

                .amount-item:hover {
                    border-color: #ff7b00;
                }
            }

            .amount-proportion {
                margin: 30px 0 20px 0;
            }
        }

        .hint {
            color: #999999;

            .title {
                margin-top: 20px;
                font-weight: bold;
            }

            .hint-item {
                .feed-back {
                    color: #999999;
                    text-decoration: underline;
                }
            }
        }
    }
</style>