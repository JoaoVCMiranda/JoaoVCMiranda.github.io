<script setup lang="ts">
const route =  useRoute()
const colorMode = useColorMode()

console.log(colorMode.preference)
</script>
<template>
	<select
		class="
		text-xl
		text-dark dark:text-light
		bg-light dark:bg-dark"
		v-model="$colorMode.preference">
		<option value="light">light</option>
		<option value="dark">dark</option>
	</select>
</template>
