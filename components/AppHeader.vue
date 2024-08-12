<script setup lang="ts">
	const route = useRoute()
	const { data } = await useAsyncData('config', () => queryContent('/config').findOne())
</script>

<template>
	<header class="
		bg-neutral-100 
		dark:bg-neutral-700
		mx-4
		rounded-lg 
		">
		<NuxtLink to="/" 
			class="
			flex">
		<img class="rounded-full" src="/profile/profile-192x192.png"/>
		<div class="mx-4">
			<h1 
			class="text-2xl 
			text-stone-700 
			dark:text-stone-300">
				{{data.titulo}}
			</h1>
			<h2 
			class="text-xl
			text-neutral-600	
			dark:text-stone-300">
				{{data.descricao}}
			</h2>
		</div>
		</NuxtLink>
	    <nav 
		    class="flex 
			mx-auto px-4 
		    	border-b-stone-700
			dark:border-b-stone-300
			my-4
		    ">
	      <ul 
	      	class="mx-auto
		text-xl
		text-stone-700 dark:text-stone-300">
		<li><NuxtLink to="/sobre">Sobre</NuxtLink></li>
		<li><NuxtLink to="/posts">Posts</NuxtLink></li>
		<li><ThemeSelector /></li>
	      </ul>
	    </nav>
	</header>
</template>
