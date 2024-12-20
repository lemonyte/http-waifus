<script lang="ts">
    import { page } from "$app/state";
    import type { PageData } from "./$types";
    import { STATUS_CODES } from "$lib/codes";

    let { data }: { data: PageData } = $props();
    const code = data.code;
    const description = STATUS_CODES[code as keyof typeof STATUS_CODES];
    const image = {
        src: `/${code}.jpeg`,
        alt: `${code} ${description}`,
    };
</script>

<div class="flex flex-row gap-32">
    <img src={image.src} alt={image.alt} class="w-1/2 object-contain" />
    <div class="text-lg flex-1">
        <h1 class="text-9xl font-bold">{code}</h1>
        <p class="text-4xl mb-8">{description}</p>
        <div class="flex flex-col gap-8">
            <div class="link-display">
                <span>Link to image</span>
                <code>{page.url.origin}{image.src}</code>
            </div>
            <div class="link-display">
                <span>Link to this page</span>
                <code>{page.url.origin}/{code}</code>
            </div>
            <div class="link-display">
                Embed this image in your website:
                <code>&lt;img src="{page.url.origin}{image.src}" alt="{image.alt}" /&gt;</code>
            </div>
            <div>
                <span>MDN Reference: </span>
                <a
                    href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/{code}"
                    aria-label="MDN Reference"
                    class="transition-all text-pink-300 hover:text-pink-500"
                >
                    {image.alt}
                </a>
            </div>
        </div>
    </div>
</div>

<style lang="postcss">
    .link-display {
        @apply flex;
        @apply flex-col;
    }

    .link-display code {
        @apply bg-neutral-900;
        @apply p-2;
        @apply rounded-lg;
        @apply w-full;
    }
</style>
