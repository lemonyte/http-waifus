<script lang="ts">
    import "../app.css";
    let { children } = $props();
</script>

<div class="flex flex-col items-center p-8">
    <a href="/">
        <h1 class="text-5xl font-bold my-6">HTTP Waifus</h1>
    </a>
    {@render children()}
</div>
