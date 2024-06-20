<script lang="ts">
	const tags = ["Data Science", "Tech Industry", "Salaries", "Demographics", "Web"];
</script>

<article>
	<h1>Predict My Tech Salary - How It was Built</h1>

	<div class="prebody">
		<span class="authors">Tomas Oh & Mariia Grushina</span>
		<span class="article-info">5 minute read · June 6, 2024</span>
	</div>

	<p>
		Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque labore eligendi quis consequatur
		impedit nostrum tempore, ex modi odio unde earum ad delectus quisquam similique eos provident
		quos ullam odit!
	</p>

	<h2>Resources</h2>

	<div class="tags">
		{#each tags as tag}
			<span class="tag">{tag}</span>
		{/each}
	</div>
</article>

<style>
	article {
		max-width: 75ch;
		margin-inline: auto;
		padding: 2rem;
		display: grid;
		gap: 1rem;
	}

	h1 {
		font-weight: 800;
		font-size: 1.5rem;
	}

	h2 {
		font-weight: 600;
		font-size: 1.25rem;
	}

	.prebody {
		display: flex;
		flex-direction: column;
		line-height: 1.2;
	}

	.prebody > .article-info {
		color: rgb(var(--foreground-400));
	}

	.tags {
		display: flex;
		flex-wrap: wrap;
		align-items: center;
		gap: 0.25rem;
	}

	.tag {
		background-color: rgb(var(--contrast-200));
		color: rgb(var(--contrast-700));
		padding-inline: 0.5rem;
		border-radius: 1rem;
		font-weight: 600;
		font-size: 0.75rem;
	}

	@media (min-width: 768px) {
		h1 {
			font-size: 2rem;
		}
		h2 {
			font-size: 1.5rem;
		}

		.tag {
			font-size: 0.8625rem;
		}
	}
</style>
