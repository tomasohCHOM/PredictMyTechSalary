import { PUBLIC_API_URL } from "$env/static/public";
import { formInputs } from "$lib/form/inputs";
import type { Actions } from "./$types";

export const actions: Actions = {
	default: async ({ request }) => {
		const requestBody: any = {};
		const formData = await request.formData();

		for (const formInput of formInputs) {
			const inputValue = formData.get(formInput.inputLabel)?.toString() ?? "";
			if (inputValue === "" || inputValue === "undefined") {
				return {
					success: false,
					message: 'Missing fields. Please complete all fields and press "Predict!" once again.'
				};
			}
			requestBody[formInput.requestAttributeName] = inputValue;
		}

		const url = PUBLIC_API_URL + "/predict";

		let data;
		// Call the API passing the request body
		try {
			const res = await fetch(url, {
				method: "post",
				headers: { "Content-Type": "application/json" },
				body: JSON.stringify(requestBody)
			});
			data = await res.json();
		} catch {
			// If the request fails, render an error message
			return {
				success: false,
				message: "The request failed, the API is likely inactive."
			};
		}
		// Format large numbers with commas and round to 2 decimal places
		let roundedSalary = Math.round((data.salary + Number.EPSILON) * 100) / 100;
		const parts = roundedSalary.toString().split(".");
		parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
		const salary = parts.join(".");

		return { success: true, salary };
	}
};
