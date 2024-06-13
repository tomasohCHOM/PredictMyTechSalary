import type { PageServerLoad } from './$types';
import { dev } from '$app/environment';
import { PUBLIC_API_URL_DEV, PUBLIC_API_URL_PROD } from '$env/static/public';

export const load: PageServerLoad = async () => {
	let url = dev ? PUBLIC_API_URL_DEV : PUBLIC_API_URL_PROD;
	const res = await fetch(url);
	const data = await res.json();
	console.log(data);
	return { response: data };
};
