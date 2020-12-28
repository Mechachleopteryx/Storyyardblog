====================
        BLOG
====================
1. Title
2. blog banner
3. blog description
4. date / Time
5. author name
6. author pic
7. Categories
8. tags


=====================
        COMMENT
=====================

# """MEDIA_URL = '/media/'
# MEDIA_ROOT = Path.joinpath(BASE_DIR, 'media')"""



{% for blog in allblogs %} 
      <div class="post col-md-4">
        <div class="post-thumbnail">
          <a href=""
            ><img
              src="{{blog.author_pic.url}}"
              alt="..."
              class="img-fluid"
          /></a>
        </div>
        <div class="post-details">
          <div class="post-meta d-flex justify-content-between">
            <div class="date">{{blog.date}}</div>
            <div class="category"><a href="#">{{blog.category}}</a></div>
          </div>
          <a href="post.html">
            <h3 class="h4">{{blog.title}}</h3></a
          >
          <p class="text-muted">
            {{blog.description|safe|slice:250}}
          </p>
        </div>
      </div>
      {% endfor %}