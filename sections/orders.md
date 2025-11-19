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
			"id": 54,
			"status": "created",
			"payment_status": "paid",
			"ordered_at": "2025-11-18T15:26:34.796Z",
			"paid_at": "2025-11-18T15:26:34.759Z",
			"date_received": null,
			"created_at": "2025-11-18T15:26:11.359Z",
			"updated_at": "2025-11-18T15:26:36.664Z",
			"price": 77.0,
			"price_in_cents": 7700,
			"stripe_invoice_id": null,
			"stripe_hosted_invoice_url": null,
			"qbench_order_id": 911,
			"orderer": {
				"email": "dev@lightlabs.com",
				"name": "Thomas A. Anderson"
			},
			"samples": [
				{
					"id": 677,
					"lot": null,
					"sku": {
						"id": 14,
						"name": "Apple Strawberry",
						"code": "BB-AS",
						"shopifyVariantId": null,
						"product": {
							"id": 2,
							"name": "Baby Food"
						}
					},
					"batch": null,
					"composite": false,
					"number_of_composites": 1,
					"tests": [
						{
							"id": 678,
							"status": "not_started",
							"created_at": "2025-11-18T15:26:25.207Z",
							"updated_at": "2025-11-18T17:49:15.312Z",
							"assay": {
								"id": 1,
								"name": "Heavy Metals"
							}
						}
					]
				}
			]
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
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" https://app.lightlabs.com/api/orders
```

## Show order

* `GET /api/orders/1` will return the order with ID 1 for the authenticated company. It returns all the necessary information about the order including its samples and tests.

###### Example JSON Response

```json
{
	"id": 1,
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
				"shopifyVariantId": null,
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
				"shopifyVariantId": null,
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
				"shopifyVariantId": null,
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
