<script lang="ts">
	const tags = ["Data Science", "Tech Industry", "Salaries", "Demographics", "Web"];
</script>

<svelte:head>
	<title>Blog | Predict My Tech Salary</title>
</svelte:head>

<article>
	<h1>Predict My Tech Salary - How It was Built</h1>

	<div class="prebody">
		<span class="authors">Tomas Oh & Mariia Grushina</span>
		<span class="article-info">3 minute read · June 6, 2024</span>
	</div>

	<p>
		<b><i>Predict My Tech Salary</i></b> focuses on the impact that demographic data has on the
		compensation of employees in the technical industry. The goal of this project is to develop a
		model that predicts a yearly salary given arbitrary parameters, such as ethnicity, gender, age,
		education level, and accessibility. This data science project is a part of the
		<b>Project ACCESS</b> Summer 2024 Research Program with the overarching goal of raising awareness
		of emerging social justice issues in STEM.
	</p>

	<h2>Exploring data sets</h2>

	<p>
		We began by first exploring which data set to use for our model. We wanted the data to include
		information such as the total yearly compensation for a tech employee and demographic data about
		those individuals. For our purposes, the <b>Stack Overflow 2022 Developer Survey </b> was the most
		suitable as it contained information about total converted compensation for developers around the
		world, including self-reported demographic data, such as gender, age, and ethnicity.
	</p>

	<h2>Cleaning the dataset</h2>

	<p>
		We started by dropping unnecessary columns and all rows that were duplicates or had at least one
		null value. We substituted all unique objects in each column (originally strings) with a number
		using the pandas factorize function, and for columns with numerical values, such as "Age,"
		splitted the values into range groups (below 18 years = 1, 18 to 24 years = 2, 25 to 34 = 3, and
		so on). Then, after analyzing the data, we removed the outliers in the output column to achieve
		better accuracy for the model.
	</p>
	<img src="/assets/data-cleaning.png" alt="Cleaning the dataset and factorizing columns" />
	<p>
		For the machine learning model, we tried the following training algorithms: Ridge Regressor,
		Lasso Regressor, K Neighbors Regressor, Ada Boost Regressor, SVR, Random Forest Regressor, and
		Gradient-Boosting Regressor. The last one performed the best on this dataset, so we did a
		hyperparameter tuning for this model and saved it, with 48.24% accuracy.
	</p>
	<img
		src="/assets/regressor-outputs.png"
		alt="Comparing regressor outputs, highest one before hyperparameter tuning was 47.13%"
	/>

	<h2>The website</h2>

	<p>
		We wanted the user to easily interact with our model, and our best idea was to create a web user
		interface with user input and a form submission button. For our purposes, we built this web
		application using <b>SvelteKit</b> and <b>FastAPI</b>.
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
		that, when the user fills in the information and presses the "Predict!" button, will create a
		request to the API endpoint (the FastAPI application). If all goes well, the endpoint will
		respond with the predicted salary and render it in the website.
	</p>
	<img src="/assets/client-server.png" alt="Client and Server interaction for our Website" />
	<p>
		Thankfully, this is quite a standard client-server interaction, so we did not encounter many
		issues implementing this part of the project.
	</p>

	<h2>Challenges with building the model</h2>

	<p>
		Our model was about 48.24% accurate. This means that there were likely other confounding
		variables that we have not accounted for, such as: the developer profession (not all categories
		in the tech industry are paid equally).
	</p>
	<p>
		On top of that, we deployed the website on Vercel, but we were unable to deploy the API because
		the package exceeded the 250 MB limit. Even after ignoring files unnecessary for the API itself
		(the CSVs, the Jupyter notebooks), the size was still being exceeded due to the Python library
		dependencies (pandas, sklearn). We found some solutions available online, but that required
		changing services in a limited amount of time; due to time constraints, we could not get the
		prediction functionality to work.
	</p>
	<p>
		This project is open source, however, so if you are interested in giving it a try, you can find
		the GitHub repository
		<a class="underline" target="_blank" href="https://github.com/tomasohCHOM/PredictMyTechSalary">
			here.
		</a>
	</p>

	<h2>Conclusion</h2>

	<p>
		Overall, despite our challenges and shortcomings, this project gave us an unique and interesting
		experience to interact with real datasets and create programs to address real social justice
		issues; we have learned so much from this and we are grateful for this learning opportunity. If
		you read this blog all the way, thank you for your time!
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
