<template>
  <header class="header">
    <div class="logo">TMDB Clone</div>
    <nav>
      <ul>
        <li><a href="#">Overview</a></li>
        <li><a href="#">Media</a></li>
        <li><a href="#">Fandom</a></li>
        <li><a href="#">Share</a></li>
      </ul>
    </nav>
  </header>
</template>

<script>
export default {
  name: "Header",
};
</script>

<style scoped>
/* Header styles */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  background-color: #20232a;
  color: #fff;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Logo styles */
.logo {
  font-size: 1.8rem;
  font-weight: bold;
  color: #61dafb;
  white-space: nowrap; /* Prevent logo from breaking */
}

/* Navigation styles */
nav ul {
  display: flex;
  list-style: none;
  gap: 1.5rem;
}

nav a {
  color: #61dafb;
  text-decoration: none;
  font-size: 1rem;
  transition: color 0.3s ease, transform 0.3s ease;
}

/* Hover effect */
nav a:hover {
  color: #21a1f1;
  transform: translateY(-2px);
}

/* Media query for smaller screens */
@media (max-width: 1024px) {
  .header {
    flex-direction: column;
    align-items: flex-start;
    padding: 1rem;
  }

  .logo {
    font-size: 1.6rem; /* Slightly smaller font for medium screens */
    margin-bottom: 1rem;
  }

  nav ul {
    flex-direction: column;
    gap: 1rem;
    width: 100%;
    padding-left: 0;
  }

  nav a {
    font-size: 1.1rem; /* Slightly larger font on tablet screens */
  }
}

@media (max-width: 768px) {
  .header {
    padding: 1rem 0.8rem;
  }

  .logo {
    font-size: 1.5rem;
    margin-bottom: 1.5rem;
  }

  nav ul {
    flex-direction: column;
    gap: 0.8rem;
    width: 100%;
  }

  nav a {
    font-size: 1.2rem;
  }
}

/* Media query for very small screens */
@media (max-width: 480px) {
  .header {
    padding: 0.8rem 0.5rem;
  }

  .logo {
    font-size: 1.4rem;
    margin-bottom: 1rem;
  }

  nav ul {
    flex-direction: column;
    gap: 0.6rem;
  }

  nav a {
    font-size: 1rem;
  }
}
</style>
