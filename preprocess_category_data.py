import csv, json
from collections import defaultdict

wiki_data = []
with open('data/WikiArtClean.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count > 0:
            # Only include paintings
            if row["Is painting"] == "yes":
                # Only include Renaissance Art
                if ("Renaissance Art" in row["Style"].split(",")) or ("Post Renaissance Art" in row["Style"].split(",")):
                    wiki_data.append(row)
        line_count += 1

# Find all categories in the data
# all_categories = list(set(elem for row in wiki_data for elem in row["Category"].split(",")))
all_categories = []
for row in wiki_data:
    for c in row["Category"].split(","):
        if not c == "Magic Realism":
            all_categories.append(c)
all_categories = list(set(all_categories))

year_to_category_count = {}
for row in wiki_data:
    if not row["Year"] in year_to_category_count:
        year_to_category_count[row["Year"]] = defaultdict(int)
    for c in row["Category"].split(","):
        if not c == "Magic Realism":
            year_to_category_count[row["Year"]][c] += 1

# Write preprocessed data to new csv file.
with open('categories_per_year_renaissance.csv', mode='w') as categories_file:
    category_writer = csv.writer(categories_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    category_writer.writerow(["year"] + all_categories)
    for year, category in year_to_category_count.items():
        category_counts = []
        for c in all_categories:
            if c in category:
                category_counts.append(category[c])
            else:
                category_counts.append(0)
        category_writer.writerow([year] + category_counts)

tmp = {}
for c in all_categories:
    category_artists = defaultdict(list)
    for row in wiki_data:
        # print(c, row["Category"].split(","))
        if c in row["Category"].split(","):
            # Title,Year,Image URL
            painting_title = row["Title"]
            painting_year = row["Year"]
            painting_url = row["Image URL"]
            category_artists[row["Artist"]].append((painting_title, painting_year, painting_url))
    tmp[c] = category_artists

data = {}
data["name"] = "categories"
data["children"] = []
categories = []
id_count = 0
for category, artists in tmp.items():
    category_artists = []
    for artist, paintings in artists.items():
        artist_paintings = []
        for (painting_title, painting_year, painting_url) in paintings:
            painting = {
                "name": painting_title,
                "year": painting_year,
                "url": painting_url,
                "size": 1,
                "id": id_count,
            }
            artist_paintings.append(painting)
            id_count += 1
        category_artists.append({"name": artist, "type": "artist", "children": artist_paintings})
    categories.append({"name": category, "type": "category", "children": category_artists})
data["children"] = categories

with open('data/category_artist_data.json', 'w') as outfile:
    # print(json.dumps(data, indent=4))
    json.dump(data, outfile, indent=4)
