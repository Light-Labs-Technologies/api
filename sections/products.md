# Products

Endpoints:

- [Get products](#get-products)

## Get products

* `GET /api/1/products` will return a paginated list of products for the company with an ID of `1`.

###### Example JSON Response

```json
{
}
```

###### Copy as cURL

``` shell
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" https://app.lightlabs.com/api/$COMPANY_ID/products
```
