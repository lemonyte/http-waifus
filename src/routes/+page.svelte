<script lang="ts">
    import { page } from "$app/state";
    import { STATUS_CODES } from "$lib/codes";
</script>

<p class="text-center text-neutral-600 dark:text-neutral-400 text-lg font-semibold mb-4">
    Waifus for every HyperText Transfer Protocol response status code
</p>
<div class="w-full my-4 mx-8 px-6 flex flex-col">
    <span class="text-lg">API usage:</span>
    <code id="api-url" class="p-4 my-2">{page.url.origin}/{"{code}.jpeg"}</code>
    <span>Replace <code>{"{code}"}</code> with a status code.</span>
</div>

<div class="flex flex-row flex-wrap gap-4 justify-center">
    {#each Object.entries(STATUS_CODES) as [code, description]}
        <a href={`/${code}`}>
            <img
                src={`/${code}.jpeg`}
                alt="{code} {description}"
                width={800}
                height={700}
                class="w-full h-64 rounded-xl"
                loading="lazy"
            />
        </a>
    {/each}
</div>
