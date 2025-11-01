import { redirect } from "@sveltejs/kit";

export const load = (_) => {
    redirect(307, "/404");
};
