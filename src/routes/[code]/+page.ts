import type { PageLoad } from "./$types";
import { STATUS_CODES } from "$lib/codes";

export const load: PageLoad = ({ params }) => {
    const code = parseInt(params.code);
    if (code in STATUS_CODES) {
        return {
            code,
        };
    }

    return {
        code: 404,
    };
};
