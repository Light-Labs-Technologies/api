# Tests

All forwards in a project are children of an Inbox resource.

Endpoints:

- [Get tests](#get-tests)


## Get tests

* `GET /api/1/tests` will return a paginated list of tests for the company with an ID of `1`.

###### Example JSON Response

```json
{
}
```

###### Copy as cURL

``` shell
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" https://app.lightlabs.com/api/$COMPANY_ID/tests
```
