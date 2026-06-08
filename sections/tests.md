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

## Custom Fields

Tests include a `custom_fields` array containing any custom fields your company has defined for the `Test` resource. Each entry has the following attributes:

| Attribute | Type | Description |
| :--- | :--- | :--- |
| `key` | String | The machine-readable identifier of the custom field (e.g., `metafield_batch_id`). |
| `name` | String | The human-readable name of the custom field (e.g., `Batch ID`). |
| `value` | String | The value set for this test. |

If the test has no custom fields, `custom_fields` will be an empty array (`[]`).

## Sample

Each test includes a `sample` object describing the specimen that was tested. Note the following about its attributes:

| Attribute | Type | Description |
| :--- | :--- | :--- |
| `name` | String | Human-readable name of the sample. Always present. |
| `sku` | Object or `null` | The SKU (product variant) the sample maps to. This field is **optional**: when a sample is not linked to a SKU, `sku` is `null`. Always check for `null` before reading nested fields such as `sku.code` or `sku.product`. |
| `serving_size` | String or `null` | The sample's serving size, formatted as a value with its unit (e.g., `"10 g"`). `null` when no serving size is set. |

## Results

Each entry in a test's `results` array includes a `loq` attribute:

| Attribute | Type | Description |
| :--- | :--- | :--- |
| `loq` | String or `null` | The analyte's Limit of Quantification, formatted as a value with its unit (e.g., `"0.5 ppm"`). `null` when no LOQ is available. |

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
      "custom_fields": [
        {
          "key": "metafield_batch_id",
          "name": "Batch ID",
          "value": "B-1234"
        },
        {
          "key": "metafield_priority",
          "name": "Priority",
          "value": "High"
        }
      ],
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
          "loq": null,
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
          "loq": null,
          "spec_result": "no_spec",
          "specification": "no_spec",
          "limit_value": "-",
          "limit": "-"
        }
      ],
      "sample": {
        "id": 677,
        "name": "Baby Food, Apple Strawberry",
        "lot": null,
        "batch": null,
        "composite": false,
        "number_of_composites": 1,
        "serving_size": "10 g",
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
            "email": "no-reply@lightlabs.com",
            "name": "John Doe"
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
  "custom_fields": [
    {
      "key": "metafield_batch_id",
      "name": "Batch ID",
      "value": "B-1234"
    },
    {
      "key": "metafield_priority",
      "name": "Priority",
      "value": "High"
    }
  ],
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
      "loq": null,
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
      "loq": null,
      "spec_result": "no_spec",
      "specification": "no_spec",
      "limit_value": "-",
      "limit": "-"
    }
  ],
  "sample": {
    "id": 677,
    "name": "Baby Food, Apple Strawberry",
    "lot": null,
    "batch": null,
    "composite": false,
    "number_of_composites": 1,
    "serving_size": "10 g",
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
        "email": "no-reply@lightlabs.com",
        "name": "John Doe"
      }
    }
  }
}
```

###### Copy as cURL

``` shell
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" https://app.lightlabs.com/api/tests/1
```
