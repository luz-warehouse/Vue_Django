<template>
    <div>

        <br>
    <form class="recharge-form" :action="global.baseURL+'/pay/aliPay'" method="post" ref="payform">
        <input v-model="payAmount" type="hidden" name="payAmount"/>
        <p class="amount-cont">
            充值金额：<span class="amount-show">{{payAmount}}</span>元
            (<span class="amount-show">{{payGold}}</span>屋币)
            <span class="amount-sure" @click="go()">确定</span>
        </p>
    </form>
         <Footer/>
        </div>
</template>

<script>


    import Header from '../components/Header'
    import Footer from '../components/Footer'
    import Navigator from '../components/Navigator'

    export default {
        data() {
            return {
                payAmount: this.$route.query.payAmount,
                payGold: this.$route.query.gold
            }
        },
        created() {

        },
        components: {
            Header,
            Footer,
            Navigator
        },

        methods: {
            go() {
                this.$refs.payform.submit();
            }
        }
    }
</script>

<style lang='scss' scoped>
    .recharge-form {
        background-color: #fff;
        margin: 20px auto;
        width: 80%;
        height: 100px;
        // input {

        // }
        .amount-cont {
            text-align: center;
            position: relative;
            top: 50%;
            transform: translateY(-50%);
            font-size: 20px;

            .amount-show {
                display: inline-block;
                color: #ff7b00;
                margin-right: 5px;
            }

            .amount-sure {
                margin-left: 20px;
                display: inline-block;
                font-size: 18px;
                width: 50px;
                cursor: pointer;
                border-radius: 5px;
                color: #fff;
                background-color: #ff7b00;
            }
        }
    }
</style>