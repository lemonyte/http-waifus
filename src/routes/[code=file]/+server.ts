export const GET = async ({ platform, params }) => {
    if (platform === undefined) {
        return new Response("Internal Server Error", { status: 500 });
    }
    const obj = await platform.env.MEDIA.get(params.code);
    if (obj === null) {
        return new Response("Not Found", { status: 404 });
    }
    return new Response(obj.body, {
        headers: {
            "Content-Type": obj.httpMetadata?.contentType || "image/jpeg",
            "Cache-Control": "max-age=604800",
        },
    });
};
