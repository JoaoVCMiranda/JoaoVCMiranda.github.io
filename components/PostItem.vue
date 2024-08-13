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
		<h1 class="text-4xl text-dark dark:text-light my-4">Posts</h1>
	</div>
	<ContentList :query="query" v-slot="{ list }">

      	<div
		v-for="post in list"
		:key="post._path"
		class="
		border
		border-dark
    hover:border-stone-500
		dark:border-light
		rounded-lg
		m-4 p-4">
	<NuxtLink
		:to="post._path">
        <h2
		class="
		text-2xl
		text-dark
		dark:text-light">
		{{ post.title }}
	</h2>
        <p
	class="text-dark dark:text-light">
	{{ post.description }}
	</p>
	<p class="text-dark dark:text-light">{{post._path}}</p>

      </NuxtLink>
      </div>
    	</ContentList>
	</div>
</template>
