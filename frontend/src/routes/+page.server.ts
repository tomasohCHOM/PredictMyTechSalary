import { PUBLIC_API_URL } from "$env/static/public";
import { formInputs } from "$lib/form/inputs";
import type { Actions } from "./$types";

export const actions: Actions = {
	default: async ({ request }) => {
		const requestBody: any = {};
		const formData = await request.formData();

		for (const formInput of formInputs) {
			// const inputValue = formData.get(formInput.inputLabel)?.toString() ?? "";
			// if (inputValue === "" || inputValue === "undefined") {
			// 	return { success: false };
			// }
			// requestBody[formInput.requestAttributeName] = inputValue;
			requestBody[formInput.requestAttributeName] = formInput.selectItems[0];
		}

		const url = PUBLIC_API_URL + "/predict";

		// Call the API passing the request body
		const res = await fetch(url, {
			method: "post",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify(requestBody)
		});
		const data = await res.json();

		// Format large numbers with commas and round to 2 decimal places
		let roundedSalary = Math.round((data.salary + Number.EPSILON) * 100) / 100;
		const parts = roundedSalary.toString().split(".");
		parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
		const salary = parts.join(".");

		return { success: true, salary };
	}
};
