<script lang="ts">
	import * as Select from "$lib/components/ui/select/index.js";

	const fruits = [
		{ value: "apple", label: "Apple" },
		{ value: "banana", label: "Banana" },
		{ value: "blueberry", label: "Blueberry" },
		{ value: "grapes", label: "Grapes" },
		{ value: "pineapple", label: "Pineapple" }
	];
</script>

<main>
	<div class="salary-card">
		<h2>Your predicted salary is:</h2>
		<span class="salary">$134,456</span>
	</div>
	<div class="salary-inputs">
		<div class="salary-input">
			<span>Fruit type</span>
			<Select.Root portal={null}>
				<Select.Trigger>
					<Select.Value placeholder="Select a fruit" />
				</Select.Trigger>
				<Select.Content>
					<Select.Group>
						<Select.Label>Fruits</Select.Label>
						{#each fruits as fruit}
							<Select.Item value={fruit.value} label={fruit.label}>{fruit.label}</Select.Item>
						{/each}
					</Select.Group>
				</Select.Content>
				<Select.Input name="favoriteFruit" />
			</Select.Root>
		</div>
		<div class="salary-input">
			<span>Fruit type</span>
			<Select.Root portal={null}>
				<Select.Trigger>
					<Select.Value placeholder="Select a fruit" />
				</Select.Trigger>
				<Select.Content>
					<Select.Group>
						<Select.Label>Fruits</Select.Label>
						{#each fruits as fruit}
							<Select.Item value={fruit.value} label={fruit.label}>{fruit.label}</Select.Item>
						{/each}
					</Select.Group>
				</Select.Content>
				<Select.Input name="favoriteFruit" />
			</Select.Root>
		</div>
		<div class="salary-input">
			<span>Fruit type</span>
			<Select.Root portal={null}>
				<Select.Trigger>
					<Select.Value placeholder="Select a fruit" />
				</Select.Trigger>
				<Select.Content>
					<Select.Group>
						<Select.Label>Fruits</Select.Label>
						{#each fruits as fruit}
							<Select.Item value={fruit.value} label={fruit.label}>{fruit.label}</Select.Item>
						{/each}
					</Select.Group>
				</Select.Content>
				<Select.Input name="favoriteFruit" />
			</Select.Root>
		</div>
		<div class="salary-input">
			<span>Fruit type</span>
			<Select.Root portal={null}>
				<Select.Trigger>
					<Select.Value placeholder="Select a fruit" />
				</Select.Trigger>
				<Select.Content>
					<Select.Group>
						<Select.Label>Fruits</Select.Label>
						{#each fruits as fruit}
							<Select.Item value={fruit.value} label={fruit.label}>{fruit.label}</Select.Item>
						{/each}
					</Select.Group>
				</Select.Content>
				<Select.Input name="favoriteFruit" />
			</Select.Root>
		</div>
	</div>
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
		font-size: 1.5rem;
	}

	.salary-card > .salary {
		font-weight: 600;
		font-size: 1.75rem;
		color: rgb(var(--contrast-700));
	}

	.salary-inputs {
		width: 100%;
		display: grid;
		grid-template-columns: repeat(1, 1fr);
		column-gap: 1rem;
		row-gap: 2rem;
	}

	.salary-input > span {
		color: rgb(var(--foreground-600));
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
		.salary-inputs {
			grid-template-columns: repeat(2, 1fr);
		}
	}
</style>
