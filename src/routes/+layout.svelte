<script lang="ts">
    import "../app.css";
    let { children } = $props();
</script>

<div class="flex flex-col min-h-screen">
    <div class="flex flex-col items-center p-8 flex-grow">
        <a href="/" class="transition-all text-black dark:text-white hover:text-pink-400 dark:hover:text-pink-300">
            <h1 class="text-5xl font-bold mb-5">HTTP Waifus</h1>
        </a>
        {@render children()}
    </div>
    <footer
        class="flex flex-col items-center text-center p-4 text-neutral-600 dark:text-neutral-400 bg-neutral-200 dark:bg-neutral-950"
    >
        <p>
            Made by <a href="https://github.com/lemonyte">Lemonyte</a> using
            <a href="https://svelte.dev">SvelteKit</a>,
            <a href="https://pages.dev">Cloudflare</a>, and a keyboard
        </p>
        <p><a href="https://github.com/lemonyte/http-waifus">Open-source</a> and tracker-free</p>
    </footer>
</div>

<style lang="postcss">
    :global(a) {
        @apply transition-all text-pink-400 dark:text-pink-300 hover:text-pink-600 dark:hover:text-pink-500;
    }

    :global(code) {
        @apply bg-neutral-950 text-neutral-200 rounded-lg p-1;
    }
</style>
