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

	<h2>Building the model</h2>

	<h2>Challenges with building the model</h2>

	<h2>The website</h2>

	<p>
		We wanted the user to easily interact with our model, and our best idea was to create a web user
		interface with user input and a form submission button. With those things in mind, we decided to
		build this web application using <b>SvelteKit</b> and <b>FastAPI</b>.
	</p>
	<p>
		SvelteKit is a framework for building robust and performant web applications using Svelte, the
		UI component framework that SvelteKit is built on top of. It supports routing (creating multiple
		pages in the same application; how you can see this <code>/about</code> page), server-side rendering,
		and building custom APIs. On the other hand, FastAPI is a fast, modern framework for building APIs
		in Python. We decided to use these technologies because they made it easy to implement our application
		features without distracting too much from the project's actual goal; developing the model.
	</p>
	<p>
		The client-server interaction works like this: the SvelteKit application has the form element
		that, when the user fills in the information and presses the "Calculate!" button, will create a
		request to the API endpoint (the FastAPI application). If all goes well, the endpoint will
		respond with the predicted salary and render it in the website.
	</p>

	<img src="/assets/client-server.png" alt="Client and Server interaction for our Website" />

	<p>
		Thankfully, this is quite a standard client-server interaction, so we did not encounter many
		issues implementing this part of the project.
	</p>

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
		padding-bottom: 5rem;
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

		p {
			font-size: 1.125rem;
		}

		.tag {
			font-size: 0.8625rem;
		}
	}
</style>
