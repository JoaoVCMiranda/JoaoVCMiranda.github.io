// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },
  modules: [
    '@nuxtjs/tailwindcss',
    '@nuxt/content',
    'nuxt-content-assets',
    '@nuxtjs/color-mode'
  ],
  colorMode: {
  classSuffix: '',
  },
  content: {
	highlight :{
		theme: {
			dark: "github-dark",
			light: "one-dark-pro"
		}
	}
  },
  mdc:{
    remarkPlugins: {
      remarkMath: {src: 'remark-math'}},
	rehypePlugins: {rehypeMathjax: {src: 'rehype-mathjax'}},	
  }
})
