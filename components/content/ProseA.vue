<template>
  <NuxtLink
    :href="href"
    :target="target"
    class="underline text-[#10b981] dark:text-[#14b8a6]"
  >
    <slot />
  </NuxtLink>
</template>

<script setup lang="ts">
import type { PropType } from 'vue'

defineProps({
  href: {
    type: String,
    default: ''
  },
  target: {
    type: String as PropType<'_blank' | '_parent' | '_self' | '_top' | (string & object) | null | undefined>,
    default: undefined,
    required: false
  }
})
</script>
