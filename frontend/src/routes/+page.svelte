<script lang="ts">
	import type { PageData } from './$types';

	export let data: PageData;
	$: response = data.response;
</script>

<h1>Our app</h1>

<p>
	{response.Hello}
</p>
