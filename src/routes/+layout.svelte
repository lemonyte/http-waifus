<script lang="ts">
    import "../app.css";
    let { children } = $props();
</script>

<div class="flex flex-col items-center p-8">
    <a href="/" class="transition-all text-black dark:text-white hover:text-pink-400 dark:hover:text-pink-300">
        <h1 class="text-5xl font-bold my-6">HTTP Waifus</h1>
    </a>
    {@render children()}
</div>

<style lang="postcss">
    :global(a) {
        @apply transition-all text-pink-400 dark:text-pink-300 hover:text-pink-600 dark:hover:text-pink-500;
    }

    :global(code) {
        @apply bg-neutral-950 text-neutral-200 rounded-lg p-1;
    }
</style>
