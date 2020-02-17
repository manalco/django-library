<template lang="html">
	<div class="container">
		<div class="row">
			<div class="col text-left">
				<h2>My Loans</h2>

				<div class="col-md-12">
					<b-table striped hover :items="loans" :fields="fields">
					</b-table>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import axios from 'axios';
	import router from "../../router";

	export default{
		data(){
			return{
				fields: [
					{key: 'book', label: 'Book'},
					{key: 'loan_starts', label: 'From'},
					{key: 'loan_ends', label: 'To'},
					{key: 'return_date', label: 'Returned on'},
				],
				loans: []
			}
		},
		mounted() {
			this.checkLoggedIn();
		},
		methods: {
			getLoans(){
				const path = 'http://localhost:8000/api/v1/loans/'
				axios.get(path).then((response) => {
					this.loans = response.data
				})
				.catch((error) => {
					console.log(error)
				})
			},
			checkLoggedIn() {
		      this.$session.start();
		      if (!this.$session.has("token")) {
		        router.push("/auth");
		      }
		    }
		},
		created(){
			this.getLoans()
		}
	}
</script>

<style lang="css" scoped>
</style>