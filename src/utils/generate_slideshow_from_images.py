from gcloud import storage
client = storage.Client()  # Implicit environ set-up

bucket_name = 'vuecli-profile-website'
bucket = client.bucket(bucket_name)

# blobs_prefix = "blog_posts/2022/11/02/resized_"
# blobs_prefix = "blog_posts/2022/11/03/resized_"
# blobs_prefix = "blog_posts/2022/11/04/resized_"
# blobs_prefix = "blog_posts/2022/11/05/resized_"
# blobs_prefix = "blog_posts/2022/11/06/resized_"
# blobs_prefix = "blog_posts/2022/11/07/resized_"
# blobs_prefix = "blog_posts/2022/11/08/resized_"
# blobs_prefix = "blog_posts/2022/11/11/resized_"
# blobs_prefix = "blog_posts/2022/11/12/resized_"
# blobs_prefix = "blog_posts/2022/11/13/resized_"
# blobs_prefix = "blog_posts/2022/11/14/resized_"
# blobs_prefix = "blog_posts/2022/11/15/resized_"
# blobs_prefix = "blog_posts/2022/11/16/resized_"
# blobs_prefix = "blog_posts/2022/11/17/resized_"
# blobs_prefix = "blog_posts/2022/11/18/resized_"
# blobs_prefix = "blog_posts/2022/11/19/resized_"
# blobs_prefix = "blog_posts/2022/11/20/resized_"
# blobs_prefix = "blog_posts/2022/11/21/resized_"
# blobs_prefix = "blog_posts/2022/11/22/resized_"
# blobs_prefix = "blog_posts/2022/11/23/resized_"
# blobs_prefix = "blog_posts/2022/11/24/resized_"
# blobs_prefix = "blog_posts/2022/11/25/resized_"
# blobs_prefix = "blog_posts/2022/11/26/resized_"

# blobs_prefix = "blog_posts/2022/11/28/resized_"
# blobs_prefix = "blog_posts/2022/11/29/resized_"
# blobs_prefix = "blog_posts/2022/11/30/resized_"
# blobs_prefix = "blog_posts/2022/12/01/resized_"
# blobs_prefix = "blog_posts/2022/12/02/resized_"
# blobs_prefix = "blog_posts/2022/12/03/resized_"
# blobs_prefix = "blog_posts/2022/12/04/resized_"
# blobs_prefix = "blog_posts/2022/12/06/resized_"
# blobs_prefix = "blog_posts/2022/12/07/resized_"
# blobs_prefix = "blog_posts/2022/12/08/resized_"
# blobs_prefix = "blog_posts/2022/12/09/resized_"

images = [i for i in bucket.list_blobs(prefix=blobs_prefix)]
count = len(images)
#
# images[0].public_url
#
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

