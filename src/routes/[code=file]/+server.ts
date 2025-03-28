import type { RequestHandler } from "./$types";

export const GET = (async ({ platform, url }) => {
    if (platform === undefined) {
        return new Response("Internal Server Error", { status: 500 });
    }
    const obj = await platform.env.MEDIA.get(url.pathname.replaceAll("/", ""));
    if (obj === null) {
        return new Response("Not Found", { status: 404 });
    }
    return new Response(obj.body, {
        headers: {
            "Content-Type": obj.httpMetadata?.contentType || "image/jpeg",
            "Cache-Control": "max-age=604800",
        },
    });
}) satisfies RequestHandler;
