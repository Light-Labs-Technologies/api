import requests
import csv
import os
import sys

class LightLabsClient:
    def __init__(self, api_key, url="https://app.lightlabs.com"):
        self.url = url
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def get_tests(self, page=1):
        response = requests.get(f"{self.url}/api/tests", headers=self.headers, params={"page": page})
        response.raise_for_status()
        return response.json()

class PaginatingLightLabsClient:
    def __init__(self, client):
        self.client = client

    def get_tests(self) -> list:
        tests, page = [], 1
        while True:
            response = self.client.get_tests(page=page)
            tests.extend(response.get("tests", []))

            next_page = response.get("pagination", {}).get("next_page")
            if not next_page:
                break
            page = next_page
        return tests

class SimplifiedCSVWriter:
    def __init__(self, out):
        self.out = out

    def _dynamic_fields(self, tests: list) -> list:
        fields = set()
        for test in tests:
            for result in test.get("results", []):
                fields.add(result.get("analyte").get("name"))
        return list(fields)
    
    def _fixed_fields(self):
        return [
            "Test ID", "Status", "Ordered At", "Orderer", "Product", "Variant", 
            "Code", "Lot", "Assay", "Notes"
        ]

    def _fields(self, tests):
        return self._fixed_fields() + self._dynamic_fields(tests)

    def write(self, tests: list):
        writer = csv.DictWriter(self.out, fieldnames=self._fields(tests))
        writer.writeheader()

        for test in tests:
            dynamic_fields = {}
            for result in test.get("results", []):
                analyte = result.get("analyte").get("name")
                dynamic_fields[analyte] = result.get("result")

            row = {
                'Test ID': test.get("id"), 
                'Status': test.get("status"), 
                'Ordered At': test.get("sample").get("order").get("ordered_at"), 
                'Orderer': test.get("sample").get("order").get("orderer").get("name"), 
                'Product': test.get("sample").get("sku").get("product").get("name"), 
                'Variant': test.get("sample").get("sku").get("name"), 
                'Code': test.get("sample").get("sku").get("code"),
                'Lot': test.get("sample").get("lot"), 
                'Assay': test.get("assay").get("name"), 
                'Notes': test.get("notes"), 
            } | dynamic_fields

            writer.writerow(row)


api_key = os.environ.get("LIGHTLABS_API_KEY")
if not api_key:
    print("Error: LIGHTLABS_API_KEY environment variable not set.", file=sys.stderr)
    sys.exit(1)

client = PaginatingLightLabsClient(LightLabsClient(api_key))
tests = client.get_tests()

writer = SimplifiedCSVWriter(sys.stdout)
writer.write(tests)