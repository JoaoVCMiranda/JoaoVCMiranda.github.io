<script setup lang="ts">
const route =  useRoute()
const colorMode = useColorMode()

console.log(colorMode.preference)
</script>
<template>
	<select	
		class="
		text-xl
		text-stone-700 dark:text-stone-300
		bg-neutral-200 dark:bg-neutral-800"
		v-model="$colorMode.preference">
		<option value="light">light</option>
		<option value="dark">dark</option>
	</select>
</template>
