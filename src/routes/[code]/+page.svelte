<script lang="ts">
    import { page } from "$app/state";
    import { STATUS_CODES } from "$lib/codes";
    import type { PageData } from "./$types";

    let { data }: { data: PageData } = $props();
    const code = data.code;
    const description = STATUS_CODES[code as keyof typeof STATUS_CODES];
    const image = {
        src: `/${code}.jpeg`,
        alt: `${code} ${description}`,
        width: 800,
        height: 700,
    };
</script>

{#snippet linkDisplay(text: string, code: string)}
    <div class="flex flex-col">
        <span>{text}</span>
        <code class="w-full p-2 whitespace-pre">{code}</code>
    </div>
{/snippet}

<div class="flex flex-row gap-32">
    <div class="w-1/2 flex-col justify-center hidden lg:flex">
        <img
            src={image.src}
            alt={image.alt}
            width={image.width}
            height={image.height}
            class="w-full object-contain rounded-xl"
        />
    </div>
    <div class="text-lg flex-1">
        <img
            src={image.src}
            alt={image.alt}
            width={image.width}
            height={image.height}
            class="w-full object-contain rounded-xl lg:hidden"
        />
        <h1 class="text-9xl font-bold hidden lg:block">{code}</h1>
        <p class="text-4xl text-pink-400 dark:text-pink-300 hidden lg:block">{description}</p>
        <div class="flex flex-col gap-8 mt-8">
            {@render linkDisplay("Link to image", page.url.origin + image.src)}
            {@render linkDisplay("Link to this page", `${page.url.origin}/${code}`)}
            {@render linkDisplay(
                "Embed this image in your website",
                `<img\n  src="${page.url.origin}${image.src}"\n  alt="${image.alt}"\n  width="${image.width}"\n  height="${image.height}"\n/>`,
            )}
            <div>
                <span>MDN Reference: </span>
                <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/{code}" aria-label="MDN Reference">
                    {image.alt}
                </a>
            </div>
        </div>
    </div>
</div>
