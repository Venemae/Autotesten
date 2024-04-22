import requests, yaml


with open(f"template_browserstack.yml") as browserstack_config:

    template = yaml.safe_load(browserstack_config)

    api_call_result = { "build_number": 456 }

    api_id = { "app_id" : "bs://albflabdflahybflbsdcfagsefktagfsd" }

    template["app_id"] = api_id["app_id"]

    template["build_number"] = api_call_result["build_number"]


with open("testje_browserstack.yml", "w") as ostream:

    yaml.dump(template, ostream, sort_keys=False)
