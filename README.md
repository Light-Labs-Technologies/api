# The Light Labs API

Welcome to the Light Labs API! 
If you're looking to integrate your application with Light Labs or create your own application in concert with data inside of Light Labs, you're in the right place. We're happy to have you!

## Authentication

Read the [authentication guide](./sections/authentication.md) to get started.

## Pagination

Endpoints that return lists of resources are paginated to improve performance and response times. The pagination metadata is included in the response to help you navigate the result set.

#### Response Structure
Paginated responses include a pagination object containing navigation links and current status.


```json
{
  ...
  "pagination": {
    "per_page": 20,
    "current_page": 1,
    "prev_page": null,
    "next_page": 2
  }
}
```

#### Pagination Object Attributes

Attribute,Type,Description
per_page,Integer,The number of items returned in the current request.
current_page,Integer,The page number of the current result set.
prev_page,Integer,Null
next_page,Integer,Null

## API endpoints

- [Orders](./sections/orders.md)
- [Products](./sections/products.md)
- [Tests](./sections/tests.md)

## Getting help

If you have a question about the API, please open a [support ticket](https://app.lightlabs.com/support_requests/new).
