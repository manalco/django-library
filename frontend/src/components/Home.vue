<template>
  <div>
    <b-container>
      <b-card 
        title="Welcome to Django Library" 
        align="center" 
        style="display: inline-flex; max-height: 150px;"
        :img-src="image"
      >
        <b-card-text>
          <a href="/login" class="btn btn-primary">I'm a Student</a> <a href="/loans" class="btn btn-primary">View My Loans</a> <a href="/books" class="btn btn-primary">List of Books</a>    
        </b-card-text>
      </b-card>
    </b-container>
  </div>
</template>

<script>
  import image from "../assets/books.jpg"

  export default {
    data: function () {
      return {
        image: image
      }
    }
  }
</script>
