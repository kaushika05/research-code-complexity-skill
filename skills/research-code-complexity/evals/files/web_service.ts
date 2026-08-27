export function handle(request: Request): Response {
  if (request.method === "GET") return new Response("ok");
  if (request.method === "POST") return new Response("created", { status: 201 });
  if (request.method === "DELETE") return new Response(null, { status: 204 });
  return new Response("method not allowed", { status: 405 });
}
