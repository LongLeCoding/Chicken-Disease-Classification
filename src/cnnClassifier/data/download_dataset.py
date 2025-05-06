from duckduckgo_search import DDGS
import os
import requests

# Directories to save images
coccidiosis_dir = "C:\Python\Chicken_Disease_Classification\Chicken_fecal_images\Coccidiosis"
healthy_dir = "C:\Python\Chicken_Disease_Classification\Chicken_fecal_images\Healthy"

os.makedirs(healthy_dir, exist_ok=True)
os.makedirs(coccidiosis_dir, exist_ok=True)

# Initialize DDGS object
ddgs = DDGS()

# Function to download images
def download_image(url, folder):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            image_name = url.split("/")[-1]
            with open(os.path.join(folder, image_name), 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {image_name} to {folder}")
        else:
            print(f"Failed to download {url}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

# Function to scrape images based on a keyword
# def scrape_images(keyword, folder):
#     results = ddgs.images(keyword, max_results=30)  # Adjust max_results as needed
#     for result in results:
#         image_url = result.get("image")
#         if image_url:
#             download_image(image_url, folder)

def scrape_images(keyword, folder, max_results=30):
    results = ddgs.images(
        keywords=keyword,
        region="wt-wt",
        safesearch="moderate",
        type_image="photo",
        layout="Square",
        license_image="Modify",
        max_results=max_results
    )
    for result in results:
        image_url = result.get("image")
        if image_url:
            download_image(image_url, folder)


# Scrape images for "Coccidiosis" and "Healthy"
scrape_images("Chicken Coccidiosis fecal microscope image", coccidiosis_dir)
scrape_images("Chicken Coccidiosis fecal  image", coccidiosis_dir)
scrape_images("Normal chicken feces microscope photo", healthy_dir)
scrape_images("Normal chicken poop  photos", healthy_dir)


