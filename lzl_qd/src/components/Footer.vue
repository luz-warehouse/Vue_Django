<template>
  <div class="foot-container">
    <p class="site-nav">
      <span class="link-to"><router-link to="/index/about">手机站</router-link></span><c-divider></c-divider>
      <span class="link-to"><router-link to="/">网站首页</router-link></span><c-divider></c-divider>
      <!-- <span class="link-to"><router-link to="/index/about">关于我们</router-link></span><c-divider></c-divider>
      <span class="link-to"><router-link to="/index/about">联系我们</router-link></span><c-divider></c-divider> -->
      <span class="link-to"><router-link to="/index/user/feedback">反馈留言</router-link></span><c-divider></c-divider>
      <span class="link-to"><router-link to="/index/author">作家专区</router-link></span>
    </p>
    <p class="copyright-notice">Copyright (C) www.ulane.top All rights reserved 小说精品屋版权所有</p>
  </div>
</template>

<script>
import cDivider from './Divider.vue';

export default {
  components:{
    cDivider
  }
}
</script>

<style lang='scss' scoped>
.foot-container{
  // background-color: #F5F5F5;
  padding-bottom: 20px;
  .site-nav, .site-nav a {
    // margin-top: 0;
    text-align: center;
    font-size: 12px;
    color: #666;
    .link-to {
      margin: 0 15px;
    }
  }
  .site-nav a:hover{
    color: #FF8800;
  }

  .copyright-notice {
    font-size: 12px;
    text-align: center;
    color: #999;
  }
}
</style>