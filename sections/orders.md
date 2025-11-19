# Orders

Endpoints:

- [Get orders](#get-orders)


## Get orders

* `GET /api/1/orders` will return a [paginated list](../README.md#pagination) of orders for the company with an ID of `1`.

###### Example JSON Response

```json
{
}
```

###### Copy as cURL

``` shell
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" https://app.lightlabs.com/api/$COMPANY_ID/orders
```
