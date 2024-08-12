<script setup lang="ts">
const route = useRoute()
useHead({
	title: 'Posts'
})
</script>
<template>
  <div class="
	mx-auto
	bg-neutral-50
	border border-stone-700 
	dark:bg-neutral-800
	dark:border-stone-300
	">
	<AppHeader />
	<PostItem />
	<AppFooter />
	</div>
</template>
