<template>
<div class="container">
    <header class="d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-3 mb-4 border-bottom">

      <ul class="nav col-12 col-md-auto mb-2 justify-content-center mb-md-0">
        <li><a href="#" class="nav-link px-2 link-secondary">Frontend</a></li>
        <li><a href="#" class="nav-link px-2 link-dark">Backend</a></li>
      </ul>

      <div v-if="user">
        <button type="button" class="btn btn-primary">{{user.first_name}} {{user.last_name}}</button>
        <a class="btn btn-outline-primary me-2" @click="logout">Logout</a>
      </div>
      
      <div class="col-md-3 text-end" v-if="!user">
        <button type="button" class="btn btn-outline-primary me-2">Login</button>
        <button type="button" class="btn btn-primary">Sign-up</button>
      </div>

    </header>
  </div>
</template>

<script>
import axios from 'axios';
import { computed } from 'vue'
import { useStore } from 'vuex'

export default {
    name: "Nav",
    setup() {
      const store = useStore();
      const user = computed(() => store.state.user);

      return {
        user,
      }
    },
    methods: {
      async logout() {
        await axios.post('logout');
        await store.dispatch('setUser',null);
      }
    }
}
</script>


<style>
    
</style>