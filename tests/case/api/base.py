"""
Utility base TestCase classes for testing APIs.

"""
from django.core.urlresolvers import reverse

from tests.case.view import WebTest
from moztrap.model import API_VERSION
import urllib
import json



class ApiTestCase(WebTest):


    def get_resource_url(self, url_name, resource_name, params={}):
        kwargs = {
            "resource_name": resource_name,
            "api_name": API_VERSION,
            }
        kwargs.update(params)
        return reverse(url_name, kwargs=kwargs)


    def get_list_url(self, resource_name):
        return self.get_resource_url("api_dispatch_list", resource_name)


    def get_detail_url(self, resource_name, id):
        return self.get_resource_url(
            "api_dispatch_detail",
            resource_name,
            {"pk": id},
            )


    def patch(self, url, payload="", params={}, status=200):
        params.setdefault("format", "json")
        url = "{0}?{1}".format(url, urllib.urlencode(params))
        return self.app.patch(url, payload, status=status)


    def post(self, url, payload="", params={}, status=200):
        params.setdefault("format", "json")
        url = "{0}?{1}".format(url, urllib.urlencode(params))
        json_data = json.dumps(payload)
        print json.dumps(payload, indent=4)
        return self.app.post(
            url,
            json_data,
            headers = {"content-type": "application/json"},
            status=status,
            )


    def get(self, url, params={}, status=200):
        params.setdefault("format", "json")
        return self.app.get(url, params=params, status=status)


    def get_list(self, params={}, status=200):
        return self.get(
            self.get_list_url(self.resource_name),
            params=params,
            status=status,
            )


    def get_detail(self, id, params={}, status=200):
        return self.get(
            self.get_detail_url(self.resource_name, id),
            params=params,
            status=status,
            )


    def get_detail_uri(self, resource_name, id):
        url = self.get_detail_url(resource_name, id)
        return "/{0}".format(url.split("/", 1)[1])