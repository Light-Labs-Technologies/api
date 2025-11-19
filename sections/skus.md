# SKUs (Variants)

Endpoints:

- [Get skus](#get-skus)
- [Show sku](#show-sku)

## Get skus

* `GET /api/skus` will return a [paginated list](../README.md#pagination) of skus for the authenticated company.

###### Example JSON Response

```json
{
	"data": [
		{
			"id": 15,
			"name": "Aerodynamic Plastic Coat",
			"code": "StellarSale910341",
			"serving_size_grams": null,
			"product_id": 1
		},
		{
			"id": 14,
			"name": "Apple Strawberry",
			"code": "BB-AS",
			"serving_size_grams": null,
			"product_id": 2
		},
		{
			"id": 23,
			"name": "Awesome Granite Chair",
			"code": "PremiumSale866518",
			"serving_size_grams": null,
			"product_id": 1
		},
		{
			"id": 11,
			"name": "Banana",
			"code": "BB-BA",
			"serving_size_grams": null,
			"product_id": 2
		},
		{
			"id": 13,
			"name": "Banana Blueberry",
			"code": "BB-BL",
			"serving_size_grams": null,
			"product_id": 2
		},
		{
			"id": 8,
			"name": "Beef Stew",
			"code": "BB-BS",
			"serving_size_grams": null,
			"product_id": 2
		},
		{
			"id": 9,
			"name": "Blueberry",
			"code": "BB-BB",
			"serving_size_grams": null,
			"product_id": 2
		},
		{
			"id": 6,
			"name": "Chicken & Peas",
			"code": "BB-CNP",
			"serving_size_grams": null,
			"product_id": 2
		},
		{
			"id": 2,
			"name": "Chocolate",
			"code": "PROPOW-CHOC",
			"serving_size_grams": null,
			"product_id": 1
		},
		{
			"id": 4,
			"name": "Cookies and Cream",
			"code": "PROPOW-COOKIES",
			"serving_size_grams": null,
			"product_id": 1
		},
		{
			"id": 33,
			"name": "Nescau",
			"code": "NESCAU",
			"serving_size_grams": "250.0",
			"product_id": 10
		},
		{
			"id": 31,
			"name": "Banana",
			"code": "",
			"serving_size_grams": null,
			"product_id": 8
		},
		{
			"id": 27,
			"name": "Apple",
			"code": "",
			"serving_size_grams": null,
			"product_id": 5
		},
		{
			"id": 21,
			"name": "Durable Bronze Bag",
			"code": "AmazingDeal370523",
			"serving_size_grams": null,
			"product_id": 1
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
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" https://app.lightlabs.com/api/skus
```

## Show sku

* `GET /api/skus/1` will return the sku with ID 1 for the authenticated company. It returns all the necessary information about the sku including the Product is belongs to.

###### Example JSON Response

```json
{
	"id": 1,
	"name": "Vanilla",
	"code": "PROPOW-VAN",
	"serving_size_grams": null,
	"product": {
		"id": 1,
		"name": "Protein Powder",
		"brand": null,
		"supplier": null,
		"product_type": "finished_good",
		"shelf_life": null,
		"lot_lookup_enabled": true,
		"pdp_embed_enabled": true,
		"show_limits_on_pip": false,
		"created_at": "2025-11-05T13:18:56.907Z",
		"updated_at": "2025-11-05T13:18:56.907Z"
	}
}
```

###### Copy as cURL

``` shell
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" https://app.lightlabs.com/api/skus/1
```
