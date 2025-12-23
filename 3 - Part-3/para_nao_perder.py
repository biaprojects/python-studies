with open('mapped_products.json', 'w', encoding='utf-8') as outfile:
        json.dump(mapped_products, outfile, indent=4, ensure_ascii=False)

        