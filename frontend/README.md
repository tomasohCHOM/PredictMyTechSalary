# PredictMyTechSalary Frontend

The frontend application was created using SvelteKit, TypeScript, and shadcn-svelte.

## Setup / Development

Ensure that you have Node.js installed on your machine.

Open the `frontend/` directory that contains the client-side code and install its dependencies:

```bash
cd frontend
npm install
```

Before making requests to the server, create a `.env` inside `frontend/` with this value:

```
PUBLIC_API_URL="http://localhost:8000"
```

This will connect the frontend application with the API.

Run the server locally with `npm run dev`. The website should now be viewable in `localhost:5173`.

## Resources

- [SvelteKit](https://kit.svelte.dev/)
- [shadcn-svelte](https://shadcn-svelte.com/)
