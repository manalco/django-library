<template lang="html">
	<div class="container">
		<div class="row">
			<div class="col text-left">
				<h2>View Book</h2>

				<div class="row">
					<div class="col">
						<div class="card">
							<div class="card-body">
								<h5 class="card-title">[Stock: {{ book.stock }}] <b>{{ book.name }}</b></h5>
								<h6 class="card-subtitle mb-2 text-muted">{{ book.author }}</h6>
								<p class="card-text">{{ book.description }}</p>
								<b-button type="submit" variant="primary" class="btn-large" :to="{ name:'ListBook' }">Back to List</b-button>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import axios from 'axios'

	export default{
		data(){
			return{
				bookId: this.$route.params.bookId,
				book: {
					stock: '',
					name: '',
					author: '',
					description: ''
				} 
			}
		},
		methods: {
			getBook(){
				const path = `http://localhost:8000/api/v1/books/${this.bookId}/`

				axios.get(path).then((response) => {
					this.book.stock = response.data.stock
					this.book.name = response.data.name
					this.book.author = response.data.author
					this.book.description = response.data.description
				})
				.catch((error) => {
					console.log(error)
				})
			}
		},
		created(){
			this.getBook()
		}
	}
</script>

<style lang="css" scoped>
</style>