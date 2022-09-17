import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Password from "../components/Reset_pwd";
import Allbook from "../views/allbook";
import order from "../components/bookorder"
import Detail from "../views/BookShow"
import Personage from "../views/personage"
import ZJdetail from "../views/zhangjiedetail"
import zhangjiedetail from "../views/zhangjiedetail";
import Recharge from "../views/Recharge";
import PaySuccess from '../views/pay_success'
import test1 from "../components/test1";

Vue.use(VueRouter)

const routes = [
    {
        path: '/text',
        name: 'test1',
        component: test1,
        // redirect: '/index/home'
    },
    {
        path: '/',
        name: 'Home',
        component: Home,
        // redirect: '/index/home'
    },
    {
        path: '/index/detail/:pk/:id',
        name: 'zhangjie',
        component: zhangjiedetail,
        // redirect: '/index/home'
    },
    {
        path: '/index/home',
        name: 'Home',
        component: Home,
        // redirect: '/index/home'
    },
    {
        path: '/index/ranked',
        name: 'order',
        component: order,
        // redirect: '/index/home'
    },


    {
        path: '/Password',
        name: 'Password',
        component: Password
    },
    {
        path: '/Allbook',
        name: 'Allbook',
        component: Allbook
    },
    {
        path: '/personage',
        name: 'Personage',
        component: Personage,
        // redirect: '/index/home'
    },
    {
        path: '/index/detail/:pk',
        name: 'Detail',
        component: Detail,
        // redirect: '/index/home'
    },
    {
        path: '/ZJdetail',
        name: 'ZJdetail',
        component: ZJdetail,
        // redirect: '/index/home'
    },
    {
        path: '/index/recharge',
        name: 'Recharge',
        component: Recharge,
        // redirect: '/index/home'
    },
    {
        path: '/pay/success',
        name: '/pay/success',
        component: PaySuccess
    },


]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
