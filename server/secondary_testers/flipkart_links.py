def generate_flipkart_url(search_query, occasion_filter=None, color_filter=None):
    base_url = "https://www.flipkart.com/search?q="
    search_query = search_query.replace(" ", "%20")
    url = f"{base_url}{search_query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"

    filters = []
    if occasion_filter:
        filters.append(f"p%5B%5D=facets.occasion%255B%255D%3D{occasion_filter}")
    if color_filter:
        filters.append(f"p%5B%5D=facets.color%255B%255D%3D{color_filter}")

    if filters:
        filter_string = "&" + "&".join(filters)
        url += filter_string

    return url

search_query = "Anarkali suit pink black purple salwar"
occasion_filter = "Formal"
color_filter = "Pink"

final_url = generate_flipkart_url(search_query, occasion_filter, color_filter)
print(final_url)
