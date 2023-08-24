<template>
  <main class="form-signin w-100 m-auto">
    <form @submit.prevent="submit">
      <h1 class="h3 mb-3 fw-normal">Please Register</h1>

      <div class="form-floating">
        <input v-model="first_name" class="form-control" placeholder="LastName" />
        <label>Fist Name</label>
      </div>

      <div class="form-floating">
        <input v-model="last_name" class="form-control" placeholder="LastName" />
        <label>Last Name</label>
      </div>

      <div class="form-floating">
        <input
          v-model="email"
          type="email"
          class="form-control"
          placeholder="name@example.com"
        />
        <label>Email address</label>
      </div>
      <div class="form-floating">
        <input v-model="password" type="password" class="form-control" placeholder="Password" />
        <label>Password</label>
      </div>

      <div class="form-floating">
        <input v-model="password_confirm" type="password" class="form-control" placeholder="Password Confirm" />
        <label>Password Confirm</label>
      </div>

      <div class="checkbox mb-3">
        <label>
          <input type="checkbox" value="remember-me" /> Remember me
        </label>
      </div>
      <button class="w-100 btn btn-lg btn-primary" type="submit">Submit</button>
      <p class="mt-5 mb-3 text-muted">&copy; 2017–2022</p>
    </form>
  </main>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            first_name: '',
            last_name: '',
            email: '',
            password: '',
            password_confirm: '',
        }
    },
    methods: {
        async submit() {
            await axios.post('register', {
                first_name: this.first_name,
                last_name: this.last_name,
                email: this.email,
                password: this.password,
                password_confirm:this.password_confirm
            });
            await this.$router.push('/login')
        }
    },
};
</script>


<style scoped>
.form-signin {
  max-width: 330px;
  padding: 15px;
}

.form-signin .form-floating:focus-within {
  z-index: 2;
}

.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
</style>