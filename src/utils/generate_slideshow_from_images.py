from gcloud import storage
client = storage.Client()  # Implicit environ set-up

bucket_name = 'vuecli-profile-website'
bucket = client.bucket(bucket_name)

# blobs_prefix = "blog_posts/2022/11/02/resized_"
# blobs_prefix = "blog_posts/2022/11/03/resized_"
# blobs_prefix = "blog_posts/2022/11/04/resized_"
# blobs_prefix = "blog_posts/2022/11/05/resized_"
blobs_prefix = "blog_posts/2022/11/06/resized_"
# blobs_prefix = "blog_posts/2022/11/07/resized_"
# blobs_prefix = "blog_posts/2022/11/08/resized_"
# blobs_prefix = "blog_posts/2022/11/09/resized_"

images = [i for i in bucket.list_blobs(prefix=blobs_prefix)]
count = len(images)
image_links = [i.public_url for i in images]

# Practice
# 
# image_name = image_links[0].replace(f"https://storage.googleapis.com/{bucket_name}/" + blobs_prefix.replace("/", "%2F"), "").replace(".jpg", "").replace(".png", "")

# i = 1
# count = 1
# image_html = f"""
# <div class="mySlides fade">
#   <div class="numbertext">{i} / {count}</div>
#   <img src=\"{image_links[0]}\" style=\"width:100%\">
#   <div class="text">{image_name}</div>
# </div>

# """

# print(image_html)

images_html = ""
dots = ""
for i, image_url in enumerate(image_links, start=1):
    image_name = image_url.replace(f"https://storage.googleapis.com/{bucket_name}/" + blobs_prefix.replace(
        "/", "%2F"), "").replace(".jpg", "").replace(".png", "")
    
    image_html = f"""
<div class="mySlides fade">
    <div class="numbertext">{i} / {count}</div>
    <img src=\"{image_url}\" style=\"width:100%\">
    <div class="text">{image_name}</div>
</div>

    """
    
    dot = f"""<span class="dot" onclick="currentSlide({i})"></span> 
    """
    
    images_html += image_html
    dots += dot
    


slide_show_html = f"""

<div class="slideshow-container">
<!-- https://www.w3schools.com/howto/howto_js_slideshow.asp -->

{images_html}


<a class="prev" onclick="plusSlides(-1)">❮</a>
<a class="next" onclick="plusSlides(1)">❯</a>

</div>
<br>

<div style="text-align:center">
  {dots}
</div>

"""

# print(slide_show_html)

with open("src/utils/slide_show.html", "w") as file:
    file.write(slide_show_html)

