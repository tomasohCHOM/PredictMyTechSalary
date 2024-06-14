<nav>
	<div class="left-section">
		<h1>
			<a href="/"> Predict My Tech Salary </a>
		</h1>
	</div>

	<div class="right-section">
		<span class="header-item">
			<a href="/about"> About </a>
		</span>
		<span class="header-item">
			<a target="_blank" href="https://github.com/tomasohCHOM/PredictMyTechSalary"> Code </a>
		</span>
	</div>
</nav>

<style>
	nav {
		padding: 1rem;
		display: flex;
		align-items: center;
		justify-content: space-between;
		border-bottom: 2px solid rgb(var(--background-500));
	}

	h1 {
		font-weight: 700;
	}

	a {
		text-decoration: none;
		color: rgb(var(--foreground-600));
	}

	.left-section > h1 {
		margin: 0;
		font-size: 1.25rem;
	}

	.right-section {
		display: flex;
		gap: 0.5rem;
	}

	.right-section > .header-item {
		font-weight: 600;
		padding: 0.25rem 0.375rem;
		border-radius: 0.25rem;
		transition: filter 150ms ease;
		background-color: rgb(var(--background-400));
		transition: background-color 150ms ease;
	}

	.right-section > .header-item:hover {
		background-color: rgb(var(--background-600));
	}
</style>
