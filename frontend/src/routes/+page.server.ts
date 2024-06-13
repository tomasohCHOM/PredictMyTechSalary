import type { PageServerLoad } from "./$types";

export const load: PageServerLoad = async () => {
	let url = "http://localhost:8000";
	const res = await fetch(url);
	const data = await res.json();
	return { response: data };
};
