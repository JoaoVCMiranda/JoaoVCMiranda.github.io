<script setup lang="ts">
	const route = useRoute()
	const { data } = await useAsyncData('config', () => queryContent('/config').findOne())
</script>

<template>
	<header >
    <div id="hero" class="grid grid-flow-row-dense grid-cols-3 content-center">

    <NuxtLink to="/" class="col-span-3 md:col-span-2 grid grid-cols-2">
		<Logo class="rounded-full p-4 max-w-[12rem]" />
		<div class="mx-auto content-center">
			<h1
			class="text-2xl
			text-dark
			dark:text-light">
				{{data.titulo}}
			</h1>
			<h2
			class="text-lg
			text-dark
			dark:text-light">
				{{data.descricao}}
			</h2>
		</div>
		</NuxtLink>

	  <nav
      class="
            mx-auto
            px-4
            col-span-3
            content-center
            md:mr-0
            md:col-span-1
            ">
      <ul
        class=" mx-auto
                text-xl
                text-dark
                dark:text-light">
          <li class="px-1 rounded-md md:p-1 hover:shadow-inner"><NuxtLink to="/sobre">Sobre</NuxtLink></li>
          <li class="px-1 rounded-md md:p-1 hover:shadow-inner"><NuxtLink to="/posts">Posts</NuxtLink></li>
          <li class="px-1 rounded-md md:p-1 hover:shadow-inner">Currículo</li>
          <li class="px-1 md:p-1"><ThemeSelector /></li>
      </ul>
    </nav>

    </div>

	</header>
</template>
