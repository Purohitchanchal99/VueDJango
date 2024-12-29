<template>
  <div id="app">
    <Header />
    <div class="container">
      <MainContent />
      <Sidebar />
    </div>
  </div>
</template>

<script>
import Header from "./components/Header.vue";
import MainContent from "./components/MainContent.vue";
import Sidebar from "./components/Sidebar.vue";

export default {
  name: "App",
  components: {
    Header,
    MainContent,
    Sidebar,
  },
};
</script>

<style>
/* General layout styling */
#app {
  font-family: Arial, sans-serif;
}

.container {
  display: flex;
  gap: 2rem;
  margin: 2rem;
  justify-content: space-between;
  align-items: flex-start;
  flex-wrap: wrap; /* Allow elements to wrap on smaller screens */
}

/* Make sure MainContent takes more space */
.container > MainContent {
  flex: 3; /* MainContent takes more space */
  min-width: 60%; /* Ensure it doesn’t get too narrow */
}

/* Sidebar should take less space */
.container > Sidebar {
  flex: 1;
  min-width: 220px;
}

/* Media query for mobile responsiveness */
@media (max-width: 768px) {
  .container {
    flex-direction: column; /* Stack MainContent and Sidebar vertically */
    gap: 1rem;
    margin: 1rem;
  }

  .container > MainContent {
    min-width: 100%;
  }

  .container > Sidebar {
    min-width: 100%;
  }
}
</style>
