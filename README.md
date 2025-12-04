# The Light Labs API

Welcome to the Light Labs API!

If you're looking to integrate your application with Light Labs or create your own application in concert with data inside of Light Labs, you're in the right place. We're happy to have you!

## Authentication

Read the [authentication guide](./sections/authentication.md) to get started.

## Pagination

Endpoints that return lists of resources are paginated to improve performance and response times. The pagination metadata is included in the response to help you navigate the result set.

#### Response Structure
Paginated responses include a pagination object containing navigation links and current status.


```
{
  ...,
  "pagination": {
    "per_page": 20,
    "current_page": 1,
    "prev_page": null,
    "next_page": 2
  }
}
```

#### Pagination Object Attributes

| Attribute | Description |
| :--- | :--- |
| `per_page` | The number of items returned in the current request. (default: 20) |
| `current_page` | The page number of the current result set. |
| `prev_page` | The page number of the previous page. Returns `null` if there is no previous page. |
| `next_page` | The page number of the next page. Returns `null` if there is no next page. |


To navigate between pages, include a `page` query parameter in your request (e.g., `GET /api/products?page=2`).

## Rate Limiting

To ensure fair usage and service stability, our API implements rate limiting.

### Limits

- **300 requests per minute** per API key

### Exceeded Limit Response

When you exceed the rate limit, the API returns:

```
HTTP/1.1 429 Too Many Requests
Retry-After: 60
Content-Type: application/json

{ "error": "Rate limit exceeded. Retry after 60 seconds." }
```

Wait for the time indicated in the `Retry-After` header before retrying your request.

## API endpoints

- [Orders](./sections/orders.md)
- [Products](./sections/products.md)
- [SKUs (Variants)](./sections/skus.md)
- [Tests](./sections/tests.md)

## Getting help

If you have a question about the API, please open a [support ticket](https://app.lightlabs.com/support_requests/new).
