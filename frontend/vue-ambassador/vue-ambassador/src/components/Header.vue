<template>
  <section class="py-5 text-center container">
    <div class="row py-lg-5">
      <div class="col-lg-6 col-md-8 mx-auto">
        <h1 class="fw-light">{{title}}</h1>
        <p class="lead text-muted">{{description}}</p>
        <p v-if="!user">
          <router-link to="/login" class="btn btn-primary my-2">Login</router-link>
          <router-link to="/register" class="btn btn-primary my-2">Register</router-link>
        </p>
      </div>
    </div>
  </section>
</template>

<script>
import { ref,computed,watch } from 'vue'
import { useStore } from 'vuex';

export default {
    name: "Header",
    setup() {
      const title = ref('Welcome');
      const description = ref('Share links to earn money'); 
      const store = useStore();

      const user = computed(() => store.state.user);
      title.value = user.value ? '$' + user.value.revenue : 'Welcome';
      description.value = user.value ? 'you have earned this far': 'share links yo earn money';
      
      watch(user,() => {
        title.value = user.value ? '$' + user.value.revenue : 'Welcome';
        description.value = user.value ? 'you have earned this far': 'share links yo earn money';
      });

      return {
        title,
        description
      } 
    }
}
</script>
