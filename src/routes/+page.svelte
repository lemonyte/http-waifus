<script lang="ts">
    import { page } from "$app/state";
    import { STATUS_CODES } from "$lib/codes";
</script>

<p class="text-neutral-600 dark:text-neutral-400 text-lg font-bold mb-4">
    Waifus for every HyperText Transfer Protocol response status code.
</p>
<div class="w-full my-4 mx-8 flex flex-col">
    <span class="text-lg">API usage:</span>
    <code id="api-url" class="p-4 my-2">{page.url.origin}/&lbrace;code&rbrace;.jpeg</code>
    <span>Replace <code>&lbrace;code&rbrace;</code> with a status code.</span>
</div>

<div class="flex flex-row flex-wrap gap-4 justify-center">
    {#each Object.entries(STATUS_CODES) as [code, description]}
        <a href={`/${code}`}>
            <img src={`/${code}.jpeg`} alt="{code} {description}" class="w-full h-64" />
        </a>
    {/each}
</div>
