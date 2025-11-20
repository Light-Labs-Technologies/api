# Orders

Endpoints:

- [Get orders](#get-orders)
- [Show order](#show-order)


## Get orders

* `GET /api/1/orders` will return a [paginated list](../README.md#pagination) of orders for the authenticated company.

###### Example JSON Response

```json
{
	"orders": [
		{
			"id": 18,
			"status": "created",
			"payment_status": "pending",
			"ordered_at": "2025-11-13T19:47:00.000Z",
			"paid_at": null,
			"date_received": null,
			"created_at": "2025-11-13T19:46:17.567Z",
			"updated_at": "2025-11-13T19:53:03.683Z",
			"orderer": {
				"email": "dev@lightlabs.com",
				"name": "Development User"
			}
		},
		{
			"id": 17,
			"status": "created",
			"payment_status": "pending",
			"ordered_at": "2025-11-13T19:41:00.000Z",
			"paid_at": null,
			"date_received": null,
			"created_at": "2025-11-13T19:38:48.052Z",
			"updated_at": "2025-11-13T19:53:03.710Z",
			"orderer": {
				"email": "dev@lightlabs.com",
				"name": "Development User"
			}
		},
		{
			"id": 16,
			"status": "created",
			"payment_status": "pending",
			"ordered_at": "2025-11-13T18:44:00.000Z",
			"paid_at": null,
			"date_received": null,
			"created_at": "2025-11-05T17:04:25.710Z",
			"updated_at": "2025-11-13T18:53:04.941Z",
			"orderer": {
				"email": "dev@lightlabs.com",
				"name": "Development User"
			}
		},
		{
			"id": 15,
			"status": "created",
			"payment_status": "pending",
			"ordered_at": "2025-11-05T13:54:00.000Z",
			"paid_at": null,
			"date_received": null,
			"created_at": "2025-11-05T13:54:02.798Z",
			"updated_at": "2025-11-05T14:08:02.166Z",
			"orderer": {
				"email": "dev@lightlabs.com",
				"name": "Development User"
			}
		},
		{
			"id": 11,
			"status": "created",
			"payment_status": "pending",
			"ordered_at": "2025-11-05T13:27:00.000Z",
			"paid_at": null,
			"date_received": null,
			"created_at": "2025-11-05T13:26:16.032Z",
			"updated_at": "2025-11-05T13:38:03.226Z",
			"orderer": {
				"email": "dev@lightlabs.com",
				"name": "Development User"
			}
		},
		{
			"id": 10,
			"status": "created",
			"payment_status": "draft",
			"ordered_at": null,
			"paid_at": null,
			"date_received": null,
			"created_at": "2025-11-05T13:19:53.176Z",
			"updated_at": "2025-11-05T13:20:45.868Z",
			"orderer": {
				"email": "dev@lightlabs.com",
				"name": "Development User"
			}
		},
		{
			"id": 9,
			"status": "created",
			"payment_status": "draft",
			"ordered_at": null,
			"paid_at": null,
			"date_received": null,
			"created_at": "2025-11-05T13:19:50.131Z",
			"updated_at": "2025-11-05T13:20:45.863Z",
			"orderer": {
				"email": "dev@lightlabs.com",
				"name": "Development User"
			}
		},
		{
			"id": 8,
			"status": "completed",
			"payment_status": "draft",
			"ordered_at": null,
			"paid_at": null,
			"date_received": null,
			"created_at": "2025-11-05T13:19:41.045Z",
			"updated_at": "2025-11-05T13:25:16.434Z",
			"orderer": {
				"email": "dev@lightlabs.com",
				"name": "Development User"
			}
		},
		{
			"id": 7,
			"status": "completed",
			"payment_status": "draft",
			"ordered_at": null,
			"paid_at": null,
			"date_received": null,
			"created_at": "2025-11-05T13:19:36.997Z",
			"updated_at": "2025-11-05T13:25:10.267Z",
			"orderer": {
				"email": "dev@lightlabs.com",
				"name": "Development User"
			}
		},
		{
			"id": 6,
			"status": "created",
			"payment_status": "draft",
			"ordered_at": null,
			"paid_at": null,
			"date_received": null,
			"created_at": "2025-11-05T13:19:31.051Z",
			"updated_at": "2025-11-05T13:20:45.843Z",
			"orderer": {
				"email": "dev@lightlabs.com",
				"name": "Development User"
			}
		},
		{
			"id": 5,
			"status": "completed",
			"payment_status": "draft",
			"ordered_at": null,
			"paid_at": null,
			"date_received": null,
			"created_at": "2025-11-05T13:19:20.440Z",
			"updated_at": "2025-11-05T13:24:52.180Z",
			"orderer": {
				"email": "dev@lightlabs.com",
				"name": "Development User"
			}
		},
		{
			"id": 4,
			"status": "created",
			"payment_status": "draft",
			"ordered_at": null,
			"paid_at": null,
			"date_received": null,
			"created_at": "2025-11-05T13:19:15.991Z",
			"updated_at": "2025-11-05T13:20:45.827Z",
			"orderer": {
				"email": "dev@lightlabs.com",
				"name": "Development User"
			}
		},
		{
			"id": 3,
			"status": "completed",
			"payment_status": "draft",
			"ordered_at": null,
			"paid_at": null,
			"date_received": null,
			"created_at": "2025-11-05T13:19:04.460Z",
			"updated_at": "2025-11-05T13:24:38.648Z",
			"orderer": {
				"email": "dev@lightlabs.com",
				"name": "Development User"
			}
		},
		{
			"id": 2,
			"status": "completed",
			"payment_status": "draft",
			"ordered_at": null,
			"paid_at": null,
			"date_received": null,
			"created_at": "2025-11-05T13:18:59.298Z",
			"updated_at": "2025-11-05T13:24:30.800Z",
			"orderer": {
				"email": "dev@lightlabs.com",
				"name": "Development User"
			}
		},
		{
			"id": 1,
			"status": "created",
			"payment_status": "draft",
			"ordered_at": null,
			"paid_at": null,
			"date_received": null,
			"created_at": "2025-11-05T13:18:58.443Z",
			"updated_at": "2025-11-05T13:20:45.797Z",
			"orderer": {
				"email": "dev@lightlabs.com",
				"name": "Development User"
			}
		}
	],
	"pagination": {
		"per_page": 20,
		"current_page": 1,
		"prev_page": null,
		"next_page": null
	}
}
```

###### Copy as cURL

``` shell
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" https://app.lightlabs.com/api/orders
```

## Show order

* `GET /api/orders/15` will return the order with ID 15 for the authenticated company. It returns all the necessary information about the order including its samples and tests.

###### Example JSON Response

```json
{
	"id": 15,
	"status": "created",
	"payment_status": "pending",
	"ordered_at": "2025-11-05T13:54:00.000Z",
	"paid_at": null,
	"date_received": null,
	"created_at": "2025-11-05T13:54:02.798Z",
	"updated_at": "2025-11-05T14:08:02.166Z",
	"orderer": {
		"email": "dev@lightlabs.com",
		"name": "Development User"
	},
	"samples": [
		{
			"id": 519,
			"lot": null,
			"sku": {
				"id": 16,
				"name": "Synergistic Copper Computer",
				"code": "StellarPromo165935",
				"serving_size_grams": null,
				"product": {
					"id": 1,
					"name": "Protein Powder"
				}
			},
			"batch": null,
			"composite": false,
			"number_of_composites": 1,
			"tests": [
				{
					"id": 517,
					"status": "not_started",
					"created_at": "2025-11-05T13:54:20.015Z",
					"updated_at": "2025-11-05T14:04:03.528Z",
					"assay": {
						"id": 69,
						"name": "Phthalates"
					}
				}
			]
		},
		{
			"id": 520,
			"lot": null,
			"sku": {
				"id": 16,
				"name": "Synergistic Copper Computer",
				"code": "StellarPromo165935",
				"serving_size_grams": null,
				"product": {
					"id": 1,
					"name": "Protein Powder"
				}
			},
			"batch": null,
			"composite": false,
			"number_of_composites": 1,
			"tests": [
				{
					"id": 518,
					"status": "not_started",
					"created_at": "2025-11-05T13:54:20.074Z",
					"updated_at": "2025-11-05T14:04:05.155Z",
					"assay": {
						"id": 587,
						"name": "Bisphenols"
					}
				}
			]
		},
		{
			"id": 521,
			"lot": null,
			"sku": {
				"id": 16,
				"name": "Synergistic Copper Computer",
				"code": "StellarPromo165935",
				"serving_size_grams": null,
				"product": {
					"id": 1,
					"name": "Protein Powder"
				}
			},
			"batch": null,
			"composite": false,
			"number_of_composites": 1,
			"tests": [
				{
					"id": 519,
					"status": "not_started",
					"created_at": "2025-11-05T13:54:20.097Z",
					"updated_at": "2025-11-05T14:04:03.337Z",
					"assay": {
						"id": 243,
						"name": "pH"
					}
				}
			]
		}
	]
}

```

###### Copy as cURL

``` shell
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" https://app.lightlabs.com/api/orders/1
```
