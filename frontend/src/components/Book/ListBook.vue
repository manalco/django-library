<template lang="html">
	<div class="container">
		<div class="row">
			<div class="col text-left">
				<h2>Book List</h2>

				<div class="col-md-12">
					<b-table striped hover :items="books" :fields="fields">
						<template v-slot:cell(actions)="data">
							<b-button size="sm" variant="primary" type="submit" :to="{ name: 'ViewBook', params: {bookId: data.item.id} }">View</b-button>
						</template>
					</b-table>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import axios from 'axios';

	export default{
		data(){
			return{
				fields: [
					{key: 'stock', label: 'Stock'},
					{key: 'name', label: 'Title'},
					{key: 'author', label: 'Author'},
					{key: 'actions', label: ''}
				],
				books: []
			}
		},
		methods: {
			getBooks(){
				const path = 'http://localhost:8000/api/v1/books/'
				axios.get(path).then((response) => {
					this.books = response.data
				})
				.catch((error) => {
					console.log(error)
				})
			}
		},
		created(){
			this.getBooks()
		}
	}
</script>

<style lang="css" scoped>
</style>