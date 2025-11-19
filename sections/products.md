# Products

Endpoints:

- [Get products](#get-products)
- [Show product](#show-product)

## Get products

* `GET /api/products` will return a [paginated list](../README.md#pagination) of products for the authenticated company.

###### Example JSON Response

```json
{
	"products": [
		{
			"id": 5,
			"name": "Apple",
			"brand": "",
			"supplier": "Acme Inc.",
			"product_type": "raw_material",
			"shelf_life": null,
			"lot_lookup_enabled": false,
			"pdp_embed_enabled": false,
			"show_limits_on_pip": false,
			"created_at": "2025-11-12T19:57:37.904Z",
			"updated_at": "2025-11-12T19:57:37.904Z"
		},
		{
			"id": 2,
			"name": "Baby Food",
			"brand": null,
			"supplier": null,
			"product_type": "finished_good",
			"shelf_life": null,
			"lot_lookup_enabled": true,
			"pdp_embed_enabled": true,
			"show_limits_on_pip": false,
			"created_at": "2025-11-05T13:18:56.934Z",
			"updated_at": "2025-11-05T13:18:56.934Z"
		},
		{
			"id": 8,
			"name": "Banana",
			"brand": "",
			"supplier": "Acme Inc.",
			"product_type": "raw_material",
			"shelf_life": null,
			"lot_lookup_enabled": false,
			"pdp_embed_enabled": false,
			"show_limits_on_pip": false,
			"created_at": "2025-11-13T18:23:40.475Z",
			"updated_at": "2025-11-13T18:23:40.475Z"
		},
		{
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
	],
	"pagination": {
		"per_page": 20,
		"current_page": 2,
		"prev_page": 1,
		"next_page": 3
	}
}
```

###### Copy as cURL

``` shell
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" https://app.lightlabs.com/api/products
```

## Show product

* `GET /api/products/1` will return the product with ID 1 for the authenticated company. It returns all the necessary information about the product including its SKUs, also known as variants.

###### Example JSON Response

```json
{
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
	"updated_at": "2025-11-05T13:18:56.907Z",
	"skus": [
		{
			"id": 1,
			"name": "Vanilla",
			"code": "PROPOW-VAN",
			"serving_size_grams": null
		},
		{
			"id": 2,
			"name": "Chocolate",
			"code": "PROPOW-CHOC",
			"serving_size_grams": null
		},
		{
			"id": 3,
			"name": "Strawberry",
			"code": "PROPOW-STRAW",
			"serving_size_grams": null
		},
		{
			"id": 4,
			"name": "Cookies and Cream",
			"code": "PROPOW-COOKIES",
			"serving_size_grams": null
		},
		{
			"id": 5,
			"name": "Tropical",
			"code": "PROPOW-TROP",
			"serving_size_grams": null
		},
		{
			"id": 15,
			"name": "Aerodynamic Plastic Coat",
			"code": "StellarSale910341",
			"serving_size_grams": null
		},
		{
			"id": 16,
			"name": "Synergistic Copper Computer",
			"code": "StellarPromo165935",
			"serving_size_grams": null
		},
		{
			"id": 17,
			"name": "Practical Bronze Chair",
			"code": "AwesomeCode418363",
			"serving_size_grams": null
		},
		{
			"id": 18,
			"name": "Intelligent Plastic Watch",
			"code": "AmazingDiscount190361",
			"serving_size_grams": null
		},
		{
			"id": 19,
			"name": "Intelligent Wool Lamp",
			"code": "IncrediblePromotion164018",
			"serving_size_grams": null
		},
		{
			"id": 20,
			"name": "Gorgeous Wooden Bench",
			"code": "CoolPromo171031",
			"serving_size_grams": null
		},
		{
			"id": 21,
			"name": "Durable Bronze Bag",
			"code": "AmazingDeal370523",
			"serving_size_grams": null
		},
		{
			"id": 22,
			"name": "Small Linen Shirt",
			"code": "SweetPromo379910",
			"serving_size_grams": null
		},
		{
			"id": 23,
			"name": "Awesome Granite Chair",
			"code": "PremiumSale866518",
			"serving_size_grams": null
		},
		{
			"id": 24,
			"name": "Small Leather Gloves",
			"code": "StellarDeal489864",
			"serving_size_grams": null
		}
	]
}
```

###### Copy as cURL

``` shell
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" https://app.lightlabs.com/api/products/1
```
