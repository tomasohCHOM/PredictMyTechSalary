<script lang="ts">
	import "../globals.css";
</script>

<nav>
	<span>
		<a href="/"> Predict </a>
	</span>
	<span>
		<a href="/about"> About </a>
	</span>
</nav>

<slot />

<style>
	nav {
		display: flex;
		gap: 1rem;
	}

	nav > span > a {
		text-decoration: none;
		color: var(--color-contrast);
	}
</style>
