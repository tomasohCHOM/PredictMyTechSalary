import { PUBLIC_API_URL } from "$env/static/public";
import type { Actions } from "./$types";

export const actions: Actions = {
	calculate: async () => {
		const res = await fetch(PUBLIC_API_URL);
		const data = await res.json();
		return { salary: data.salary };
	}
};
