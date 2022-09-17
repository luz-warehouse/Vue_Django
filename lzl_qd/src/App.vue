<template>
  <div id="app">
        <router-view/>
  </div>
</template>

<style lang='scss'>
html, body{
  margin: 0;
  padding: 0;
  font-size: 14px;
    background:#fff;
}
p {
  margin: 10px 0;
}
a {
  color: #333;
  text-decoration: none;
}
a:hover {
  color: #FF8800;
}
.el-pagination{
  text-align: center!important;
}
.el-pager li.active{
  background-color:#FF8800!important;
}
.hidden{
  display: none;
}
</style>