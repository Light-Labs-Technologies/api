# The Light Labs API

Welcome to the Light Labs API!
If you're looking to integrate your application with Light Labs or create your own application in concert with data inside of Light Labs, you're in the right place. We're happy to have you!

## Authentication

Read the [authentication guide](./sections/authentication.md) to get started.

## Pagination

Paginated endpoints return a `data` array containing the items for the current page, along with a `pagination` object that includes:
- `per_page`: The number of items returned per page (default: 20)
- `current_page`: The current page number
- `prev_page`: The previous page number (null if on the first page)
- `next_page`: The next page number (null if on the last page)

To navigate between pages, include a `page` query parameter in your request (e.g., `GET /api/products?page=2`).

## API endpoints

- [Orders](./sections/orders.md)
- [Products](./sections/products.md)
- [SKUs (Variants)](./sections/skus.md)
- [Tests](./sections/tests.md)

## Getting help

If you have a question about the API, please open a [support ticket](https://app.lightlabs.com/support_requests/new).
