import type { RequestHandler } from "./$types";

export const GET = (async ({ platform, url }) => {
    const obj = await platform.env.MEDIA.get(url.pathname.replaceAll("/", ""));
    if (obj === null) {
        return new Response("Not Found", { status: 404 });
    }
    return new Response(obj.body, {
        headers: {
            "Content-Type": obj.httpMetadata?.contentType || "image/png",
            "Cache-Control": "max-age=604800",
        },
    });
}) satisfies RequestHandler;
