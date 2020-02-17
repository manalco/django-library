import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'

import Auth from '@/components/Auth'
import ListBook from '@/components/Book/ListBook'
import ViewBook from '@/components/Book/ViewBook'
import ListLoan from '@/components/Loan/ListLoan'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/login',
      name: 'Auth',
      component: Auth
    },
    {
      path: '/books',
      name: 'ListBook',
      component: ListBook
    },
    {
      path: '/books/:bookId/view',
      name: 'ViewBook',
      component: ViewBook
    },
    {
      path: '/loans',
      name: 'ListLoan',
      component: ListLoan
    }
  ],
  mode: 'history'
})
