<template>
  <aside class="sidebar">
    <ul>
      <li><a href="#">Cast & Crew</a></li>
      <li><a href="#">Reviews</a></li>
      <li><a href="#">Similar Movies</a></li>
    </ul>
  </aside>
</template>

<script>
export default {
  name: "Sidebar",
};
</script>

<style scoped>
/* Sidebar styling */
.sidebar {
  width: 240px;
  padding: 1.5rem;
  background-color: #f4f4f9;
  border-radius: 8px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  position: sticky;
  top: 2rem;
  transition: width 0.3s ease;
}

/* Sidebar links styling */
.sidebar ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.sidebar a {
  text-decoration: none;
  color: #007bff;
  font-size: 1.1rem;
  display: block;
  margin: 1rem 0;
  padding: 0.7rem;
  border-radius: 4px;
  transition: background-color 0.3s ease, color 0.3s ease, transform 0.2s ease;
}

/* Hover effects for the links */
.sidebar a:hover {
  background-color: #007bff;
  color: white;
  transform: translateX(5px);
}

/* Media query for responsiveness */
@media (max-width: 1024px) {
  .sidebar {
    width: 220px;
  }

  .sidebar a {
    font-size: 1rem;
  }
}

@media (max-width: 768px) {
  .sidebar {
    width: 100%;
    padding: 1rem;
    margin-bottom: 1.5rem;
  }

  .sidebar ul {
    display: flex;
    justify-content: space-evenly;
    flex-wrap: wrap;
  }

  .sidebar a {
    margin: 0.5rem;
    padding: 0.6rem 1.2rem;
    font-size: 1rem;
  }
}

@media (max-width: 480px) {
  .sidebar {
    padding: 1rem 0.5rem;
  }

  .sidebar a {
    padding: 0.6rem;
    font-size: 0.95rem;
  }
}
</style>
