<script setup lang="ts">
const route = useRoute()
import type { QueryBuilderParams }  from '@nuxt/content/dist/runtime/types'
// Runtime? Funtime!
const query: QueryBuilderParams = { path: '/posts', where: [{ layout: 'post' }], limit: 20, sort: [{ date: -1 }] }
console.log(query)
</script>

<template>
	<div class="flex flex-col mx-auto max-w-[64rem]">
		<!-- Lembrar de usar wrapper-->
	<div class="mx-auto">
		<h1 class="text-4xl text-stone-700 dark:text-stone-300">Posts</h1>
	</div>
	<ContentList :query="query" v-slot="{ list }">

      	<div 
		v-for="post in list" 
		:key="post._path"
		class="
		border
		border-stone-700 
		hover:border-stone-500 
		bg-stone-100
		dark:bg-neutral-700
		rounded-lg
		m-4 p-4">
	<NuxtLink 
		:to="post._path">
        <h2 
		class="
		text-2xl 
		text-stone-700
		dark:text-stone-300">
		{{ post.title }}
	</h2>
        <p 
	class="
	text-stone-400">
	{{ post.description }}
	</p>
	<p class="text-stone-700 dark:text-stone-400">{{post._path}}</p>

      </NuxtLink>
      </div>
    	</ContentList>
	</div>
</template>
