<template>
  <main class="main-content">
    <div class="poster">
      <img :src="movie.Poster" alt="Poster" />
    </div>
    <div class="details">
      <h1>{{ movie.Title }}</h1>
      <p class="movie-info">{{ movie.Released }} • {{ movie.Genre }} • {{ movie.Runtime }}</p>
      <p><strong>Plot:</strong> {{ movie.Plot }}</p>
      <div class="actions">
        <button @click="likeMovie">Like</button>
        <button @click="watchTrailer">Watch Trailer</button>
      </div>
    </div>
  </main>
</template>

<script>
import axios from "axios";

export default {
  name: "MainContent",
  data() {
    return {
      movie: {},
      error: null,
    };
  },
  created() {
    axios
      .get("http://www.omdbapi.com/?i=tt3896198&apikey=d2132124")
      .then((response) => {
        this.movie = response.data;
      })
      .catch((err) => {
        this.error = "Failed to fetch movie data. Please try again later.";
        console.error(err);
      });
  },
  methods: {
    likeMovie() {
      alert("You liked the movie!");
    },
    watchTrailer() {
      const trailerUrl = `https://www.youtube.com/results?search_query=${this.movie.Title} trailer`;
      window.open(trailerUrl, "_blank");
    },
  },
};
</script>

<style scoped>
/* Main content layout */
.main-content {
  display: flex;
  gap: 2rem;
  padding: 2rem;
  flex-wrap: wrap;
}

.poster img {
  width: 100%;
  max-width: 250px;
  height: auto;
  border-radius: 8px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

/* Movie details */
.details {
  display: flex;
  flex-direction: column;
  max-width: 600px;
}

.details h1 {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #333;
}

.movie-info {
  font-size: 1rem;
  color: #777;
  margin-bottom: 1rem;
}

.actions {
  margin-top: 1.5rem;
}

button {
  padding: 0.75rem 1.5rem;
  margin-right: 1rem;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
  font-size: 1rem;
  border-radius: 4px;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

button:hover {
  background-color: #0056b3;
  transform: translateY(-2px);
}

button:focus {
  outline: none;
}

/* Error handling message */
.error-message {
  color: red;
  font-size: 1rem;
  margin-top: 1rem;
}
</style>
