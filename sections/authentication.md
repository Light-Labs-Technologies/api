# Authentication

## Overview
The API uses API Keys to authenticate requests. You must include your API Key in the Authorization header of every HTTP request.

## Obtaining an API Key
Currently, API Keys are not generated via a self-service portal. To obtain your production credentials:

Contact your dedicated account manager.

Or, reach out to our support team directly.

Once issued, please store your API Key defined as a secret in your environment. Do not share your API Key or commit it to public repositories.

## How to Authenticate
To authenticate, add the Authorization header to your request with the Bearer scheme, followed by your API Key.

Header Format:
```
Authorization: Bearer <YOUR_API_KEY>
```

### Example Request
Here is an example of how to structure a curl request using the authentication header:

```shell
curl -X GET https://app.lightlabs.com/api/tests \
  -H "Authorization: Bearer <YOUR_API_TOKEN>" \
  -H "Content-Type: application/json"
```
