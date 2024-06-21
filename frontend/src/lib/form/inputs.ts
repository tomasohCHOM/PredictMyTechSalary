type SelectFormInput = {
	inputLabel: string;
	selectLabel: string;
	selectItems: {
		value: string;
		label: string;
	}[];
};

const educationLevel: SelectFormInput = {
	inputLabel: "Education Level",
	selectLabel: "Select education Level",
	selectItems: [
		{ value: "Primary/elementary school", label: "Primary/elementary school" },
		{
			value: "Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)",
			label: "Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)"
		},
		{
			value: "Some college/university study without earning a degree",
			label: "Some college/university study without earning a degree"
		},
		{
			value: "Bachelor’s degree (B.A., B.S., B.Eng., etc.)",
			label: "Bachelor’s degree (B.A., B.S., B.Eng., etc.)"
		},
		{
			value: "Master’s degree (M.A., M.S., M.Eng., MBA, etc.)",
			label: "Master’s degree (M.A., M.S., M.Eng., MBA, etc.)"
		},
		{ value: "Associate degree (A.A., A.S., etc.)", label: "Associate degree (A.A., A.S., etc.)" },
		{ value: "Professional degree (JD, MD, etc.)", label: "Professional degree (JD, MD, etc.)" },
		{
			value: "Other doctoral degree (Ph.D., Ed.D., etc.)",
			label: "Other doctoral degree (Ph.D., Ed.D., etc.)"
		},
		{ value: "Something else", label: "Something else" }
	]
};

const gender: SelectFormInput = {
	inputLabel: "Gender",
	selectLabel: "Select a gender",
	selectItems: [
		{ value: "Man", label: "Man" },
		{ value: "Woman", label: "Woman" },
		{
			value: "Non-binary, genderqueer, or gender non-conforming",
			label: "Non-binary, genderqueer, or gender non-conforming"
		},
		{ value: "Prefer not to say", label: "Prefer not to say" }
	]
};

const age: SelectFormInput = {
	inputLabel: "Age",
	selectLabel: "Select an age",
	selectItems: [
		{ value: "Under 18 years old", label: "Under 18 years old" },
		{ value: "18-24 years old", label: "18-24 years old" },
		{ value: "25-34 years old", label: "25-34 years old" },
		{ value: "35-44 years old", label: "35-44 years old" },
		{ value: "45-54 years old", label: "45-54 years old" },
		{ value: "55-64 years old", label: "55-64 years old" },
		{ value: "65 years or older", label: "65 years or older" },
		{ value: "Prefer not to say", label: "Prefer not to say" }
	]
};

export const formInputs: SelectFormInput[] = [educationLevel, age, gender];
