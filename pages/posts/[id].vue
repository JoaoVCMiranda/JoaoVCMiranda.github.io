<script setup lang="ts">
const route = useRoute()
console.log(route.params.id)
defineProps(['title', 'content'])
</script>

<template>
  <div class="
	min-h-screen
	mx-auto
	bg-neutral-50
	border border-stone-700 
	dark:bg-neutral-800
	dark:border-stone-300
	">
	<!--Adicionar a opção de retornar para a página anterior (Muito útil em mobile) + Compartilhar Postagem -->
	<AppHeader />
	<AppMain />

  </div>
</template>
