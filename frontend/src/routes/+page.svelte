<script lang="ts">
	import * as Select from "$lib/components/select/index.js";
	import type { ActionData } from "./$types";
	import { formInputs } from "$lib/form/inputs";
	import Spinner from "$lib/components/spinner.svelte";

	export let form: ActionData;
</script>

<main>
	<div class="salary-card">
		<h2>Your predicted salary is:</h2>
		{#if !form || !form.salary}
			<span class="salary-empty">$ - - - , - - -</span>
		{:else}
			<span class="salary">$ {form.salary}</span>
		{/if}
	</div>

	<form method="post" class="salary-form">
		{#if form && !form.success}
			<p class="text-red-400">{form.message}</p>
		{/if}
		<div class="salary-inputs">
			{#each formInputs as formInput}
				<div class="salary-input">
					<span>{formInput.inputLabel}</span>
					<Select.Root portal={null}>
						<Select.Trigger>
							<Select.Value placeholder={formInput.selectLabel} />
						</Select.Trigger>
						<Select.Content>
							<Select.Group>
								<Select.Label>{formInput.inputLabel}</Select.Label>
								{#each formInput.selectItems as selectItem}
									<Select.Item value={selectItem} label={selectItem}>
										{selectItem}
									</Select.Item>
								{/each}
							</Select.Group>
						</Select.Content>
						<Select.Input name={formInput.inputLabel} />
					</Select.Root>
				</div>
			{/each}
		</div>

		<div class="submit">
			<button type="submit" class="btn-submit">Predict!</button>
		</div>
	</form>
</main>

<style>
	main {
		padding: 3rem;
		display: flex;
		flex-direction: column;
		gap: 2rem;
	}

	.salary-card {
		max-width: max-content;
		height: max-content;

		display: flex;
		flex-direction: column;
		padding-inline: 2rem;
		padding-block: 1rem;
		border-radius: 0.5rem;
		background-color: rgb(var(--background-600));
	}

	.salary-card > h2 {
		font-weight: 600;
		font-size: 1.25rem;
	}

	.salary-card > span {
		font-weight: 600;
		font-size: 1.5rem;
		color: rgb(var(--contrast-400));
	}

	.salary-card > .salary {
		color: rgb(var(--contrast-700));
	}

	.salary-form {
		width: 100%;
		display: grid;
		gap: 1rem;
	}

	.salary-inputs {
		width: 100%;
		display: grid;
		grid-template-columns: repeat(1, 1fr);
		column-gap: 1rem;
		row-gap: 1rem;
	}

	.salary-input > span {
		color: rgb(var(--foreground-600));
	}

	.submit {
		place-self: end;
		display: flex;
		align-items: center;
		gap: 0.5rem;
	}

	.btn-submit {
		justify-self: end;
		max-width: max-content;
		padding: 0.25rem 0.5rem;
		border-radius: 0.25rem;
		background-color: rgb(var(--contrast-200));
		color: rgb(var(--contrast-700));
		font-size: 1rem;
		font-weight: 600;
		transition: filter 150ms ease;
	}

	.btn-submit:hover {
		filter: brightness(1.1);
	}

	@media (min-width: 640px) {
		main {
			flex-direction: row;
		}
		.salary-card {
			max-width: none;
			min-width: max-content;
		}
	}

	@media (min-width: 1024px) {
		.salary-card > h2 {
			font-size: 1.5rem;
		}

		.salary-card > span {
			font-size: 1.75rem;
		}

		.salary-inputs {
			grid-template-columns: repeat(2, 1fr);
			row-gap: 2rem;
		}
	}
</style>
