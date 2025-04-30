import { redirect } from "@sveltejs/kit";

export const load = async (_) => {
    redirect(307, "/404");
};
