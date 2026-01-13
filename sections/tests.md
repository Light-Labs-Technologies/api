# Tests

Endpoints:

- [Get tests](#get-tests)
- [Show test](#show-test)

## Deprecation Notice

Some attributes in these responses are currently being deprecated for consistency. While both the legacy and new attributes are available at this time to maintain backward compatibility, support for the legacy fields will be removed in a future release. Please, make sure to use the new attributes.

Please refer to the table below to map the fields that require updates in your integration:

| Deprecated Field | Replacement Field | Type | Notes |
| :--- | :--- | :--- | :--- |
| `spec_status` | `specification` | String | Renamed for consistency. The value format remains the same. |
| `results[spec_result]` | `results[specification]` | String | Renamed for consistency. The value format remains the same. |
| `results[limit_value]` | `results[limit]` | String | Renamed for consistency. The value format remains the same. |


## Get tests

* `GET /api/tests` will return a [paginated list](../README.md#pagination) of tests or the authenticated company.

###### Example JSON Response

```json
{
	"tests": [
		{
			"id": 678,
			"status": "not_started",
			"spec_status": "no_spec",
			"start_date": null,
			"complete_date": "2025-11-20T01:11:02.491Z",
			"published_at": "2025-11-20T01:11:02.360Z",
            "notes": "Some notes",
			"created_at": "2025-11-18T15:26:25.207Z",
			"updated_at": "2025-11-20T01:34:05.304Z",
            "specification": "no_spec",
			"assay": {
				"id": 1,
				"name": "Heavy Metals"
			},
			"results": [
				{
					"analyte": {
						"id": 1,
						"name": "Lead"
					},
					"result": "-",
					"spec_result": "no_spec",
                    "specification": "no_spec",
					"limit_value": "-",
                    "limit": "-"
				},
				{
					"analyte": {
						"id": 2,
						"name": "Mercury"
					},
					"result": "-",
					"spec_result": "no_spec",
                    "specification": "no_spec",
					"limit_value": "-",
                    "limit": "-"
				},
			],
			"sample": {
				"id": 677,
				"lot": null,
				"batch": null,
				"composite": false,
				"number_of_composites": 1,
				"sku": {
					"id": 14,
					"name": "Apple Strawberry",
					"code": "BB-AS",
					"product": {
						"id": 2,
						"name": "Baby Food"
					}
				},
				"order": {
					"id": 54,
					"status": "created",
					"ordered_at": "2025-11-18T15:26:00.000Z",
					"orderer": {
						"email": "dev@lightlabs.com",
						"name": "José Anchieta"
					}
				}
			}
		}
	],
	"pagination": {
		"per_page": 20,
		"current_page": 1,
		"prev_page": null,
		"next_page": 2
	}
}
```

###### Copy as cURL

``` shell
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" https://app.lightlabs.com/api/tests
```

## Show test

* `GET /api/1/tests` will return the test with ID 1 for the authenticated company. It returns all the necessary information about the test including its results.

###### Example JSON Response

```json
{
	"id": 678,
	"status": "not_started",
	"spec_status": "no_spec",
	"start_date": null,
	"complete_date": "2025-11-20T01:11:02.491Z",
	"published_at": "2025-11-20T01:11:02.360Z",
	"notes": "Some notes",
	"created_at": "2025-11-18T15:26:25.207Z",
	"updated_at": "2025-11-20T01:34:05.304Z",
    "specification": "no_spec",
	"assay": {
		"id": 1,
		"name": "Heavy Metals"
	},
	"results": [
		{
			"analyte": {
				"id": 1,
				"name": "Lead"
			},
			"result": "-",
			"spec_result": "no_spec",
            "specification": "no_spec",
			"limit_value": "-",
            "limit": "-"
		},
		{
			"analyte": {
				"id": 2,
				"name": "Mercury"
			},
			"result": "-",
			"spec_result": "no_spec",
            "specification": "no_spec",
			"limit_value": "-",
            "limit": "-"
		},
	],
	"sample": {
		"id": 677,
		"lot": null,
		"batch": null,
		"composite": false,
		"number_of_composites": 1,
		"sku": {
			"id": 14,
			"name": "Apple Strawberry",
			"code": "BB-AS",
			"product": {
				"id": 2,
				"name": "Baby Food"
			}
		},
		"order": {
			"id": 54,
			"status": "created",
			"ordered_at": "2025-11-18T15:26:00.000Z",
			"orderer": {
						"email": "dev@lightlabs.com",
						"name": "José Anchieta"
            }
		}
	}
}
```

###### Copy as cURL

``` shell
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" https://app.lightlabs.com/api/tests/1
```
