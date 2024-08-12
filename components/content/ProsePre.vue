<template>
	<!--Code Block--> 
	<div class="
		bg-gray-700
		border
		border-stone-800
		rounded-md
		text-stone-300
		">
		<!--"Header"-->
		<div class="
			grid grid-cols-3 gap-2	
			rounded-md
			justify-items-stretch
			bg-gray-600"
		     v-if="$props.filename || $props.language">
		<!--Filename if exists-->
		<div 
		  id="filename-container" 
		  >
		<button @click="copy(code)">
		<div 
			class="m-1 p-1 
			hover:border 
			rounded-lg
			drop-shadow-md
			"
			id="copy-btn">

	<svg width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" fill="None">
		<rect x="1" y="1" rx="1" width="12" height="12" stroke="white" style=""/>
		<rect x="3" y="3" rx="1" width="12" height="12" stroke="white" style=""/>
	</svg>
		</div>
		</button>
		<span v-if="copied">
			Copiado!
		</span>
		  <div 
			v-if="$props.filename"
			class="
			bg-gray-700 
			mt-2 p-2 pl-4 flex-wrap
			rounded-t-lg
			">
		<p>
		  {{ $props.filename }}
		</p>
		  </div>
	  	</div>
		<!--Code lang container-->
		  <div    id="code-lang-container"
			  
			  class="mx-auto my-2 text-neutral-300"
			  >
			  <p v-if="$props.language">
			  {{$props.language}}
			  </p>
		  </div>
		
			  <!--UI-->
		<div class="justify-self-end m-4">

		
		<div class="w-16 grid grid-cols-4 justify-items-center">

		  <div class="w-2 h-2 bg-emerald-400 rounded-full"></div>
		  <div class="w-2 h-2 bg-yellow-400 rounded-full"></div>
		  <div class="w-2 h-2 bg-red-400 rounded-full"></div>
		</div>
		</div>

		</div>
		<!--Code-->

		  <pre :class="$props.class"
			class="p-2"
		  ><slot /></pre>
  </div>
</template>

<script setup lang="ts">
defineProps({
  code: {
    type: String,
    default: ''
  },
  language: {
    type: String,
    default: null
  },
  filename: {
    type: String,
    default: null
  },
  highlights: {
    type: Array as () => number[],
    default: () => []
  },
  meta: {
    type: String,
    default: null
  },
  class: {
    type: String,
    default: null
  }
})
import { useClipboard } from '@vueuse/core'


const { copy, copied, text } = useClipboard()
</script>

<style>
pre code .line {
  display: block;
}
</style>
