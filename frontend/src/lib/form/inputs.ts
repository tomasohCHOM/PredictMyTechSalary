type SelectFormInput = {
	inputLabel: string;
	selectLabel: string;
	selectItems: string[];
};

const devProfessionStatus: SelectFormInput = {
	inputLabel: "Developer Profession Status",
	selectLabel: "Select your developer profession status",
	selectItems: [
		"I am not primarily a developer, but I write code sometimes as part of my work",
		"I am a developer by profession"
	]
};

const employmentStatus: SelectFormInput = {
	inputLabel: "Employment Status",
	selectLabel: "Select your employment status",
	selectItems: [
		"Employed, full-time",
		"Employed, part-time",
		"Retired",
		"Independent contractor, freelancer, or self-employed"
	]
};

const remoteWork: SelectFormInput = {
	inputLabel: "Remote Work",
	selectLabel: "Select remote work option",
	selectItems: ["Fully remote", "Hybrid (some remote, some in-person)", "Full in-person"]
};

const educationLevel: SelectFormInput = {
	inputLabel: "Education Level",
	selectLabel: "Select education Level",
	selectItems: [
		"Primary/elementary school",
		"Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)",
		"Some college/university study without earning a degree",
		"Bachelor’s degree (B.A., B.S., B.Eng., etc.)",
		"Master’s degree (M.A., M.S., M.Eng., MBA, etc.)",
		"Associate degree (A.A., A.S., etc.)",
		"Professional degree (JD, MD, etc.)",
		"Other doctoral degree (Ph.D., Ed.D., etc.)",
		"Something else"
	]
};

const yearsCoding: SelectFormInput = {
	inputLabel: "Years Coding",
	selectLabel: "Select the number of years you have been coding for (professionally or not)",
	selectItems: [
		"Less than 5 years",
		"From 5 to 10 years",
		"From 11 to 20 years",
		"From 21 to 40 years",
		"More than 40 years"
	]
};

const country: SelectFormInput = {
	inputLabel: "Country",
	selectLabel: "Select your country",
	selectItems: [
		"United States",
		"India",
		"United Kingdom",
		"Germany",
		"Canada",
		"Brazil",
		"France",
		"Spain",
		"Australia",
		"Netherlands",
		"Poland",
		"Italy",
		"Russian Federation",
		"Sweden"
	]
};

const organizationSize: SelectFormInput = {
	inputLabel: "Organization Size",
	selectLabel: "Select the size of your organization",
	selectItems: [
		"20 to 99 employees",
		"2 to 9 employees",
		"5,000 to 9,999 employees",
		"100 to 499 employees",
		"10,000 or more employees",
		"Just me - I am a freelancer, sole proprietor, etc.",
		"500 to 999 employees",
		"1,000 to 4,999 employees",
		"10 to 19 employees",
		"I don’t know"
	]
};

const age: SelectFormInput = {
	inputLabel: "Age",
	selectLabel: "Select an age",
	selectItems: [
		"Under 18 years old",
		"18-24 years old",
		"25-34 years old",
		"35-44 years old",
		"45-54 years old",
		"55-64 years old",
		"65 years or older",
		"Prefer not to say"
	]
};

const gender: SelectFormInput = {
	inputLabel: "Gender",
	selectLabel: "Select a gender",
	selectItems: [
		"Man",
		"Woman",
		"Non-binary, genderqueer, or gender non-conforming",
		"Prefer not to say"
	]
};

const ethnicity: SelectFormInput = {
	inputLabel: "Ethnicity",
	selectLabel: "Select your ethnicity",
	selectItems: [
		"White",
		"European",
		"Indian",
		"Asian",
		"Hispanic or Latino/a",
		"South American",
		"Middle Eastern",
		"Prefer not to say",
		"African",
		"South Asian",
		"Southeast Asian",
		"I don't know",
		"East Asian"
	]
};

const workExperience: SelectFormInput = {
	inputLabel: "Work Experience",
	selectLabel: "Select the number of years that you have been coding professionally for",
	selectItems: [
		"Less than 5 years",
		"From 5 to 10 years",
		"From 11 to 20 years",
		"From 21 to 40 years",
		"More than 40 years"
	]
};

export const formInputs: SelectFormInput[] = [
	devProfessionStatus,
	employmentStatus,
	remoteWork,
	educationLevel,
	yearsCoding,
	country,
	organizationSize,
	age,
	gender,
	ethnicity,
	workExperience
];
