<template>
  <div class="navigator">
    <router-link class="router-to" to='/index/home'>首页</router-link>
    <router-link class="router-to" to='/allBook'>全部书籍</router-link>
    <router-link class="router-to" to='/index/ranked'>排行榜</router-link>
    <router-link class="router-to" to='/index/recharge'>充值</router-link>
     <router-link class="router-to" to='/index/author'>作家专区</router-link>
  </div>
</template>

<script>
export default {
  data(){
    return {
    }
  },
  components: {
  }
}
</script>

<style lang='scss' scoped>

.navigator {
  height: 50px;
  padding-left: 15%;
  background-color: #FF8800;
  line-height: 50px;

  .nav-place{
    opacity: 0;
    display: inline-block;
    height: 100%;
    width: 15%;
  }

}

.navigator a:hover{
  color: #fff;
}

.router-to {
  display: inline-block;
  margin-right: 70px;
  height: 46px;
  font-size: 17px;
  color: #fff;
  text-decoration: none;
}

.router-link-active{
  border: 1px solid #fff;
  border-width: 0 0 2px 0;
}

</style>