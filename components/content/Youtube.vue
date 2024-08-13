<template>
  <iframe :src="'https://www.youtube.com/embed/'+ $props.url" title="Video do Youtube" frameborder="0" allow="clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen class="mx-auto w-full h-auto m-4 aspect-video">
  </iframe>
</template>

<script setup lang="ts">
  defineProps({
    url:{
      type: String,
      default: '',
    }
  })
</script>
