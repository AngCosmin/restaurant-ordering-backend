import Vue from 'vue'
import Router from 'vue-router'
import { canMakeRequest } from '@/services/token.service'

Vue.use(Router)

function loadView(view) {
    return () => import(/* webpackChunkName: "view-[request]" */ `@/views/${view}.vue`)
}

let routes = [
    {
        path: '/',
        component: loadView('Home'),
        meta: { requiresAuth: true },
        name: 'home',
    },
    {
        path: '/login',
        component: loadView('Login'),
        meta: { requiresAuth: false },
        name: 'login',
    },
    {
        path: '/products',
        component: loadView('Products'),
        meta: { requiresAuth: true },
        name: 'products',
    },
    {
        path: '/dashboard',
        component: loadView('Dashboard'),
        meta: { requiresAuth: true },
        name: 'dashboard',
    },
]

const router = new Router({
    routes: routes,
})

router.beforeEach((to, from, next) => {
    let email = localStorage.getItem('email')
    let password = localStorage.getItem('password')
    let requireAuth = to.matched.some(record => record.meta.requiresAuth)

    if (to.path === '/login' && email) {
        next('/products') 
    }

    if (!requireAuth) {
        next()
    }
    else {
        if (email) { 
            next() 
        }
        else {
            next('/login')                 
        }
    }
});


export default router