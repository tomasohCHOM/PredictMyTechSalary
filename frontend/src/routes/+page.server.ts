import { PUBLIC_API_URL } from "$env/static/public";
import type { Actions } from "./$types";

export const actions: Actions = {
	default: async () => {
		const res = await fetch(PUBLIC_API_URL);
		const data = await res.json();

		// Format large numbers with commas
		const parts = data.salary.toString().split(".");
		parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
		const salary = parts.join(".");

		return { success: true, salary };
	}
};
