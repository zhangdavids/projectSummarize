<template>

<div class="container-fluid app">
  <nav class="navbar navbar-default app__navbar">

    <div class="container-fluid ">
      <div class="navbar-header">
        <router-link to="/" class="navbar-brand">Wetalk</router-link>
      </div>
      <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
        <ul class="nav navbar-nav">
          <li>
            <router-link to="/about">About</router-link>
          </li>
        </ul>
        <ul class="nav navbar-nav navbar-right">
          <li v-if="!$store.state.me.username">
            <a @click="$store.commit('showLoginForm')">登陆</a>
          </li>
          <li class="dropdown" v-if="$store.state.me.username">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">
              <avatar :alt="$store.state.me.username" :size="28"></avatar>
              <span class="caret"></span>
            </a>

              <ul class="dropdown-menu">
                <li><a href="#">my homepage</a> </li>
                <li><a href="#">personal settings</a> </li>
                  <li role="separator" class="divider"></li>
                <li><router-link to="/">login out</router-link></li>
              </ul>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <router-view></router-view>

  <div class="app__footer">
    <div class="container app__container">
      Copyright @ 2017 By John Cheung
    </div>
  </div>

  <login-form v-if="$store.state.loginForm"></login-form>
</div>
</template>

<script>
  import Avatar from './components/Avatar.vue'
  import LoginForm from './components/LoginForm.vue'

  export default {
    components: {
      Avatar,
      LoginForm
    }
  }
</script>

<style>
body {
  margin-top: 15px;
}
.jumbotron h1, h2 {
  color: #FF5A5F;
}
.app,
.app__body {
  padding-right: 0;
  padding-left: 0;
}
.app {
  width: 940px;
}
.app .app__navbar {
  background: #fff;
  border: 0;
}
.app__container {
  width: 940px;
  margin: 0 auto;
}
.app__footer {
  border-top: 1px solid #eee;
  padding: 16px 0 24px;
  color: #999;
  font-size: 14px;
}
</style>
