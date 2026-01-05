import requests
import json


class Search:

    def get_search_results(self):
        search_term = "the lord of the rings"

        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1

        url = (
            f"https://openlibrary.org/search.json"
            f"?title={search_term_formatted}"
            f"&fields={fields_formatted}"
            f"&limit={limit}"
        )

        response = requests.get(url)
        return response.content

    def get_search_results_json(self):
        search_term = "the lord of the rings"

        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1

        url = (
            f"https://openlibrary.org/search.json"
            f"?title={search_term_formatted}"
            f"&fields={fields_formatted}"
            f"&limit={limit}"
        )

        response = requests.get(url)
        return response.json()

    def get_user_search_results(self, search_term):
        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1

        url = (
            f"https://openlibrary.org/search.json"
            f"?title={search_term_formatted}"
            f"&fields={fields_formatted}"
            f"&limit={limit}"
        )

        response = requests.get(url).json()
        return (
            f"Title: {response['docs'][0]['title']}\n"
            f"Author: {response['docs'][0]['author_name'][0]}"
        )
