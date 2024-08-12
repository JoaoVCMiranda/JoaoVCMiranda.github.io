<script setup lang="ts">
const route = useRoute()
console.log(route.params.id)
defineProps(['title', 'content'])
</script>

<template>
  <div class="
	min-h-screen
	mx-auto
	bg-light
	dark:bg-dark
	">
	<!--Adicionar a opção de retornar para a página anterior (Muito útil em mobile) + Compartilhar Postagem -->
	<AppHeader />
	<AppMain />

  </div>
</template>
