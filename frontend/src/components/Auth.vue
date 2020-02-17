<template>
  <div>
    <b-card title="Login" align="center" style="display: inline-flex;">
      <b-card-text>
        <v-form inline style="width: auto; display: inline-flex;" ref="form" v-model="valid" lazy-validation>
          <label class="sr-only" for="inline-form-input-username">Username</label>
          <b-input-group prepend="@" class="mb-2 mr-sm-2 mb-sm-0">
            <b-input 
              id="inline-form-input-username" 
              placeholder="Username" 
              v-model="credentials.username"
              :rules="rules.username"
            ></b-input>
          </b-input-group>

          <label class="sr-only" for="inline-form-input-name">Password</label>
          <b-input
            id="inline-form-input-name"
            class="mb-2 mr-sm-2 mb-sm-0"
            type="password"
            placeholder="Password"
            v-model="credentials.password"
            :rules="rules.password"
          ></b-input>

          <b-button variant="primary" @click="login">Login</b-button>
        </v-form>
      </b-card-text>
    </b-card>
  </div>
</template>


<script>
  import axios from 'axios';
  import swal from 'sweetalert2';
  import router from "../router";

  export default {
      name: 'Auth',
      data: () => ({
          credentials: {},
          valid:true,
          loading:false,
          rules: {
            username: [
              v => !!v || "Username is required.",
              v => /[a-z0-9]+$/.test(v) || "Username must have only letters and digits."
            ],
            password: [
              v => !!v || "Password is required."
            ]
          }
      }),
      methods: {
          login() {
              if (this.$refs.form.validate()) {
                this.loading = true;
                axios.post('http://localhost:8000/auth/', this.credentials).then(res => {
                  this.$session.start();
                  this.$session.set('token', res.data.token);
                  router.push('/');
                }).catch(e => {
                  this.loading = false;
                  alert('Worng username or password');
                  console.log(e);
                })
              }
          },
          checkLoggedIn() {
              this.$session.start();
              if (this.$session.has("token")) {
                router.push("/");
              }
            }
      },
      mounted() {
        this.checkLoggedIn();
      }
  }
</script>